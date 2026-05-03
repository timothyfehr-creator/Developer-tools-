# Maximum Statutory Abundance in Los Angeles County

**A scenario-modeling memo on what California could plausibly do without a constitutional amendment, and what would actually happen if it did**

---

## 1. Executive summary

California has the legal authority — short of a constitutional amendment — to substantially preempt Los Angeles County's housing and commercial-permitting regime. SB 79 (transit density), AB 130/SB 131 (CEQA infill streamlining), SB 35 / SB 423 (ministerial approval), AB 2011 (office-to-residential), AB 2097 (parking minimums), and SB 4 (religious land) are existing precedents. Adding a state zoning floor, a hard ministerial shot clock with deemed-approved backstop, a state permitting office, comprehensive CEQA exemption for infill and grid infrastructure, and standardized commercial-permitting preemption is a reform package the Legislature can enact under the statewide-concern doctrine. Charter cities will sue; most of the housing core is likely to survive.

What the package would *not* do is solve the housing shortage in Los Angeles. The model in this project routes legal capacity through five gates — entitlement, permit, completion, energization, occupation — and finds that the binding constraint shifts from law to physical delivery. In our central case (Scenario C, improved utility execution, partial fiscal capture) Los Angeles County adds roughly **1.6 million net new housing units by 2045** versus roughly **332,000 units in the no-reform baseline**. Population reaches about **11.6 million** versus **11.1 million** in baseline. Real median rent rises about **8.5 percent** over twenty years versus about **18 percent** in baseline — a meaningful improvement, but rent does not fall in absolute terms. Real residual income after rent rises by about **$2,100 per household per year**.

The model also produces a wide spread across scenarios: from roughly **45,000 cumulative units by 2045** under "implementation drag with severe utility bottleneck" to roughly **1.7 million units** under "high build with improved utilities and high fiscal capture." That spread is the most important finding. **The constraint that determines outcomes is not legal authority. It is the simultaneous performance of LADWP, Southern California Edison, the construction-trades labor pool, the state's enforcement capacity, capital markets, and local-government compliance.** Legal preemption opens the funnel; institutional execution determines what comes out the other end.

A growth dividend exists but is fiscally misaligned. Scenario C generates about **$11.7 billion per year in net new public revenue by 2045**, of which roughly **$3.3 billion per year** is captured for infrastructure reinvestment under partial-capture parameters. The remainder leaks to schools (via ERAF), the state (via income tax), and other entities with no direct claim on LA infrastructure. Without targeted fiscal-plumbing reforms — Enhanced Infrastructure Financing Districts, state matching grants, value capture, and a property-tax-allocation fix — local infrastructure investment will run behind population growth, eventually choking the funnel.

The honest forecast is therefore conditional. *If* utility interconnection moves from current 12-22 month lags to 5-8 month service-level agreements, *if* state HCD enforcement actually has the staff to discipline 88 LA County jurisdictions, *if* construction trades expand at 30-40% per year, *if* mortgage and capital-market conditions remain workable, and *if* fiscal capture mechanisms are wired into law — then 1.5-1.7 million net new units and a 10-percentage-point improvement in real rent versus counterfactual is plausible. Lose any of those conditions, and the trajectory collapses toward the baseline or worse.

This memo presents the reform package, the model, the scenario results, the limits of what we can know, and a red-team critique of the central forecast.

---

## 2. Baseline Los Angeles County conditions

The model anchors against the following 2024-vintage values for LA County (Census QuickFacts, ACS 5-year 2020-2024, Census County Business Patterns 2023, LA County FY24 budget). Sources are stored in `data/baseline_assumptions.json` with evidence labels.

| Indicator | Value | Source label |
|---|---|---|
| Housing units, 2024 | 3,709,507 | Census QuickFacts (HSG010224) |
| Building permits, 2024 | 19,809 | Census Building Permits Survey |
| Median owner-occupied home value | $834,200 | ACS 5-yr 2020-2024 |
| Median gross rent | $1,954 | ACS 5-yr 2020-2024 |
| Median selected monthly owner cost (with mortgage) | $3,160 | ACS 5-yr 2020-2024 |
| Households | 3,416,449 | ACS 5-yr 2020-2024 |
| Persons per household | 2.81 | ACS 5-yr 2020-2024 |
| Median household income (2024 dollars) | $90,112 | ACS 5-yr 2020-2024 |
| Per capita income | $45,792 | ACS 5-yr 2020-2024 |
| Poverty rate | 13.3% | ACS 5-yr 2020-2024 |
| Employer establishments, 2023 | 304,988 | Census CBP 2023 |
| Total employment, 2023 | 3,987,736 | Census CBP 2023 |
| Annual payroll, 2023 | $299.6 billion | Census CBP 2023 |
| Accommodation/food sales, 2022 | $44.0 billion | Economic Census 2022 (NAICS 72) |
| Mean commute, minutes | 30.4 | ACS 5-yr 2020-2024 |
| Estimated population, 2024 | ~9.85 million | derived from HH × PPH |

Several baseline conditions matter for what reform can and cannot do.

**The county already produces roughly 25,000 to 30,000 net new units per year** in the no-reform trajectory, mostly in unincorporated areas, the City of Los Angeles, and a handful of large infill jurisdictions. About 19,800 permits in 2024 understates total production because of multifamily project size effects and conversion completions. The baseline trajectory is not zero — it is quietly producing units against a wall of friction. Reform's job is to remove the wall, not to invent production from nothing.

**The county is governed by 88 incorporated cities plus the unincorporated balance.** Charter cities (including the City of LA, Long Beach, Pasadena, Glendale, Burbank, Beverly Hills, Santa Monica, Inglewood, Torrance, and many others) have constitutional home rule for "municipal affairs" but are subject to state law on "matters of statewide concern." Housing has been ruled a matter of statewide concern under the Housing Accountability Act and SB 9; the question for the most aggressive future reforms is how broadly that doctrine extends.

**Homelessness pressure is severe and concentrated.** The 2024 LAHSA count put the countywide homeless population at roughly 75,000 (sheltered + unsheltered). Per-person public costs (emergency response, jail, hospital, sanitation, outreach) are estimated by the LA Economic Roundtable and HUD-HMIS data at approximately $30,000 to $55,000 per unsheltered person per year, with a central estimate near $42,500.

**Infrastructure is constrained.** LADWP and SCE interconnection lags for new multifamily commonly run 9-22 months. Distribution transformer lead times have run 12-24+ months since 2022. LA County Public Works and the city public works departments face permit-staffing shortages. These constraints are real, do not appear in housing-element calculations, and are largely absent from the YIMBY policy discourse.

**Fiscal capture is fragmented.** Under Prop 13, the property-tax rate is 1% (plus voter-approved overrides averaging ~0.25% in LA County). After ERAF redirects to schools, the city or county receives roughly 20-25% of new construction property tax; the school districts receive a similar share; the state pockets most of the income-tax growth from new residents and new wages. There is no mechanism that automatically channels growth-related revenue back to the jurisdictions that bear the marginal infrastructure cost.

These five baseline facts are what the reform package must work against and through.

---

## 3. What the state can plausibly do without a constitutional amendment

California's authority over local land use and permitting is broader than is commonly understood, and narrower than maximalist YIMBY reformers would prefer.

**What the Legislature can clearly do.** The state has clear authority to:

- Preempt local zoning to allow specified uses by right, subject to objective standards (precedent: SB 9, SB 35/423, AB 2011, AB 2097, SB 4, SB 79).
- Impose ministerial approval timelines on local agencies (Permit Streamlining Act, SB 35).
- Restrict CEQA review for specified project categories (existing categorical and statutory exemptions; AB 130/SB 131).
- Cap or standardize impact fees and require nexus studies (AB 602).
- Require objective standards for residential review and bar discretionary aesthetic veto (Housing Accountability Act).
- Empower HCD or a state successor agency to audit local compliance and, in cases of repeated violation, issue determinations, fines, and Builder's Remedy expansion (existing HCD Housing Element enforcement, expanded in 2017 and 2019).
- Standardize statewide building code, fire code, and accessibility code (existing statutory authority via HCD and OSFM).
- Authorize and expand infrastructure-financing districts (EIFDs, IFDs, CRIAs, post-redevelopment tools).

**What is more legally fraught but probably defensible.** The state can probably:

- Establish a state permitting backstop office that issues binding approvals when a local agency misses deadlines or applies invalid standards. Charter cities will sue. The likely outcome is upheld for housing, narrowed for commercial.
- Preempt parking minimums broadly (precedent: AB 2097 already does this within half a mile of transit; statewide expansion is plausible).
- Require utilities (including municipally-owned LADWP) to meet shot-clock interconnection SLAs. This is novel but the state's regulation of utilities is broad. LADWP's municipal status complicates but does not preclude.
- Limit conditional-use-permit abuse and the discretionary commercial veto. This collides with charter-city home rule on "municipal affairs"; some retreat is likely.
- Standardize statewide health, fire, and building signoffs for tenant improvements. Will face county resistance.

**What cannot be done without constitutional change.** The state cannot:

- Abolish cities, suspend elected officials, or impose total receivership.
- Bypass the California Coastal Commission's constitutional jurisdiction for shoreline parcels.
- Override Prop 13's 1% property tax cap or the acquisition-value reassessment limit.
- Repeal CEQA in its entirety (though the legislature can carve out very broad statutory exemptions, which is what the reform package proposes).
- Override Prop 218 / Prop 26 on local taxes and fees beyond their existing carve-outs.
- Reallocate property tax revenue across jurisdictions in ways that violate Prop 13's allocation rules without a separate ballot measure.

**The legal envelope, in summary.** The Legislature can build a regime in which most multifamily housing is by-right under objective state standards, most infill projects are CEQA-exempt, most discretionary local vetoes are constrained by shot clocks and deemed approvals, most commercial tenant improvements are fast-tracked under standardized statewide rules, and a state office issues binding approvals when locals misbehave. It cannot eliminate the Coastal Act, Prop 13, or municipal corporate existence. Within those limits, "Maximum Statutory Abundance" is a real legal possibility — not a fantasy.

---

## 4. The Maximum Statutory Abundance policy package

The package modeled in this project consists of twelve interlocking reform tracks. They are designed to be enacted as a coordinated bundle, not à la carte, because each reform's effectiveness depends on the others.

**1. State zoning floor.** Multifamily housing legal by right on parcels in urbanized LA County above a minimum size threshold; missing-middle (4-12 unit buildings) legal in formerly single-family zones; higher density on commercial corridors and near jobs centers; SB 79-style transit-oriented development treated as a binding floor that local governments cannot reduce; apartments by right on underused retail, office, and parking sites; religious and institutional land housing-by-right (SB 4 expansion); public-land fast-track. Adaptive reuse and office-to-residential conversion legal under objective standards.

**2. Ministerial approval with strict shot clocks.** 60-day shot clock for ministerial review of qualifying projects. Missed deadline equals automatic approval. Objective standards only — no discretionary design review, no planning commission veto, no city council veto, no neighborhood compatibility findings. Limited appeals under existing HAA framework. State backstop approval if local government fails to act.

**3. CEQA reform.** Statutory categorical exemption for infill housing, mixed-use infill, adaptive reuse, office-to-residential conversion, public-land housing, energy and grid projects, water and sewer upgrades, transit and bus-priority projects, active-transportation infrastructure, commercial tenant improvements, and light industrial in appropriate zones. Federal NEPA, Coastal Act, seismic and life-safety, tribal consultation, sensitive habitat, and hazardous-materials rules remain in force.

**4. Fee and exaction reform.** Cap impact fees at evidentiary-nexus level; standardized statewide fee schedules; transparent nexus studies; no late-stage surprise fees; fee deferral until certificate of occupancy; limits on inclusionary requirements that make otherwise feasible projects infeasible; targeted value capture only where it does not kill feasibility.

**5. Parking reform.** AB 2097 expansion: zero parking minimums near transit, jobs centers, and commercial corridors. Parking maximums permitted in high-demand areas. Unbundled parking required. Local governments cannot use parking as a de facto housing or business veto.

**6. State permitting backstop.** New Office of Housing Approval authorized to issue binding approvals when local agencies miss deadlines, apply invalid standards, or repeatedly violate state law. Escalating enforcement: warning, determination, fines, deemed approval, automatic Builder's Remedy expansion.

**7. Commercial and small-business permitting reform.** Restaurants, cafes, bars, gyms, clinics, childcare, and small venues by right in mixed-use and commercial zones, subject to objective health, fire, and noise standards. Fast-track tenant improvements. Standardized countywide health/fire/building signoffs. Outdoor dining permanent. Conditional-use-permit abuse limited where state economic-development policy is impaired.

**8. Infrastructure and utility acceleration.** State CEQA exemption for grid upgrades, transformer and substation installs, water and sewer rehab, and bus-priority lanes. Coordinated trenching mandate (dig-once). Standardized pre-approved electrification packages for common multifamily building types. State transformer procurement pool to break the post-2022 lead-time bottleneck.

**9. LADWP, SCE, SoCalGas interconnection reform.** 60-day plan review and 120-day energization service-level agreement for new multifamily. Missed deadlines equal deemed-energized for occupancy purposes. CPUC enforcement on regulated utilities; for municipally-owned LADWP, separate state regulatory authority over connection timelines under the statewide-concern doctrine. Transparent online capacity maps. Dedicated housing-growth interconnection teams.

**10. Building-code and construction-cost reforms.** Single-stair multifamily up to 6 stories with sprinklers (Seattle-Honolulu-Vancouver model). Modular and factory-built housing fast-track. Statewide pattern-book multifamily designs accepted by-right. Construction-defect liability reform for condos. Harmonized fire-code interpretations.

**11. Labor and delivery-capacity reforms.** State permitting surge teams. Building-department staffing grants tied to permit-velocity benchmarks. Apprenticeship-pipeline expansion for electricians, plumbers, elevator technicians, inspectors, and utility crews. Public infrastructure design-build authority. Standardized P3 templates.

**12. Growth dividend and infrastructure reinvestment.** Expanded EIFDs, IFDs, and CRIAs. State matching grants for infrastructure bonds in growth corridors. Value-capture frameworks calibrated to preserve project feasibility. Fiscal-plumbing reforms to channel growth-related revenue back to jurisdictions bearing marginal infrastructure cost.

The legal-survival probability of each track varies. The housing core (tracks 1-3, 5, 6, parts of 8) is most likely to survive litigation. Commercial preemption (track 7) and fiscal-allocation reforms (track 12) face the highest legal and political risk. The Maximum Statutory Abundance scenario assumes the housing core survives more or less intact; the Legal Collision scenario (Scenario F) assumes commercial and fiscal pieces are narrowed by the courts.

---

## 5. Additional supply-side reform menu

Beyond the twelve-track core package, this project compiles a menu of 36 candidate reforms (see `outputs/reform_menu.csv` and `src/reforms.py`). Each reform is scored on seven dimensions: legal plausibility (1-5), housing supply impact (1-5), commercial impact (1-5), implementation complexity (1-5), litigation risk (1-5), political difficulty (1-5), and time to material impact. Each is also tagged with the primary constraint it addresses (legal capacity, approvals, construction cost, financing, infrastructure, utilities, fiscal capture, anti-sabotage) and a yes/no flag for inclusion in the central scenario.

The top ten reforms by combined score (housing+commercial impact, weighted by legal plausibility, deducted by litigation risk and complexity) are:

1. **Restaurants, cafes, clinics by-right in commercial zones.** Legal: 5. Housing: 1. Commercial: 5. Litigation: 2. Political: 3.
2. **Ministerial approval with strict shot clocks.** Legal: 5. Housing: 5. Commercial: 4. Litigation: 2.
3. **CEQA exemption for infill housing and adaptive reuse.** Legal: 5. Housing: 4. Commercial: 3. Litigation: 2.
4. **State multifamily zoning floor in urbanized areas.** Legal: 4. Housing: 5. Litigation: 4. Political: 5.
5. **Office/retail-to-residential by-right conversions.** Legal: 5. Housing: 4. Commercial: 3.
6. **Outdoor dining and small-venue by-right (statewide).** Legal: 5. Commercial: 4. Political: 2.
7. **Parking minimum elimination near transit and corridors.** Legal: 5. Housing: 3. Commercial: 4.
8. **State permitting backstop office.** Legal: 4. Housing: 5. Litigation: 3. Implementation: 5.
9. **State permitting surge teams and building-dept staffing grants.** Legal: 5. Housing: 3. Political: 1.
10. **Religious and institutional land housing-by-right (SB 4 expansion).** Legal: 5. Housing: 3. Political: 2.

Reforms intentionally excluded from the central scenario but visible in the menu include:

- **Mandatory loser-pays for non-environmental CEQA suits.** High litigation impact but politically toxic.
- **Inclusionary feasibility floor.** Affordable-housing politics.
- **Coastal Act delegation reform for non-shoreline parcels.** Coastal Commission's constitutional protection makes this hard.
- **Property-tax allocation reform for growth.** Schools coalition opposition; politically very difficult.
- **CUP-abuse limit and formula-retail-ban preemption.** Charter-city home rule and 1st Amendment complications.

The reform menu is not a wish list. It is a research artifact: an attempt to lay out the full landscape of what could plausibly be done, scored consistently, so that the pieces selected for the central scenario are visible against alternatives that were considered and rejected. Several included reforms are politically hard; several excluded reforms would be empirically high-impact if enacted. The exclusion criterion is roughly: legal plausibility ≥ 4, political difficulty ≤ 4, or special strategic value.

---

## 6. Modeling architecture

The model is a deterministic, annual time-step simulation written in Python (`src/model.py`). It runs from 2026 through 2045 and produces a `YearState` record for each year of each scenario. Output is a CSV with one row per scenario × utility variant × fiscal-capture variant × year — 1,080 rows for the full grid, 216 rows for the milestone-year headline view.

**Funnel logic.** The single most important architectural decision is to route housing production through five gates:

1. **Legal capacity** — units that *could* be built under the scenario's zoning regime, after coastal/fire haircuts.
2. **Entitlements** — applications that clear ministerial review, after shot-clock multipliers, local-resistance haircuts, state-backstop relief, and litigation drag.
3. **Permits** — entitlements that obtain building permits, capped by ministerial-share and building-department staffing.
4. **Completions** — permits that finish construction, drawn from a five-year permit-to-completion lag distribution and capped by the construction-labor pool.
5. **Energization** — completions that obtain utility connections, drawn from a utility-lag distribution and capped by LADWP/SCE distribution capacity.
6. **Occupied** — energized units multiplied by occupancy rate (~0.97).

A unit only enters the housing stock when it is energized. Units that are completed but not energized accumulate as a "delayed completed units due to utilities" backlog. This backlog is a key headline output because it makes visible the gap between what the policy package allows and what physical infrastructure can absorb.

**Module sequence per year.** Each year, modules execute in a fixed order:

1. Legal capacity → 2. Entitlements → 3. Permits → 4. Completions → 5. Energization → 6. Occupation → 7. Housing cost (rents and values respond to stock vs. demand) → 8. Population (occupied stock × persons-per-household, with crowding feedback) → 9. Income (agglomeration × composition effects) → 10. Homelessness pressure → 11. Business formation → 12. Fiscal feedback (gross revenue, net of service costs, reinvestment pool) → 13. Risk scoring.

There is no within-year fixed-point iteration. All cross-module feedbacks lag one year:

- Fiscal capture in year *t* funds utility capacity in year *t+1*.
- Completions in year *t* expand the construction labor pool for year *t+1* (capped at 1.4× rolling capacity).
- Rent levels in year *t* feed into latent migration demand in year *t+1*.

**Housing cost equation.** Real rent change is a reduced-form log-linear:

`Δlog(rent_real) = α · Δlog(occupied_stock − latent_demand) + β · Δlog(real_income) + γ · drift`

with α = −0.30 central (range −0.20 to −0.45), β = 0.70, γ = 0.005. The α range brackets Hsieh-Moretti 2019's implied −0.25, Anenberg-Kung 2014's −0.40 to −0.50 in submarket data, and Baum-Snow & Han 2024's roughly −0.20 metro-level estimate. The literature is *not* unanimous; we treat the central value as medium-evidence.

Latent demand is the model's most important behavioral lever. Population *desired* in LA grows with reduced rent versus peer metros: `desired_pop = baseline_pop × (1 + μ · max(0, rent_LA / rent_peer − 1))` with μ = 0.20 central, 0.28 in the high-build scenario. This is what generates the model's most important counterintuitive prediction: when supply expands, population catches up so that rents do not fall as much as a partial-equilibrium intuition suggests.

**Population endogeneity.** Actual population is `min(desired_pop, occupied_units × persons_per_household)`. PPH responds to crowding: when desired exceeds available housing, crowding rises; when supply exceeds desire, household formation increases (PPH falls). PPH is bounded between 2.50 and 3.21 (2.81 baseline ± 0.40).

**Income decomposition.** Median household income is decomposed into agglomeration uplift (0.03 per density doubling, Combes-Gobillon 2015) and a composition factor that pulls median *down* as moderate-income households are able to afford to live in LA. The welfare metric the model emphasizes is `real_residual_income_after_housing` — the median minus annualized rent — which rises in abundance scenarios even when nominal median falls.

**Homelessness pressure index.** A bounded 0-100 composite anchored at 50, computed as 50 + 30·tanh(rent-to-income deviation × 4) + 15·tanh(rent-growth deviation × 50) − 10·tanh(ELI-supply deviation) − 10·tanh(employment-growth × 25) − 12·tanh(residual-income deviation × 4). Weights are derived from Colburn & Aldern 2022 (*Homelessness is a Housing Problem*); the tanh smoothers prevent saturation.

**Fiscal module.** Per new unit and per new household, the model computes property tax (1.0% × home value × 0.55 LA share post-ERAF), one-time construction sales tax, recurring local sales tax, business tax lift, utility revenue, and state income-tax pass-through (5% return assumption). Service cost is $1,500/capita/year marginal (lower than full general-fund average because schools are state-funded under LCFF, and police/fire/parks have substantial fixed components). Net revenue × fiscal-capture rate × value-capture-feasibility-factor flows into next year's utility capacity, with a hard cap at 1.5× baseline to prevent runaway feedback.

**Risk scoring.** Three composite scores in 0-100: legal/implementation risk (preemption intensity, CEQA exposure, HCD enforcement gap, local resistance, litigation, political reversal), delivery risk (utility lag, labor shortage, capital cost, infrastructure funding inadequacy, litigation, local resistance), and infrastructure stress (population pressure, fiscal alignment relief, utility execution lift, delayed-units share). Each component contributes additively; weights documented in `src/model.py`.

**What the model does not do.** It is not stochastic. It does not run Monte Carlo over interest rates, immigration, climate shocks, or recession risk. It does not model city-by-city heterogeneity (everything is countywide). It does not solve a general equilibrium for capital, labor, or land prices. It does not endogenize peer-metro rent. These limitations are documented in the red-team memo.

---

## 7. Core assumptions

The most consequential assumptions are listed here in order of how much each one drives 2045 outcomes. Sensitivity analysis (Section 24) shows the magnitude of each.

**Latent migration elasticity μ (central 0.20, range 0.10-0.30).** This determines how much of new supply is absorbed by population growth versus rent reduction. At μ = 0.30 most of the supply effect is absorbed by population; rent moderation is small. At μ = 0.10 supply meaningfully reduces rents but population growth is more limited.

**Rent-to-supply elasticity α (central −0.30, range −0.20 to −0.45).** The instantaneous rent response to net supply growth. Combined with μ above, these two parameters together determine whether the model produces the "more people, similar rents" pattern (Hsieh-Moretti) or the "rent moderation, modest population growth" pattern (Anenberg-Kung partial equilibrium).

**Utility capacity (variant-dependent).** Improved: 75,000 units/year baseline absorptive capacity, 5-month interconnection lag. Current drag: 38,000 units/year, 12-month lag. Severe bottleneck: 18,000 units/year, 22-month lag. Each variant also adjusts transformer constraint factor and a LADWP modernization index. The differences between variants drive the largest spread in final outcomes.

**Construction labor capacity (scenario-dependent).** Baseline 28,000 units/year of effective trades capacity, scaling up to 80,000 in high-build via apprenticeship expansion and modular productivity. Capped at 1.4× rolling 3-year average growth, modulated by productivity, financing cost, construction cost inflation, and developer confidence.

**State backstop effectiveness (0.10 baseline → 0.85 high-build).** What fraction of local-resistance friction the state actually neutralizes. This depends on HCD/Office-of-Housing-Approval staffing and political will.

**Fiscal capture rate (0.0 / 0.30 / 0.60 across variants).** Share of net new public revenue actually channeled into infrastructure reinvestment. The remainder leaks to schools, the state, and other entities.

**Service cost per capita marginal ($1,500/yr).** Lower than LA County's average general-fund per-capita because schools are largely state-funded, police/fire/parks have fixed components, and many county services are budgeted at the system level rather than per-capita. This is on the optimistic side — a more pessimistic alternative (e.g., $2,500/capita) would push service costs above gross revenue in most scenarios.

**Income composition λ (0.15).** How much each percentage point of moderate-income inflow pulls median household income down. Bounded; effects in the model are visible but small at the population growth levels we observe.

**Permit-to-completion lag distribution.** {0.15, 0.45, 0.75, 0.90, 1.00} cumulative over 5 years (Glaeser-Gyourko 2018, NMHC pipeline data). Determines how quickly permits convert to occupied units.

**Demolition rate (0.0012/year).** Modest; reflects HCD APR loss data for LA. Higher under aggressive redevelopment.

**Construction cost inflation (3.0%/yr baseline, 5.5%/yr in drag scenarios).** Affects how quickly the labor pool can scale and project feasibility.

Each of these assumptions is editable in `data/scenario_parameters.json`. The model is parameter-driven, not hard-coded; reviewers can substitute their own values.

---

## 8. Scenario results — overview

The model runs six scenarios across three utility variants and three fiscal-capture variants (54 total combinations). The "headline pairings" represent the most internally consistent pairing per scenario.

| Scenario | Pair (utility / fiscal) | Cum new units 2045 | Pop 2045 | Real rent 2045 | HPI 2045 | Net rev 2045 |
|---|---|---|---|---|---|---|
| A — Baseline | current_drag / partial | 332,000 | 11.1M | $2,310 | 55 | $0.9B |
| B — Moderate | current_drag / partial | 582,000 | 11.7M | $2,268 | 51 | $2.0B |
| **C — Max central** | **improved / partial** | **1,631,000** | **11.6M** | **$2,121** | **41** | **$11.7B** |
| D — High build | improved / high | 1,699,000 | 12.0M | $2,116 | 41 | $11.6B |
| E — Implementation drag | severe / none | 45,000 | 10.4M | $2,362 | 71 | −$0.6B |
| F — Legal collision | current_drag / partial | 658,000 | 11.8M | $2,256 | 51 | $2.5B |

(Real rent figures in 2024 dollars. HPI baseline = 50; lower is better. Net revenue is annual flow in 2045.)

The most important observation is the **40× spread** between Scenario E (45k cumulative units) and Scenario D (1.7M cumulative units), under the same notional policy package. The Maximum Statutory Abundance package gets passed in both scenarios. The difference is whether the institutions execute. This is the central thesis of the model: legal authority is a necessary but very far from sufficient condition.

The second important observation is that **Scenarios C and D produce nearly identical headline numbers**, despite C having a less aggressive zoning multiplier (2.20 vs 2.60) and lower developer confidence. The reason is that under the improved-utility variant, both scenarios are constrained by utility capacity (which sits at ~75-112k/year given the 1.5× cap on infrastructure-driven expansion). The legal capacity in D goes unused because the funnel chokes downstream. This is a *finding*, not a bug: it means that beyond a certain point, additional zoning capacity has zero marginal return until physical infrastructure expands.

The third observation is that **Scenario F (legal collision) lands close to Scenario B (moderate reform)**, not close to Scenario C. If the courts narrow the housing core or the fiscal/commercial pieces, the package degrades to something only modestly better than tightened HCD enforcement. This is consistent with the legal-survival probabilities: most of the value is in the housing core.

The fourth observation is that **Scenario A (baseline) shows real rent rising 18 percent over twenty years** — meaningful rent inflation under counterfactual, despite the baseline producing 332k cumulative units. This baseline trajectory is itself somewhat optimistic; without continued state-level pressure (SB 35/423 enforcement, HCD compliance, builder's remedy), the actual no-reform path could be worse.

---

## 9. Housing production forecast

Cumulative net new housing units by 2045 across the headline pairings:

| Scenario | 2030 | 2035 | 2040 | 2045 |
|---|---|---|---|---|
| A — Baseline | −10,600 | 92,700 | 212,700 | 331,900 |
| B — Moderate | −11,800 | 126,900 | 325,100 | 582,500 |
| C — Max central | 52,600 | 562,600 | 1,098,200 | 1,630,600 |
| D — High build | 93,000 | 631,400 | 1,166,600 | 1,698,500 |
| E — Implementation drag | −14,400 | 5,400 | 25,100 | 44,600 |
| F — Legal collision | 5,100 | 179,000 | 398,300 | 658,100 |

Several patterns:

**The slow start.** All scenarios except the baseline are *negative* through about 2028-2029 because annual demolitions (~4,400/year at 0.0012 × 3.7M units) exceed slow ramp-up completions in the first phase-in years. This is realistic. Policy reform takes time to translate into permits, then permits take 2-5 years to finish, then completions wait for utility connection. Anyone who tells you a 2026 reform produces 2027 units is selling something.

**The acceleration window.** Scenarios C and D reach their stride between 2030 and 2035, when the legal-capacity ramp is complete, the entitlement pipeline is full, and the construction labor pool has scaled. By 2035, C is producing roughly 80,000 cumulative-net-new-units per year and D is at roughly 100,000 — both well above LA County's recent best.

**The plateau.** After 2035, growth in C and D slows because the utility capacity constraint is binding. The model shows annual new occupied units leveling off at approximately the utility cap × 1.5 (the maximum reinvestment-driven capacity expansion). Beyond this plateau, more legal capacity is wasted unless utilities also scale.

**The drag scenario.** Scenario E never escapes the bottleneck. Cumulative units stay below 50,000 by 2045 — essentially no net production over twenty years. This is the scenario where everything fails: utility capacity stays at 18k/year-equivalent, transformer constraints worsen, construction cost inflation runs at 5.5%, financing is expensive, and local sabotage holds down approvals. It is a possible outcome, not a fantasy. The 2022-2023 transformer shortage is a small preview of what severe bottleneck looks like.

**Comparison to user prior.** The project specification anticipated 900,000-1,400,000 cumulative units in C central and 1,500,000-2,200,000 in D high build by 2045. The model lands at 1.63M for C and 1.70M for D — at the upper end of the C range, the lower end of the D range, and approximately consistent with both. The C-D collapse (to nearly identical numbers) is a model finding tied to utility capacity; it would not replicate if utilities scaled more aggressively in D than they do in our parameterization.

---

## 10. Housing cost forecast

Median gross rent in real 2024 dollars (baseline 2024 = $1,954):

| Scenario | 2030 | 2035 | 2040 | 2045 | Change vs 2024 |
|---|---|---|---|---|---|
| A — Baseline | $2,053 | $2,148 | $2,241 | $2,310 | +18.2% |
| B — Moderate | $2,052 | $2,130 | $2,201 | $2,268 | +16.1% |
| C — Max central | $2,041 | $2,061 | $2,086 | $2,121 | +8.5% |
| D — High build | $2,036 | $2,052 | $2,080 | $2,116 | +8.3% |
| E — Drag | $2,052 | $2,150 | $2,253 | $2,362 | +20.9% |
| F — Legal collision | $2,049 | $2,121 | $2,189 | $2,256 | +15.5% |

Median home value in real 2024 dollars (baseline = $834,200):

| Scenario | 2030 | 2035 | 2040 | 2045 | Change vs 2024 |
|---|---|---|---|---|---|
| A — Baseline | $909k | $977k | $1,049k | $1,127k | +35% |
| B — Moderate | $909k | $973k | $1,036k | $1,096k | +31% |
| C — Max central | $902k | $926k | $955k | $992k | +19% |
| D — High build | $898k | $921k | $951k | $988k | +18% |
| E — Drag | $909k | $987k | $1,073k | $1,165k | +40% |
| F — Legal collision | $907k | $967k | $1,027k | $1,088k | +30% |

Two patterns deserve emphasis.

**Real rent does not fall in absolute terms in any scenario.** Even Maximum Statutory Abundance produces an 8.3-8.5% real rent *increase* over twenty years. What it does is reduce rent inflation by roughly *10 percentage points* versus the baseline counterfactual. That is real welfare improvement — it represents about $170/month per household by 2045 versus the no-reform path — but it is not "rents come down" in the way some advocates promise. Latent demand, peer-metro convergence, and ongoing real-income growth all push rent upward; abundance offsets but does not reverse this.

**Rent-to-income ratio implications.** With median household income real essentially flat at ~$90,000 across scenarios (composition effect mostly washes out at the population growth levels we see), the rent-to-income ratio rises everywhere but rises *less* under abundance:

- Baseline 2045: 12 × $2,310 / $89,900 = 30.8% rent-to-income
- C central 2045: 12 × $2,121 / $89,800 = 28.4%
- D high build 2045: 12 × $2,116 / $89,700 = 28.3%

The model predicts about 2.4 percentage points of rent-burden reduction under abundance — meaningful but not transformative. This is the central honest message of the housing-cost forecast: **abundance materially eases pressure but does not abolish high housing cost in coastal California.** Anyone promising otherwise is overselling.

**Home-value implications.** Real home values *rise* in every scenario, including abundance. This is partly because home-value growth in the model is partly driven by income growth, and partly because zoning-floor expansion creates short-term land-value uplift before supply materializes. Existing homeowners get a substantial windfall in C central (+19% real over 20 years) — a politically important fact. The "abundance kills home values" narrative that some opponents float is not what the model produces.

---

*[End of chunk 2 of 5. Sections 11-15 follow.]*
