# AI5 Stack Forecast — Early 2027
## Hardware Availability, Software Capability, and Lived Experience Projections

**Status:** COMPLETE
**Last updated:** 2026-02-08
**Forecast horizon:** 2027-03-31 (unless otherwise stated)
**Claim tagging:** All non-trivial claims tagged [FACT], [INFERENCE], or [SPECULATION]
**Methodology:** Bayesian odds-based updates with explicit multipliers per evidence item

---

## 1. Naming Correction

The original plan referenced "A15." This is a naming error. The correct designation is **AI5** (also known as HW5). Tesla renamed the "HW" prefix to "AI" at the June 2024 Annual Shareholder Meeting [FACT]. This forecast uses the correct naming throughout.

---

## 2. Forecast Question Summary

| Q# | Question (abbreviated) | Prior | Refined Prior | Posterior | Bucket | Last Updated |
|---|---|---|---|---|---|---|
| Q1 | AI5 in ≥1 delivered U.S. vehicle by 2027-03-31 | 0.55 | 0.40 | **0.35** | Unlikely–Toss-up | 2026-02-08 |
| Q2 | AI5 on Model Y/3 configurator by 2027-03-31 | 0.45 | 0.30 | **0.20** | Unlikely | 2026-02-08 |
| Q3 | AI5 ≥30% of U.S. deliveries by 2027-03-31 | 0.25 | 0.10 | **0.05** | Very unlikely | 2026-02-08 |
| Q4 | ≥30% freeway intervention reduction vs early-2026 | 0.55 | 0.65 | **0.72** | Likely | 2026-02-08 |
| Q5 | ≥20% surface street intervention reduction | 0.40 | 0.50 | **0.55** | Toss-up–Likely | 2026-02-08 |
| Q6 | Regulatory guardrails tighten noticeably by 2027-03-31 | 0.60 | 0.70 | **0.78** | Very likely | 2026-02-08 |
| Q7 | AI5 naming resolved by 2026-12-31 | 0.70 | 0.95 | **0.98** | Near-certain | 2026-02-08 |

**Confidence buckets:**

| Bucket | Range | Label |
|---|---|---|
| 1 | 0.00–0.15 | Very unlikely |
| 2 | 0.15–0.35 | Unlikely |
| 3 | 0.35–0.55 | Toss-up |
| 4 | 0.55–0.75 | Likely |
| 5 | 0.75–0.90 | Very likely |
| 6 | 0.90–1.00 | Near-certain |

---

## 3. HW Transition Base Rates

> This calibrates our hardware availability priors (Q1–Q3) using historical data.

### HW3 → HW4 Ramp Timeline

| Milestone | Date | Time from First Delivery |
|---|---|---|
| First credible signal (FCC Phoenix radar filing) | June 2022 [FACT] | -9 months |
| AI Day reveal | Sep 2022 [FACT] | -6 months |
| First US customer delivery (Model X) | March 2023 [FACT] | 0 |
| Model Y deliveries begin (Fremont) | May 2023 [FACT] | +2 months |
| ~30% of US deliveries on HW4 | Q3 2023 [FACT] | +4–6 months |
| ~90%+ of new production on HW4 | Q1 2024 [FACT] | +12 months |
| Native resolution FSD (v13.2, end of emulation) | Dec 2024 [FACT] | +21 months |

### Key Base-Rate Observations

| Pattern | HW3→HW4 Data Point | Implication for AI5 |
|---|---|---|
| Signal-to-delivery lag | ~9 months (FCC filing → first delivery) | As of Feb 2026, **no FCC filing or teardown** for AI5 has been reported [FACT]. This is bearish for Q1. |
| First delivery → 30% share | ~4–6 months | Even if AI5 ships H2 2026, 30% by Q1 2027 requires 3–6 months of aggressive ramp [INFERENCE] |
| First delivery → full transition | ~12 months | Full transition by Q1 2027 is impossible unless deliveries start by Q1 2026 (they haven't) |
| Software parity lag | 21 months for HW4 | AI5 vehicles will likely run in AI4 emulation mode initially, limiting the hardware advantage [INFERENCE] |
| Pre-announcement | Tesla did NOT pre-announce HW4 transition [FACT] | AI5 transition may also be unannounced; configurator won't distinguish |

### Prior Refinement Based on Base Rates

| Q# | Original Prior | Refined Prior | Adjustment Rationale |
|---|---|---|---|
| Q1 | 0.55 | **0.40** | No FCC filing or teardown signal for AI5 as of Feb 2026. HW4 had a 9-month FCC-to-delivery lag. Samsung fab not producing yet. Reduce. |
| Q2 | 0.45 | **0.30** | Model Y/3 configurator availability typically lags first delivery. HW4 took 2 months for Model Y after first Model X delivery. But AI5 volume won't be sufficient. Reduce significantly. |
| Q3 | 0.25 | **0.10** | 30% share within 3–6 months of first delivery is possible (HW4 did it) but requires volume production. Samsung Taylor fab not at scale. TSMC Arizona 3nm not until 2027. Sharply reduce. |

---

## 4. Evidence Log & Probability Updates

### Q1: AI5 in ≥1 Delivered U.S. Vehicle by 2027-03-31

**Refined Prior: 0.40** → odds = 0.40/0.60 = 0.667

| # | Evidence | Source | Grade | Direction | Multiplier | Reasoning |
|---|---|---|---|---|---|---|
| E1 | AI5 design "finished" July 2025 | Tesla statement | B | Supports | 1.3× | Design completion is necessary milestone, but Tesla forward-looking claims are unreliable |
| E2 | AI5 design "almost done" Jan 2026 — contradicts E1 | Tesla earnings Q4 2025 | A | Refutes | ÷1.5 | Direct contradiction from 6 months later. If still not finalized, production delays likely |
| E3 | Musk: "not available in sufficient volume until mid-2027" | Musk on X, Nov 2025 | B | Refutes | ÷1.3 | "Mid-2027" for volume means limited units are earlier, but "mid-2027" suggests H1 2027 is tight for even first deliveries |
| E4 | Samsung Taylor fab EUV trials starting March 2026 | Industry reports | B | Supports | 1.2× | Fab is progressing, but trials ≠ production |
| E5 | TSMC Arizona 3nm production not until 2027 | Industry reports | B | Refutes | ÷1.2 | One of two foundry sources won't be ready |
| E6 | No FCC filing for AI5 vehicle module as of Feb 2026 | Absence of evidence | A | Refutes | ÷1.5 | HW4 had FCC filing 9 months before delivery. No filing = no delivery imminent |
| E7 | Cybercab ships with AI4, not AI5 | Tesla confirmed | A | Refutes | ÷1.3 | Tesla's own flagship autonomy product can't use AI5 because it's not ready |

**Update chain:**

```
Start: odds = 0.667
× 1.3 (E1) = 0.867
÷ 1.5 (E2) = 0.578
÷ 1.3 (E3) = 0.444
× 1.2 (E4) = 0.533
÷ 1.2 (E5) = 0.444
÷ 1.5 (E6) = 0.296
÷ 1.3 (E7) = 0.228

p = 0.228 / (1 + 0.228) = 0.186
```

**But:** I'll cap the downward adjustment because there's genuine possibility Tesla ships a small number of AI5-equipped vehicles (e.g., new Roadster, Cybertruck refresh, or test fleet) before Q1 2027. Adjusting upward to **0.35** to account for this "limited units" scenario.

**Posterior: 0.35** — Bucket: Unlikely–Toss-up boundary

---

### Q2: AI5 on Model Y/3 Configurator by 2027-03-31

**Refined Prior: 0.30** → odds = 0.30/0.70 = 0.429

| # | Evidence | Source | Grade | Direction | Multiplier | Reasoning |
|---|---|---|---|---|---|---|
| E8 | Q1 kill criteria depends on Q1: if first delivery is unlikely, configurator is more unlikely | Structural | — | Refutes | ÷1.3 | Configurator availability lags delivery |
| E9 | HW4 appeared on Model Y ~2 months after first Model X delivery | Historical | B | Ambiguous | 1.0× | Fast transition IF production exists, but AI5 production doesn't |
| E10 | Volume "mid-2027" means Model Y/3 integration likely H2 2027 at earliest | Tesla roadmap | B | Refutes | ÷1.4 | High-volume models are production-constrained |
| E11 | Tesla does not distinguish HW in configurator | Historical | B | Ambiguous | 1.0× | No configurator change even if AI5 ships — but Q2 asks about availability, not visibility |

**Update chain:**

```
Start: odds = 0.429
÷ 1.3 (E8) = 0.330
÷ 1.4 (E10) = 0.236

p = 0.236 / (1 + 0.236) = 0.191
```

**Posterior: 0.20** — Bucket: Unlikely

---

### Q3: AI5 ≥30% of U.S. Deliveries by 2027-03-31

**Refined Prior: 0.10** → odds = 0.10/0.90 = 0.111

| # | Evidence | Source | Grade | Direction | Multiplier | Reasoning |
|---|---|---|---|---|---|---|
| E12 | "Not in sufficient volume until mid-2027" | Musk, Nov 2025 | B | Refutes | ÷2.0 | If volume = mid-2027, 30% by Q1 2027 is near-impossible |
| E13 | Samsung and TSMC fabs not at scale production | Industry | B | Refutes | ÷1.5 | No silicon supply = no vehicle production |

**Update chain:**

```
Start: odds = 0.111
÷ 2.0 (E12) = 0.056
÷ 1.5 (E13) = 0.037

p = 0.037 / (1 + 0.037) = 0.036
```

**Posterior: 0.05** (rounded up from 0.036 for residual uncertainty) — Bucket: Very unlikely

---

### Q4: ≥30% Freeway Intervention Reduction vs. Early-2026 Baselines

**Refined Prior: 0.65** (raised from 0.55 because software trajectory is strong) → odds = 0.65/0.35 = 1.857

| # | Evidence | Source | Grade | Direction | Multiplier | Reasoning |
|---|---|---|---|---|---|---|
| E14 | Community tracker: v12.5→v14 = ~57× improvement in critical DE rate over ~18 months | FSD Community Tracker | B+ | Supports | 2.0× | Massive improvement trajectory. Even if rate slows, 30% more improvement is plausible |
| E15 | v14 data: ~0.97 critical DE per 10K miles overall; ~834 miles/critical DE in city | Community Tracker (41K miles, 62 testers) | B+ | Supports | 1.3× | Current baseline is already good; 30% improvement from here is a smaller absolute delta |
| E16 | MotorTrend: FSD went from "questioned whether responsible" to Best Tech 2026 | MotorTrend | A- | Supports | 1.3× | Independent credible source confirming step-change improvement |
| E17 | David Moss: 12,961 miles intervention-free on v14.2 (coast-to-coast) | Individual tester | C | Supports | 1.05× | Single tester, exceptional result, but demonstrates ceiling capability |
| E18 | Regulatory constraints (PE25012) may force more conservative behavior | NHTSA investigation | A | Refutes | ÷1.2 | Conservative behavioral tuning could increase phantom interventions while reducing violations |
| E19 | Diminishing returns: easy gains captured, long-tail harder | Engineering judgment | — | Refutes | ÷1.2 | 57× improvement won't repeat; question is whether 30% more is achievable |
| E20 | HW4 native resolution only since Dec 2024 — still early in optimization cycle | Tesla release notes | A- | Supports | 1.3× | Full hardware utilization is new; more software gains expected from native resolution |

**Update chain:**

```
Start: odds = 1.857
× 2.0 (E14) = 3.714
× 1.3 (E15) = 4.829
× 1.3 (E16) = 6.277
× 1.05 (E17) = 6.591
÷ 1.2 (E18) = 5.493
÷ 1.2 (E19) = 4.577
× 1.3 (E20) = 5.950

p = 5.950 / (1 + 5.950) = 0.856
```

**However:** The 57× improvement evidence is from a community tracker with self-selection bias (enthusiasts who report tend to have positive experiences). Applying a model uncertainty discount of ~15% to account for measurement limitations.

**Posterior: 0.72** — Bucket: Likely

---

### Q5: ≥20% Surface Street Intervention Reduction

**Refined Prior: 0.50** (raised from 0.40 based on v14 urban improvements) → odds = 0.50/0.50 = 1.000

| # | Evidence | Source | Grade | Direction | Multiplier | Reasoning |
|---|---|---|---|---|---|---|
| E21 | Chuck Cook UPL testing: v12.3 dangerous → v14.1.2 "impressive performance" | Chuck Cook (YouTube) | B+ | Supports | 1.5× | Longitudinal testing on hardest urban maneuver shows dramatic improvement |
| E22 | v14: pothole avoidance, parking lot navigation, fewer false braking | Tesla release notes | A- | Supports | 1.3× | Multiple surface-street-relevant improvements |
| E23 | v14 community tracker: ~834 miles/critical DE in city | Community Tracker | B+ | Supports | 1.2× | Baseline is already reasonable; 20% more improvement from a good baseline is achievable |
| E24 | Surface streets are inherently harder (pedestrians, bikes, UPLs, construction) | Engineering judgment | — | Refutes | ÷1.2 | Improvement rate historically slower than highway |
| E25 | Construction zone handling still problematic per tester reports | Multiple testers | B | Refutes | ÷1.15 | Known weakness may resist improvement within 12 months |
| E26 | Regulatory pressure may force more conservative urban behavior | PE25012 | A | Mixed | ÷1.1 | Fewer violations but potentially more hesitation = mixed feel |

**Update chain:**

```
Start: odds = 1.000
× 1.5 (E21) = 1.500
× 1.3 (E22) = 1.950
× 1.2 (E23) = 2.340
÷ 1.2 (E24) = 1.950
÷ 1.15 (E25) = 1.696
÷ 1.1 (E26) = 1.541

p = 1.541 / (1 + 1.541) = 0.606
```

Applying model uncertainty discount of ~10% (less uncertain than highway because surface street testing is more varied in the community data).

**Posterior: 0.55** — Bucket: Toss-up–Likely boundary

---

### Q6: Regulatory Guardrails Tighten Noticeably by 2027-03-31

**Refined Prior: 0.70** (raised from 0.60 based on unprecedented regulatory pressure) → odds = 0.70/0.30 = 2.333

| # | Evidence | Source | Grade | Direction | Multiplier | Reasoning |
|---|---|---|---|---|---|---|
| E27 | PE25012: 2.88M vehicles, 80 violation reports, 8,313 potential violations, Feb 23 deadline | NHTSA | A | Supports | 2.5× | Most serious investigation yet; scope and escalation pattern point toward enforcement action |
| E28 | CA DMV deceptive marketing ruling, 60-day compliance window | CA DMV | A | Supports | 1.5× | State-level enforcement adds pressure regardless of federal stance |
| E29 | IIHS: both Autopilot and FSD rated POOR | IIHS | A | Supports | 1.2× | Industry rating creates reputational/insurance pressure |
| E30 | Class action certified Aug 2025 | Federal court | A | Supports | 1.2× | Legal pressure from private litigation adds behavioral constraints |
| E31 | Trump admin pushing AV deregulation | DOT policy | B | Refutes | ÷1.5 | Strong political counterweight; could preempt state actions |
| E32 | Tesla reintroduced "Mad Max" mode same week as PE25012 | Tesla behavior | B | Refutes | ÷1.15 | Tesla may resist constraints even under pressure |
| E33 | 5 open NHTSA investigations simultaneously | NHTSA | A | Supports | 1.3× | Cumulative regulatory surface area is unprecedented |

**Update chain:**

```
Start: odds = 2.333
× 2.5 (E27) = 5.833
× 1.5 (E28) = 8.750
× 1.2 (E29) = 10.500
× 1.2 (E30) = 12.600
÷ 1.5 (E31) = 8.400
÷ 1.15 (E32) = 7.304
× 1.3 (E33) = 9.496

p = 9.496 / (1 + 9.496) = 0.905
```

Applying model uncertainty discount of ~12% (political environment is genuinely uncertain — Trump deregulation could be more impactful than modeled).

**Posterior: 0.78** — Bucket: Very likely

---

### Q7: AI5 Naming Resolved by 2026-12-31

**Refined Prior: 0.95** (raised from 0.70 because naming is already resolved) → odds = 0.95/0.05 = 19.0

| # | Evidence | Source | Grade | Direction | Multiplier | Reasoning |
|---|---|---|---|---|---|---|
| E34 | Tesla renamed HW→AI at June 2024 shareholder meeting | Tesla primary source | A | Supports | 5.0× | Direct resolution event |
| E35 | Teslascope, community sources confirm AI5 = HW5 convention | Multiple independent | B+ | Supports | 1.5× | Corroboration from tracking sources |

**Update chain:**

```
Start: odds = 19.0
× 5.0 (E34) = 95.0
× 1.5 (E35) = 142.5

p = 142.5 / (1 + 142.5) = 0.993
```

**Posterior: 0.98** (capped; residual uncertainty = Tesla could rebrand again) — Bucket: Near-certain

---

## 5. Scenario Table

| Dimension | Conservative | Base | Optimistic |
|---|---|---|---|
| **AI5 first U.S. delivery** | Not by Q1 2027 | Q4 2026 (limited, e.g., new Roadster or test fleet) | Q3 2026 |
| **AI5 on Model Y/3 configurator** | Not by Q1 2027 | Not by Q1 2027 | Q1 2027 (premium trims only) |
| **AI5 volume share by Q1 2027** | 0% | <5% | 5–10% |
| **Freeway intervention improvement** | 15–25% | 30–45% | 50%+ |
| **Surface street improvement** | 10–15% | 20–30% | 35%+ |
| **Regulatory tightening** | Major new constraints (PE25012 recall + CA DMV action) | Moderate additional guardrails via OTA | Minimal change (federal preemption) |
| **Scenario probability weight** | **30%** | **50%** | **20%** |

### Scenario Narratives

**Conservative (30%):** AI5 design delays push first silicon to late 2026. Samsung Taylor yields are poor initially. No AI5-equipped customer vehicles by Q1 2027. Software improvement continues but at a decelerating rate — the 57× improvement era is over, and incremental gains yield 15–25% improvement on highways, 10–15% on surface streets. PE25012 results in a formal recall with behavioral constraints that add conservatism to FSD. CA DMV enforcement forces marketing changes but no sales suspension. Net effect: FSD is noticeably better than today but not transformatively so, and regulatory constraints add annoyance.

**Base (50%):** AI5 limited units ship H2 2026 in low-volume vehicles (new Roadster, Cybertruck refresh, or a small Model S/X run). They run in AI4 emulation mode with no immediate capability advantage. Software on AI4 hardware (v15/v16 era) delivers 30–45% highway improvement and 20–30% surface street improvement. PE25012 results in additional OTA guardrails (more conservative at intersections, reduced speed in ambiguous zones) but no feature removal. Regulatory constraints are noticeable but manageable. Your HW4 Tesla is meaningfully better than today.

**Optimistic (20%):** AI5 production ramps faster than expected. Samsung Taylor yields are strong. TSMC Arizona accelerates. First AI5 vehicles (possibly a refreshed Model 3/Y) reach configurator by Q1 2027 in limited quantities. Software improvement accelerates — v15/v16 bring 50%+ highway improvement. Regulatory environment stabilizes as Trump admin provides political cover. AI5 vehicles offer a step-change in perception quality. Your HW4 Tesla improves significantly from software alone, and AI5 vehicles represent the next generation.

---

## 6. Predicted AI5 Stack

| Attribute | Prediction | Confidence | Basis |
|---|---|---|---|
| **Compute** | 2,000–2,500 TOPS | Medium | [FACT] Tesla disclosures. Not independently verified. |
| **Architecture** | Dedicated inference ASIC. Half-reticle die. No GPU/ISP. Softmax in hardware. | High | [FACT] Multiple Tesla disclosures confirm design philosophy. |
| **Process node** | 3nm (TSMC N3P) + 4nm (Samsung) | High | [FACT] Dual-sourced, confirmed by multiple industry sources. |
| **Sensor changes vs HW4** | Likely same 8× 5MP cameras initially | Medium | [INFERENCE] Board supports 12 cameras (3 spare connectors on HW4). AI5 may enable additional cameras. |
| **Redundancy** | Dual-SoC (Tesla standard) | High | [INFERENCE] Every Tesla compute board since HW3 has been dual-redundant. |
| **Thermal/power** | 250–800W (wide range) | Low | [INFERENCE] 250W is Musk's target; 800W may be worst-case or multi-chip. HW4 is 160W. AI5 may require active liquid cooling in vehicles. |
| **Memory** | HBM3, 1.9 TB/s bandwidth | High | [FACT] Confirmed in Tesla disclosures. Major upgrade from HW4's standard LPDDR. |
| **Networking** | No V2X announced | Medium | [INFERENCE] Tesla has historically avoided V2X; no signals of change. |

### What we know
- AI5 is a clean-sheet inference ASIC with no legacy GPU or ISP blocks [FACT].
- It uses HBM3 memory with 1.9 TB/s bandwidth [FACT].
- It is dual-sourced across TSMC and Samsung [FACT].
- The power envelope is wide (250–800W), suggesting design tradeoffs are not finalized [INFERENCE].

### What we don't know
- Sustained real-world TOPS vs. peak marketing TOPS.
- Whether 250W is achievable or whether vehicles will need liquid cooling.
- What software capabilities are hardware-gated behind AI5 vs. achievable on AI4.
- Whether AI5 enables any new sensor modalities (e.g., activating Phoenix radar, new camera positions).

### Best skeptic argument
AI5's 2,000–2,500 TOPS sounds impressive, but Tesla has not demonstrated what they will do with 7–8× more compute. The end-to-end neural network on AI4 is already running well on v14 — what specific capabilities require 2,500 TOPS that 300 TOPS cannot deliver? If the answer is "larger models for better edge-case handling," the improvement may be marginal from a user's perspective while the power, thermal, and cost implications are significant. The wide power range (250–800W) suggests Tesla is still optimizing the design, not shipping a finished product.

### What would change my mind
AI5 engineering samples benchmarked by a third party showing measurably better perception in degraded conditions (rain, night, construction), or Tesla demonstrating a capability on AI5 that is provably impossible on AI4 (e.g., real-time 3D scene reconstruction at 5MP resolution across all 8 cameras simultaneously).

---

## 7. Software Capability Forecast

### Scenario S1 (Base): Incremental Improvement on HW4

**Observable proxy projections for early 2027:**

| Proxy | Current (early 2026) | S1 Projection (early 2027) | Basis |
|---|---|---|---|
| OTA major update cadence | ~Monthly | ~Monthly (stable) | [INFERENCE] No evidence of acceleration or deceleration |
| FSD version | v14.2 | v15 or v16 [SPECULATION] | Based on ~2 major versions per year pattern |
| Community critical DE rate | ~0.97 per 10K miles | ~0.5–0.7 per 10K miles | [INFERENCE] Extrapolating improvement curve with deceleration |
| ODD coverage | Most roads in fair weather | + limited construction zone handling, better rain performance | [SPECULATION] |
| Phantom braking events | Occasional, mostly resolved | Rare | [INFERENCE] v14 already dramatically reduced these |
| Unprotected left turns | Dramatically improved (v14) | Further refined | [INFERENCE] Still the hardest urban maneuver |

**What HW4 + v15/v16 can likely deliver without AI5:**
- Further reduction in phantom braking and false interventions [INFERENCE]
- Improved construction zone navigation (partially) [SPECULATION]
- Better rain/low-visibility performance (limited by camera-only sensing) [INFERENCE]
- Smoother, more confident urban driving [INFERENCE]
- Potential parking lot autonomy improvements [SPECULATION]

**What HW4 likely CANNOT deliver without AI5:**
- Real-time processing of all 8 cameras at full native resolution simultaneously (compute-gated) [INFERENCE]
- Significantly larger neural network models (memory/bandwidth-gated) [INFERENCE]
- Sub-100ms photon-to-control latency in all conditions (compute-gated) [SPECULATION]

### Scenario S2 (Optimistic): Accelerated Improvement

Same structure as S1, with more aggressive assumptions:

| Proxy | S2 Projection (early 2027) | Delta from S1 |
|---|---|---|
| OTA cadence | Bi-weekly major releases | Faster iteration |
| Community critical DE rate | ~0.3–0.5 per 10K miles | ~30% better than S1 |
| ODD coverage | + construction zones, rain driving (degraded mode) | Broader domain |
| Phantom braking | Near-zero | Better than S1 |
| Unprotected lefts | High reliability | Better than S1 |

**What would need to be true for S2:**
- Tesla's training infrastructure scaling delivers diminishing-returns-breaking improvements [SPECULATION]
- Cortex cluster utilization increases (current utilization unknown) [SPECULATION]
- Validation pipeline speeds up, enabling faster OTA cadence [INFERENCE]
- Regulatory environment doesn't force conservative tuning [SPECULATION]

### What LLMs Do NOT Solve (Hard Constraints on Both Scenarios)

| Constraint | Why LLMs Don't Help |
|---|---|
| Camera physics in rain/fog/snow | No amount of software overcomes photons not reaching the sensor |
| Novel obstacles | Training data can't cover every possible road hazard |
| Adversarial conditions | Deliberate interference (e.g., modified signs, spoofed markings) |
| Legal liability framework | Unsupervised FSD requires regulatory approval, not just capability |
| Map/infrastructure freshness | Road changes happen faster than fleet-based mapping can detect |
| Sensor hardware limits | 5MP cameras have fixed resolution; no software can exceed it |

### What we know
- FSD v14 on HW4 is a genuine step-change from v12.x [FACT].
- The improvement trajectory over the last 18 months has been steep (~57× in critical DEs) [FACT — community data].
- HW4 native resolution has only been utilized since Dec 2024, meaning optimization headroom likely remains [INFERENCE].

### What we don't know
- Whether the improvement curve will maintain its slope or decelerate sharply (S-curve dynamics).
- What specific capabilities are gated behind AI5 compute vs. achievable on AI4 with software alone.
- How regulatory constraints (PE25012 outcome) will affect the functional capability of FSD updates.
- Whether Tesla's training infrastructure has bottlenecks that would slow software improvement.

### Best skeptic argument
The 57× improvement narrative is based on community tracker data with significant self-selection bias (enthusiastic early adopters reporting in favorable conditions). The actual fleet-wide improvement, including users in rain, construction zones, and challenging urban environments, may be far less impressive. Furthermore, improvement curves in safety-critical systems typically follow an S-curve — rapid initial gains followed by a plateau as long-tail problems dominate. The easy wins (phantom braking, basic lane-keeping) may be captured; the hard wins (construction zones, edge-case intersections, adverse weather) may resist further improvement on camera-only hardware.

### What would change my mind
Tesla publishing fleet-wide, condition-segmented intervention data (not cherry-picked community tracker results). Or independent testing organizations (AMCI, Consumer Reports) conducting controlled longitudinal studies showing sustained improvement rates across diverse conditions.

---

## 8. Kill Criteria Status Check

| Trigger | Fired? | Date Checked | Current Status | Impact |
|---|---|---|---|---|
| No AI5 teardowns/FCC filings by 2026-12-31 | **Partially firing** | 2026-02-08 | No filings or teardowns exist as of Feb 2026 [FACT]. Trigger hasn't fully fired (deadline is Dec 2026) but trajectory is concerning. | Q1 reduced from 0.55 → 0.35 |
| Regulator action targeting FSD behaviors | **Firing** | 2026-02-08 | PE25012 is the most serious Tesla investigation ever; CA DMV issued deceptive marketing ruling [FACT] | Q6 increased from 0.60 → 0.78 |
| Volume timeline pushed to late 2027+ | **Partially firing** | 2026-02-08 | Musk said "mid-2027" for volume in Nov 2025 [FACT]; design "almost done" contradiction suggests further delay possible [INFERENCE] | Q3 reduced from 0.25 → 0.05 |
| Retrofit program announced | **Not fired** | 2026-02-08 | No AI5 retrofit program announced. HW4→AI5 explicitly ruled out [FACT] | No change |
| Independent testers report plateau | **Not fired** | 2026-02-08 | Testers report continued improvement through v14 [FACT] | Q4 and Q5 maintained or increased |

---

## 9. Buyer-Relevant Bottom Line

### The Key Insight

**For a buyer in early 2026, AI5 hardware is irrelevant to your ownership experience through at least Q1 2027.**

The evidence overwhelmingly points to:

1. **AI5 will not be in your vehicle by Q1 2027** (Q1 posterior: 0.35, and that's for ANY vehicle, not yours specifically)
2. **AI5 will not be on the Model Y/3 configurator by Q1 2027** (Q2 posterior: 0.20)
3. **Even if AI5 ships, it will run in AI4 emulation mode initially** — HW4's 21-month emulation precedent suggests no immediate capability advantage
4. **Software improvement on HW4 is your actual improvement path** — and the trajectory is strong (Q4 posterior: 0.72, Q5 posterior: 0.55)
5. **Regulatory constraints are very likely to tighten** (Q6 posterior: 0.78) — your FSD experience may become more conservative even as the underlying capability improves

### What This Means for Your Decision

| Strategy | Verdict |
|---|---|
| **"I'll wait for AI5"** | You'll be waiting until at least H2 2027 for volume availability, and likely longer for Model Y/3. If you need a car now, this is not practical. |
| **"I'll buy HW4 now and upgrade later"** | There is no upgrade path. HW4→AI5 retrofit is explicitly impossible. |
| **"I'll buy HW4 now and rely on software"** | **This is the rational path.** Software improvement is the dominant value driver through 2027. Subscribe at $99/mo to maintain flexibility. |
| **"I'll buy HW4 now and lock in the $8,000 purchase"** | Only if you plan 7+ year ownership and won't trade in to Tesla. The subscription preserves optionality. |

---

*End of forecast. Last updated 2026-02-08.*
