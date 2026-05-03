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

*[End of chunk 1 of 5. Sections 6-10 follow.]*
