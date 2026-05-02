"""
LA County Max Statutory Abundance — main runner.

Loads JSON parameters, runs all 54 scenarios, writes scenario_summary.csv
and a milestone-only headline CSV, renders charts, runs sensitivities,
and writes the reform menu CSV.

Usage:
    python -m src.run_model            (from project root)
    python src/run_model.py            (also works)
"""

from __future__ import annotations

import csv
import sys
from dataclasses import asdict
from pathlib import Path
from typing import List

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from src.scenarios import load_baseline, load_scenario_config, resolve_params, all_scenario_combinations, central_combinations
from src.model import run_scenario, YearState
from src.reforms import reforms_to_csv

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
OUTPUTS = ROOT / "outputs"
CHARTS = OUTPUTS / "charts"


REPORT_COLUMNS = [
    "year", "scenario", "utility_infrastructure_variant", "fiscal_capture_variant",
    "housing_stock", "theoretical_housing_capacity", "annual_entitlements",
    "annual_permits", "annual_completions", "annual_occupied_new_units",
    "cumulative_net_new_units", "delayed_completed_units_due_to_utilities",
    "population", "households", "persons_per_household",
    "median_gross_rent_nominal", "median_gross_rent_real_2024",
    "median_home_value_nominal", "median_home_value_real_2024",
    "median_household_income_nominal", "median_household_income_real_2024",
    "per_capita_income_real_2024", "rent_to_income_ratio",
    "residual_income_after_rent", "poverty_rate",
    "homelessness_pressure_index", "estimated_homelessness_cost_avoidance",
    "employer_establishments", "employment", "annual_payroll",
    "accommodation_food_sales", "commercial_vitality_index",
    "gross_new_public_revenue", "net_new_public_revenue_after_service_costs",
    "estimated_benefit_cost_avoidance",
    "infrastructure_reinvestment_capacity", "infrastructure_funding_gap",
    "years_until_growth_fiscal_dividend_turns_positive",
    "share_of_infrastructure_need_self_funded_by_growth",
    "fiscal_score", "fiscal_leakage_score", "fiscal_alignment_score",
    "infrastructure_execution_score", "infrastructure_stress_score",
    "legal_implementation_risk_score", "delivery_risk_score",
]


def state_to_row(state: YearState, scenario: str, util: str, fcap: str) -> dict:
    d = asdict(state)
    return {
        "year": state.year,
        "scenario": scenario,
        "utility_infrastructure_variant": util,
        "fiscal_capture_variant": fcap,
        "housing_stock": d["housing_stock"],
        "theoretical_housing_capacity": d["legal_capacity_cumulative"],
        "annual_entitlements": d["annual_entitlements"],
        "annual_permits": d["annual_permits"],
        "annual_completions": d["annual_completions"],
        "annual_occupied_new_units": d["annual_occupied_new_units"],
        "cumulative_net_new_units": d["cumulative_net_new_units"],
        "delayed_completed_units_due_to_utilities": d["delayed_completed_units_due_to_utilities"],
        "population": d["population"],
        "households": d["households"],
        "persons_per_household": d["persons_per_household"],
        "median_gross_rent_nominal": d["median_gross_rent_nominal"],
        "median_gross_rent_real_2024": d["median_gross_rent_real_2024"],
        "median_home_value_nominal": d["median_home_value_nominal"],
        "median_home_value_real_2024": d["median_home_value_real_2024"],
        "median_household_income_nominal": d["median_household_income_nominal"],
        "median_household_income_real_2024": d["median_household_income_real_2024"],
        "per_capita_income_real_2024": d["per_capita_income_real_2024"],
        "rent_to_income_ratio": d["rent_to_income_ratio"],
        "residual_income_after_rent": d["residual_income_after_rent"],
        "poverty_rate": d["poverty_rate"],
        "homelessness_pressure_index": d["homelessness_pressure_index"],
        "estimated_homelessness_cost_avoidance": d["estimated_homelessness_cost_avoidance"],
        "employer_establishments": d["employer_establishments"],
        "employment": d["employment"],
        "annual_payroll": d["annual_payroll"],
        "accommodation_food_sales": d["accommodation_food_sales"],
        "commercial_vitality_index": d["commercial_vitality_index"],
        "gross_new_public_revenue": d["gross_new_public_revenue"],
        "net_new_public_revenue_after_service_costs": d["net_new_public_revenue_after_service_costs"],
        "estimated_benefit_cost_avoidance": d["estimated_benefit_cost_avoidance"],
        "infrastructure_reinvestment_capacity": d["infrastructure_reinvestment_capacity"],
        "infrastructure_funding_gap": d["infrastructure_funding_gap"],
        "years_until_growth_fiscal_dividend_turns_positive": d["years_until_growth_fiscal_dividend_turns_positive"],
        "share_of_infrastructure_need_self_funded_by_growth": d["share_of_infrastructure_need_self_funded_by_growth"],
        "fiscal_score": d["fiscal_score"],
        "fiscal_leakage_score": d["fiscal_leakage_score"],
        "fiscal_alignment_score": d["fiscal_alignment_score"],
        "infrastructure_execution_score": d["infrastructure_execution_score"],
        "infrastructure_stress_score": d["infrastructure_stress_score"],
        "legal_implementation_risk_score": d["legal_implementation_risk_score"],
        "delivery_risk_score": d["delivery_risk_score"],
    }


def write_csv(path: Path, rows: list, columns: list):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=columns)
        w.writeheader()
        for r in rows:
            w.writerow(r)


def run_all(baseline: dict, cfg: dict):
    full_rows = []
    headline_rows = []
    central_runs = {}

    milestone_years = set(cfg["milestone_years"])

    combos = all_scenario_combinations(cfg)
    for scenario, util, fcap in combos:
        params = resolve_params(cfg, scenario, util, fcap)
        series: List[YearState] = run_scenario(params, baseline)
        for state in series:
            row = state_to_row(state, scenario, util, fcap)
            full_rows.append(row)
            if state.year in milestone_years:
                headline_rows.append(row)

    central = central_combinations(cfg)
    for scenario, util, fcap in central:
        params = resolve_params(cfg, scenario, util, fcap)
        central_runs[scenario] = run_scenario(params, baseline)

    write_csv(OUTPUTS / "scenario_summary_full.csv", full_rows, REPORT_COLUMNS)
    write_csv(OUTPUTS / "scenario_summary.csv", headline_rows, REPORT_COLUMNS)

    return full_rows, headline_rows, central_runs


# ---------------------------------------------------------------------------
# Charts
# ---------------------------------------------------------------------------

SCENARIO_COLORS = {
    "A_baseline": "#888888",
    "B_moderate": "#4a90d9",
    "C_max_central": "#1f5f1f",
    "D_max_high_build": "#1f8b1f",
    "E_max_drag": "#d94a4a",
    "F_legal_collision": "#c47a00",
}


def _series(states: List[YearState], attr: str):
    return [getattr(s, attr) for s in states]


def _years(states: List[YearState]):
    return [s.year for s in states]


def render_chart(central_runs: dict, attr: str, title: str, ylabel: str, filename: str, real_format: bool = False):
    fig, ax = plt.subplots(figsize=(9, 5))
    for scen, series in central_runs.items():
        ax.plot(_years(series), _series(series, attr),
                color=SCENARIO_COLORS.get(scen, "#000"), label=scen, linewidth=2)
    ax.set_title(title)
    ax.set_xlabel("Year")
    ax.set_ylabel(ylabel)
    ax.legend(loc="best", fontsize=8)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    CHARTS.mkdir(parents=True, exist_ok=True)
    fig.savefig(CHARTS / filename, dpi=120)
    plt.close(fig)


def render_all_charts(central_runs: dict):
    chart_specs = [
        ("housing_stock", "Housing stock by scenario", "Housing units", "housing_stock.png"),
        ("annual_completions", "Annual completions by scenario", "Units/year", "annual_completions.png"),
        ("annual_occupied_new_units", "Occupied new units by scenario", "Units/year", "annual_occupied_new_units.png"),
        ("delayed_completed_units_due_to_utilities", "Utility-delayed completed units", "Units (backlog)", "delayed_units.png"),
        ("population", "Population by scenario", "Persons", "population.png"),
        ("median_gross_rent_real_2024", "Median rent (real 2024 USD) by scenario", "USD/month", "rent_real.png"),
        ("median_home_value_real_2024", "Median home value (real 2024 USD)", "USD", "home_value_real.png"),
        ("rent_to_income_ratio", "Rent-to-income ratio by scenario", "Annual rent / median HH income", "rent_to_income.png"),
        ("residual_income_after_rent", "Residual income after rent (real 2024 USD)", "USD/year", "residual_income.png"),
        ("homelessness_pressure_index", "Homelessness pressure index (50=baseline)", "Index 0-100", "hpi.png"),
        ("employer_establishments", "Employer establishments by scenario", "Establishments", "establishments.png"),
        ("commercial_vitality_index", "Commercial vitality index", "Index (100=baseline)", "commercial_vitality.png"),
        ("gross_new_public_revenue", "Gross new public revenue", "USD/year", "gross_revenue.png"),
        ("net_new_public_revenue_after_service_costs", "Net new public revenue (after service costs)", "USD/year", "net_revenue.png"),
        ("infrastructure_funding_gap", "Infrastructure funding gap", "USD/year", "infra_funding_gap.png"),
        ("share_of_infrastructure_need_self_funded_by_growth", "Share of infrastructure self-funded by growth", "Share 0-1", "infra_self_funded_share.png"),
        ("infrastructure_stress_score", "Infrastructure stress score", "Index 0-100", "infra_stress.png"),
        ("legal_implementation_risk_score", "Legal/implementation risk score", "Index 0-100", "legal_risk.png"),
        ("delivery_risk_score", "Delivery risk score", "Index 0-100", "delivery_risk.png"),
    ]
    for attr, title, ylabel, fname in chart_specs:
        render_chart(central_runs, attr, title, ylabel, fname)


# ---------------------------------------------------------------------------
# Entry
# ---------------------------------------------------------------------------

def main():
    baseline = load_baseline(DATA / "baseline_assumptions.json")
    cfg = load_scenario_config(DATA / "scenario_parameters.json")

    OUTPUTS.mkdir(parents=True, exist_ok=True)
    CHARTS.mkdir(parents=True, exist_ok=True)

    full_rows, headline_rows, central_runs = run_all(baseline, cfg)

    print(f"Wrote {len(full_rows)} full rows, {len(headline_rows)} milestone-year rows.")
    render_all_charts(central_runs)
    print(f"Charts written to {CHARTS}")

    reforms_to_csv(OUTPUTS / "reform_menu.csv")
    print("Reform menu written.")

    try:
        from src.sensitivity import run_sensitivity
        run_sensitivity(baseline, cfg, OUTPUTS)
        print("Sensitivity tornado written.")
    except Exception as exc:
        print(f"Sensitivity step failed: {exc}", file=sys.stderr)


if __name__ == "__main__":
    main()
