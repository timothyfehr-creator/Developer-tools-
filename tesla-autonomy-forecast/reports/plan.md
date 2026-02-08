# Tesla Autonomy Deep-Dive + A15 Forecast (Early 2027) + Hermosa Lived Experience
## Streamlined Evidence-Weighted Forecasting Plan

---

## 1. Goal & Scope

An evidence-based, buyer-relevant assessment of Tesla's autonomy system, a rigorous forecast
of what the A15-based hardware/software stack will look like by early 2027, and a "lived
driving experience" simulation for a driver in Hermosa Beach, CA.

### Target Persona

| Attribute | Detail |
|---|---|
| **Local trips** | 5–8 mi around South Bay (Hermosa / Redondo / Manhattan Beach / Torrance). Surface streets + short freeway hops. |
| **Medium trips** | Hermosa ↔ Santa Monica; Hermosa ↔ DTLA. A few times/month. |
| **Road trips** | ~1×/quarter: Central CA, Ojai, Palm Springs, San Diego. |
| **Priority** | Techy feel + maximum practical automation + low annoyance. Will supervise; wants workload reduction without surprise "WTF moments." |

### Buyer Decision This Plan Must Answer

> **Buy now, wait for A15, or do something else — and what signals should I watch?**

---

## 2. Analytical Standards (Non-Negotiable QA Gates)

These gates apply to every section of every deliverable. Violation = rewrite.

### 2.1 Claim Tagging

Every non-trivial claim must be tagged:

| Tag | Requirements |
|---|---|
| **[FACT]** | Citation required: URL + date + publisher. Verifiable. |
| **[INFERENCE]** | Explicit reasoning + the supporting citations that justify the inference. |
| **[SPECULATION]** | Stated uncertainty level + why evidence is missing + what would resolve it. |

### 2.2 Source Quality Ladder

| Grade | Description | Allowed Forecast Impact |
|---|---|---|
| **A** (hard evidence) | Tesla primary docs (manuals, release notes, configurator). NHTSA/IIHS/regulators. Reuters/FT/WSJ/Bloomberg with named sourcing. Hardware teardowns with board photos + part numbers. FCC filings. Supplier/foundry press releases tied to specific nodes/volume. | Can move odds materially (multiplier 2.0×–5.0×) |
| **B** (medium evidence) | Earnings calls/presentations (if corroborated). Credible auto journalism with repeatable tests + disclosed methodology. Narrowly specific job postings (e.g., "HW5 bring-up", "ASIL-D validation"). | Modest odds shift (multiplier 1.2×–2.0×) |
| **C** (soft signal) | Forums, influencers, rumor accounts. | Hypothesis generation only (multiplier ≤1.1×, only when multiple independent C sources converge) |

### 2.3 Section End Requirements

Every major section must close with:

- **What we know** (FACT-tagged items only)
- **What we don't know** (explicit gaps)
- **Best skeptic argument** against the section's conclusions
- **What would change my mind** (specific, obtainable evidence)

### 2.4 Naming Reconciliation Requirement

Before any forecasting, resolve (or explicitly fail to resolve) the mapping between:
- HW generations (HW3 / HW4 / HW5)
- Chip naming (AI4 / AI5 / AI6 and/or A14 / A15 / A16)
- Foundry/manufacturer (if known)
- First appearance windows (sightings vs. deliveries vs. volume)

If unresolvable, present competing hypotheses with tag markers and state what evidence would resolve it. This is an acceptable outcome — false certainty is not.

---

## 3. Forecasting Protocol

This is the analytical spine. It stays rigorous.

### 3.1 Forecast Questions

Binary, dated. Default horizon: **2027-03-31** unless stated otherwise.

**Hardware Availability**

| ID | Question |
|---|---|
| **Q1** | At least one Tesla production vehicle delivered to U.S. customers includes an A15-class compute module by 2027-03-31. |
| **Q2** | A15-class compute is available in the U.S. configurator on at least one high-volume Tesla model (Model Y/3) by 2027-03-31. |
| **Q3** | A15-class compute reaches "meaningful volume" (≥30% of U.S. deliveries across models) by 2027-03-31. |

**Capability / Lived Experience**

| ID | Question |
|---|---|
| **Q4** | Noticeable reduction in driver interventions on LA-area freeways (clear weather, light-to-moderate traffic) vs. early-2026 community-reported baselines by 2027-03-31. Defined as: ≥30% reduction where measurable, OR consensus among ≥3 credible independent testers that highway performance is "meaningfully better." |
| **Q5** | Noticeable reduction in driver interventions on LA-area surface streets (arterials + unprotected turns) vs. early-2026 baselines by 2027-03-31. Defined as: ≥20% reduction where measurable, OR consensus among ≥3 credible independent testers. |
| **Q6** | Regulatory pressure results in additional guardrails or constraints that noticeably reduce risky/non-compliant behaviors (rolling stops, late aggressive merges, etc.) by 2027-03-31. |

**Naming Reconciliation**

| ID | Question |
|---|---|
| **Q7** | By 2026-12-31, decisive public evidence exists that A15 is (or is not) the same generation as AI5/HW5. |

### 3.2 Priors

Initialize with conservative priors. These will be refined after HW transition timeline research.

| Q# | Prior | Rationale |
|---|---|---|
| Q1 | 0.55 | Tesla has announced next-gen compute; HW4 ramp precedent took ~12 months from first sighting to meaningful deliveries. |
| Q2 | 0.45 | Configurator availability typically lags first deliveries; Tesla has historically gated new HW to premium trims first. |
| Q3 | 0.25 | Meaningful volume within months of first delivery is historically rare for Tesla HW transitions. |
| Q4 | 0.55 | Software improvements are continuous; question is whether delta is perceptible. HW4 showed gains; OTA cadence is frequent. |
| Q5 | 0.40 | Surface street performance improves slower than highway; unprotected turns and pedestrian interactions are harder problems. |
| Q6 | 0.60 | NHTSA investigations active; CA regulatory scrutiny increasing; Tesla has already been forced into behavioral constraints. |
| Q7 | 0.70 | Tesla naming usually becomes clear through teardowns/FCC filings 6–12 months before volume. |

**After timeline research, update priors using HW3→HW4 ramp data as the primary base-rate analog. Document every adjustment.**

### 3.3 Update Mechanics

Bayesian odds-based updates:

```
odds = p / (1 - p)
odds_new = odds × multiplier         (if evidence supports)
odds_new = odds / multiplier          (if evidence refutes)
p_new = odds_new / (1 + odds_new)
```

For each evidence item, record:
- **Direction:** supports / refutes / ambiguous
- **Multiplier:** justified by grade and directness
- **Reasoning:** why this multiplier, not higher or lower

Present final posteriors as point estimates with **ordinal confidence buckets**:

| Bucket | Probability Range | Label |
|---|---|---|
| 1 | 0.00–0.15 | Very unlikely |
| 2 | 0.15–0.35 | Unlikely |
| 3 | 0.35–0.55 | Toss-up |
| 4 | 0.55–0.75 | Likely |
| 5 | 0.75–0.90 | Very likely |
| 6 | 0.90–1.00 | Near-certain |

This dual representation (point estimate + bucket) preserves the math while being honest about precision limits.

### 3.4 Kill Criteria

Per-question falsification triggers. If these fire, sharply adjust probabilities:

| Trigger | Affected Qs | Action |
|---|---|---|
| By 2026-12-31: no credible teardowns, FCC filings, or primary-source references to a new compute module entering builds | Q1, Q2, Q3 | Reduce Q1 to ≤0.25; Q2/Q3 proportionally |
| Regulators publish binding constraints or Tesla issues recall targeting core FSD behaviors | Q6 ↑ ; Q4/Q5 mixed | Increase Q6; reassess Q4/Q5 (capability may improve while allowed behavior narrows) |
| Credible reporting shifts "volume 2027" to "late 2027/2028" | Q3 | Reduce to ≤0.10 |
| Tesla announces A15 retrofit program for HW4 vehicles | Q1, buyer strategy | Major positive signal for "buy now" path |
| Multiple independent testers report regression or plateau in FSD v13+ | Q4, Q5 | Reduce by 0.10–0.15 each |

### 3.5 LLM Acceleration Scenarios

Used in Q4/Q5 capability forecasts. Based on **observable proxies**, not internal velocity guesses.

**Scenario S1 (Base):**
- OTA update cadence remains similar to 2025–2026 (~monthly major, weekly minor)
- Release notes scope stays comparable
- Community-reported regression rates flat or modestly improved
- ODD (Operational Design Domain) expands incrementally

**Scenario S2 (Optimistic):**
- OTA cadence increases OR scope per release grows measurably
- Community regression reports decline
- ODD expands to new road types / conditions (e.g., unsignaled intersections, construction zones)
- Validation speed improves (shorter gap between limited release and wide rollout)

**What LLMs do NOT solve** (explicit constraints on both scenarios):
- Sensing hardware limits (camera resolution, occlusion, rain/fog physics)
- Long-tail safety events (novel obstacles, adversarial road conditions)
- Regulatory/legal speed limits on deployment
- Liability framework uncertainty
- Map/infrastructure data freshness

---

## 4. Deliverables

Three core reports + one unified data file. That's it.

### 4.1 reports/tesla_autonomy_dossier.md

The foundational research document. Everything else builds on this.

**Sections:**

1. **Naming Reconciliation Map**
   - HW generation ↔ chip name ↔ foundry ↔ first appearance matrix
   - Competing hypotheses if unresolved, with resolution criteria
   - [Must be completed before forecast sections are written]

2. **System Architecture**
   - Sensor suite by HW generation (sourced only; no fan-site specs without verification)
   - Compute architecture (board-level where teardowns exist)
   - Software approach: end-to-end neural net, occupancy networks, training/inference pipeline (as publicly knowable)
   - OTA update model and release cadence

3. **De Facto Autonomy Assessment**
   - Not SAE levels (which are definitional, not experiential)
   - Where it works well (highway cruise, lane changes, on-ramps)
   - Where it struggles (unprotected lefts, construction, pedestrian-dense areas, rain)
   - Failure mode taxonomy: disengagements, phantom braking, aggressive/passive oscillation, routing errors

4. **Human Factors & Driver Experience**
   - Driver monitoring system: what it detects, nag cadence, escalation path
   - Misuse prevention: what Tesla does vs. what it should do
   - Comparison to top supervised systems:
     * GM Super Cruise / Ultra Cruise (highway ODD, attention monitoring)
     * BMW Highway Assistant (if data available)
     * Mercedes Drive Pilot (L3, limited ODD — useful as a regulatory contrast)
   - Note: Waymo as a competitive anchor for "what full autonomy feels like in LA" — relevant because it operates on some of your routes

5. **Regulatory & Safety Landscape**
   - Active NHTSA investigations and their likely behavioral impacts
   - CA DMV requirements (autonomous vehicle testing permits, reporting)
   - IIHS safeguard ratings and what they measure
   - Marketing restriction precedents (CA AG actions, FTC if applicable)
   - Likely trajectory: more conservative? more constrained? what that means for the driving experience

6. **Deprecation & Retrofit Risk** *(added)*
   - HW2.5 → HW3 retrofit history: what happened, timelines, costs
   - HW3 → HW4 retrofit status
   - Implications for HW4 → A15 path
   - Risk to "buy now" buyers

### 4.2 reports/a15_stack_forecast_early_2027.md

The quantitative forecast. Depends on the dossier.

**Sections:**

1. **Forecast Question Summary**
   - All 7 questions with current priors displayed

2. **HW Transition Base Rates**
   - HW3 → HW4 ramp timeline (from first sighting through volume)
   - What analogies hold and what's different for A15
   - [This is the key base-rate calibration step]

3. **Evidence Log**
   - Organized by question
   - For each evidence item: source, grade, direction, multiplier, reasoning, excerpt
   - Inline in the report (not a separate file) for readability
   - Numbered for cross-reference

4. **Probability Updates**
   - Per question: prior → evidence chain → posterior
   - Explicit stepwise updates shown (not just "I ended up at X")
   - Ordinal bucket assignment for each posterior

5. **Scenario Table**

   | Dimension | Conservative | Base | Optimistic |
   |---|---|---|---|
   | A15 first delivery | Not by Q1 2027 | Late 2026 | Mid 2026 |
   | A15 configurator availability | Not by Q1 2027 | Q1 2027 (premium trims) | Late 2026 |
   | A15 volume share by Q1 2027 | <5% | 10–20% | 30%+ |
   | Freeway intervention improvement | <15% | 20–35% | 40%+ |
   | Surface street improvement | <10% | 15–25% | 30%+ |
   | Regulatory tightening | Significant new constraints | Moderate additional guardrails | Minimal change |

   *(Values to be filled during research; this is the template structure)*

6. **Predicted A15 Stack** (with confidence levels per attribute)
   - Compute (TOPS, architecture class)
   - Sensors (any changes from HW4 suite)
   - Redundancy architecture
   - Thermal/power envelope
   - Memory/bandwidth
   - Networking (V2X, connectivity)

7. **Software Capability Forecast**
   - S1 (base) and S2 (optimistic) scenario projections
   - What changes are hardware-gated vs. software-gated
   - "Even without A15, software on HW4 could deliver X" assessment

### 4.3 reports/hermosa_lived_experience.md

The experiential translation of the forecast into your daily life.

**Sections:**

1. **Route Class Definitions**

   | Class | Example | Key Stressors |
   |---|---|---|
   | **Local surface** | Hermosa loops, errands in Torrance/Redondo | Unprotected lefts, parking lots, pedestrians, bikes, delivery trucks, stop signs |
   | **Short freeway hop** | PCH → 405 → Rosecrans | Merge/exit in <2 miles, lane changes, speed differential |
   | **Medium: beach cities** | Hermosa → Santa Monica via 405 or PCH | 405 congestion, SM surface streets, parking at destination |
   | **Medium: downtown** | Hermosa → DTLA via 405/110 | 110 freeway (narrow, sharp curves, older infrastructure), downtown grid (peds, bikes, one-ways, Uber/Lyft stops) |
   | **Road trip: desert** | Hermosa → Palm Springs via I-10 | Long highway cruise, wind, sun glare, construction zones, destination resort streets |
   | **Road trip: coastal/mountain** | Hermosa → Ojai/Central CA via 101/1 | Two-lane roads, curves, limited passing, rural intersections |
   | **Road trip: I-5 corridor** | Hermosa → San Diego via I-5 | Long monotonic highway, Camp Pendleton stretch, SD urban arrival |

2. **Per Route Class: Automation Usage Map**

   For each class:
   - Where you'd realistically engage FSD (freeway segments, arterials, residential)
   - Where you'd proactively disengage (and why)
   - Expected intervention rate range: low / medium / high + reasoning
   - "Critical intervention" risk hotspots (specific intersections, merge points, known problem areas)
   - Annoyance score: nags, false positives, phantom events
   - "Feel" score: relaxing ←→ vigilant spectrum
   - Practical operating guidance: settings, when to take over proactively, tips for minimizing surprises

   **Scoring rubric:**

   | Score | Intervention Rate (per trip) | Annoyance | Feel |
   |---|---|---|---|
   | 5 (excellent) | 0–1 minor | Rare nags, no phantoms | Relaxing; you forget you're supervising |
   | 4 (good) | 1–2 minor | Occasional nag, rare phantom | Comfortable; occasional glance-checks |
   | 3 (acceptable) | 2–4 minor OR 1 significant | Noticeable nags | Alert but not stressed |
   | 2 (mediocre) | 4+ minor OR 2+ significant | Frequent nags/phantoms | Vigilant; hands hovering |
   | 1 (poor) | Frequent significant | Constant | Stressful; why bother? |

3. **Two Narrated Drives**

   **Drive A: Rush-hour Hermosa → Santa Monica (Tuesday, 5:30 PM)**
   - Minute-by-minute narrative
   - Where FSD is engaged/disengaged and why
   - Specific stress points and how the system handles them
   - Overall feel assessment
   - Presented as two versions: current HW4/FSD v13+ AND projected A15/early-2027 software

   **Drive B: Weekend Hermosa → Palm Springs (Saturday, 8:00 AM)**
   - Same structure
   - Emphasis on highway cruise comfort, construction zones, destination navigation
   - Two versions: current vs. projected

4. **Comparative Context**
   - "What if you just used Waymo for the Santa Monica trip?" (availability, cost, experience)
   - "What does Super Cruise give you on the I-10 to Palm Springs?" (highway-only, but how good?)
   - Not a full competitive analysis — just enough to calibrate expectations

5. **Your Personalized Score Card**

   Summary table: each route class × current system score × projected early-2027 score × confidence level

---

## 5. Data Files

Two files. Structured, but not over-engineered.

### 5.1 data/evidence_registry.json

Unified evidence + source tracking. One file instead of four.

```json
{
  "metadata": {
    "created": "YYYY-MM-DD",
    "last_updated": "YYYY-MM-DD",
    "plan_version": "2.0-streamlined"
  },
  "forecasts": [
    {
      "question_id": "Q1",
      "statement": "At least one Tesla production vehicle delivered to U.S. customers includes an A15-class compute module by 2027-03-31.",
      "horizon_date": "2027-03-31",
      "prior_p": 0.55,
      "current_p": null,
      "confidence_bucket": null,
      "evidence": [
        {
          "evidence_id": "E001",
          "summary": "",
          "source_url": "",
          "publisher": "",
          "date": "",
          "grade": "A|B|C",
          "direction": "supports|refutes|ambiguous",
          "multiplier": 1.0,
          "multiplier_justification": "",
          "excerpt": "",
          "reliability_notes": ""
        }
      ],
      "kill_criteria": [
        "By 2026-12-31: no credible teardowns, FCC filings, or primary-source references to new compute module entering builds → reduce to ≤0.25"
      ],
      "skeptic_case": "",
      "what_changes_my_mind": [],
      "key_assumptions": [],
      "last_updated": ""
    }
  ],
  "sources_index": [
    {
      "source_id": "S001",
      "url": "",
      "publisher": "",
      "date": "",
      "doc_type": "",
      "grade": "A|B|C",
      "key_claims": [],
      "referenced_by_evidence": ["E001"]
    }
  ]
}
```

### 5.2 data/timeline.json

Structured timeline for HW generations and milestones.

```json
{
  "hardware_generations": [
    {
      "generation": "HW3",
      "also_known_as": ["FSD Computer", "AI3"],
      "chip": "Tesla FSD Chip (Samsung 14nm)",
      "first_sighting": "2019-03",
      "first_deliveries": "2019-04",
      "volume_threshold_date": "2019-Q3",
      "notes": "",
      "sources": ["S00X"]
    }
  ],
  "software_milestones": [
    {
      "date": "YYYY-MM-DD",
      "event": "",
      "significance": "",
      "sources": ["S00X"]
    }
  ],
  "regulatory_actions": [
    {
      "date": "YYYY-MM-DD",
      "body": "NHTSA|CA DMV|IIHS|other",
      "action": "",
      "impact": "",
      "sources": ["S00X"]
    }
  ]
}
```

---

## 6. Execution Plan

Streamlined from 7 steps to 5 phases, with parallelism where possible.

### Phase 1: Foundation (source acquisition + naming reconciliation — parallel)

**Track A: Source Acquisition**
- Gather sources across all categories:
  * Tesla primary docs (manuals, FSD pages, release notes)
  * Safety/regulators (NHTSA ODI investigations, recalls, IIHS ratings)
  * Hardware (HW4 teardowns, next-gen chip reporting, supplier/foundry info)
  * Independent testing (methodology-forward road tests with intervention counts)
  * Legal/compliance (marketing restrictions, driver monitoring requirements)
- For each source, create an entry in `evidence_registry.json → sources_index`
- **Minimum before proceeding:** 4+ Grade A, 4+ Grade B, 1+ teardown/compute source
- Note: if A-grade sources for A15 specifically are scarce, that itself is evidence (bearish for Q1/Q2/Q3 timelines)

**Track B: Naming Reconciliation (runs in parallel with Track A)**
- Research HW generation naming across all available sources
- Build the mapping table for the dossier
- Populate `timeline.json → hardware_generations`
- Accept "competing hypotheses" as a valid outcome — do not force resolution
- Output: reconciliation section draft for dossier

**Gate:** Proceed to Phase 2 when both tracks have minimum outputs.

### Phase 2: System Analysis → Dossier

Using Phase 1 sources, write `tesla_autonomy_dossier.md`:

1. Naming reconciliation (from Phase 1 Track B)
2. System architecture (sensors, compute, software)
3. De facto autonomy assessment (where it works, where it doesn't)
4. Human factors and driver experience (monitoring, nags, competitive comparison)
5. Regulatory landscape (investigations, constraints, trajectory)
6. Deprecation/retrofit risk

**All claims tagged. All sections close with the required four elements.**

**Gate:** Dossier draft complete before forecast.

### Phase 3: Forecast Build

Using the dossier as foundation:

1. Initialize `evidence_registry.json` with priors
2. Refine priors using HW3→HW4 ramp data from the dossier
3. For each question: ingest evidence, compute stepwise updates, log multipliers
4. Build scenario table (conservative / base / optimistic)
5. Write `a15_stack_forecast_early_2027.md`
6. Apply kill criteria check: do any currently fire? If so, adjust.

### Phase 4: Lived Experience Simulation

Using the dossier (system capabilities) and forecast (projected improvements):

1. Define route classes and stressors for Hermosa Beach persona
2. Score each route class: current system and projected early-2027
3. Write the two narrated drives (Santa Monica rush hour + Palm Springs weekend)
4. Add comparative context (Waymo, Super Cruise)
5. Build the personalized scorecard
6. Write `hermosa_lived_experience.md`

### Phase 5: Buyer Strategy Synthesis

Final section appended to the lived experience report OR as a standalone section in the dossier:

- **Buy now:** which Tesla config maximizes odds of best early-2027 experience? Retrofit likelihood?
- **Wait:** target quarter + hard signals to watch (A-grade evidence only)
- **Hedge:** "workload reduction" vs. "tail-risk minimization" tradeoff framing
- **Monitor list:** 5–7 specific, observable signals with check-in dates

---

## 7. What Changed From the Original Plan

| Original | Streamlined | Why |
|---|---|---|
| 7 data files + 2 schemas | 2 data files, schemas inline | Infrastructure was becoming the project |
| `/data/raw` + `/data/extracted` directories | Dropped | Excerpts live in evidence_registry; no need to archive raw HTML |
| `sources.yaml` + `evidence_log.jsonl` + `forecast_registry.json` + `priors.yaml` | Single `evidence_registry.json` | One file to maintain; cross-referencing is trivial |
| `sources_seed.yaml` | Dropped | Source targets described in Phase 1 prose; a seed file adds no value |
| Schema files (`*.schema.json`) | Schema shown inline in plan | The schema IS the plan; separate files are ceremony |
| 7 execution steps | 5 phases with explicit parallelism | Faster; naming reconciliation no longer blocks on 5+ A-grade sources |
| Point probability outputs only | Point estimates + ordinal buckets | Honest about precision limits without losing the math |
| No competitive context | Waymo + Super Cruise anchors added | "What can I get today" is essential for buyer calibration |
| No deprecation/retrofit analysis | Added to dossier | Directly affects "buy now vs wait" decision |
| Intervention rate targets as pure percentages | Percentage OR tester consensus (dual criterion) | Solves the "floating baseline" problem you correctly identified |
| LLM scenarios based on internal velocity | Reframed around observable proxies (OTA cadence, regression rates, ODD expansion) | Can't observe internal dev speed; can observe output |

## 8. What Did NOT Change

- **FACT/INFERENCE/SPECULATION tagging** — non-negotiable
- **Source quality ladder (A/B/C)** — enforced strictly
- **Bayesian update mechanics** — full odds-based computation with logged multipliers
- **Kill criteria** — per question, explicit triggers
- **Red-team requirement** — skeptic case + "what changes my mind" per section
- **Section close format** — know / don't know / skeptic argument / what changes my mind
- **Forecast questions (Q1–Q7)** — identical, with improved Q4/Q5 measurement criteria
- **Narrated drive format** — both drives, current vs projected versions
- **Buyer strategy as final output** — the whole point

---

## Estimated Research Scope

| Category | Target Sources | Grade Mix |
|---|---|---|
| Tesla primary docs | 3–5 | Mostly A |
| NHTSA / regulators | 3–4 | A |
| Hardware teardowns / chip reporting | 2–3 | A–B |
| Independent road tests | 3–5 | B (methodology-dependent) |
| Earnings calls / presentations | 2–3 | B |
| Credible journalism | 3–5 | A–B |
| Community / forums | As needed | C only |
| **Total** | **~20–25 sources** | |

This is enough to populate the evidence registry without drowning in source management.
