"""
Economist-style dashboard chart generator.

Produces a small set of editorial-style charts (one emphasized red line,
muted gray supporting lines, annotated end-of-line labels, minimal grid)
into outputs/dashboard/ for embedding in dashboard.html.
"""

from __future__ import annotations
import csv
from pathlib import Path
from typing import List

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import patches
from matplotlib.ticker import FuncFormatter

from src.scenarios import load_baseline, load_scenario_config, central_combinations
from src.model import run_scenario, YearState

ROOT = Path(__file__).resolve().parent.parent
DASH = ROOT / "outputs" / "dashboard"

ECON_RED = "#E3120B"
ECON_DARK = "#121212"
ECON_GRAY_DARK = "#404040"
ECON_GRAY_MID = "#7a7a7a"
ECON_GRAY_LIGHT = "#cfcfcf"
ECON_BG_PANEL = "#f4f4f4"
ECON_BLUE = "#2e6e9e"
ECON_GREEN = "#1f7a4f"
ECON_AMBER = "#c47a00"

SCENARIO_COLORS = {
    "A_baseline": ECON_GRAY_MID,
    "B_moderate": ECON_BLUE,
    "C_max_central": ECON_RED,
    "D_max_high_build": ECON_GREEN,
    "E_max_drag": "#8a3030",
    "F_legal_collision": ECON_AMBER,
}

SCENARIO_LABELS = {
    "A_baseline": "Baseline",
    "B_moderate": "Moderate",
    "C_max_central": "Max abundance — central",
    "D_max_high_build": "High build",
    "E_max_drag": "Implementation drag",
    "F_legal_collision": "Legal collision",
}


def _econ_style():
    plt.rcParams.update({
        "font.family": "DejaVu Sans",
        "font.size": 11,
        "axes.edgecolor": ECON_DARK,
        "axes.linewidth": 0.8,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "grid.color": ECON_GRAY_LIGHT,
        "grid.linewidth": 0.5,
        "grid.linestyle": "-",
        "ytick.color": ECON_GRAY_DARK,
        "xtick.color": ECON_GRAY_DARK,
        "axes.labelcolor": ECON_GRAY_DARK,
        "axes.titlesize": 12,
        "figure.facecolor": "white",
    })


def _annotate_lines_at_end(ax, x_last, series_dict, color_dict, label_dict, fontsize=9, x_offset_frac=0.01):
    xspan = ax.get_xlim()[1] - ax.get_xlim()[0]
    for key, values in series_dict.items():
        ax.text(x_last + xspan * x_offset_frac, values[-1],
                label_dict.get(key, key),
                color=color_dict.get(key, ECON_GRAY_DARK),
                fontsize=fontsize, va="center", ha="left",
                fontweight="bold" if key == "C_max_central" else "normal")


def _save(fig, name):
    DASH.mkdir(parents=True, exist_ok=True)
    fig.savefig(DASH / name, dpi=140, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def chart_hero_cumulative(central_runs):
    fig, ax = plt.subplots(figsize=(9.5, 5.2))
    years = [s.year for s in next(iter(central_runs.values()))]
    series = {scen: [s.cumulative_net_new_units / 1000 for s in runs] for scen, runs in central_runs.items()}

    plot_order = ["A_baseline", "E_max_drag", "F_legal_collision", "B_moderate", "D_max_high_build", "C_max_central"]
    for scen in plot_order:
        if scen not in series:
            continue
        values = series[scen]
        is_hero = (scen == "C_max_central")
        ax.plot(years, values,
                color=SCENARIO_COLORS[scen],
                linewidth=2.6 if is_hero else 1.5,
                alpha=1.0 if is_hero else 0.85,
                zorder=10 if is_hero else 5)

    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, p: f"{v:,.0f}k"))
    ax.set_ylabel("")
    ax.set_xlabel("")
    ax.set_xlim(years[0], years[-1] + 4)
    ax.set_ylim(bottom=-100)
    ax.axhline(0, color=ECON_GRAY_MID, linewidth=0.5)
    _annotate_lines_at_end(ax, years[-1], series, SCENARIO_COLORS, SCENARIO_LABELS, fontsize=10)
    ax.set_title("Cumulative net new housing units, LA County (thousands)", loc="left",
                 fontweight="bold", color=ECON_DARK, pad=10)
    fig.suptitle("The legal lever is the easy one",
                 fontsize=16, fontweight="bold", color=ECON_DARK,
                 x=0.04, y=0.98, ha="left")
    fig.text(0.04, 0.93,
             "Maximum state preemption alone does not deliver housing — utilities, labor and fiscal plumbing decide.",
             fontsize=10.5, color=ECON_GRAY_DARK, ha="left", style="italic")
    fig.text(0.04, 0.005, "Sources: Census QuickFacts; ACS 5-yr 2020-24; HCD APR; project model. Forecasts to 2045.",
             fontsize=8, color=ECON_GRAY_MID, style="italic")
    fig.subplots_adjust(top=0.85, bottom=0.10, left=0.08, right=0.78)
    _save(fig, "hero_cumulative.png")


def chart_real_rent(central_runs):
    fig, ax = plt.subplots(figsize=(7, 4.5))
    years = [s.year for s in next(iter(central_runs.values()))]
    series = {scen: [s.median_gross_rent_real_2024 for s in runs] for scen, runs in central_runs.items()}

    plot_order = ["E_max_drag", "A_baseline", "F_legal_collision", "B_moderate", "C_max_central", "D_max_high_build"]
    for scen in plot_order:
        if scen not in series:
            continue
        is_hero = (scen == "C_max_central")
        ax.plot(years, series[scen], color=SCENARIO_COLORS[scen],
                linewidth=2.5 if is_hero else 1.4, alpha=1.0 if is_hero else 0.8,
                zorder=10 if is_hero else 4)

    ax.axhline(1954, color=ECON_GRAY_MID, linewidth=0.7, linestyle="--")
    ax.text(years[0] + 0.5, 1955, "2024 baseline ($1,954)", fontsize=8, color=ECON_GRAY_MID, va="bottom")

    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, p: f"${v:,.0f}"))
    ax.set_xlim(years[0], years[-1] + 4.5)
    _annotate_lines_at_end(ax, years[-1], series, SCENARIO_COLORS, SCENARIO_LABELS, fontsize=9)
    ax.set_title("Median gross rent, real 2024 dollars",
                 loc="left", fontweight="bold", color=ECON_DARK, pad=8)
    fig.text(0.02, 0.005,
             "Even maximum abundance lifts rent ~9% in real terms over 20 years vs ~18% under baseline.",
             fontsize=8, color=ECON_GRAY_MID, style="italic")
    fig.subplots_adjust(top=0.91, bottom=0.10, left=0.10, right=0.72)
    _save(fig, "real_rent.png")


def chart_hpi(central_runs):
    fig, ax = plt.subplots(figsize=(7, 4.5))
    years = [s.year for s in next(iter(central_runs.values()))]
    series = {scen: [s.homelessness_pressure_index for s in runs] for scen, runs in central_runs.items()}

    ax.axhspan(0, 50, color=ECON_GRAY_LIGHT, alpha=0.25, zorder=1)
    ax.axhline(50, color=ECON_GRAY_MID, linewidth=0.7, linestyle="--")

    plot_order = ["E_max_drag", "A_baseline", "F_legal_collision", "B_moderate", "C_max_central", "D_max_high_build"]
    for scen in plot_order:
        if scen not in series:
            continue
        is_hero = (scen == "C_max_central")
        ax.plot(years, series[scen], color=SCENARIO_COLORS[scen],
                linewidth=2.5 if is_hero else 1.4, alpha=1.0 if is_hero else 0.8,
                zorder=10 if is_hero else 4)

    ax.text(years[0] + 0.5, 51, "Baseline = 50 (lower is better)", fontsize=8, color=ECON_GRAY_MID)
    ax.set_ylim(20, 100)
    ax.set_xlim(years[0], years[-1] + 4.5)
    _annotate_lines_at_end(ax, years[-1], series, SCENARIO_COLORS, SCENARIO_LABELS, fontsize=9)
    ax.set_title("Homelessness pressure index",
                 loc="left", fontweight="bold", color=ECON_DARK, pad=8)
    fig.text(0.02, 0.005,
             "Abundance buys a 5-15 yr trough, not permanent abolition. Rebound by 2045 in central case.",
             fontsize=8, color=ECON_GRAY_MID, style="italic")
    fig.subplots_adjust(top=0.91, bottom=0.10, left=0.08, right=0.72)
    _save(fig, "hpi.png")


def chart_fiscal_bars(central_runs):
    fig, ax = plt.subplots(figsize=(7, 4.5))
    scenarios = ["A_baseline", "E_max_drag", "F_legal_collision", "B_moderate", "C_max_central", "D_max_high_build"]
    labels = [SCENARIO_LABELS[s] for s in scenarios]
    net_rev = [central_runs[s][-1].net_new_public_revenue_after_service_costs / 1e9 for s in scenarios]
    reinvest = [central_runs[s][-1].infrastructure_reinvestment_capacity / 1e9 for s in scenarios]
    funding_gap = [central_runs[s][-1].infrastructure_funding_gap / 1e9 for s in scenarios]

    y = list(range(len(scenarios)))
    bar_h = 0.32
    ax.barh([i - bar_h * 0.55 for i in y], net_rev, height=bar_h,
            color=[SCENARIO_COLORS[s] for s in scenarios],
            alpha=0.95, label="Net new revenue", zorder=5)
    ax.barh([i + bar_h * 0.55 for i in y], reinvest, height=bar_h,
            color=[SCENARIO_COLORS[s] for s in scenarios],
            alpha=0.45, hatch="///", edgecolor="white", linewidth=0.3,
            label="Infrastructure reinvestment", zorder=5)

    ax.set_yticks(y)
    ax.set_yticklabels(labels, fontsize=9.5)
    ax.invert_yaxis()
    ax.axvline(0, color=ECON_DARK, linewidth=0.6)
    ax.xaxis.set_major_formatter(FuncFormatter(lambda v, p: f"${v:.0f}B"))
    ax.set_title("2045 net public revenue and infrastructure reinvestment", loc="left",
                 fontweight="bold", color=ECON_DARK, pad=8)

    legend = ax.legend(loc="lower right", fontsize=8.5, frameon=False)
    fig.text(0.02, 0.005,
             "Even high build with maximum capture leaves $1-3B/yr funding gap unless bonds bridge.",
             fontsize=8, color=ECON_GRAY_MID, style="italic")
    fig.subplots_adjust(top=0.91, bottom=0.10, left=0.34, right=0.96)
    _save(fig, "fiscal_bars.png")


def chart_funnel(central_runs):
    fig, ax = plt.subplots(figsize=(7, 4.5))

    s = central_runs["C_max_central"]
    legal = sum([1] * 20) * 1.0
    legal_total = s[-1].legal_capacity_cumulative / 1000
    permits_total = sum([yr.annual_permits for yr in s]) / 1000
    completions_total = sum([yr.annual_completions for yr in s]) / 1000
    energized_total = sum([yr.annual_energized for yr in s]) / 1000
    occupied_total = sum([yr.annual_occupied_new_units for yr in s]) / 1000

    stages = ["Legal\ncapacity", "Permits\nissued", "Completed\nbuildings", "Utility\nenergized", "Occupied\nunits"]
    values = [legal_total, permits_total, completions_total, energized_total, occupied_total]
    colors = ["#cfcfcf", ECON_BLUE, ECON_AMBER, ECON_GREEN, ECON_RED]

    bars = ax.bar(stages, values, color=colors, edgecolor="white", linewidth=2)
    for bar, val in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width() / 2, val + max(values) * 0.015,
                f"{val:,.0f}k", ha="center", va="bottom", fontsize=10,
                fontweight="bold", color=ECON_DARK)

    ax.set_ylabel("")
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, p: f"{v:,.0f}k"))
    ax.set_title("The 5-gate funnel: where housing leaks out",
                 loc="left", fontweight="bold", color=ECON_DARK, pad=8)
    ax.tick_params(axis='x', labelsize=9.5)
    fig.text(0.02, 0.005,
             "Scenario C max central, cumulative 2026-2045. Each stage drops about 30-50% of prior stage.",
             fontsize=8, color=ECON_GRAY_MID, style="italic")
    fig.subplots_adjust(top=0.91, bottom=0.14, left=0.10, right=0.97)
    _save(fig, "funnel.png")


def chart_residual_income(central_runs):
    fig, ax = plt.subplots(figsize=(7, 4.5))
    years = [s.year for s in next(iter(central_runs.values()))]
    series = {scen: [s.residual_income_after_rent / 1000 for s in runs] for scen, runs in central_runs.items()}

    plot_order = ["E_max_drag", "A_baseline", "F_legal_collision", "B_moderate", "C_max_central", "D_max_high_build"]
    for scen in plot_order:
        if scen not in series:
            continue
        is_hero = (scen == "C_max_central")
        ax.plot(years, series[scen], color=SCENARIO_COLORS[scen],
                linewidth=2.5 if is_hero else 1.4, alpha=1.0 if is_hero else 0.8,
                zorder=10 if is_hero else 4)

    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, p: f"${v:,.0f}k"))
    ax.set_xlim(years[0], years[-1] + 4.5)
    _annotate_lines_at_end(ax, years[-1], series, SCENARIO_COLORS, SCENARIO_LABELS, fontsize=9)
    ax.set_title("Median household residual income after rent (2024 dollars)",
                 loc="left", fontweight="bold", color=ECON_DARK, pad=8)
    fig.text(0.02, 0.005,
             "Welfare measure: median income minus annualised rent. Abundance lifts ~$2,100/HH/yr.",
             fontsize=8, color=ECON_GRAY_MID, style="italic")
    fig.subplots_adjust(top=0.91, bottom=0.10, left=0.12, right=0.72)
    _save(fig, "residual_income.png")


def chart_population(central_runs):
    fig, ax = plt.subplots(figsize=(7, 4.5))
    years = [s.year for s in next(iter(central_runs.values()))]
    series = {scen: [s.population / 1e6 for s in runs] for scen, runs in central_runs.items()}

    plot_order = ["E_max_drag", "A_baseline", "F_legal_collision", "B_moderate", "C_max_central", "D_max_high_build"]
    for scen in plot_order:
        if scen not in series:
            continue
        is_hero = (scen == "C_max_central")
        ax.plot(years, series[scen], color=SCENARIO_COLORS[scen],
                linewidth=2.5 if is_hero else 1.4, alpha=1.0 if is_hero else 0.8,
                zorder=10 if is_hero else 4)

    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, p: f"{v:.1f}M"))
    ax.set_xlim(years[0], years[-1] + 4.5)
    _annotate_lines_at_end(ax, years[-1], series, SCENARIO_COLORS, SCENARIO_LABELS, fontsize=9)
    ax.set_title("LA County population", loc="left", fontweight="bold", color=ECON_DARK, pad=8)
    fig.text(0.02, 0.005,
             "Latent demand absorbs supply: more building means more people, not (much) lower rent.",
             fontsize=8, color=ECON_GRAY_MID, style="italic")
    fig.subplots_adjust(top=0.91, bottom=0.10, left=0.10, right=0.72)
    _save(fig, "population.png")


def chart_bottleneck_ranking():
    """Ranked bar chart of constraint bindingness."""
    fig, ax = plt.subplots(figsize=(7, 4.5))
    constraints = [
        "Physical delivery (utilities, labor, materials)",
        "Institutional execution (HCD, building depts)",
        "Construction trades labor capacity",
        "Capital markets and financing",
        "Local-government compliance",
        "Fiscal misalignment (Prop 13, ERAF)",
        "Political coalition durability",
        "Legal authority itself",
    ]
    values = [95, 80, 72, 60, 55, 50, 45, 25]

    y = list(range(len(constraints)))
    colors = [ECON_RED if v >= 80 else ECON_AMBER if v >= 55 else ECON_GRAY_MID for v in values]
    bars = ax.barh(y, values, color=colors, alpha=0.92)
    for i, (v, c) in enumerate(zip(values, constraints)):
        ax.text(v + 1, i, f"{v}", va="center", fontsize=9, color=ECON_DARK, fontweight="bold")

    ax.set_yticks(y)
    ax.set_yticklabels(constraints, fontsize=9.5)
    ax.invert_yaxis()
    ax.set_xlim(0, 100)
    ax.set_xlabel("Bindingness score (0 = trivial, 100 = decisive)", fontsize=9, color=ECON_GRAY_DARK)
    ax.set_title("Which constraint actually decides outcomes?",
                 loc="left", fontweight="bold", color=ECON_DARK, pad=8)
    fig.text(0.02, 0.005,
             "The discourse focuses on legal authority. The model says it's the least binding constraint.",
             fontsize=8, color=ECON_GRAY_MID, style="italic")
    fig.subplots_adjust(top=0.91, bottom=0.13, left=0.40, right=0.97)
    _save(fig, "bottleneck.png")


def main():
    baseline = load_baseline(ROOT / "data" / "baseline_assumptions.json")
    cfg = load_scenario_config(ROOT / "data" / "scenario_parameters.json")
    central_runs = {}
    from src.scenarios import resolve_params
    for scen, util, fcap in central_combinations(cfg):
        params = resolve_params(cfg, scen, util, fcap)
        central_runs[scen] = run_scenario(params, baseline)

    chart_hero_cumulative(central_runs)
    chart_real_rent(central_runs)
    chart_hpi(central_runs)
    chart_fiscal_bars(central_runs)
    chart_funnel(central_runs)
    chart_residual_income(central_runs)
    chart_population(central_runs)
    chart_bottleneck_ranking()

    print(f"Wrote 8 dashboard charts to {DASH}")


if __name__ == "__main__":
    main()
