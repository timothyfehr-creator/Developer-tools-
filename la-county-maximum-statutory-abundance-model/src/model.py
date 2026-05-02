"""
LA County Maximum Statutory Abundance — equation core.

Annual time step 2026-2045. Each per-year module is a pure function.
Funnel: legal capacity -> entitlements -> permits -> completions -> energized -> occupied.
All cross-module feedbacks are 1-year lagged; no within-year fixed-point iteration.

Evidence labeling: every parameter sourced in data/baseline_assumptions.json carries
an evidence tag (strong / medium / weak / speculative). The model deliberately does
not pretend to higher precision than the inputs justify.
"""

from __future__ import annotations

from dataclasses import dataclass, field, asdict
from typing import Dict, List
import math


# ---------------------------------------------------------------------------
# State container
# ---------------------------------------------------------------------------

@dataclass
class YearState:
    year: int

    legal_capacity_cumulative: float = 0.0
    annual_entitlements: float = 0.0
    annual_permits: float = 0.0
    annual_completions: float = 0.0
    annual_energized: float = 0.0
    annual_occupied_new_units: float = 0.0

    entitlement_backlog: Dict[int, float] = field(default_factory=dict)
    permit_backlog: Dict[int, float] = field(default_factory=dict)
    completion_backlog: Dict[int, float] = field(default_factory=dict)

    housing_stock: float = 0.0
    cumulative_net_new_units: float = 0.0
    delayed_completed_units_due_to_utilities: float = 0.0

    population: float = 0.0
    households: float = 0.0
    persons_per_household: float = 0.0
    desired_population: float = 0.0
    crowding_proxy: float = 0.0

    median_gross_rent_real_2024: float = 0.0
    median_gross_rent_nominal: float = 0.0
    median_home_value_real_2024: float = 0.0
    median_home_value_nominal: float = 0.0
    rent_to_income_ratio: float = 0.0
    residual_income_after_rent: float = 0.0

    median_household_income_real_2024: float = 0.0
    median_household_income_nominal: float = 0.0
    per_capita_income_real_2024: float = 0.0
    poverty_rate: float = 0.0

    homelessness_pressure_index: float = 50.0
    estimated_homelessness_cost_avoidance: float = 0.0

    employer_establishments: float = 0.0
    employment: float = 0.0
    annual_payroll: float = 0.0
    accommodation_food_sales: float = 0.0
    commercial_vitality_index: float = 100.0

    gross_new_public_revenue: float = 0.0
    net_new_public_revenue_after_service_costs: float = 0.0
    estimated_benefit_cost_avoidance: float = 0.0
    infrastructure_reinvestment_capacity: float = 0.0
    infrastructure_funding_gap: float = 0.0
    years_until_growth_fiscal_dividend_turns_positive: float = -1.0
    share_of_infrastructure_need_self_funded_by_growth: float = 0.0

    fiscal_score: float = 50.0
    fiscal_leakage_score: float = 50.0
    fiscal_alignment_score: float = 50.0
    infrastructure_execution_score: float = 50.0
    infrastructure_stress_score: float = 50.0
    legal_implementation_risk_score: float = 50.0
    delivery_risk_score: float = 50.0

    cpi_index: float = 1.0
    construction_labor_pool: float = 0.0
    utility_capacity_units: float = 0.0
    reinvestment_pool_prior: float = 0.0


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _draw_from_backlog(backlog: Dict[int, float], year: int, lag_cdf: List[float]) -> tuple[float, Dict[int, float]]:
    """Draw a fraction of each vintage from a backlog dict using a CDF.

    lag_cdf[k] is the cumulative share that has been released by k+1 years after entry.
    Returns (drawn_total, updated_backlog).
    """
    drawn_total = 0.0
    new_backlog: Dict[int, float] = {}
    for vintage, remaining in backlog.items():
        age = year - vintage
        if age < 1:
            new_backlog[vintage] = remaining
            continue
        idx = min(age - 1, len(lag_cdf) - 1)
        prev_idx = idx - 1
        cdf_now = lag_cdf[idx]
        cdf_prev = lag_cdf[prev_idx] if prev_idx >= 0 else 0.0
        if cdf_now >= 1.0 - 1e-9:
            drawn_total += remaining
        else:
            cohort_total = remaining / max(1.0 - cdf_prev, 1e-6)
            draw = cohort_total * (cdf_now - cdf_prev)
            draw = min(draw, remaining)
            drawn_total += draw
            still_remaining = remaining - draw
            if still_remaining > 1.0:
                new_backlog[vintage] = still_remaining
    return drawn_total, new_backlog


def _zscore(value: float, anchor: float) -> float:
    """Crude z-score against an anchor (the baseline value); 1 standard 'unit' = 10% deviation."""
    if anchor == 0:
        return 0.0
    return (value - anchor) / (anchor * 0.10)


# ---------------------------------------------------------------------------
# Module 1: Legal capacity
# ---------------------------------------------------------------------------

def step_legal_capacity(prev: YearState, params: dict, baseline: dict) -> dict:
    base_legal = params["legal_capacity_baseline_units"]
    multiplier = params["zoning_capacity_multiplier"]
    transit = params["transit_corridor_uplift"]
    missing_middle = params["missing_middle_share_legalized"]
    o2r = params["office_to_residential_capacity"]
    religious = params["religious_land_capacity"]
    public_land = params["public_land_capacity"]

    annual_target = base_legal * multiplier * (1 + transit) * (1 + 0.5 * missing_middle)
    annual_extra = (o2r + religious + public_land) / max(params["legal_capacity_phase_in_years"], 1)

    phase_in_years = params["legal_capacity_phase_in_years"]
    years_since_start = max(0, prev.year + 1 - params["horizon_start"])
    phase_in_factor = min(1.0, (years_since_start + 1) / phase_in_years)

    legal_units_this_year = (annual_target + annual_extra) * phase_in_factor
    coastal_fire_haircut = 0.05
    legal_units_this_year *= (1 - coastal_fire_haircut)

    return {
        "legal_capacity_cumulative_delta": legal_units_this_year,
        "legal_capacity_this_year": legal_units_this_year,
    }


# ---------------------------------------------------------------------------
# Module 2: Entitlements
# ---------------------------------------------------------------------------

def step_entitlements(prev: YearState, params: dict, baseline: dict, legal_units_this_year: float) -> dict:
    shot_clock = params["shot_clock_multiplier"]
    resistance = params["local_resistance_haircut"]
    state_backstop = params["state_backstop_effectiveness"]
    litigation = params["litigation_delay_years"]
    objective = params["objective_standard_clarity"]

    effective_resistance = resistance * (1 - state_backstop * 0.7)

    base_conversion = 0.55
    conversion_rate = base_conversion * shot_clock * (1 - effective_resistance) * (0.7 + 0.5 * objective)
    conversion_rate = max(0.0, min(0.95, conversion_rate))

    litigation_drag = max(0.0, 1 - 0.10 * litigation)
    new_entitlements = legal_units_this_year * conversion_rate * litigation_drag

    return {
        "annual_entitlements": new_entitlements,
        "entitlement_conversion_rate": conversion_rate,
    }


# ---------------------------------------------------------------------------
# Module 3: Permits
# ---------------------------------------------------------------------------

def step_permits(prev: YearState, params: dict, baseline: dict, new_entitlements: float) -> dict:
    ministerial = params["ministerial_share"]
    staffing = params["building_dept_staffing_index"]

    permit_rate = (0.55 + 0.40 * ministerial) * staffing
    permit_rate = max(0.30, min(0.99, permit_rate))

    new_permits = new_entitlements * permit_rate

    return {
        "annual_permits": new_permits,
        "permit_rate": permit_rate,
    }


# ---------------------------------------------------------------------------
# Module 4: Construction (permits -> completions)
# ---------------------------------------------------------------------------

def step_completions(prev: YearState, params: dict, baseline: dict, new_permits: float) -> dict:
    cdf_dict = baseline["construction"]["permit_to_completion_lag_cdf"]
    lag_cdf = [cdf_dict[f"year_{i}"] for i in range(1, 6)]

    permit_backlog = dict(prev.permit_backlog)
    permit_backlog[prev.year + 1] = permit_backlog.get(prev.year + 1, 0.0) + new_permits

    drawn, updated_backlog = _draw_from_backlog(permit_backlog, prev.year + 1, lag_cdf)

    labor_baseline = params["construction_labor_capacity_baseline_units"]
    growth_cap_raw = baseline["construction"].get("construction_labor_capacity_growth_cap_per_year", 1.40)
    growth_cap = growth_cap_raw["value"] if isinstance(growth_cap_raw, dict) and "value" in growth_cap_raw else float(growth_cap_raw)

    productivity = 1.0 + params["modular_productivity_lift"]
    cost_inflation_drag = max(0.7, 1 - 0.6 * (params["construction_cost_inflation"] - 0.030))
    financing_drag = 1.0 / max(0.7, params["financing_cost_index"])
    confidence = params["developer_confidence"]

    if prev.construction_labor_pool > 0:
        next_labor_cap = max(labor_baseline, prev.construction_labor_pool * growth_cap)
    else:
        next_labor_cap = labor_baseline

    next_labor_cap *= productivity * cost_inflation_drag * financing_drag * (0.6 + 0.6 * confidence)

    completed = min(drawn, next_labor_cap)
    if drawn > completed:
        unfinished = drawn - completed
        future_year = prev.year + 2
        updated_backlog[future_year] = updated_backlog.get(future_year, 0.0) + unfinished

    return {
        "annual_completions": completed,
        "permit_backlog": updated_backlog,
        "construction_labor_pool": completed,
    }


# ---------------------------------------------------------------------------
# Module 5: Utility / infrastructure connection
# ---------------------------------------------------------------------------

def step_energized(prev: YearState, params: dict, baseline: dict, new_completions: float) -> dict:
    util_baseline = params["utility_capacity_baseline_units"]
    transformer = params["transformer_constraint_factor"]
    ladwp_mod = params["ladwp_modernization_index"]
    lag_months = params["utility_lag_months"]

    util_cap_max_mult = baseline["utilities"]["utility_capacity_max_multiplier"]["value"]
    cost_per_conn = baseline["utilities"]["utility_cost_per_new_connection_usd"]["value"]

    reinvestment_capacity_units = prev.reinvestment_pool_prior / max(cost_per_conn, 1.0)
    capacity = (util_baseline / max(transformer, 0.5)) * ladwp_mod
    capacity += reinvestment_capacity_units
    capacity = min(capacity, util_baseline * util_cap_max_mult)

    completion_backlog = dict(prev.completion_backlog)
    completion_backlog[prev.year + 1] = completion_backlog.get(prev.year + 1, 0.0) + new_completions

    util_lag_cdf = [
        max(0.0, min(1.0, 1 - lag_months / 12)),
        max(0.0, min(1.0, 1 - max(0, lag_months - 12) / 12)),
        1.0,
        1.0,
        1.0,
    ]
    util_lag_cdf = sorted(util_lag_cdf)
    util_lag_cdf = [max(0.05, x) for x in util_lag_cdf]

    drawn, updated_backlog = _draw_from_backlog(completion_backlog, prev.year + 1, util_lag_cdf)

    energized = min(drawn, capacity)
    delayed_units = drawn - energized
    if delayed_units > 0:
        future_year = prev.year + 2
        updated_backlog[future_year] = updated_backlog.get(future_year, 0.0) + delayed_units

    sum_delayed = sum(updated_backlog.values())

    return {
        "annual_energized": energized,
        "completion_backlog": updated_backlog,
        "utility_capacity_units": capacity,
        "delayed_completed_units_due_to_utilities": sum_delayed,
    }


# ---------------------------------------------------------------------------
# Module 6: Occupied
# ---------------------------------------------------------------------------

def step_occupied(prev: YearState, params: dict, baseline: dict, new_energized: float) -> dict:
    occ_rate = baseline["housing"]["occupancy_rate_assumed"]["value"]
    new_occupied = new_energized * occ_rate
    demolition_rate = params["demolition_loss_rate"]

    prior_stock = prev.housing_stock if prev.housing_stock > 0 else baseline["housing"]["housing_units_2024"]["value"]
    demolitions = prior_stock * demolition_rate
    new_stock = prior_stock + new_energized - demolitions
    cumulative_net = new_stock - baseline["housing"]["housing_units_2024"]["value"]

    return {
        "annual_occupied_new_units": new_occupied,
        "housing_stock": new_stock,
        "cumulative_net_new_units": cumulative_net,
    }


# ---------------------------------------------------------------------------
# Module 7: Housing cost
# ---------------------------------------------------------------------------

def step_housing_cost(prev: YearState, params: dict, baseline: dict, new_stock: float) -> dict:
    base_rent = baseline["housing"]["median_gross_rent_2020_2024"]["value"]
    base_value = baseline["housing"]["median_owner_occupied_value_2020_2024"]["value"]
    base_pop = baseline["population"]["estimated_population_2024"]["value"]

    if prev.median_gross_rent_real_2024 == 0.0:
        prev_rent = base_rent
    else:
        prev_rent = prev.median_gross_rent_real_2024

    if prev.median_home_value_real_2024 == 0.0:
        prev_value = base_value
    else:
        prev_value = prev.median_home_value_real_2024

    base_pop_growth_baseline = 0.003
    income_growth = baseline["income"]["real_wage_drift_annual"]["value"]
    drift = params["rent_drift_real"]
    alpha = params["rent_alpha"]
    beta = params["rent_beta_income"]

    prior_stock = prev.housing_stock if prev.housing_stock > 0 else baseline["housing"]["housing_units_2024"]["value"]
    stock_growth = (new_stock - prior_stock) / max(prior_stock, 1.0)

    mu = params["latent_demand_mu"]
    rent_ratio = prev_rent / max(baseline["population"]["peer_metro_rent_anchor"]["value"], 1.0)
    latent_demand_growth = mu * 0.01 * max(0.0, rent_ratio - 1.0)
    population_demand_growth = base_pop_growth_baseline + latent_demand_growth

    net_supply_growth = stock_growth - population_demand_growth

    delta_log_rent = alpha * net_supply_growth + beta * income_growth + drift
    new_rent_real = prev_rent * math.exp(delta_log_rent)

    delta_log_value = 1.5 * delta_log_rent + 0.5 * income_growth
    new_value_real = prev_value * math.exp(delta_log_value)

    cpi = prev.cpi_index if prev.cpi_index > 0 else 1.0
    new_cpi = cpi * 1.025

    new_rent_nominal = new_rent_real * new_cpi
    new_value_nominal = new_value_real * new_cpi

    return {
        "median_gross_rent_real_2024": new_rent_real,
        "median_gross_rent_nominal": new_rent_nominal,
        "median_home_value_real_2024": new_value_real,
        "median_home_value_nominal": new_value_nominal,
        "cpi_index": new_cpi,
        "stock_growth": stock_growth,
        "population_demand_growth": population_demand_growth,
    }


# ---------------------------------------------------------------------------
# Module 8: Population
# ---------------------------------------------------------------------------

def step_population(prev: YearState, params: dict, baseline: dict, new_stock: float, new_rent: float) -> dict:
    base_pop = baseline["population"]["estimated_population_2024"]["value"]
    base_pph = baseline["households"]["persons_per_household"]["value"]
    pph_floor = baseline["households"]["persons_per_household_floor"]["value"]
    pph_ceiling = baseline["households"]["persons_per_household_ceiling"]["value"]
    occupancy = baseline["housing"]["occupancy_rate_assumed"]["value"]
    peer_rent = baseline["population"]["peer_metro_rent_anchor"]["value"]

    mu = params["latent_demand_mu"]
    prev_rent = prev.median_gross_rent_real_2024 if prev.median_gross_rent_real_2024 > 0 else baseline["housing"]["median_gross_rent_2020_2024"]["value"]

    rent_signal = max(0.0, prev_rent / peer_rent - 1.0)
    desired_pop = base_pop * (1 + mu * rent_signal + 0.005 * (prev.year - baseline["_meta"]["anchor_year"]))

    occupied_units = new_stock * occupancy
    max_pop_with_baseline_pph = occupied_units * base_pph

    if desired_pop > max_pop_with_baseline_pph:
        excess = desired_pop / max(max_pop_with_baseline_pph, 1.0) - 1.0
        pph_now = base_pph + 0.3 * excess
        pph_now = min(pph_now, pph_ceiling)
        if params["state_backstop_effectiveness"] < 0.5 and rent_signal > 0.3:
            pph_now = max(pph_now, base_pph)
    else:
        relief = 1 - desired_pop / max(max_pop_with_baseline_pph, 1.0)
        pph_now = base_pph - 0.15 * relief
        pph_now = max(pph_now, pph_floor)

    actual_pop = min(desired_pop, occupied_units * pph_now)
    households = occupied_units
    crowding_proxy = actual_pop / max(occupied_units * base_pph, 1.0)

    return {
        "population": actual_pop,
        "households": households,
        "persons_per_household": pph_now,
        "desired_population": desired_pop,
        "crowding_proxy": crowding_proxy,
    }


# ---------------------------------------------------------------------------
# Module 9: Income / labor market
# ---------------------------------------------------------------------------

def step_income(prev: YearState, params: dict, baseline: dict, population: float, new_rent: float) -> dict:
    base_income = baseline["income"]["median_household_income_2024"]["value"]
    base_pcap = baseline["income"]["per_capita_income_2024"]["value"]
    base_poverty = baseline["income"]["poverty_rate_2024"]["value"]
    base_pop = baseline["population"]["estimated_population_2024"]["value"]

    aggl_per_doubling = params["agglomeration_per_density_doubling"]
    pop_ratio = population / max(base_pop, 1.0)
    if pop_ratio > 0:
        agglomeration_lift = aggl_per_doubling * math.log2(pop_ratio) if pop_ratio >= 1 else aggl_per_doubling * 0.5 * math.log2(pop_ratio)
    else:
        agglomeration_lift = 0.0

    pop_growth_pct = max(0.0, pop_ratio - 1.0)
    moderate_inflow_lift = params["moderate_share_inflow_lift_per_pct_pop_growth"] * pop_growth_pct
    moderate_share_now = baseline["income"].get("moderate_share_baseline", 0.30) if isinstance(baseline["income"].get("moderate_share_baseline"), (int, float)) else params["moderate_share_baseline"]
    moderate_share_delta = moderate_inflow_lift
    composition_factor = 1 - params["income_composition_lambda"] * moderate_share_delta

    median_income_real = base_income * (1 + agglomeration_lift) * composition_factor
    per_capita_real = base_pcap * (1 + agglomeration_lift) * (composition_factor + 0.05)

    poverty_now = base_poverty * (1 - 0.4 * agglomeration_lift) * (1 + 0.2 * moderate_share_delta)
    poverty_now = max(0.04, min(0.30, poverty_now))

    cpi = prev.cpi_index if prev.cpi_index > 0 else 1.0
    median_income_nominal = median_income_real * cpi

    rent_to_income = (new_rent * 12) / max(median_income_real, 1.0)
    residual_income = median_income_real - new_rent * 12

    return {
        "median_household_income_real_2024": median_income_real,
        "median_household_income_nominal": median_income_nominal,
        "per_capita_income_real_2024": per_capita_real,
        "poverty_rate": poverty_now,
        "rent_to_income_ratio": rent_to_income,
        "residual_income_after_rent": residual_income,
    }


# ---------------------------------------------------------------------------
# Module 10: Homelessness pressure
# ---------------------------------------------------------------------------

def step_homelessness(prev: YearState, params: dict, baseline: dict, year_state: dict) -> dict:
    base_rent = baseline["housing"]["median_gross_rent_2020_2024"]["value"]
    base_income = baseline["income"]["median_household_income_2024"]["value"]
    base_residual = base_income - base_rent * 12
    base_rent_to_income = (base_rent * 12) / base_income

    rent_to_income_now = year_state["rent_to_income_ratio"]
    dev_rent_income = (rent_to_income_now - base_rent_to_income) / base_rent_to_income

    prev_rent = prev.median_gross_rent_real_2024 if prev.median_gross_rent_real_2024 > 0 else base_rent
    rent_growth = (year_state["median_gross_rent_real_2024"] - prev_rent) / max(prev_rent, 1.0)
    dev_rent_growth = rent_growth - 0.005

    eli_share = baseline["homelessness"]["eli_share_of_new_units_baseline"]["value"]
    base_eli_pipeline = 19809 * 0.85 * eli_share
    new_eli_units = max(0.0, year_state.get("annual_occupied_new_units", 0.0)) * eli_share * 1.5
    dev_eli = (new_eli_units - base_eli_pipeline) / max(base_eli_pipeline, 1.0)

    base_pop = baseline["population"]["estimated_population_2024"]["value"]
    pop_growth = (year_state.get("population", base_pop) - base_pop) / max(base_pop, 1.0)
    dev_employment = pop_growth

    dev_residual = (year_state["residual_income_after_rent"] - base_residual) / max(base_residual, 1.0)

    hpi = (
        50.0
        + 30.0 * math.tanh(dev_rent_income * 4.0)
        + 15.0 * math.tanh(dev_rent_growth * 50.0)
        - 10.0 * math.tanh(dev_eli)
        - 10.0 * math.tanh(dev_employment * 25.0)
        - 12.0 * math.tanh(dev_residual * 4.0)
    )
    hpi = max(0.0, min(100.0, hpi))

    base_unsheltered = baseline["homelessness"]["estimated_unsheltered_population_la_county"]["value"]
    cost_per_person = baseline["homelessness"]["cost_per_unsheltered_person_year_central"]["value"]
    delta_hpi = 50.0 - hpi
    persons_avoided = (delta_hpi / 50.0) * base_unsheltered * 0.6
    cost_avoidance = max(0.0, persons_avoided * cost_per_person)

    return {
        "homelessness_pressure_index": hpi,
        "estimated_homelessness_cost_avoidance": cost_avoidance,
    }


# ---------------------------------------------------------------------------
# Module 11: Business formation / commercial vitality
# ---------------------------------------------------------------------------

def step_business(prev: YearState, params: dict, baseline: dict, year_state: dict) -> dict:
    base_estab = baseline["business"]["employer_establishments_2023"]["value"]
    base_employment = baseline["business"]["total_employment_2023"]["value"]
    base_payroll = baseline["business"]["annual_payroll_2023_usd"]["value"]
    base_food_sales = baseline["business"]["accommodation_food_sales_2022_usd"]["value"]
    base_pop = baseline["population"]["estimated_population_2024"]["value"]

    pop_ratio = year_state.get("population", base_pop) / max(base_pop, 1.0)
    friction = params["permitting_friction_index"]
    friction_lift = (1.0 / max(friction, 0.4)) ** abs(params["commercial_friction_elasticity"])
    density_lift = pop_ratio ** params["commercial_density_elasticity"]

    estab = base_estab * pop_ratio * friction_lift ** 0.5
    employment = base_employment * pop_ratio * (1 + 0.2 * (friction_lift - 1.0))
    payroll = base_payroll * (employment / base_employment) * (1 + 0.6 * (year_state["per_capita_income_real_2024"] / baseline["income"]["per_capita_income_2024"]["value"] - 1.0)) * (year_state.get("cpi_index", 1.0))
    food_sales = base_food_sales * pop_ratio * density_lift * friction_lift * year_state.get("cpi_index", 1.0)

    commercial_vitality_index = 100.0 * pop_ratio * density_lift * friction_lift
    commercial_vitality_index = max(50.0, min(250.0, commercial_vitality_index))

    return {
        "employer_establishments": estab,
        "employment": employment,
        "annual_payroll": payroll,
        "accommodation_food_sales": food_sales,
        "commercial_vitality_index": commercial_vitality_index,
    }


# ---------------------------------------------------------------------------
# Module 12: Fiscal / infrastructure
# ---------------------------------------------------------------------------

def step_fiscal(prev: YearState, params: dict, baseline: dict, year_state: dict, fiscal_year: int) -> dict:
    fdict = baseline["fiscal"]
    f = {k: v["value"] if isinstance(v, dict) and "value" in v else v for k, v in fdict.items()}
    base_pop = baseline["population"]["estimated_population_2024"]["value"]
    base_units = baseline["housing"]["housing_units_2024"]["value"]

    new_units_this_year = year_state.get("annual_occupied_new_units", 0.0)
    cumulative_new_units = year_state.get("cumulative_net_new_units", 0.0)

    new_value = year_state.get("median_home_value_nominal", baseline["housing"]["median_owner_occupied_value_2020_2024"]["value"])
    property_tax_per_unit = f["property_tax_rate"] * new_value * f["la_share_post_eraf"]
    property_tax_revenue = property_tax_per_unit * cumulative_new_units * 0.85

    sales_tax_one_time = (
        f["sales_tax_rate_combined"] * f["sales_tax_local_share_of_combined"]
        * f["construction_materials_taxable_per_unit"] * new_units_this_year
    )
    new_households = cumulative_new_units * 0.97
    sales_tax_recurring = (
        f["sales_tax_rate_combined"] * f["sales_tax_local_share_of_combined"]
        * f["annual_taxable_spend_per_household"] * new_households
    )

    population_now = year_state.get("population", base_pop)
    delta_pop = max(0.0, population_now - base_pop)
    income_tax_revenue = (
        f["income_tax_state_marginal_for_growth"]
        * year_state.get("per_capita_income_real_2024", 45000.0) * delta_pop
        * f["income_tax_share_returned_to_la_infrastructure"]
    )

    utility_revenue = f["utility_revenue_per_unit_annual"] * cumulative_new_units * 0.10
    business_revenue_lift = (
        (year_state.get("annual_payroll", 0.0) - baseline["business"]["annual_payroll_2023_usd"]["value"])
        * 0.001
    )
    business_revenue_lift = max(0.0, business_revenue_lift)

    gross_revenue = (
        property_tax_revenue + sales_tax_one_time + sales_tax_recurring
        + income_tax_revenue + utility_revenue + business_revenue_lift
    )

    service_cost = f["service_cost_per_capita_annual"] * delta_pop * (1 + 0.025) ** (fiscal_year - baseline["_meta"]["anchor_year"])
    infra_capex_need = f["infrastructure_capex_per_unit_one_time"] * new_units_this_year
    infra_opex_need = f["infrastructure_opex_per_unit_annual"] * cumulative_new_units

    homelessness_savings = year_state.get("estimated_homelessness_cost_avoidance", 0.0)
    benefit_savings = max(0.0, (baseline["income"]["poverty_rate_2024"]["value"] - year_state.get("poverty_rate", baseline["income"]["poverty_rate_2024"]["value"])) * population_now * 4500.0)

    net_revenue = gross_revenue + homelessness_savings + benefit_savings - service_cost - infra_opex_need

    capture_rate = params["fiscal_capture_rate"]
    feasibility_drag = 1 - params.get("value_capture_feasibility_drag", 0.05)
    reinvestment = max(0.0, capture_rate * net_revenue * feasibility_drag)

    funding_gap = max(0.0, infra_capex_need - reinvestment)
    share_self_funded = min(1.0, reinvestment / max(infra_capex_need, 1.0))

    if prev.years_until_growth_fiscal_dividend_turns_positive < 0:
        years_to_positive = float(fiscal_year - baseline["_meta"]["anchor_year"]) if net_revenue > 0 else -1.0
    else:
        years_to_positive = prev.years_until_growth_fiscal_dividend_turns_positive

    fiscal_score = max(0.0, min(100.0, 50.0 + 0.000000005 * net_revenue))
    fiscal_leakage_score = 100.0 - 100.0 * f["income_tax_share_returned_to_la_infrastructure"] * 4
    fiscal_leakage_score = max(0.0, min(100.0, fiscal_leakage_score))
    fiscal_alignment_score = max(0.0, min(100.0, 30.0 + 70.0 * capture_rate * feasibility_drag))

    return {
        "gross_new_public_revenue": gross_revenue,
        "net_new_public_revenue_after_service_costs": net_revenue,
        "estimated_benefit_cost_avoidance": benefit_savings,
        "infrastructure_reinvestment_capacity": reinvestment,
        "infrastructure_funding_gap": funding_gap,
        "share_of_infrastructure_need_self_funded_by_growth": share_self_funded,
        "years_until_growth_fiscal_dividend_turns_positive": years_to_positive,
        "fiscal_score": fiscal_score,
        "fiscal_leakage_score": fiscal_leakage_score,
        "fiscal_alignment_score": fiscal_alignment_score,
        "reinvestment_pool_for_next_year": reinvestment,
    }


# ---------------------------------------------------------------------------
# Module 13: Risk
# ---------------------------------------------------------------------------

def step_risk(prev: YearState, params: dict, baseline: dict, year_state: dict, fiscal_year: int) -> dict:
    preemption = (params["zoning_capacity_multiplier"] - 1.0) / 1.6
    preemption = max(0.0, min(1.0, preemption))
    ceqa = (1.0 - params.get("permitting_friction_index", 1.0))
    enforcement_gap = 1.0 - params["state_backstop_effectiveness"]
    local_resistance = params["local_resistance_haircut"]
    litigation = min(1.0, params["litigation_delay_years"] / 3.0)
    political_reversal = min(1.0, params["political_reversal_risk_annual"] * (fiscal_year - baseline["_meta"]["anchor_year"]) / 5.0)

    legal_risk = (
        20 * preemption + 15 * ceqa + 10 * enforcement_gap
        + 10 * local_resistance + 10 * litigation + 10 * political_reversal
    )
    legal_risk = max(0.0, min(100.0, legal_risk))

    util_lag = params["utility_lag_months"]
    util_risk = min(1.0, util_lag / 24.0)
    labor_short = max(0.0, 1.0 - params["construction_labor_capacity_baseline_units"] / 80000.0)
    capital_risk = max(0.0, params["financing_cost_index"] - 1.0)
    funding_inadequacy = max(0.0, 1.0 - params["infrastructure_funding_adequacy"])

    delivery_risk = (
        25 * util_risk + 20 * labor_short + 15 * capital_risk
        + 20 * funding_inadequacy + 10 * litigation + 10 * local_resistance
    )
    delivery_risk = max(0.0, min(100.0, delivery_risk))

    infra_exec = max(0.0, 100.0 - 100 * util_risk - 50 * funding_inadequacy)
    infra_exec = max(0.0, min(100.0, infra_exec))

    pop_now = year_state.get("population", baseline["population"]["estimated_population_2024"]["value"])
    base_pop = baseline["population"]["estimated_population_2024"]["value"]
    pop_growth = (pop_now - base_pop) / max(base_pop, 1.0)
    delayed_units = year_state.get("delayed_completed_units_due_to_utilities", 0.0)
    cum_units = max(1.0, year_state.get("cumulative_net_new_units", 0.0) + delayed_units)
    delayed_share = delayed_units / cum_units
    fiscal_align = year_state.get("fiscal_alignment_score", 30.0) / 100.0
    util_lift = (params.get("ladwp_modernization_index", 1.0) - 1.0)
    infra_stress = 40.0 + 70.0 * pop_growth - 25.0 * fiscal_align - 15.0 * util_lift + 35.0 * delayed_share
    infra_stress = max(0.0, min(100.0, infra_stress))

    return {
        "legal_implementation_risk_score": legal_risk,
        "delivery_risk_score": delivery_risk,
        "infrastructure_execution_score": infra_exec,
        "infrastructure_stress_score": infra_stress,
    }


# ---------------------------------------------------------------------------
# Orchestrator
# ---------------------------------------------------------------------------

def init_state(baseline: dict, start_year: int) -> YearState:
    h = baseline["housing"]
    p = baseline["population"]
    inc = baseline["income"]
    biz = baseline["business"]

    return YearState(
        year=start_year - 1,
        housing_stock=h["housing_units_2024"]["value"],
        cumulative_net_new_units=0.0,
        population=p["estimated_population_2024"]["value"],
        households=baseline["households"]["households_2020_2024"]["value"],
        persons_per_household=baseline["households"]["persons_per_household"]["value"],
        median_gross_rent_real_2024=h["median_gross_rent_2020_2024"]["value"],
        median_gross_rent_nominal=h["median_gross_rent_2020_2024"]["value"],
        median_home_value_real_2024=h["median_owner_occupied_value_2020_2024"]["value"],
        median_home_value_nominal=h["median_owner_occupied_value_2020_2024"]["value"],
        median_household_income_real_2024=inc["median_household_income_2024"]["value"],
        median_household_income_nominal=inc["median_household_income_2024"]["value"],
        per_capita_income_real_2024=inc["per_capita_income_2024"]["value"],
        poverty_rate=inc["poverty_rate_2024"]["value"],
        employer_establishments=biz["employer_establishments_2023"]["value"],
        employment=biz["total_employment_2023"]["value"],
        annual_payroll=biz["annual_payroll_2023_usd"]["value"],
        accommodation_food_sales=biz["accommodation_food_sales_2022_usd"]["value"],
        rent_to_income_ratio=(h["median_gross_rent_2020_2024"]["value"] * 12) / inc["median_household_income_2024"]["value"],
        residual_income_after_rent=inc["median_household_income_2024"]["value"] - h["median_gross_rent_2020_2024"]["value"] * 12,
        cpi_index=1.0,
        construction_labor_pool=0.0,
        utility_capacity_units=baseline["utilities"]["utility_capacity_baseline_units_per_year"]["value"],
        reinvestment_pool_prior=0.0,
    )


def run_one_year(prev: YearState, params: dict, baseline: dict) -> YearState:
    year = prev.year + 1
    state = YearState(year=year)

    legal_out = step_legal_capacity(prev, params, baseline)
    state.legal_capacity_cumulative = prev.legal_capacity_cumulative + legal_out["legal_capacity_this_year"]

    ent_out = step_entitlements(prev, params, baseline, legal_out["legal_capacity_this_year"])
    state.annual_entitlements = ent_out["annual_entitlements"]

    perm_out = step_permits(prev, params, baseline, state.annual_entitlements)
    state.annual_permits = perm_out["annual_permits"]

    comp_out = step_completions(prev, params, baseline, state.annual_permits)
    state.annual_completions = comp_out["annual_completions"]
    state.permit_backlog = comp_out["permit_backlog"]
    state.construction_labor_pool = comp_out["construction_labor_pool"]

    energ_out = step_energized(prev, params, baseline, state.annual_completions)
    state.annual_energized = energ_out["annual_energized"]
    state.completion_backlog = energ_out["completion_backlog"]
    state.utility_capacity_units = energ_out["utility_capacity_units"]
    state.delayed_completed_units_due_to_utilities = energ_out["delayed_completed_units_due_to_utilities"]

    occ_out = step_occupied(prev, params, baseline, state.annual_energized)
    state.annual_occupied_new_units = occ_out["annual_occupied_new_units"]
    state.housing_stock = occ_out["housing_stock"]
    state.cumulative_net_new_units = occ_out["cumulative_net_new_units"]

    cost_out = step_housing_cost(prev, params, baseline, state.housing_stock)
    state.median_gross_rent_real_2024 = cost_out["median_gross_rent_real_2024"]
    state.median_gross_rent_nominal = cost_out["median_gross_rent_nominal"]
    state.median_home_value_real_2024 = cost_out["median_home_value_real_2024"]
    state.median_home_value_nominal = cost_out["median_home_value_nominal"]
    state.cpi_index = cost_out["cpi_index"]

    pop_out = step_population(prev, params, baseline, state.housing_stock, state.median_gross_rent_real_2024)
    state.population = pop_out["population"]
    state.households = pop_out["households"]
    state.persons_per_household = pop_out["persons_per_household"]
    state.desired_population = pop_out["desired_population"]
    state.crowding_proxy = pop_out["crowding_proxy"]

    inc_out = step_income(prev, params, baseline, state.population, state.median_gross_rent_real_2024)
    state.median_household_income_real_2024 = inc_out["median_household_income_real_2024"]
    state.median_household_income_nominal = inc_out["median_household_income_nominal"]
    state.per_capita_income_real_2024 = inc_out["per_capita_income_real_2024"]
    state.poverty_rate = inc_out["poverty_rate"]
    state.rent_to_income_ratio = inc_out["rent_to_income_ratio"]
    state.residual_income_after_rent = inc_out["residual_income_after_rent"]

    yr_dict = asdict(state)
    hl_out = step_homelessness(prev, params, baseline, yr_dict)
    state.homelessness_pressure_index = hl_out["homelessness_pressure_index"]
    state.estimated_homelessness_cost_avoidance = hl_out["estimated_homelessness_cost_avoidance"]

    yr_dict = asdict(state)
    biz_out = step_business(prev, params, baseline, yr_dict)
    state.employer_establishments = biz_out["employer_establishments"]
    state.employment = biz_out["employment"]
    state.annual_payroll = biz_out["annual_payroll"]
    state.accommodation_food_sales = biz_out["accommodation_food_sales"]
    state.commercial_vitality_index = biz_out["commercial_vitality_index"]

    yr_dict = asdict(state)
    fisc_out = step_fiscal(prev, params, baseline, yr_dict, year)
    state.gross_new_public_revenue = fisc_out["gross_new_public_revenue"]
    state.net_new_public_revenue_after_service_costs = fisc_out["net_new_public_revenue_after_service_costs"]
    state.estimated_benefit_cost_avoidance = fisc_out["estimated_benefit_cost_avoidance"]
    state.infrastructure_reinvestment_capacity = fisc_out["infrastructure_reinvestment_capacity"]
    state.infrastructure_funding_gap = fisc_out["infrastructure_funding_gap"]
    state.share_of_infrastructure_need_self_funded_by_growth = fisc_out["share_of_infrastructure_need_self_funded_by_growth"]
    state.years_until_growth_fiscal_dividend_turns_positive = fisc_out["years_until_growth_fiscal_dividend_turns_positive"]
    state.fiscal_score = fisc_out["fiscal_score"]
    state.fiscal_leakage_score = fisc_out["fiscal_leakage_score"]
    state.fiscal_alignment_score = fisc_out["fiscal_alignment_score"]
    state.reinvestment_pool_prior = fisc_out["reinvestment_pool_for_next_year"]

    yr_dict = asdict(state)
    risk_out = step_risk(prev, params, baseline, yr_dict, year)
    state.legal_implementation_risk_score = risk_out["legal_implementation_risk_score"]
    state.delivery_risk_score = risk_out["delivery_risk_score"]
    state.infrastructure_execution_score = risk_out["infrastructure_execution_score"]
    state.infrastructure_stress_score = risk_out["infrastructure_stress_score"]

    return state


def run_scenario(params: dict, baseline: dict) -> List[YearState]:
    start = params["horizon_start"]
    end = params["horizon_end"]

    prev = init_state(baseline, start)
    series: List[YearState] = []
    for _ in range(end - start + 1):
        new = run_one_year(prev, params, baseline)
        series.append(new)
        prev = new
    return series
