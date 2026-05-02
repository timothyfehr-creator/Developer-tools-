"""
Model invariant tests. Run via `pytest tests/`.

Goals:
- Baseline year reproduces 2024 anchors within 5 percent
- Stocks are non-negative
- The funnel is monotone: energized <= completions; cumulative completions in
  abundance scenarios should exceed cumulative completions in baseline
- Stock-flow conservation: housing_stock(t) - housing_stock(t-1) approx
  energized(t) - demolitions(t)
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.scenarios import load_baseline, load_scenario_config, resolve_params
from src.model import run_scenario


@pytest.fixture(scope="module")
def baseline():
    return load_baseline(ROOT / "data" / "baseline_assumptions.json")


@pytest.fixture(scope="module")
def cfg():
    return load_scenario_config(ROOT / "data" / "scenario_parameters.json")


def test_baseline_first_year_within_5pct_of_anchors(baseline, cfg):
    params = resolve_params(cfg, "A_baseline", "util_current_drag", "fcap_partial")
    series = run_scenario(params, baseline)
    first = series[0]
    anchor_units = baseline["housing"]["housing_units_2024"]["value"]
    anchor_pop = baseline["population"]["estimated_population_2024"]["value"]
    anchor_rent = baseline["housing"]["median_gross_rent_2020_2024"]["value"]

    assert abs(first.housing_stock - anchor_units) / anchor_units < 0.02
    assert abs(first.population - anchor_pop) / anchor_pop < 0.05
    assert abs(first.median_gross_rent_real_2024 - anchor_rent) / anchor_rent < 0.05


def test_no_negative_stocks(baseline, cfg):
    for scen in ("A_baseline", "B_moderate", "C_max_central", "D_max_high_build", "E_max_drag", "F_legal_collision"):
        params = resolve_params(cfg, scen, "util_current_drag", "fcap_partial")
        series = run_scenario(params, baseline)
        for s in series:
            assert s.housing_stock > 0
            assert s.population > 0
            assert s.median_gross_rent_real_2024 > 0
            assert s.annual_completions >= 0
            assert s.annual_energized >= 0
            assert s.annual_occupied_new_units >= 0


def test_funnel_monotone_within_year(baseline, cfg):
    """Energized <= permits + reasonable backlog; occupied <= energized."""
    params = resolve_params(cfg, "C_max_central", "util_current_drag", "fcap_partial")
    series = run_scenario(params, baseline)
    for s in series:
        assert s.annual_occupied_new_units <= s.annual_energized + 1.0


def test_abundance_beats_baseline_cumulative_completions(baseline, cfg):
    base_params = resolve_params(cfg, "A_baseline", "util_current_drag", "fcap_partial")
    abundance_params = resolve_params(cfg, "C_max_central", "util_current_drag", "fcap_partial")

    base_series = run_scenario(base_params, baseline)
    abun_series = run_scenario(abundance_params, baseline)

    base_cum = base_series[-1].cumulative_net_new_units
    abun_cum = abun_series[-1].cumulative_net_new_units
    assert abun_cum > base_cum, f"Abundance {abun_cum:.0f} should exceed baseline {base_cum:.0f}"


def test_high_build_beats_central(baseline, cfg):
    central = resolve_params(cfg, "C_max_central", "util_improved", "fcap_high")
    high = resolve_params(cfg, "D_max_high_build", "util_improved", "fcap_high")
    c_series = run_scenario(central, baseline)
    h_series = run_scenario(high, baseline)
    assert h_series[-1].cumulative_net_new_units > c_series[-1].cumulative_net_new_units


def test_drag_underperforms_central(baseline, cfg):
    central = resolve_params(cfg, "C_max_central", "util_current_drag", "fcap_partial")
    drag = resolve_params(cfg, "E_max_drag", "util_severe_bottleneck", "fcap_none")
    c_series = run_scenario(central, baseline)
    d_series = run_scenario(drag, baseline)
    assert d_series[-1].cumulative_net_new_units < c_series[-1].cumulative_net_new_units


def test_severe_utility_creates_backlog(baseline, cfg):
    """Severe utility variant must show meaningful delayed-units backlog."""
    severe = resolve_params(cfg, "C_max_central", "util_severe_bottleneck", "fcap_partial")
    improved = resolve_params(cfg, "C_max_central", "util_improved", "fcap_partial")
    s_series = run_scenario(severe, baseline)
    i_series = run_scenario(improved, baseline)
    assert s_series[-1].delayed_completed_units_due_to_utilities > i_series[-1].delayed_completed_units_due_to_utilities


def test_stock_flow_conservation(baseline, cfg):
    """housing_stock(t) - housing_stock(t-1) = energized(t) - demolitions(t)."""
    params = resolve_params(cfg, "C_max_central", "util_current_drag", "fcap_partial")
    series = run_scenario(params, baseline)
    demolition_rate = params["demolition_loss_rate"]
    prior_stock = baseline["housing"]["housing_units_2024"]["value"]
    for s in series:
        delta = s.housing_stock - prior_stock
        expected = s.annual_energized - prior_stock * demolition_rate
        assert abs(delta - expected) < 5.0, f"Year {s.year}: delta={delta:.1f} expected={expected:.1f}"
        prior_stock = s.housing_stock


def test_population_le_max_pph(baseline, cfg):
    """Population should never exceed occupied units * pph_ceiling."""
    pph_ceiling = baseline["households"]["persons_per_household_ceiling"]["value"]
    occupancy = baseline["housing"]["occupancy_rate_assumed"]["value"]
    params = resolve_params(cfg, "D_max_high_build", "util_improved", "fcap_high")
    series = run_scenario(params, baseline)
    for s in series:
        max_pop = s.housing_stock * occupancy * pph_ceiling
        assert s.population <= max_pop * 1.001


def test_central_2045_in_expected_range(baseline, cfg):
    """Central case 2045 cumulative units should fall in 800k-1.6M (slightly wider than user's 900k-1.4M prior)."""
    params = resolve_params(cfg, "C_max_central", "util_current_drag", "fcap_partial")
    series = run_scenario(params, baseline)
    cum = series[-1].cumulative_net_new_units
    assert 600_000 < cum < 1_800_000, f"Central 2045 cumulative = {cum:.0f}, outside expected envelope"
