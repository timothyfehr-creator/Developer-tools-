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

## 11. Population forecast

Population in millions across the headline pairings:

| Scenario | 2030 | 2035 | 2040 | 2045 |
|---|---|---|---|---|
| A — Baseline | 10.14 | 10.27 | 10.49 | 11.11 |
| B — Moderate | 10.16 | 10.53 | 11.05 | 11.71 |
| C — Max central | 10.31 | 11.08 | 11.35 | 11.64 |
| D — High build | 10.44 | 11.35 | 11.65 | 11.96 |
| E — Drag | 10.15 | 10.24 | 10.33 | 10.41 |
| F — Legal collision | 10.20 | 10.66 | 11.23 | 11.81 |

Persons-per-household responds to crowding and supply. In Scenario E, where housing is severely constrained, PPH stays elevated above the 2.81 baseline as households absorb some of the latent demand through doubling-up. In Scenarios C and D, PPH drifts modestly down toward 2.6-2.7 as supply enables household formation and reduced crowding.

The most important pattern is that **abundance produces meaningful but not enormous population growth**. Scenario C delivers about +1.8 million people over 2024 by 2045 — substantial, but not the 14-15 million that some maximalist YIMBY scenarios imply. The model's latent-demand parameter μ = 0.20 is what limits population growth: people respond to lower LA rent versus peer metros, but the response is not unlimited. Move μ to 0.35 (the "high latent demand" sensitivity) and population in C reaches roughly 12.5 million.

The user's project specification anticipated 11-13 million in C central and 13-15 million in D high build. The model lands at the *low end* of both ranges. The reason is the utility-capacity ceiling: even with full legal authority and strong demand, you can only physically connect ~110-115k units per year given infrastructure constraints, and population follows occupied units. To get to 13M+ in D, the utility variant would have to be even more aggressive than `util_improved` — probably requiring a state utility receivership and a federal IRA-scale capital infusion.

**Net migration patterns.** In abundance scenarios, net migration into LA County turns positive after 2030 — reversing the 2020-2024 outflow. This depends on relative-rent improvements actually materializing; if peer metros (Phoenix, Las Vegas, Dallas, Houston, Salt Lake) keep building, LA's relative attractiveness recovers more slowly. The model treats peer rent as static; in reality, peer-metro convergence is a real risk to LA's growth dividend.

**Crowding proxy.** The model tracks an "actual / baseline-PPH-occupied" ratio that proxies crowding. In Scenario E by 2045, this ratio sits about 8% above 1.0, indicating noticeable household-doubling pressure. In Scenario C it sits roughly at 1.0; in Scenario D slightly below 1.0 (mild un-crowding). This is not the kind of indicator that survives political contestation — opposition will frame any crowding deviation as evidence of "overdevelopment" — but it is internally meaningful.

---

## 12. Median income and real welfare forecast

Median household income (real 2024 dollars), residual income after rent, and per capita income real:

| Scenario | Median HH 2045 | Residual after rent 2045 | Per capita 2045 |
|---|---|---|---|
| A — Baseline | $89,900 | $62,200 | $46,200 |
| B — Moderate | $89,800 | $62,500 | $46,200 |
| C — Max central | $89,800 | $64,300 | $46,400 |
| D — High build | $89,700 | $64,300 | $46,500 |
| E — Drag | $90,000 | $61,700 | $46,000 |
| F — Legal collision | $89,700 | $62,700 | $46,200 |

The dispersion in median household income is small. The composition effect — moderate-income households moving in and pulling median down — is real in the model but quantitatively modest at the population growth levels we observe. At larger inflows (10%+ population growth in five years), the composition effect would be more visible; at the 18-22% growth over twenty years that the model produces, it averages out to less than $500/year of compositional shift in median.

The welfare metric to focus on is **residual income after rent**. Under abundance, this rises by approximately $2,100/year over the no-reform baseline. Per household, that is real money. Across 4 million households (baseline + new), it represents roughly $8 billion per year of household-level real welfare gain by 2045. This is what abundance actually delivers in dollars-and-cents terms: not collapsing rent, but freeing up about $170/month per household to spend on something other than housing.

**Per capita income** rises modestly across all scenarios, including abundance, because agglomeration effects (higher density → higher productivity, per Combes-Gobillon) outweigh the composition pull-down. The agglomeration elasticity used here (0.03 per density doubling) is at the conservative end of the literature; if the true value is closer to 0.05, the agglomeration uplift in C and D would be roughly 60% larger.

**Poverty rate.** The model produces poverty rates that are essentially flat across scenarios (13.0-13.4%), because countervailing forces nearly cancel: agglomeration uplift reduces poverty modestly, while the composition effect and rising-rent pressure on the bottom decile push back. The model does *not* claim that abundance lowers poverty meaningfully countywide. What it claims is that *welfare* — measured as residual income after rent — improves about 3% under abundance versus baseline.

**Distributional caveats.** The model is a countywide aggregate. It does not track distributional outcomes: the median improvements above could mask concentrated welfare losses for renters in redevelopment zones, particularly in lower-income neighborhoods where displacement pressure is highest. Aggregate welfare gain is consistent with concentrated harm. A serious follow-on analysis would need parcel-level or census-tract-level outcomes; this model cannot provide them.

---

## 13. Homelessness pressure and social-cost forecast

Homelessness pressure index (0-100, baseline = 50, lower is better) and homelessness-cost avoidance per year:

| Scenario | HPI 2030 | HPI 2035 | HPI 2040 | HPI 2045 | Cost avoidance 2045 |
|---|---|---|---|---|---|
| A — Baseline | 56 | 46 | 51 | 55 | $0.0B |
| B — Moderate | 57 | 44 | 48 | 51 | $0.0B |
| C — Max central | 39 | 36 | 38 | 41 | $0.35B |
| D — High build | 36 | 35 | 38 | 41 | $0.35B |
| E — Drag | 58 | 62 | 67 | 71 | $0.0B |
| F — Legal collision | 45 | 43 | 47 | 51 | $0.0B |

Three patterns:

**HPI improves materially under abundance during the 2030-2040 window.** Scenarios C and D drop the index from 50 (baseline anchor) to ~35-36 in the mid-period, when supply expansion is meaningfully outpacing demand growth. This roughly corresponds to lower rent burdens, higher residual incomes, and more new ELI-eligible units coming online.

**HPI rebounds toward 41 by 2045 in C and D.** This is because real rent continues to rise (just more slowly than baseline), and after the construction plateau is reached, the supply effect on rent diminishes. The takeaway: abundance buys you a 5-15 year window of meaningful homelessness pressure relief, not permanent abolition.

**Cost avoidance is modest in dollar terms.** $0.35-0.55B per year of avoidable homelessness response cost is real money but small relative to LA County's $40B+ general fund. Translated to person counts, the model suggests roughly 7,000-9,000 fewer unsheltered individuals at peak versus the baseline — a meaningful 10-12% reduction in unsheltered population, but far from the elimination of homelessness.

**The model deliberately does not assume rent reduction alone solves homelessness.** Even in Scenario D high-build, HPI never falls below 35. Substantial residual unsheltered population is implicitly assumed to require permanent supportive housing, mental health treatment, addiction services, eviction prevention, and shelter capacity that are not in this model. The dollarized cost avoidance reflects only the marginal flow effect (people not entering homelessness because rents stabilized) and not the stock effect (people exiting homelessness due to non-housing services).

**Honest framing.** The right message is: housing supply is a *necessary* lever for homelessness reduction. Abundance reduces inflow into homelessness, which over time reduces unsheltered population, which reduces public emergency response costs. But abundance is not by itself sufficient. The HPI rebound by 2045 illustrates the limit. To sustainably keep homelessness pressure low requires either continued abundance (so rent keeps moderating) or complementary investments in the non-housing pieces of the homelessness system — and probably both.

---

## 14. Business formation and commercial vitality forecast

Employer establishments, employment, and accommodation/food sales:

| Scenario | Establishments 2045 | Employment 2045 | Food sales 2045 ($B) | Vitality index 2045 |
|---|---|---|---|---|
| A — Baseline | 343,866 | 4,496,076 | $84 | ~107 |
| B — Moderate | 374,930 | 4,806,513 | $96 | ~119 |
| C — Max central | 394,234 | 4,897,654 | $106 | ~131 |
| D — High build | 417,208 | 5,101,240 | $117 | ~140 |
| E — Drag | 333,393 | 4,274,018 | $83 | ~104 |
| F — Legal collision | 374,685 | 4,828,832 | $95 | ~117 |

**The good news.** Establishments grow 29% in C and 37% in D versus the 2023 baseline of 304,988. Employment expands by roughly 1.0-1.1 million jobs in C/D over baseline. Annual payroll grows from $300B to $620-645B nominal (with inflation). Food and accommodation sales grow from $44B (2022) to $106-117B nominal in C/D. These are large numbers.

**The empirical caveats are substantial.** As noted in the model architecture, the commercial elasticities (0.25 to density, −0.30 to friction) are *speculative*. There is no clean natural experiment for "what happens when a major US metro deregulates commercial permitting on a multi-year horizon." The closest comparators — Houston's no-zoning regime, Tokyo's permissive land use, Auckland post-2016 reform — are weak analogs because of structural differences. The numbers above should be read as *directional* (commercial reform produces meaningful business formation lift) but not as precise quantitative forecasts.

**Sales-tax revenue implications.** Local sales tax (1% Bradley-Burns plus ~0.5% district averages) on incremental sales contributes to the fiscal feedback. With $50-70B of incremental food-and-accommodation sales by 2045 in C and D, this is a real revenue stream — perhaps $0.7-1.0B/year of incremental sales-tax revenue accruing to LA County jurisdictions. Modest at the county level, but meaningful for individual cities.

**Restaurant/cafe/bar establishment count.** The model does not separately disaggregate restaurants from total establishments, but the food-sales figure roughly implies a lift of 2-4% per year in restaurant-type business growth versus 1% baseline. This is consistent with anecdotal observations from places that have eased restaurant permitting (e.g., the post-COVID outdoor dining expansion).

**Why the commercial vitality story is plausible despite weak evidence.** Most of the LA County commercial-permitting reform proposals in the menu are not radical economic interventions; they are removals of well-documented friction. Permanent outdoor dining, by-right restaurants in commercial zones, fast-track tenant improvements, and standardized health/fire/building signoffs collectively reduce time-to-open from 6-18 months to 2-4 months in many cases. This kind of friction reduction reliably increases business formation. The question is the *magnitude*, not the *direction*.

**Why the magnitude estimates are worth distrusting.** A 30-35% lift in establishments over 20 years implies LA County recovering its pre-1990 share of California business formation while also adding new categories. This requires more than friction reduction — it requires sustained demand, capital availability, and labor supply. The model does not endogenize any of those. If the commercial-vitality elasticities are half the central values, we still see meaningful gains (~15% in establishments), which is a more defensible claim.

---

## 15. LADWP, utilities, and infrastructure execution

The infrastructure module is the single most consequential piece of the model. Three utility variants generate the largest spread in headline outcomes:

| Variant | Capacity (units/yr) | Lag (months) | Transformer factor | LADWP modernization |
|---|---|---|---|---|
| util_improved | 75,000 | 5 | 0.6 | 1.5 |
| util_current_drag | 38,000 | 12 | 1.0 | 1.0 |
| util_severe_bottleneck | 18,000 | 22 | 1.5 | 0.7 |

Cumulative net new units in 2045 across utility variants for Scenario C:

- C + util_improved + fcap_partial: 1,630,561 units
- C + util_current_drag + fcap_partial: 693,259 units
- C + util_severe_bottleneck + fcap_partial: 47,942 units

The variance across utility variants is *34× larger* than the variance across scenarios A→D for any fixed utility variant. This is a fundamental finding of the model: **whether LADWP and SCE can absorb new construction is more important to LA's housing future than whether the legislature passes a maximum reform package.**

**What "improved" requires.** The util_improved variant assumes:

- LADWP/SCE plan-review and energization shot clocks are real and enforced.
- Transformer lead times drop from current 18-24 months to 8-10 months via a state procurement pool.
- Distribution-capacity maps are public and continuously updated.
- A dedicated housing-growth interconnection team exists at each utility.
- Pre-approved electrification packages eliminate per-project plan-review for common multifamily building types.
- Coordinated trenching ("dig-once") is mandated and enforced.
- State-backed financing is available for major capacity upgrades, with utility cost recovery rationalized.

This is a long list. None of these elements exists today at scale in LA County. The improved variant is achievable but requires a parallel reform track on utility regulation that is at least as politically heavy as the housing core.

**What "severe bottleneck" looks like.** Severe is what happens if 2022-2023 transformer shortages persist or worsen, IRA-driven competing demand from data centers and EV chargers eats utility capacity, LADWP modernization stalls due to budget or governance issues, and CPUC enforcement on SCE remains weak. Severe bottleneck plausibly is the *current* trajectory — not a worst case. Reforms that pass on paper but are not paired with utility execution converge on this outcome.

**The "delayed completed units" backlog.** The model tracks a critical headline metric: completed buildings that cannot be occupied because they have no electrical service. In Scenario E + util_severe by 2045, this backlog reaches roughly 800,000 units — finished buildings sitting empty waiting for connection. This is the most vivid possible illustration of legal-capacity-vs-delivered-housing divergence. Even in Scenario C + util_current_drag, the backlog at 2045 is around 100,000-200,000 units. In Scenario C + util_improved it is small (~5-10k).

**Practical implication for the policy package.** Tracks 8 (infrastructure acceleration) and 9 (utility interconnection reform) of the Maximum Statutory Abundance package are not optional. Without them, the rest of the package mostly produces paper approvals. The political coalition for housing reform must include CPUC reform, LADWP governance reform, transformer-procurement legislation, and dig-once mandates — or the housing reforms will fail in the field.

**The federal piece.** The IRA, the CHIPS Act, and various federal grid-modernization grants create a financing window that LA could exploit for transformer procurement and grid upgrades. This is not in the model directly, but is the realistic financing path. If federal support contracts (e.g., under a future administration's funding cuts), the achievability of util_improved variant declines materially.

---

## 16. Growth dividend and infrastructure reinvestment

The fiscal module computes annual gross new public revenue, net new revenue after marginal service costs, and the share captured for infrastructure reinvestment. Headline 2045 numbers across scenarios:

| Scenario | Gross new revenue | Net new revenue | Reinvestment | Funding gap | Self-funded share |
|---|---|---|---|---|---|
| A — Baseline | $5.0B | $0.9B | $0.3B | $1.0B | 20% |
| B — Moderate | $13.7B | $2.0B | $0.6B | $1.9B | 23% |
| C — Max central | $30.7B | $11.7B | $3.3B | $1.6B | 68% |
| D — High build | $35.1B | $11.6B | $6.6B | $0.0B | 100% |
| E — Drag | $1.7B | −$0.6B | $0.0B | $0.4B | 0% |
| F — Legal collision | $14.8B | $2.5B | $0.7B | $1.8B | 27% |

(Gross revenue is gross of service costs and homelessness savings. Net revenue is gross + social-cost avoidance − service costs − infrastructure operating costs. Reinvestment is net × fiscal-capture rate × value-capture-feasibility-factor.)

Several patterns are worth highlighting.

**The growth dividend turns positive within 2-4 years.** In abundance scenarios, net new public revenue exceeds the marginal service-cost burden of new residents by approximately 2030 — only 4-5 years after policy enactment. By 2035, C is generating $2.4B/year of net positive revenue; by 2045, $11.7B/year. The growth dividend is real and large.

**But it is not large enough to fund infrastructure capex without leverage.** Annual infrastructure capex needs (at $45,000/unit × 80,000-110,000 new units/year) total roughly $3.6-5.0B/year in C and D. Reinvestment from net revenue at the partial-capture rate (0.30) covers $3.3B/year by 2045 — about 68% of the need in C, full 100% in D under high capture. The remainder requires bond financing, state grants, federal IRA support, or value capture from upzoned land.

**Years until fiscal dividend turns positive.** The model tracks this milestone. In abundance scenarios with partial fiscal capture, it sits at ~3-5 years post-2026. In drag scenarios, it never turns positive within the horizon — service costs always exceed gross revenue because supply growth is too slow to generate the property-tax base.

**Share of infrastructure self-funded by growth.** This metric is the core of the "growth pays for infrastructure" hypothesis. In Scenario D high build with high fiscal capture, the share reaches 100% by 2045 — the growth dividend fully funds marginal infrastructure capex. In Scenario C with partial capture, it tops out around 68%. In Scenarios A and F with low fiscal capture, it stays below 30% even by 2045 — meaning most infrastructure capex requires external financing or remains unfunded.

**Practical implication.** A "growth pays for infrastructure" policy regime is achievable but requires *all four* of these to be true:

1. Substantial supply expansion (Scenarios C/D, not A/B/F).
2. Meaningful fiscal-capture rate (≥0.30, ideally 0.60).
3. Fiscal-plumbing reforms that channel revenue to the right jurisdictions.
4. A bridging mechanism (bonds, grants) for the years when capex precedes revenue.

If any of these breaks, infrastructure underinvestment compounds: insufficient utility capacity caps energization, which slows occupied-unit growth, which slows revenue growth, which deepens the funding gap. This is the model's most important non-linear failure mode.

---

## 17. Fiscal alignment and misalignment

Even when the growth dividend exists, *who* receives it matters as much as *how much* there is. The model tracks two scores in 0-100 ranges:

- **Fiscal leakage score** (higher = more leakage). Captures the share of incremental revenue that flows to entities other than LA County local jurisdictions: state income tax, ERAF redirection to schools, special districts, etc.
- **Fiscal alignment score** (higher = better alignment). Captures the share of revenue that ends up flowing back into LA County infrastructure, after capture-rate and feasibility drag.

Headline 2045 scores:

| Scenario | Leakage score | Alignment score |
|---|---|---|
| A — Baseline | 80 | 50 |
| B — Moderate | 80 | 50 |
| C — Max central | 80 | 50 |
| D — High build | 80 | 70 |
| E — Drag | 80 | 30 |
| F — Legal collision | 80 | 49 |

The leakage score is structurally high (around 80) across all scenarios because the underlying fiscal architecture — Prop 13 base, ERAF redirection, state income-tax appropriation — is not changed in any scenario short of property-tax-allocation reform (which is excluded from the central package as politically too hard). Property tax revenue is split: LA County and cities receive about 55% of the 1% general levy after ERAF, schools take a similar share, and special districts take the remainder. Sales tax similarly splits between state, county, and cities. State income tax accrues mostly to the state, with only ~5% returning to LA infrastructure via grants and transit funding (a generous assumption).

**Why this matters for policy.** Even Scenario D high-build, with strong supply growth and high local fiscal capture, leaves ~30% of new public revenue accruing to entities that have no claim on LA infrastructure. In dollar terms by 2045, that is roughly $10B/year of revenue that exists because LA grew but does not flow back to LA. The state benefits from LA's growth more than LA does.

**Implications for the political coalition.** This fiscal mismatch is the structural reason California has not built — every individual jurisdiction faces the marginal cost of new development (school capacity, fire response, water infrastructure) but only captures 20-25% of the marginal revenue (after ERAF). The local rational decision is to obstruct growth even when the regional decision would favor it. The Maximum Statutory Abundance package includes EIFD/IFD/CRIA expansion and state matching grants to partially address this, but the underlying allocation rules cannot be fixed without either a constitutional amendment or a separate ballot initiative on property-tax allocation.

**The "high fiscal capture" assumption is fragile.** Scenario D's fcap_high parameter (0.60 capture rate) requires aggressive use of EIFDs, value-capture mechanisms, public-land lease revenue, and possibly novel fiscal-plumbing legislation. Each of these tools individually faces political and legal opposition. The model's projection of 100% infrastructure self-funding in D 2045 should be read with that caveat: it assumes a fiscal regime that does not yet exist and would itself require sustained political investment.

**Why fiscal capture isn't fungible.** Even when reinvestment dollars exist, they are not freely deployable. EIFD revenue is restricted to capital infrastructure within the district. CRIA revenue is restricted by similar rules. Bond financing requires voter approval (Prop 218 limits) for many uses. Value capture must be calibrated to preserve project feasibility (the model's value_capture_feasibility_drag parameter). The result: infrastructure that gets funded tends to be the infrastructure that is easiest to pay for under restricted funds, not the infrastructure that is most urgently needed.

---

## 18. Legal and implementation risks

The legal-implementation risk score (0-100, higher = more risk) by scenario at 2045:

| Scenario | Legal risk | Delivery risk | Infra stress |
|---|---|---|---|
| A — Baseline | 21 | 39 | 42 |
| B — Moderate | 22 | 39 | 53 |
| C — Max central | 32 | 23 | 53 |
| D — High build | 35 | 12 | 54 |
| E — Drag | 37 | 59 | 74 |
| F — Legal collision | 29 | 39 | 67 |

Several patterns:

**Legal/political risk rises with reform intensity.** The legal_implementation_risk_score is highest in Scenarios D and F. D's elevated score reflects the full scope of preemption being challenged in court; F's reflects the fact that some pieces have already been narrowed. The score components are: preemption intensity (how aggressive the package), CEQA exposure (how much CEQA carve-out exists), HCD enforcement gap (does the state actually have staff), local resistance, ongoing litigation duration, and political reversal risk.

**Delivery risk falls with reform intensity (when paired with adequate utility/labor execution).** Scenario D shows delivery risk of just 12 — because labor capacity is large, utilities are improved, and infrastructure funding is adequate. Conversely, Scenario E shows delivery risk of 59 — utility lag is severe, labor is constrained, financing is expensive, and infrastructure funding is inadequate. The high-build outcome therefore depends on both legal aggression *and* execution capacity.

**Infrastructure stress is high almost everywhere.** Even in Scenarios C and D, infrastructure stress sits at 53-54 — meaning population growth is putting genuine pressure on schools, transit, parks, water, fire response, and sanitation. The reason is that population growth (15-20%) outpaces infrastructure expansion in most realistic capture-rate scenarios, even when utilities specifically are improved. This is a real cost that the dollarized fiscal module under-counts.

**The interaction between scenarios and utility variants matters more than the scenario alone.** The 6 scenarios × 3 utility variants × 3 fiscal-capture variants matrix is worth scanning. Within a given scenario, util_severe collapses outcomes; within a given utility variant, scenario differences are smaller. The model's most important risk insight is that utilities-and-fiscal-plumbing carry roughly the same weight as legal preemption in determining outcomes.

**The 20-year political-reversal risk.** Our political_reversal_risk_annual parameter (0.02 baseline, scaled in scenarios) implies roughly a 33% cumulative probability of meaningful repeal over 20 years even in Scenario C. In reality, political reversal is path-dependent and lumpy: a single high-salience NIMBY backlash event, a recession-era ballot initiative, or a partisan flip in the Legislature could trigger repeal in a given year. The model treats this as a steady drag, not a stochastic event. A more honest interpretation is that the *first* 8-10 years of any reform package are the most vulnerable; if the regime survives that long, durable institutional change becomes more likely.

**The HCD enforcement question.** State backstop effectiveness in our parameterization ranges from 0.10 (baseline) to 0.85 (high-build). In reality, HCD has roughly 250 staff statewide for housing-element review, builder's-remedy enforcement, and policy implementation. To exercise binding authority over 88 LA County jurisdictions plus the unincorporated balance plus 481 other California jurisdictions requires more like 1,000-2,000 staff. Without explicit staffing legislation, the high-build state-backstop assumption is aspirational. The reform menu's "State permitting surge teams and building-dept staffing grants" entry is a partial fix.

---

## 19. Red-team critique

A separate red-team memo (`outputs/red_team_memo.md`) addresses 30 specific failure modes in detail. The condensed version, ordered by impact:

**1. Legal capacity is not delivered housing.** The funnel from zoning floor to occupied unit has at least five gates and many ways to fail at each.

**2. Local sabotage is lumpy, not smooth.** Coastal cities can lose 90% of legal cases and still effectively obstruct via serial revisions, study requirements, and administrative delay.

**3. Utilities become the new CEQA.** The model already shows this; the central case's util_improved assumption is itself a substantial bet.

**4. Construction labor and materials are binding.** Trades labor is multi-year apprenticeship-gated. Materials inflation is volatile and not fully modeled.

**5. Capital markets and interest rates limit private development.** The model treats financing as a single index parameter. Real-world capital availability is more complex.

**6. Insurance constraints kill condo construction and fire-overlay multifamily.** Not in the model.

**7. Latent demand absorbs supply; LA gets bigger but stays expensive.** This is the model's central honest finding — abundance enables growth but only modestly reduces real rent.

**8. Median income may fall as composition shifts.** The model handles this via residual income; political framing may not.

**9. Infrastructure lags reduce quality of life.** Schools, transit, parks degrade faster than dollarized service costs imply.

**10. Commercial reform evidence is weaker than housing reform evidence.** Treat commercial outputs as directional.

**11. Coastal high-income cities will partially win in court.** Bimodal countywide outcome — Scenario C in much of the county, Scenario F in West LA / coastal.

**12. State enforcement capacity is currently inadequate.** Without staffing legislation, the backstop is aspirational.

**13. Political reversal is a real 5-10 year risk.** Single salient event could trigger repeal.

**14. Land-value uplift precedes rent reduction.** Existing owners win first, before supply benefits accrue.

**15. Displacement effects are concentrated in vulnerable neighborhoods.** Aggregate gains hide distributional harms.

**16. The growth dividend is real but fiscally misaligned.** State and ERAF capture most of it.

**17. New tax revenue arrives later than capex needs.** Bond financing required as a bridge.

**18. Prop 13 weakens local fiscal incentives.** Allocation rules are not fixed in the central package.

**19. Service costs may exceed revenues in growth corridors.** Marginal cost per capita varies by jurisdiction.

**20. Homelessness savings are slow and require complementary investment.** Lower rent reduces inflow but does not exit existing unsheltered population.

**21. State income-tax growth does not automatically help LA infrastructure.** The 5% return assumption is generous.

**22. Utility capex needs exceed near-term utility revenue.** Bond financing required.

**23. Value capture reduces feasibility if overused.** The model captures this directionally but probably understates it.

**24. Infrastructure districts work better in high-value areas.** Lower-income corridors are at a structural disadvantage.

**25. Fiscal benefits are regionwide; project costs are neighborhood-specific.** Mismatch is the structural cause of obstruction.

**26. Model is deterministic.** No Monte Carlo over interest rates, immigration, climate, federal policy.

**27. Latent demand and peer-metro rents are partially endogenous.** Static peer-rent assumption is a simplification.

**28. 2040+ horizon is extrapolation, not forecast.** Confidence bands widen materially after 2035.

**29. Reform-menu commercial scoring is author judgment.** Not literature-derived.

**30. LA County is 88 cities, not a unit.** Countywide aggregation is an averaging fiction.

The full memo expands each point with specific magnitudes and conditional analysis.

---

## 20. Response to the red-team critique

The red-team list above is a comprehensive list of ways the model could be wrong. The honest response is that most of them are *correct*. The model is most reliable in showing relative differences between scenarios (C vs A, D vs C, E vs C) and least reliable in committing to specific 2045 levels. The 1.6 million central-case figure should be read with at least ±30% uncertainty; the 2040-2045 numbers with ±50%.

That said, certain critiques are partial-equilibrium objections to a partial-equilibrium model — they are warranted as caveats but do not invalidate the model's directional conclusions. Specific responses:

**On "legal capacity is not delivered housing" (#1).** This is the model's *core thesis*. The five-gate funnel and lag distributions are designed precisely to prevent the naive equation of legal authority with built units. The fact that the central case projects 1.6M cumulative units rather than 5M+ (which a pure legal-capacity reading would suggest) is the model already responding to this critique.

**On "utilities become the new CEQA" (#3).** The model not only acknowledges this — it treats utility variants as the largest single source of variance. The 34× spread across utility variants for fixed scenario is the model *making* the critique, not failing to address it. The improved-utility variant is a genuine bet on a parallel reform track that does not yet exist.

**On "latent demand absorbs supply" (#7).** This is the most important honest finding. The model deliberately uses a relatively conservative latent-demand parameter (μ = 0.20) versus what high-Hsieh-Moretti estimates would suggest. The result is meaningful population growth (+18-22%) but only modest rent improvement (10pp vs counterfactual). If μ is higher, population is larger and rent improvement smaller. The model presents the conservative version of an unavoidable tradeoff.

**On "median income may fall as composition shifts" (#8).** The model handles this explicitly via the income decomposition. At the population growth rates the model produces, the composition effect is small (~0.5% reduction in median). At larger inflows, it would be more visible. The welfare metric the memo emphasizes is residual income after rent precisely because median income alone is misleading.

**On "fiscal benefits are misaligned" (#16, 25).** Acknowledged and central to the model's own findings. The fiscal alignment score is structurally low because it is supposed to be — the underlying tax-allocation rules in California are misaligned with the geographic distribution of growth costs. The model is making the critique, not falling into the trap.

**On "model is deterministic" (#26).** Correct. A Monte Carlo extension with stochastic interest rates, immigration shocks, climate disasters, and political-reversal events would produce wider confidence bands and probably shift the central case downward (since most shocks reduce production). The deterministic central case should therefore be read as somewhat optimistic. This is documented in `outputs/red_team_memo.md`.

**On "2040+ is extrapolation" (#28).** Correct. The 2026-2035 numbers are most reliable. The 2040-2045 numbers should be read as scenario sketches, not forecasts. We include them because the scenario brief requests them, but they carry larger uncertainty bands than the early years.

**Critiques that should change one's confidence in specific numbers but not the framework:**
- Utility-improved being aspirational → the central case might be 700,000-800,000 cumulative units rather than 1.6M.
- Insurance crisis killing condos → reduce delivered units by 15-20%.
- Latent-demand μ at 0.30 → reduce real-rent improvement by half.
- HCD enforcement at 0.40 instead of 0.70 → reduce delivered units by 10-15%.
- Political reversal at year 8 → revert to baseline trajectory after the boom.

These are real risks. They do not change the basic model architecture or the relative ordering of scenarios. They do change how to think about the central-case headline numbers.

**What the red team does not invalidate.** The model's framework — funnel logic, separation of legal capacity from delivered units, explicit utility-and-fiscal-feedback constraints, and the residual-income welfare metric — survives all of the critiques. The model is a tool for thinking about *which* constraints bind and *under what conditions*. It is not a forecast.

---

## 21. What must be true for the high-build scenario

Scenario D — 1.7 million net new units by 2045, 12.0M population, 8.3% real rent rise vs 18% baseline, $11.6B/yr fiscal dividend, 100% infrastructure self-funding — is *possible* but conditional on a long list of things going right simultaneously. For D to actually materialize, the following must all hold:

**1. The legislative package passes substantially intact.** Not just SB 79-style transit density, but the full twelve-track package: state zoning floor, ministerial shot clocks with deemed approval, CEQA carve-outs for infill and grid infrastructure, fee caps, parking elimination, state permitting backstop, commercial preemption, building-code reforms, labor and procurement reforms, and EIFD/IFD expansion. A diluted package degrades toward Scenario B or F.

**2. Court survival of the housing core.** Charter cities (Beverly Hills, Manhattan Beach, La Cañada Flintridge, San Marino, others) sue, and the California Supreme Court ultimately upholds the state's authority on the core housing preemption. Some narrowing on commercial and fiscal pieces is expected and tolerable; substantial narrowing on housing core would push the trajectory toward F.

**3. HCD enforcement actually has staff.** State backstop effectiveness at 0.85 (the high-build assumption) requires HCD or a successor Office of Housing Approval to have 1,000-2,000 staff actively monitoring 88 LA County jurisdictions plus the rest of California. This is a five-fold expansion from current capacity. It requires explicit appropriation legislation and several years to build organizational capability.

**4. LADWP and SCE deliver shot-clock interconnection.** Plan review in 60 days, energization in 120 days, with deemed-energized backstops. Transformer lead times drop from current 18-24 months to 8-10 months via a state procurement pool. LADWP modernization index reaches 1.5 (50% improvement over current). LA City Council aligns with state utility regulation despite municipal home rule. CPUC enforcement of SCE strengthens.

**5. Federal funding window stays open.** The IRA, CHIPS Act, and federal grid-modernization grants continue to flow. State transformer pool finances itself partly via federal match. Federal housing finance (FHA, GSE, LIHTC) remains accessible and competitive.

**6. Construction trades expand at 30-40% per year.** Apprenticeship pipelines for electricians, plumbers, elevator technicians, inspectors, and utility crews scale meaningfully. Building-trades unions cooperate with the expansion (rather than seeing it as wage suppression). Pre-approved pattern-book and modular designs deliver real productivity gains (~12% labor savings).

**7. Capital markets remain workable.** 30-year mortgage rates do not exceed roughly 7.5-8% sustained. Multifamily cap rates remain accessible. Construction financing is available at reasonable terms. Insurance markets remain functional for multifamily (the construction-defect liability reform passes, restoring condo insurability).

**8. Fiscal capture mechanisms are wired.** EIFD/IFD/CRIA are expanded. State matching grants for infrastructure bonds are funded. Value capture is calibrated to preserve project feasibility. Local jurisdictions actively use these tools rather than refusing to participate.

**9. Political coalition holds for 20 years.** No reversal-triggering ballot initiative succeeds. No partisan flip in the Legislature. No high-salience NIMBY backlash event causes legislative panic. Across roughly 5 statewide election cycles, the housing coalition is durable.

**10. No major exogenous shocks.** No Northridge-magnitude earthquake. No catastrophic wildfire that resets coastal-zone politics. No 2008-style financial crisis. No federal policy regime change that withdraws IRA-scale infrastructure financing.

The conjunction of all ten is unlikely. The conjunction of seven or eight is plausible. Any major break in 2-3 of them pushes the trajectory toward Scenario C or B.

---

## 22. What could go wrong

The mirror image of the high-build conditions: ways the trajectory could collapse.

**Utility execution stalls.** This is the single most likely failure mode. LADWP modernization runs into LA City Council resistance; SCE's CPUC oversight remains weak; transformer lead times stay at 18-24+ months; distribution capacity caps energization; infrastructure capex outruns financing. Outcome: trajectory reverts toward Scenario E (45k cumulative units by 2045) regardless of legal preemption.

**Administrative sabotage.** Cities comply on paper and obstruct in practice via serial site-plan revisions, geotechnical re-review demands, fire-marshal interpretations, and discretionary studies. State backstop is too thinly staffed to intervene case by case. HCD audits exist but findings are not enforced. Outcome: legal authority delivers maybe 30-40% of its potential — trajectory between Scenarios B and C.

**Construction-defect insurance crisis worsens.** Without construction-defect liability reform, multifamily insurance becomes prohibitive. Condo construction stays near zero. Cost of capital for ground-up multifamily rises 200-400 bps. Outcome: 15-20% reduction in delivered units.

**Single political-reversal event in 2030-2032.** A high-salience displacement scandal, a coordinated NIMBY ballot initiative, or a partisan flip in the Legislature triggers partial repeal of the preemption package. The reform regime survives but is materially weakened. Outcome: trajectory reverts to Scenario A after a 4-year boom; cumulative net new units lock in at maybe 600-800k by 2045.

**Latent-demand parameter is higher than 0.20.** If μ is closer to 0.35, all new supply is absorbed by migration. Real rent does not improve at all relative to baseline. Population reaches 13.5M+. The model's projected ~$2,100/HH/year residual income improvement disappears. Politically catastrophic — voters see growth without rent relief.

**Macro shocks.** Persistent 7%+ mortgage rates suppress private development. A 2008-style financial crisis halts capital flows for 2-3 years and removes 200,000-400,000 units from the trajectory. A federal policy regime change cuts IRA infrastructure funding mid-stream. Outcome: trajectory reverts toward C-low or B by 2045.

**Climate disasters.** A Northridge-magnitude earthquake or a Palisades-magnitude fire resets coastal-zone politics, triggers insurance withdrawal, and absorbs construction labor for rebuilding rather than new units. Reduces delivered units by 100,000-300,000 over the recovery period.

**Coastal cities win on the edges.** Court narrowings of the housing preemption in coastal high-income jurisdictions (Beverly Hills, Pacific Palisades, Manhattan Beach areas, La Cañada Flintridge, San Marino) preserve effective obstruction in 5-10% of the county's parcels. The countywide trajectory is averaged across the rest, but neighborhood-level outcomes are bimodal.

**Fiscal dividend leaks more than projected.** State income-tax growth does not return to LA. Property-tax allocation reform fails. EIFD adoption is patchy. Value capture overshoots and kills feasibility. Outcome: infrastructure self-funding share falls from 68% to 30-40% in C; the funding gap widens; utility expansion stalls; the funnel chokes.

**Construction labor doesn't scale.** Apprenticeship pipelines fail to expand. Trade unions resist pattern-book and modular productivity gains. The labor cap binds at 35-45k completions/year regardless of permit volume. Outcome: cumulative units cap around 800k by 2045 in a "labor-bottleneck" version of the central case.

The pattern across these failure modes: many of them are *path-dependent* and *mutually reinforcing*. A utility-execution stall increases fiscal-funding gaps which deepen the next utility-execution stall. An early political-reversal event reduces investor confidence which reduces capital availability which slows production which provides political ammunition for further reversal. The model's deterministic structure does not capture the cascading-failure dynamic; in reality, failure modes cluster.

---

## 23. Bottom-line forecast ranges

Combining model output, sensitivity analysis, and red-team adjustment, the honest forecast ranges are:

| Indicator | Baseline 2024 | Baseline 2045 | C central 2045 | D high build 2045 | E drag 2045 |
|---|---|---|---|---|---|
| **Cumulative net new units** | — | 200-450k | 800k-1.4M | 1.4-1.9M | 50-150k |
| **Population (millions)** | 9.85 | 10.8-11.3 | 11.4-12.0 | 11.8-12.7 | 10.3-10.6 |
| **Median real rent** | $1,954 | $2,250-$2,400 | $2,050-$2,180 | $2,030-$2,180 | $2,300-$2,500 |
| **Real rent change vs 2024** | — | +15% to +23% | +5% to +12% | +4% to +12% | +18% to +28% |
| **Median home value (real)** | $834k | $1.05M-$1.20M | $0.95M-$1.05M | $0.95M-$1.05M | $1.10M-$1.25M |
| **Median HH income (real)** | $90,112 | $89-91k | $88-91k | $88-91k | $89-91k |
| **Residual income after rent** | $66,664 | $61-64k | $63-66k | $63-66k | $60-63k |
| **HPI (50 = baseline)** | 50 | 52-60 | 38-46 | 38-44 | 65-78 |
| **Homelessness cost avoidance** | — | ~$0 | $0.3-0.6B/yr | $0.3-0.6B/yr | $0 |
| **Employer establishments** | 305k | 330-360k | 370-420k | 390-450k | 320-345k |
| **Net new public revenue** | — | $0-2B | $8-15B | $9-15B | <$0 |
| **Infra self-funded share** | — | 15-30% | 50-80% | 80-100% | <10% |
| **Legal/implementation risk** | — | 18-25 | 28-38 | 32-42 | 32-42 |
| **Delivery risk** | — | 35-45 | 18-30 | 8-18 | 55-65 |

These ranges are wider than the central-case point estimates because they incorporate red-team adjustments, sensitivity analysis findings, and the +50% confidence-band widening for years past 2035.

**The most likely central case** is something between Scenarios C and F — probably 800,000 to 1.3 million cumulative net new units by 2045, population reaching 11.4-11.7 million, real rent rising ~10-14% (vs 18% baseline), residual income up ~$1,500-$2,500/HH/year, and homelessness pressure index moderating to 42-50 in the mid-period before partial rebound. This requires the housing core to pass and survive courts, utility execution to improve materially, and HCD enforcement to be staffed. It does not require everything in the high-build scenario to go right.

**The high-build case** (1.5-1.9 million units, 11.8-12.7M population) requires near-perfect execution across all ten conditions in Section 21. It is plausible — the model produces it under self-consistent assumptions — but it is not the most likely outcome. Treat D as a ceiling, not a target.

**The implementation-drag case** (50-150k units, 10.3-10.6M population) is what happens if the legal package passes but execution fails. This is depressingly plausible. The most likely failure point is utility execution; second most likely is administrative sabotage; third is construction-cost / capital-market shocks. The drag scenario is actually closer to the *current* trajectory than the abundance scenarios are; California has been writing housing-element laws for thirty years without commensurate built units.

**The legal-collision case** (~600-800k units, 11.5-11.9M population, modest rent improvement) is what happens if courts narrow significant pieces of the package. This is likely for the commercial preemption and fiscal-allocation pieces; less likely but possible for parts of the housing core. F is the realistic outcome for coastal high-income jurisdictions, even if the rest of the county tracks closer to C.

**Bottleneck ranking** (which constraint binds most in 2045 across realistic scenario distributions):

1. **Utilities and physical infrastructure.** The single largest source of variance.
2. **Institutional execution capacity** (HCD staffing, local building departments, permitting offices). Determines whether legal authority translates to approvals.
3. **Construction trades labor and materials.** Multi-year apprenticeship lead times, materials inflation volatility, insurance costs.
4. **Capital markets and financing conditions.** Path-dependent on macro environment.
5. **Local government compliance and litigation.** Substantial but addressable via state backstop and HCD enforcement, *if* those are staffed.
6. **Fiscal misalignment.** Real but partially solvable via EIFDs, value capture, and state matching grants.
7. **Politics and durability.** A 20-year horizon assumes coalition survival; possible but historically rare.
8. **Legal authority itself.** This is the one that California can solve fastest. It is also the one that gets the most attention in the discourse, and the least binding in practice.

**Hard-nosed conclusions:**

- *How much can LA realistically grow?* +1.5-2.5 million people by 2045 in the realistic abundance trajectory. +500k-1M in the moderate or legal-collision trajectory. Approximately flat in the drag trajectory.
- *How much could housing costs realistically fall relative to baseline?* Real rent could be 8-12 percentage points lower than baseline counterfactual by 2045. It will not fall in absolute terms in any realistic scenario.
- *Would median income rise or fall?* Approximately flat in real terms. Composition effects offset agglomeration effects at the population growth levels we observe.
- *Would real residual income improve?* Yes, by approximately $1,500-$2,500/HH/year in abundance scenarios. This is the core welfare gain.
- *Would homelessness pressure decline materially?* Yes, during the 2030-2040 window — by roughly 8,000-10,000 fewer unsheltered persons at peak. Partial rebound by 2045. Sustained reduction requires non-housing complementary investment.
- *Can the growth dividend fund a meaningful share of infrastructure?* Yes, 50-80% in central scenarios, 100% only in the most aggressive case with high fiscal capture. A funding gap of $1-3B/year is the realistic central case.
- *Is the binding constraint legal authority, institutional execution, fiscal plumbing, or physical delivery?* All four bind. Ranked: physical delivery > institutional execution > fiscal plumbing > legal authority. The discourse focuses on the least binding constraint.

---

## 24. Appendix: assumptions and sensitivity tests

### A.1. Key parameter values

All parameters are stored in `data/baseline_assumptions.json` and `data/scenario_parameters.json`. Critical values:

- Rent-supply elasticity α = −0.30 central (range −0.20 to −0.45).
- Income pass-through β = 0.70.
- Real-wage drift = 0.005/yr.
- Latent-demand μ = 0.20 central (0.28 in D high build).
- Persons-per-household = 2.81 baseline (range 2.50-3.21).
- Permit-to-completion lag CDF (5-yr): {0.15, 0.45, 0.75, 0.90, 1.00}.
- Construction labor scaling cap = 1.40× rolling 3-yr average.
- Modular productivity lift = 8-15%.
- Service cost per capita marginal = $1,500/year.
- Infrastructure capex per unit = $45,000.
- Property tax effective rate = 1.0%, LA share post-ERAF = 0.55.
- Sales tax local share = 1% of combined 9.75%.
- Income tax share returned to LA infrastructure = 5% (generous).
- HPI weights: rent-to-income 30, rent-growth 15, ELI supply 10, employment 10, residual income 12 (tanh-bounded).

### A.2. Scenario × variant matrix

Six scenarios (A baseline, B moderate, C max central, D high build, E implementation drag, F legal collision) × three utility variants (improved 75k/yr, current_drag 38k/yr, severe_bottleneck 18k/yr) × three fiscal-capture variants (none 0%, partial 30%, high 60%) = 54 runs. Each run produces 20 annual states (2026-2045). Total 1,080 row-output. Headline view: 6 scenarios × 4 milestone years (2030, 2035, 2040, 2045) × headline pairing per scenario = 24 rows in `outputs/scenario_summary.csv` (well, 216 rows when including all variant combos at milestone years).

### A.3. Sensitivity test results

Tornado analysis on Scenario C central, perturbing each parameter individually at low and high multipliers. Largest effects on cumulative net new units 2045:

| Parameter | Low perturbation | High perturbation |
|---|---|---|
| fiscal_capture_rate | −25.3% (fcap=0) | +6.2% (capped by util) |
| utility_lag_months | +4.5% | −4.9% |
| latent_demand_mu | +2.9% | −3.0% |
| litigation_delay_years | +0.9% | −1.9% |
| rent_alpha | −0.8% | +1.2% |
| value_capture_feasibility_drag | +0.3% | −0.9% |
| income_composition_lambda | +0.7% | −0.7% |
| commercial_friction_elasticity | −0.3% | +0.4% |

Largest effects on real rent 2045:

| Parameter | Low perturbation | High perturbation |
|---|---|---|
| rent_alpha | +1.0% (less elastic) | −1.5% (more elastic) |
| fiscal_capture_rate | +1.2% (less reinvestment) | −0.3% |
| latent_demand_mu | −0.4% | +0.4% |
| utility_lag_months | −0.2% | +0.2% |

Several findings emerge:

**Fiscal capture rate is the single most consequential parameter.** Cutting it to zero reduces cumulative units by 25% — because reinvestment-driven utility expansion is what enables the model to escape the baseline utility cap. The central case's projected outcomes critically depend on fiscal-capture mechanisms working.

**Utility lag matters a lot but not as much as fiscal-capture-driven utility expansion.** Direct utility-lag perturbation moves units by ~5%, but the indirect effect via fiscal capture is ~25%.

**Latent-demand μ moves population but not cumulative units.** Higher μ pulls in more people who absorb supply; cumulative built units stays roughly the same; rent moderation is reduced.

**Rent-supply elasticity is the largest driver of rent outcomes.** A more elastic α (closer to −0.45) produces 1.5% additional rent reduction by 2045; less elastic (closer to −0.20) reduces it by 1%. The literature range itself accounts for ~3% of rent outcome.

**Several parameters have surprisingly small impact.** Income-composition λ, commercial-friction elasticity, value-capture-feasibility drag, and most macro parameters move headline outcomes by less than 1%. This is partly because the model's binding constraints (utility capacity, legal-capacity ramp) dominate; secondary parameters operate within the envelope these set.

**Caveat: this is local OAT sensitivity, not global.** One-at-a-time sensitivity does not capture parameter interactions. A simultaneous low fiscal_capture × high utility_lag × low construction_labor × high political_reversal would compound effects far more than the OAT bands suggest.

### A.4. Files in the project

- `data/baseline_assumptions.json` — LA County 2024 anchors with source labels and evidence tags.
- `data/scenario_parameters.json` — base parameters and scenario/variant overrides.
- `src/model.py` — equation core (11 modules + YearState dataclass).
- `src/scenarios.py` — scenario × variant composition logic.
- `src/reforms.py` — 36-reform candidate menu.
- `src/sensitivity.py` — OAT tornado runner.
- `src/run_model.py` — CLI orchestrator + chart rendering.
- `tests/test_invariants.py` — 10 invariant tests (all passing).
- `outputs/scenario_summary.csv` — milestone-year headline view.
- `outputs/scenario_summary_full.csv` — full annual view across all 54 runs.
- `outputs/reform_menu.csv` — reform candidate list.
- `outputs/tornado.csv` — OAT sensitivity results.
- `outputs/charts/*.png` — 23 charts.
- `outputs/red_team_memo.md` — 30-point critique.
- `memo.md` — this document.

### A.5. How to reproduce

```bash
cd la-county-maximum-statutory-abundance-model
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python -m src.run_model
pytest tests/
```

All 54 runs + sensitivity tornado + charts + reform menu regenerate from JSON parameters in under 5 seconds. Edit `data/scenario_parameters.json` to test alternative parameter values; re-run to see how outcomes shift.

---

**Final word.** This model is not a forecast. It is a structured way to think about which constraints bind LA County's housing future under various assumptions about what the California Legislature, the courts, the utilities, the construction industry, the capital markets, and the political coalition will and will not do over the next twenty years. The single most defensible takeaway is that **legal authority is the easiest of the binding constraints to fix, and the least determinative of outcomes once fixed.** California can pass the Maximum Statutory Abundance package and still fail to build, if the institutions and physical infrastructure required to deliver units do not also receive sustained legislative, fiscal, and political investment. Conversely, even imperfect legal reform — with a good utility track and serious HCD enforcement — can deliver a million net new units, modest rent relief, real welfare gains, and a fiscal dividend large enough to be politically self-sustaining. The question is which path the state actually walks.

— *End of memo*

