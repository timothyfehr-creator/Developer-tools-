# Tesla Autonomy Dossier
## System Architecture, De Facto Capability, Human Factors, and Regulatory Landscape

**Status:** TEMPLATE — awaiting Phase 1 source acquisition
**Last updated:** 2026-02-08
**Claim tagging:** All non-trivial claims tagged [FACT], [INFERENCE], or [SPECULATION]

---

## 1. Naming Reconciliation Map

> **Prerequisite:** This section must be completed before any forecasting (Phase 3).

### Hardware Generation ↔ Chip Name ↔ Foundry Matrix

| HW Generation | Chip Name(s) | Foundry | Process Node | First Sighting | First Deliveries | Volume | Status |
|---|---|---|---|---|---|---|---|
| HW2.5 | Nvidia Parker | TSMC (Nvidia) | — | — | 2017-08 | 2017–2019 | Discontinued |
| HW3 | FSD Chip / AI3 | Samsung | 14nm | 2019-03 | 2019-04 | 2019-Q3 | Legacy; still in some fleet |
| HW4 | AI4 | TBD | TBD | 2023-Q1 | 2023-Q2 | 2023-Q4+ | Current production |
| A15 / HW5? | A15 / AI5? | TBD | TBD | TBD | TBD | TBD | **RESEARCH NEEDED** |

### Competing Hypotheses

**H1:** A15 == AI5 == HW5 — single next-gen vehicle compute platform
- Supporting evidence: *(to be populated)*
- Against: *(to be populated)*

**H2:** A15 is datacenter/training silicon; AI5/HW5 is vehicle inference silicon
- Supporting evidence: *(to be populated)*
- Against: *(to be populated)*

**Resolution criteria:** Teardown, FCC filing, or Tesla primary doc that unambiguously maps the names.

### What we know
*(to be populated with [FACT]-tagged items)*

### What we don't know
*(to be populated)*

### Best skeptic argument
*(to be populated)*

### What would change my mind
*(to be populated)*

---

## 2. System Architecture

### 2.1 Sensor Suite by Hardware Generation

| Sensor | HW3 | HW4 | A15/HW5 (projected) |
|---|---|---|---|
| Forward cameras | | | |
| Side/rear cameras | | | |
| Ultrasonic sensors | | | |
| Radar | | | |
| Other | | | |

*(Populate from teardowns and Tesla documentation only. No fan-site specs without verification.)*

### 2.2 Compute Architecture

#### HW3
*(Board-level description from teardowns)*

#### HW4
*(Board-level description from teardowns)*

#### A15 / HW5 (Projected)
*(Only what can be sourced. Separate [FACT] from [INFERENCE] from [SPECULATION].)*

### 2.3 Software Approach

- **Architecture:** End-to-end neural network (FSD v12+)
- **Occupancy networks:** *(describe role)*
- **Training pipeline:** *(as publicly knowable)*
- **Inference pipeline:** *(on-vehicle compute flow)*
- **OTA update model:** *(cadence, staged rollout process, rollback capability)*

### What we know
### What we don't know
### Best skeptic argument
### What would change my mind

---

## 3. De Facto Autonomy Assessment

> Not SAE levels. This section is about what actually happens behind the wheel.

### 3.1 Where It Works Well
*(Sourced from independent testing and community consensus)*

- Highway cruise (straight, well-marked)
- Lane changes (initiated or auto)
- On-ramps / off-ramps
- Stop-and-go traffic
- *(others as evidenced)*

### 3.2 Where It Struggles
*(Sourced; quantify where possible)*

- Unprotected left turns
- Construction zones
- Pedestrian-dense areas
- Adverse weather (rain, fog, low sun)
- Unusual road geometry
- Parking lots / tight maneuvers
- *(others as evidenced)*

### 3.3 Failure Mode Taxonomy

| Failure Mode | Frequency (est.) | Severity | Typical Context | Source(s) |
|---|---|---|---|---|
| Phantom braking | | | | |
| Aggressive/passive oscillation | | | | |
| Missed or late lane change | | | | |
| Unprotected turn hesitation/error | | | | |
| Routing error | | | | |
| Disengagement (driver-initiated) | | | | |

### What we know
### What we don't know
### Best skeptic argument
### What would change my mind

---

## 4. Human Factors & Driver Experience

### 4.1 Driver Monitoring System
- What it detects (gaze, hands, attention)
- Nag cadence and escalation path
- What happens on escalation (warnings → slowdown → lockout)

### 4.2 Misuse Prevention
- What Tesla does
- What Tesla should do (based on safety research / competitor standards)
- Known exploits and their prevalence

### 4.3 Competitive Comparison

| Feature | Tesla FSD | GM Super Cruise | BMW Highway Assistant | Mercedes Drive Pilot |
|---|---|---|---|---|
| ODD (where it works) | | | | |
| Driver monitoring method | | | | |
| Nag frequency | | | | |
| Hands-free capability | | | | |
| Liability model | | | | |
| Geographic coverage | | | | |

### 4.4 Waymo as Experiential Anchor
- Availability in LA (your routes)
- Cost per trip
- What "real autonomy" feels like as a passenger (no supervision)
- Why this matters for calibrating Tesla expectations

### What we know
### What we don't know
### Best skeptic argument
### What would change my mind

---

## 5. Regulatory & Safety Landscape

### 5.1 Active NHTSA Actions

| Investigation/Recall | Status | Key Findings | Behavioral Impact on FSD |
|---|---|---|---|
| PE 22-002 | | | |
| 23V-838 (2M recall) | | | |
| *(others)* | | | |

### 5.2 CA DMV Requirements
- Autonomous vehicle testing permits
- Reporting requirements
- How Tesla's approach differs from Waymo/Cruise permitting

### 5.3 IIHS Safeguard Ratings
- What they measure
- Tesla's current rating
- What would need to change for upgrade/downgrade

### 5.4 Marketing Restrictions
- CA AG actions (if any)
- FTC scrutiny (if any)
- "Full Self-Driving" naming controversy

### 5.5 Regulatory Trajectory Forecast
- [INFERENCE] More conservative? More constrained?
- Political environment considerations (administration stance)
- What this means for the driving experience in practice

### What we know
### What we don't know
### Best skeptic argument
### What would change my mind

---

## 6. Deprecation & Retrofit Risk

### 6.1 Historical Precedent

| Transition | Retrofit Offered? | Timeline | Cost | Completion Rate | Notes |
|---|---|---|---|---|---|
| HW2.5 → HW3 | Yes | *(dates)* | *(cost)* | *(est.)* | |
| HW3 → HW4 | *(status)* | | | | |

### 6.2 Implications for HW4 → A15

- [INFERENCE] Will Tesla offer retrofits?
- What "buy now" buyers should expect
- Software-only improvements available on HW4 (what's not hardware-gated)

### What we know
### What we don't know
### Best skeptic argument
### What would change my mind
