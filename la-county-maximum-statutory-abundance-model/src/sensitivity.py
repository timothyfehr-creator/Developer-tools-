"""
One-at-a-time (OAT) sensitivity tornado runner.

Runs Scenario C max_central with central util/fiscal variants. Perturbs each
parameter listed in scenario_parameters.json:sensitivity_parameters at low
and high multiples; records four headline outcomes at 2045.

This is *local* sensitivity, not global. Documented in red-team memo.
"""

from __future__ import annotations

import csv
from pathlib import Path
from typing import List

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from src.scenarios import resolve_params
from src.model import run_scenario, YearState


HEADLINE_METRICS = [
    "cumulative_net_new_units",
    "median_gross_rent_real_2024",
    "homelessness_pressure_index",
    "net_new_public_revenue_after_service_costs",
]


def _final(series: List[YearState], attr: str) -> float:
    return getattr(series[-1], attr)


def _perturb(params: dict, name: str, mult: float, fallback: float = None) -> dict:
    p = dict(params)
    if name in p:
        p[name] = p[name] * mult
    elif fallback is not None:
        p[name] = fallback * mult
    return p


def run_sensitivity(baseline: dict, cfg: dict, outputs_dir: Path):
    base_params = resolve_params(cfg, "C_max_central", "util_current_drag", "fcap_partial")
    central_series = run_scenario(base_params, baseline)
    central_values = {m: _final(central_series, m) for m in HEADLINE_METRICS}

    rows = []
    for spec in cfg["sensitivity_parameters"]:
        name = spec["name"]
        fallback = spec.get("fallback")
        for which, mult in (("low", spec["low_mult"]), ("high", spec["high_mult"])):
            perturbed = _perturb(base_params, name, mult, fallback)
            try:
                series = run_scenario(perturbed, baseline)
            except Exception as exc:
                print(f"Sensitivity {name} {which} failed: {exc}")
                continue
            row = {"parameter": name, "perturbation": which, "multiplier": mult}
            for m in HEADLINE_METRICS:
                row[m] = _final(series, m)
                row[m + "_pct_vs_central"] = (row[m] - central_values[m]) / max(abs(central_values[m]), 1e-9)
            rows.append(row)

    columns = ["parameter", "perturbation", "multiplier"] + [
        c
        for m in HEADLINE_METRICS
        for c in (m, m + "_pct_vs_central")
    ]
    out = outputs_dir / "tornado.csv"
    with out.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=columns)
        w.writeheader()
        for r in rows:
            w.writerow(r)

    _render_tornado_charts(rows, central_values, outputs_dir / "charts")
    return rows


def _render_tornado_charts(rows, central_values, charts_dir: Path):
    charts_dir.mkdir(parents=True, exist_ok=True)
    for metric in HEADLINE_METRICS:
        params = sorted({r["parameter"] for r in rows})
        lows = []
        highs = []
        for p in params:
            r_low = next((r for r in rows if r["parameter"] == p and r["perturbation"] == "low"), None)
            r_high = next((r for r in rows if r["parameter"] == p and r["perturbation"] == "high"), None)
            lows.append(r_low[metric + "_pct_vs_central"] if r_low else 0.0)
            highs.append(r_high[metric + "_pct_vs_central"] if r_high else 0.0)

        spans = [abs(h - l) for l, h in zip(lows, highs)]
        order = sorted(range(len(params)), key=lambda i: spans[i], reverse=True)
        params = [params[i] for i in order]
        lows = [lows[i] for i in order]
        highs = [highs[i] for i in order]

        fig, ax = plt.subplots(figsize=(10, max(4, len(params) * 0.32)))
        y = list(range(len(params)))
        ax.barh(y, [h - l for l, h in zip(lows, highs)], left=lows, color="#4a90d9", alpha=0.7)
        ax.set_yticks(y)
        ax.set_yticklabels(params, fontsize=8)
        ax.axvline(0, color="black", linewidth=0.8)
        ax.set_xlabel(f"% deviation from central in {metric} (2045)")
        ax.set_title(f"OAT sensitivity tornado: {metric}")
        ax.invert_yaxis()
        ax.grid(True, alpha=0.3, axis="x")
        fig.tight_layout()
        fig.savefig(charts_dir / f"tornado_{metric}.png", dpi=120)
        plt.close(fig)
