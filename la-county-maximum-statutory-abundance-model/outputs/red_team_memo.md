# Red-team memo: why this model could be wrong

This memo is the deliberately hostile critique of the LA County Maximum Statutory Abundance model. It is structured around the 25 failure modes specified in the project brief plus a handful added during implementation.

The model's central case (Scenario C, util_improved, fcap_partial) shows ~1.6M cumulative net new units by 2045, population reaching ~11.6M, real rent rising ~8.5% over 20 years vs ~18% under baseline, and a fiscal dividend of ~$11.7B/yr by 2045 with ~$3.3B/yr available for infrastructure reinvestment. Below is why each of those numbers might be substantially wrong, in approximate order of how much I worry about them.

## 1. Legal capacity ≠ delivered housing

This is the failure mode the model is most explicitly designed to address — and yet the model still risks understating it. We route legal capacity through entitlements → permits → completions → energization → occupation, with multipliers and lags at each stage. But the model's legal-capacity multipliers under Scenario C (zoning_capacity_multiplier 2.20, missing-middle 0.55, transit uplift 0.45) are themselves *political-feasibility* parameters, not legal-feasibility parameters. The legal floor could be enacted yet have local governments reduce *de facto* zoning through floor-area ratios, height-overlay reductions, lot-coverage limits, ground-floor activation rules, and other parameters not preempted by the state floor. The model treats those as captured by `local_resistance_haircut`. They could easily be larger.

Implication: even my "central" 1.6M number could be 30-50% optimistic.

## 2. Local governments comply on paper but sabotage administratively

The model treats `local_resistance_haircut` and `state_backstop_effectiveness` as continuous parameters. In reality, sabotage is lumpy. A coastal-strip city can lose 90% of cases on appeal and still effectively block 80% of projects through delay, site-plan review, traffic studies, geotechnical re-review, fire-marshal interpretations, and serial revisions. The state backstop office I model assumes a level of HCD administrative capacity that does not exist today and would require substantial new staffing.

Implication: F (legal collision) may be the more realistic case for cities like Beverly Hills, Manhattan Beach, Santa Monica, La Cañada Flintridge, Calabasas, San Marino, and Rolling Hills.

## 3. Utilities become the new CEQA

The model already shows this: in `util_severe_bottleneck` cases, cumulative production collapses. But the model's central case assumes `util_improved` (75k/yr capacity, 5-month lag, transformer constraint at 0.6). This is a *substantial* assumption about LADWP, SCE, and SoCalGas execution. LADWP is municipally owned, not CPUC-regulated, and politically protected by an LA City Council that may resist state-imposed shot clocks. The transformer supply chain is global and constrained by IRA-driven demand from data centers, EV chargers, and grid-scale storage. We mark `transformer_lead_time_months_baseline` as `SOURCE_NEEDED` (evidence: weak) because reliable LA-specific data is not public.

Implication: util_current_drag may be the realistic central case, dropping cumulative production to ~700k by 2045 — half the headline.

## 4. Construction labor and materials become binding constraints

The model uses a `construction_labor_capacity_growth_cap_per_year` of 1.40 (40%/yr ramp from rolling 3-yr average). This is generous. Trades labor (electricians, plumbers, elevator techs, sheet-metal, pipefitters) is multi-year apprenticeship-gated. Materials inflation is in the model only via `construction_cost_inflation` (3% baseline, 5.5% in Scenario E). But supply shocks are not modeled — Trump-era tariffs, Mexican lumber duties, Chinese steel restrictions, copper-wire shortages all could materially alter the cost trajectory.

Implication: Scenario E's "implementation drag" may be more central than my Scenario C in macro-shock years.

## 5. Interest rates and capital markets limit private development

The model represents financing only via `financing_cost_index` (1.0 baseline, 0.85 high-build, 1.20 drag). It does not model interest-rate path dependence, the bond-market feedback to muni infrastructure financing, the cap-rate sensitivity of multifamily institutional demand, or the relationship between mortgage rates and household formation. A 7% mortgage rate environment could keep ownership demand low and rental demand elevated even as we add supply.

Implication: medium uncertainty band; could swing cumulative units by ±20%.

## 6. Insurance, seismic, fire, and environmental constraints are real

The model applies a 5% "coastal/fire haircut" to legal capacity and assumes federal NEPA, Coastal Act, tribal consultation, seismic, and hazmat rules remain in force. In practice, the California insurance crisis is making multifamily uninsurable in fire-overlay zones and reducing condo construction nationwide. The model's "construction-defect liability reform for condos" is in the reform menu but flagged as politically very hard.

Implication: condo construction may stay near zero. Multifamily in fire-overlay LA County (much of the county outside the basin) may face insurance-driven cost increases that aren't in the model.

## 7. High latent demand absorbs new supply, so LA gets larger but remains expensive

This is by far the model's most important *expected* result and also its biggest source of disappointment. Under Scenario D (high build), population reaches 12.0M (+22% over baseline) but real rent only falls relative to counterfactual baseline by 9-10 percentage points. Real rent does *not* fall in absolute terms compared to 2024. The latent-demand parameter `μ` is set to 0.20-0.28 — meaning if LA rent falls 10% relative to peer metros, ~2-3% more population is "called in" by reduced rent. This calibration is consistent with Hsieh-Moretti-implied migration suppression but is itself uncertain. If μ is higher (say 0.35), all new supply is absorbed by migration and rent does not fall at all.

Implication: the policy could be extremely successful at *enabling growth* and disappointing at *lowering rents*. This is closer to the historical pattern than any other model output.

## 8. Median income may fall if LA becomes more accessible to moderate-income households

The model explicitly addresses this via `income_composition_lambda` and the residual-income welfare metric. In our 2045 outputs:
- median HH income real: ~$89.7k-$90.0k across scenarios (essentially flat)
- residual income after rent: $62.2k baseline, $64.3k under abundance (+$2.1k welfare gain)

The composition effect is real but small in our parameterization because population growth is modest. In reality, if abundance opens LA to a much larger working-class inflow (e.g., construction workers, food-service, transit operators), median income could fall 5-10% even as residual income rises. The model does not currently accommodate that scale of compositional shift.

Implication: media/political reaction to "median income fell under YIMBY" could derail the political coalition needed to maintain the reform package — even if welfare unambiguously rose.

## 9. Infrastructure lags reduce quality of life

Population grows, schools fill up, transit overcrowds, parks degrade, water pressure drops. The model's `infrastructure_stress_score` rises from ~42 (baseline 2045) to ~53 (Scenario C 2045) and ~74 (Scenario E 2045). The cost of degraded services may not show up in the dollarized fiscal feedback. Schools especially: state-funded under LCFF, but the local political reaction to overcrowded schools has historically been a *primary* source of NIMBY resistance.

Implication: model under-counts the political-economy backlash to infrastructure stress.

## 10. Commercial permitting reform has weaker empirical grounding than housing reform

Our `commercial_density_elasticity` (0.25), `commercial_friction_elasticity` (-0.30), and the 100-point `commercial_vitality_index` are *speculative* parameters. The literature on commercial permitting reform's effect on establishments, payroll, and food sales is thin. We project that under Scenario C, employer establishments grow from 305k (2023) to 394k (2045, +29%) — but this is mostly mechanical scaling on population growth × density × inverse friction. There is little hard evidence that permitting reform delivers a 30%+ establishment lift over 20 years.

Implication: business and commercial-vitality results should be read as *directional*, not quantitative.

## 11. Coastal/high-income cities litigate successfully around some edges

Beverly Hills, Manhattan Beach, Pacific Palisades areas, La Cañada Flintridge, San Marino: these jurisdictions have the legal budgets and political will to litigate every preemption case to the California Supreme Court. The state may win on broad strokes but lose on details (e.g., specific objective standards, parking-overlay reductions, height transitions). Scenario F (legal collision) is the *honest* base case for these jurisdictions, even if the rest of LA County operates under Scenario C.

Implication: countywide aggregates may average out to something between C and F. But neighborhood-level outcomes will be wildly bimodal.

## 12. The state lacks enforcement capacity

HCD has roughly 250 staff statewide. The reform package requires HCD to monitor, audit, fine, and override 88 jurisdictions in LA County alone. The state permitting backstop office is in our reform menu (`include_in_maximum_scenario: True`) but its actual operational capacity is speculative. State agencies move slowly. The gap between policy on paper and policy in practice has historically been measured in years.

Implication: realistic state backstop effectiveness is 0.40-0.60, not the 0.70 we assume in C central. Drops cumulative production by ~10-15%.

## 13. Political backlash causes partial repeal or underfunding

We model `political_reversal_risk_annual` at 0.02 (2% chance per year of meaningful repeal), but this is not implemented as a stochastic shock — it's a steady drag. In reality, a single year of high salience NIMBY backlash (e.g., a high-profile displacement scandal in a redevelopment project) could trigger a ballot initiative or repeal package. The 2024 Prop 5 fight (which lost) shows how vulnerable abundance-side reforms are to a coordinated opposition campaign.

Implication: 20-year time horizon assumes 5 election cycles of unbroken state political alignment. That is historically rare.

## 14. New development increases land values before it reduces rents

The model captures medium-term filtering but not the early-cycle land-value uplift that occurs when zoning is lifted. In year 1-3 of upzoning, owners of newly-up-zoned land hold for option value, supply does not materialize quickly, but expectations push existing rent up *because the neighborhood is "improving."* The model's `median_home_value_real_2024` rises in Scenario C from $834k to $992k — a +19% real increase. Existing owners get a windfall before any new units arrive.

Implication: short-term political backlash is concentrated in the first 3-5 years, before the supply effect manifests. This is when the policy is most vulnerable to repeal (see #13).

## 15. Displacement and redevelopment effects are concentrated in vulnerable neighborhoods

The model is *countywide*. It does not show that high-friction parcels in Boyle Heights, Westlake, Pico-Union, or South LA may experience disproportionate redevelopment pressure while wealthy neighborhoods continue to obstruct. Tenant displacement, even partial, in low-income neighborhoods can cause severe individual welfare losses that are not in the dollarized model.

Implication: countywide welfare gain ($2.1k residual income/HH) may coexist with concentrated welfare loss in specific neighborhoods. Aggregate-level success is consistent with neighborhood-level harm.

## 16. The growth dividend is real but fiscally misaligned

Our `fiscal_alignment_score` (50 baseline, 70 in D high) and `fiscal_leakage_score` (high under all scenarios because state income-tax revenue mostly does not return to LA infrastructure) attempt to capture this. Net new public revenue in Scenario C 2045 is ~$11.7B/yr but only ~$3.3B/yr is captured for infrastructure reinvestment. The remaining ~$8.4B accrues to schools, the state, ERAF redistribution, and other entities — useful societally, but not available to fund LA's local infrastructure.

Implication: even with strong growth, the *share of infrastructure self-funded by growth* tops out at 100% in Scenario D 2045 only because we assume `fcap_high` (0.6 capture rate). With realistic capture (`fcap_partial`, 0.3), it is ~68%.

## 17. New tax revenue arrives too late to fund upfront infrastructure

Our model has the timing right in one sense: revenue lags construction, capex needs lead it. Scenario C's `years_until_growth_fiscal_dividend_turns_positive` typically lands at ~2-4 years out from anchor — but that's because we count from when *any* net positive revenue accrues. The cumulative cash-flow break-even (when accumulated revenue covers accumulated capex) likely arrives 8-12 years later. The model does not currently produce that statistic. Bond markets can finance the gap, but only at a price.

Implication: state infrastructure bonds and bridge financing are required. Without them, the funding gap turns into actual underinvestment, which feeds back through utility capacity caps to slow energization, which slows the growth dividend itself. This is the model's most important non-linear risk.

## 18. Prop 13 and tax-allocation rules weaken local incentives

Property tax rate is fixed at 1% by Prop 13. New construction is assessed at market value but reassessment rules limit upward adjustment on existing parcels. ERAF redirects 25-50% of property-tax revenue to schools. Cities pursuing growth do not capture proportional fiscal upside; the math is closer to "city gets 20-25% of new property tax, school district gets the rest, county gets some, special districts get some." The model uses `la_share_post_eraf = 0.55` which may overstate the effective city/county capture.

Implication: fiscal capture is structurally weak. The "Property-tax allocation reform for growth" reform in our menu is flagged as politically extremely hard (`political_difficulty_score: 5`) and excluded from the central scenario.

## 19. Service costs rise faster than revenues in some jurisdictions

Our service-cost-per-capita marginal estimate of $1,500/year is on the optimistic side. It assumes most state-funded school capacity scales without local cost; that fire and police are largely fixed; that parks and sanitation scale modestly. In jurisdictions where new construction is heavily concentrated, the marginal service cost may approach $2,500-$3,500/capita. The model assumes a single countywide rate.

Implication: revenues may not cover marginal service costs in growth corridors, even if they cover the countywide average.

## 20. Homelessness savings are slower and smaller than advocates expect

Our `estimated_homelessness_cost_avoidance` reaches ~$0.55B/yr in Scenario C 2035 but falls back to ~$0.35B/yr by 2045 because real rent continues to rise vs the 2024 anchor. The homelessness pressure index drops from 50 to ~36 in mid-period and rebounds to ~41 by 2045. If the empirical evidence (Colburn-Aldern) is right that rent levels dominate, then unsheltered population should fall meaningfully during the 2030-2040 window. But the rebound suggests savings are not durable.

Beyond modeling: lower rents reduce *inflow* to homelessness, but the existing unsheltered population requires permanent supportive housing, mental health treatment, addiction treatment, eviction prevention, and shelter capacity to actually exit homelessness. None of those are in the model. The cost-avoidance number assumes a 60% conversion of HPI deviation to actual unsheltered population — itself a weak assumption.

Implication: $0.35-0.55B/yr is plausibly the upper bound. Real cost avoidance could be half or a third of that, depending on the rest of the homelessness system.

## 21. State income-tax gains do not automatically help local infrastructure

We assume `income_tax_share_returned_to_la_infrastructure = 0.05` — 5% of incremental state income tax accrues to LA infrastructure via grants, transit funding, etc. This is generous. There is no formula or pipeline that automatically routes state income tax growth into LA County local infrastructure. It depends on annual budget negotiations and competes with statewide priorities.

Implication: fiscal leakage is even higher than we model.

## 22. Utility capex needs exceed near-term utility revenue

Our `utility_revenue_per_unit_annual = $1,800` × 1.6M new units = $2.9B/yr ongoing utility revenue from growth. But $45,000 capex per unit × 1.6M = $72B cumulative capex need by 2045. Annual capex burden in peak years could reach $4-6B. Utility revenue alone cannot fund this — it requires bond financing, state matching, or rate increases. None are guaranteed.

Implication: utilities under-resourced is the most likely failure mode in a successful policy regime.

## 23. Value capture reduces project feasibility if overused

Our `value_capture_feasibility_drag` parameter (0.05 baseline, 0.12 in F legal collision) captures this directionally but probably understates it. EIFDs, IFDs, inclusionary zoning, public-benefit fees, prevailing-wage requirements, transit-impact fees — each individually plausible, in aggregate fatal to feasibility. Coastal Commission and CEQA mitigation requirements add more. The model assumes the state actively rationalizes and standardizes; in practice, every reform brings new exactions.

Implication: project feasibility could fail in ways that look like "the policy worked but no one built."

## 24. Infrastructure districts work better in high-value areas than in lower-income areas

EIFDs, CRIAs, value capture: all generate more revenue per acre in high-property-value areas. They produce less revenue per acre in South LA, East LA, and the Antelope Valley. The model's countywide aggregation hides this. Growth corridors that need infrastructure most (because they're the lowest-value, highest-need areas) are the worst at self-funding.

Implication: state grants must subsidize infrastructure in lower-income corridors. Without that, growth concentrates in already-wealthy areas, magnifying existing geographic inequality.

## 25. Fiscal benefits are regionwide but project costs are neighborhood-specific

A new 200-unit building in West LA generates property tax revenue that goes 55% to LA County (fiscal share post-ERAF) — but the immediate infrastructure costs (school capacity, transit access, fire response, water connection) fall on the immediate jurisdiction and special districts. The mismatch between *who pays* and *who benefits* is the structural reason California has not built. The model's fiscal capture variants attempt to address this but cannot solve it without legal/institutional change.

Implication: even Scenario D's "high fiscal capture" is fragile. Underlying mismatch persists.

## Additional concerns I have

### 26. The model is not stochastic

All parameters are deterministic. There is no Monte Carlo over interest rates, immigration, recession risk, climate disasters (LA fires, earthquake), federal policy. A single year of severe shock (e.g., Northridge 2.0, severe wildfire, recession) could push the trajectory toward Scenario E for a decade.

### 27. Latent-demand circularity is partially broken

I use prior-year rent in latent_pop to break the circularity, but the "peer_metro_rent_anchor" of $1,500 is itself a static assumption. In reality, peer metros (Phoenix, Las Vegas, Dallas, Houston) are also growing supply and reducing rent. The relative LA-peer ratio is endogenous in ways the model doesn't capture.

### 28. The 2040+ horizon is extrapolation

Years 2040-2045 are ~15-20 years past the 2024 anchor. Macro structure (interest rates, demographic trends, climate, federal policy, AI/automation impact on labor) cannot be reliably projected at that horizon. The 2045 numbers should be read with at least ±50% uncertainty bands.

### 29. The reform menu's commercial scoring is weak

The 30+ reform menu uses 1-5 scoring for housing impact, commercial impact, etc. These are author judgments, not literature-derived. The scoring is reproducible (in `src/reforms.py`) but not validated.

### 30. The model assumes LA County is solvable as a unit

LA County is 88 cities + unincorporated. The political dynamics, sheriff disputes, water disputes, and fragmented governance make any countywide model an averaging fiction. A more honest model would run city-by-city, but data sparsity makes that impractical.

## Top 5 things that, if true, would invalidate the central case

1. **LADWP/SCE interconnection lag stays at 14+ months** (vs the 5-month assumption in util_improved). Pushes cumulative production from 1.6M to ~700k by 2045.
2. **Latent-demand μ is 0.35+ rather than 0.20**. All new supply absorbed by migration; real rent does not ease. Population reaches 13M+ but residual income gain disappears.
3. **HCD enforcement capacity remains at current ~250 staff**. State backstop effectiveness is 0.30 instead of 0.70. Local sabotage prevails.
4. **Construction-defect insurance crisis kills condo construction permanently**. Removes ~25% of legal capacity from realized production.
5. **A single political reversal in 2030-2032** (e.g., voter rejection of the package) repeals key preemption. Reverts to Scenario A trajectory after a 4-year boom.

## Honest summary

The model's central output — 1.6M cumulative new units, 11.6M population, 8.5% real rent rise vs 18% baseline counterfactual, $11.7B/yr fiscal dividend — is plausibly correct in *direction* but probably 30-50% optimistic in *magnitude*. The honest range for Scenario C delivered units by 2045 is more like 800k-1.4M; for population growth, +10%-20%; for real rent moderation vs counterfactual, 5-12 percentage points; for fiscal dividend, $5-12B/yr.

The model is most reliable in showing relative differences between scenarios. It is least reliable in committing to specific 2045 levels.
