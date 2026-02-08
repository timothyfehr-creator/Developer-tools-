# Tesla Autonomy Dossier
## System Architecture, De Facto Capability, Human Factors, and Regulatory Landscape

**Status:** COMPLETE
**Last updated:** 2026-02-08
**Claim tagging:** All non-trivial claims tagged [FACT], [INFERENCE], or [SPECULATION]
**Audience:** Prospective and current Tesla buyers evaluating FSD purchase/subscription decisions
**Stance:** Skeptical, evidence-first, no hype

---

> **How to read this document:** Every non-trivial claim is tagged:
> - **[FACT]** — verified from Tesla filings, teardowns, NHTSA records, or multiple independent sources
> - **[INFERENCE]** — reasonable conclusion drawn from available facts, but not directly confirmed
> - **[SPECULATION]** — plausible scenario with limited evidentiary support; treat with caution
>
> Each major section ends with a structured uncertainty audit.

---

## Table of Contents

1. [Naming Reconciliation Map](#1-naming-reconciliation-map)
2. [Hardware Generations](#2-hardware-generations)
3. [System Architecture](#3-system-architecture)
4. [Driver Monitoring & Human Factors](#4-driver-monitoring--human-factors)
5. [Competitive Comparison](#5-competitive-comparison)
6. [Regulatory & Safety Landscape](#6-regulatory--safety-landscape)
7. [Deprecation & Retrofit Risk](#7-deprecation--retrofit-risk)
8. [FSD Pricing & Ownership Economics](#8-fsd-pricing--ownership-economics)
9. [Buyer Decision Framework](#9-buyer-decision-framework)

---

## 1. Naming Reconciliation Map

Tesla's hardware naming has been a source of persistent confusion in the community. This section resolves it.

### The Rename Event

Tesla officially renamed the "HW" (Hardware) prefix to "AI" at the **June 13, 2024 Annual Shareholder Meeting** [FACT]. This was a branding change only — no silicon changes accompanied the rename.

### Definitive Name Mapping

| Old Name | Current Name | Notes |
|---|---|---|
| HW3 | AI3 | Same chip. Samsung 14nm. |
| HW4 | AI4 | Same chip. Samsung 7nm. |
| HW5 | AI5 | New chip. TSMC 3nm + Samsung 4nm. |
| "A15" | **Error** | Community/analyst misnomer. Correct designation is AI5. |

### Role Segmentation

| Chip | Target Platform | Status |
|---|---|---|
| AI3 | Vehicles (legacy fleet) | End-of-life; FSD capped at v12.6.x [FACT] |
| AI4 | Vehicles (current production + Cybercab) | Current production silicon [FACT] |
| AI5 | Vehicles (next-gen) | Last vehicle-targeted chip [FACT]. Limited units H2 2026 [INFERENCE] |
| AI6 | Optimus robot / datacenter only | Not for vehicles [FACT] |
| Dojo D1 | Training (datacenter) | Shut down Aug 2025, restarted Jan 2026 as "Dojo 3/Space" using AI5 silicon [FACT] |

### What we know
- The HW-to-AI rename was a branding exercise at the June 2024 shareholder meeting [FACT].
- "A15" references in analyst reports and community forums are a naming error for AI5 [FACT].
- AI5 is explicitly described as the last chip intended for vehicles; AI6 targets Optimus and datacenter workloads [FACT].

### What we don't know
- Whether AI5-based Dojo 3/Space will ever deliver meaningful training throughput (the original Dojo D1 was shut down after failing to compete with H100 GPU clusters).
- Whether future software requirements could force yet another vehicle chip beyond AI5, contradicting the "last vehicle chip" claim.

### Best skeptic argument
Tesla has renamed, re-numbered, and re-scoped its chip roadmap multiple times. The claim that AI5 is the "last vehicle chip" is a forward-looking statement from a company whose forward-looking statements on autonomy have a poor track record (e.g., "robotaxis by 2020"). Treat it as an aspiration, not a commitment.

### What would change my mind
An independent teardown or FCC filing confirming AI5 vehicle integration specs, coupled with AI6 silicon that is physically incompatible with vehicle form factors.

---

## 2. Hardware Generations

### Generation Comparison Matrix

| Attribute | HW3 / AI3 | HW4 / AI4 | AI5 / HW5 (Projected) |
|---|---|---|---|
| **Foundry** | Samsung [FACT] | Samsung [FACT] | TSMC 3nm + Samsung 4nm (dual-sourced) [FACT] |
| **Process node** | 14nm [FACT] | 7nm [FACT] | 3nm / 4nm [FACT] |
| **Compute (TOPS)** | 144 [FACT] | ~300+ [FACT] | 2,000-2,500 [INFERENCE — from Tesla presentations, not independently verified] |
| **Power draw** | ~100W [FACT] | ~160W [FACT] | 250-800W [INFERENCE — wide range suggests design not finalized] |
| **Memory** | — | 16GB RAM, 256GB storage [FACT] | HBM3 [FACT — confirmed in Tesla disclosures] |
| **Die design** | — | — | Half-reticle [FACT]. No GPU/ISP — pure AI inference [FACT]. Softmax in hardware [FACT] |
| **Camera resolution** | 1.2 MP [FACT] | 5 MP (Sony IMX963) [FACT] | TBD |
| **Camera count** | 8 [FACT] | 8 (reduced front cameras: 3 to 2, higher res compensates) [FACT] | TBD |
| **Radar** | None (removed May 2021) [FACT] | Phoenix HD radar present in some S/X, but **not SW-enabled** for FSD [FACT] | TBD |
| **Ultrasonic sensors** | Present [FACT] | Removed (Oct 2022 onward) [FACT] | TBD |
| **CPU cores** | 12 [FACT] | 20 [FACT] | TBD |
| **First US delivery** | March 2019 [FACT] | March 2023 (Model X), May 2023 (Model Y) [FACT] | Limited units H2 2026; volume mid-2027 [INFERENCE] |
| **FSD software cap** | v12.6.x (end of line) [FACT] | Current (v13+) [FACT] | Future |
| **Retrofit from prior gen** | Yes (HW2.5 was drop-in, same board size) [FACT] | **No** (different form factor from HW3) [FACT] | **No** (different cooling/power from HW4) [FACT] |

### HW4 Rollout Timeline

| Milestone | Date | Source |
|---|---|---|
| First US delivery (Model X) | March 2023 [FACT] | VIN tracking / deliveries |
| Model Y deliveries begin | May 2023 [FACT] | VIN tracking / deliveries |
| ~30% of deliveries on HW4 | Q3 2023 [FACT] | Tesla quarterly data |
| Full production transition to HW4 | Q1 2024 [FACT] | Tesla quarterly data |
| HW4 running in HW3 emulation mode | March 2023 — Dec 2024 (~21 months) [FACT] | Community testing, Tesla release notes |
| FSD v13.2 uses native HW4 resolution | Dec 2024 [FACT] | Tesla release notes |

**Buyer note:** HW4 vehicles delivered between March 2023 and December 2024 ran FSD in HW3 emulation mode — meaning the 5MP cameras were downsampled to 1.2MP-equivalent and the extra CPU cores were largely unused [FACT]. Buyers who paid $8,000-$15,000 for FSD during this period received HW3-equivalent performance on HW4 hardware for up to 21 months.

### AI5 Status (as of Feb 2026)

| Claim | Date | Source | Assessment |
|---|---|---|---|
| Design "finished" | July 2025 | Tesla statement | [FACT — Tesla's claim] |
| Design "almost done" | Jan 2026 | Tesla statement | [FACT — Tesla's claim; contradicts July 2025 "finished"] |
| Samsung Taylor fab EUV trials | March 2026 | Industry reports | [INFERENCE] |
| Limited production units | H2 2026 | Tesla roadmap | [INFERENCE — subject to delay] |
| Volume production | Mid-2027 | Tesla roadmap | [SPECULATION — Tesla hardware timelines routinely slip] |

**Critical inconsistency:** Tesla described AI5 design as "finished" in July 2025, then "almost done" in January 2026 [FACT]. This contradiction suggests either (a) post-tape-out validation revealed issues requiring redesign, or (b) different Tesla representatives used imprecise language [INFERENCE]. Either way, this is not confidence-inspiring for the stated timeline.

**Cybercab ships with AI4, not AI5** [FACT]. This is a strong signal that AI5 is not production-ready and that Tesla's own robotaxi bet is hedged on existing silicon.

### What we know
- HW4 is current production silicon and runs FSD v13+ at native resolution since Dec 2024 [FACT].
- AI5 exists as a design but has contradictory "finished" / "almost done" signals [FACT].
- No HW3-to-HW4 retrofit is physically possible (different form factor) [FACT].
- No HW4-to-AI5 retrofit is planned or possible (different cooling and power requirements) [FACT].
- Cybercab launches on AI4, not AI5 [FACT].

### What we don't know
- Whether AI5's 2,000-2,500 TOPS figure is a marketing number or reflects real-world sustained throughput.
- Whether the 250-800W power range means AI5 will require liquid cooling in vehicles (current HW4 is passively cooled).
- What FSD capabilities AI5 will unlock that AI4 cannot achieve through software alone.
- Whether AI5's "half-reticle die" design was a cost optimization or a performance compromise.

### Best skeptic argument
AI5 is vaporware for vehicles on any buyer-relevant timeline. The design was "finished" and then "almost done" six months later. The Cybercab — Tesla's flagship autonomy product — ships on AI4 because AI5 is not ready. Volume production in mid-2027 means most buyers purchasing a Tesla in 2026 will receive AI4, and there is no upgrade path. If you are buying a Tesla today, AI5 is irrelevant to your ownership experience.

### What would change my mind
AI5 engineering samples benchmarked by a credible third party (not Tesla marketing), a confirmed tape-out with TSMC 3nm, or AI5 appearing in FCC filings with a vehicle form factor.

---

## 3. System Architecture

### 3.1 FSD Software Architecture (v12+)

| Component | Description |
|---|---|
| **Architecture type** | End-to-end neural network [FACT] |
| **What it replaced** | ~300,000 lines of C++ planning/rules code [FACT] |
| **Neural networks** | 48 neural networks running concurrently [FACT] |
| **Input** | 8 cameras (vision-only) [FACT] |
| **Training method** | Imitation learning from ~10 million human driving clips [FACT] |
| **Spatial awareness** | Occupancy networks: 3D voxel grid + occupancy flow from 2D camera input, >100 FPS [FACT] |

### 3.2 Training Infrastructure

| Attribute | Value |
|---|---|
| **GPU cluster** | 67,000 H100-equivalent GPUs at Cortex (Gigafactory Texas) [FACT] |
| **Training cycle cost** | ~70,000 GPU-hours per cycle [FACT] |
| **Training data volume** | >1.5 PB [FACT] |
| **Fleet data collection** | ~4 million vehicles in Shadow Mode [FACT] |
| **Data throughput** | 400,000 video clips/second processed [FACT] |
| **Dojo status** | D1 shut down Aug 2025 [FACT]; restarted Jan 2026 as Dojo 3/Space using AI5 silicon [FACT] |

### 3.3 Vision-Only Decision and Its Consequences

Tesla removed radar in May 2021 and ultrasonic sensors in October 2022 [FACT]. This makes Tesla the only major ADAS provider relying exclusively on cameras for environmental perception.

| Sensor | HW3 | HW4 | Implication |
|---|---|---|---|
| Cameras | 8x 1.2MP | 8x 5MP | Primary (and only) perception input |
| Radar | Removed May 2021 | Phoenix HD radar present in some S/X but **not enabled for FSD** [FACT] | No radar fallback in rain, fog, snow, direct sun |
| Ultrasonic | Present | Removed Oct 2022 | No close-range object detection for parking/low-speed |
| LiDAR | Never offered | Never offered | No depth verification layer |

**Buyer implication:** In degraded visibility conditions (heavy rain, fog, low sun angle, snow), Tesla FSD has no sensor fallback [INFERENCE]. Every competitor offering L2+ or higher uses at least camera + radar fusion. The Phoenix HD radar exists in some HW4 Model S/X vehicles but Tesla has not enabled it in software for FSD [FACT], which is either a deliberate architectural choice or a capability they have been unable to integrate [INFERENCE].

### 3.4 The HW3/HW4 Emulation Problem

| Period | HW4 Behavior | Impact |
|---|---|---|
| March 2023 — Dec 2024 (~21 months) | HW4 ran in HW3 emulation mode [FACT] | 5MP cameras downsampled; extra CPU cores unused |
| Dec 2024 onward (v13.2+) | Native HW4 resolution enabled [FACT] | Full sensor suite utilized for the first time |

This means HW4 buyers who purchased FSD between March 2023 and December 2024 paid for hardware capability they could not use for up to 21 months [FACT]. Tesla did not publicly disclose the emulation mode or provide timeline estimates for native HW4 support during this period [INFERENCE].

### What we know
- FSD v12+ is an end-to-end neural network trained on human driving imitation data, replacing handcoded rules [FACT].
- Tesla operates the largest known automotive AI training cluster (67K H100-equivalent GPUs) [FACT].
- Vision-only means zero sensor redundancy for adverse weather conditions [FACT].
- HW4 ran in degraded (emulation) mode for 21 months after first delivery [FACT].
- The original Dojo training chip failed commercially and was shut down, then restarted on different silicon [FACT].

### What we don't know
- How FSD v12+ performs in a statistically rigorous comparison to the prior rules-based system (Tesla has not published controlled studies).
- What the actual failure rate is per mile in specific conditions (rain, construction zones, unmarked roads). Tesla does not publish disengagement reports.
- Whether the Cortex cluster's 67K GPUs are fully utilized or partially allocated to other Tesla AI projects (Optimus, etc.).
- Why the Phoenix HD radar in HW4 S/X remains software-disabled — is it a principled architecture decision or an integration failure?

### Best skeptic argument
Tesla's "end-to-end neural network" is a black box trained on imitation learning. Unlike Waymo, which publishes safety reports and operates under regulatory oversight with disengagement data, Tesla provides no independent verification of FSD's statistical safety profile. The 48-network architecture is impressive on paper, but the vision-only approach means a single sensor modality failure (dirty cameras, sun glare, heavy rain) has no fallback. The 21-month HW4 emulation debacle shows Tesla will ship hardware it cannot fully utilize and charge full price for the privilege.

### What would change my mind
Tesla publishing a peer-reviewed safety report with per-mile disengagement and collision rates segmented by weather, road type, and time of day. Alternatively, NHTSA or an independent body conducting such a study with Tesla's cooperation.

---

## 4. Driver Monitoring & Human Factors

### 4.1 Monitoring System Components

| Component | Method | Role | Active Since |
|---|---|---|---|
| **Cabin camera** | Tracks eye gaze and head position [FACT] | Primary monitoring (since v12.4) [FACT] | May 2024 |
| **Steering wheel torque sensor** | Detects hands-on-wheel via resistance [FACT] | Fallback monitoring [FACT] | Original |

### 4.2 Alert Escalation Sequence

| Stage | Trigger | Response | Timing |
|---|---|---|---|
| 1. Visual alert | Inattention detected by cabin camera | Dashboard warning, chime | ~3 seconds after detection [FACT] |
| 2. Repeated warnings | Continued inattention | Larger visual alerts, audible warnings [FACT] | Seconds after Stage 1 |
| 3. Forced disengagement | Persistent non-compliance | FSD deactivates, driver must take control [FACT] | After repeated Stage 2 |
| 4. Strikeout (1 of 5) | Forced disengagement event | Logged to account [FACT] | Immediate |
| 5. Lockout | 5 strikeouts accumulated | FSD locked for 1 week [FACT] | Upon 5th strikeout |
| **Decay** | Time-based | 1 strikeout removed per 7 days [FACT] | Rolling |

### 4.3 Post-Recall Changes (Recall 23V-838)

Following the 2-million-vehicle recall, Tesla implemented via OTA [FACT]:

| Change | Description |
|---|---|
| Larger visual alerts | More prominent on-screen warnings [FACT] |
| Stricter intersection monitoring | Enhanced attention checks at intersections [FACT] |
| Simplified activation | Reduced complexity of FSD engagement [FACT] |

### 4.4 Torque Nag Intervals

| Monitoring Mode | Nag Interval |
|---|---|
| Cabin camera active (primary) | ~3 seconds if inattention detected [FACT] |
| Steering wheel torque (fallback, e.g., camera blocked) | ~30-60 seconds between nag prompts [FACT] |

**Buyer note:** The 30-60 second torque nag interval means that if the cabin camera is obscured (aftermarket tint, obstruction, failure), the system falls back to a monitoring method that allows up to a full minute of unmonitored driving between checks. This is significantly less safe than the camera-based system and well behind competitors like GM Super Cruise, which will not operate without functional eye tracking.

### What we know
- Cabin camera is the primary monitoring method since May 2024, with ~3-second detection [FACT].
- The strikeout/lockout system provides a progressive deterrent against misuse [FACT].
- Post-recall 23V-838 changes improved alert visibility and intersection monitoring [FACT].

### What we don't know
- How effective the cabin camera is at detecting inattention while the driver wears sunglasses (IR-based gaze tracking varies by sunglass lens type).
- The actual false-positive rate of the attention system (does it nag attentive drivers?).
- Whether Tesla logs and acts on patterns of near-miss events correlated with monitoring data.
- How the system handles rear-seat passengers or unusual seating positions.

### Best skeptic argument
Tesla's monitoring system was a late addition, bolted on under regulatory and legal pressure rather than designed in from the start. The fallback to 30-60 second torque nags is a known weakness that has been exploited by aftermarket "defeat devices" (steering wheel weights). Compared to GM Super Cruise's refusal-to-operate without eye tracking, Tesla's layered approach has a known degraded-monitoring path. The 5-strikeout system sounds strict but resets weekly, enabling chronic misusers to maintain access indefinitely.

### What would change my mind
Tesla implementing a hard requirement that cabin camera gaze tracking be functional for FSD engagement (no torque-only fallback), similar to GM's approach. Or data showing the current system's misuse rate is statistically negligible.

---

## 5. Competitive Comparison

### 5.1 L2/L2+ ADAS Feature Matrix

| Feature | Tesla FSD (Supervised) | GM Super Cruise | BMW Highway Assistant | Mercedes Drive Pilot |
|---|---|---|---|---|
| **SAE Level** | L2 (driver responsible) [FACT] | L2 hands-free [FACT] | L2 hands-free [FACT] | L3 certified in CA (but paused for 2026+ models) [FACT] |
| **Operational domain** | All roads (highways + surface streets) [FACT] | Highway only, 750K mapped miles [FACT] | Highway only, up to 85 mph [FACT] | Mapped highways only, <40 mph, daylight only [FACT] |
| **Hands-free?** | No — hands on wheel or strikeout [FACT] | Yes, on mapped highways [FACT] | Yes, on highways [FACT] | Yes, within ODD [FACT] |
| **Driver monitoring** | Cabin camera + torque (fallback) [FACT] | Eye-tracking (IR camera) [FACT] | Eye-tracking [FACT] | Eye-tracking [FACT] |
| **Surface street capability** | Yes [FACT] | No [FACT] | No [FACT] | No [FACT] |
| **Lane change** | Automatic [FACT] | Automatic (with eye-tracking confirmation) [FACT] | Eye-tracking confirmation required [FACT] | N/A (single-lane, low-speed) [FACT] |
| **Pricing model** | $8,000 purchase (ending Feb 14, 2026) or $99/mo [FACT] | OnStar subscription required [FACT] | One-time ~$1,700-$2,500 [FACT] | Included in equipped models [FACT] |
| **Fleet size** | ~4M vehicles with hardware [FACT] | ~500K vehicles [FACT] | N/A | Limited (S-Class/EQS only) |
| **Liability** | Driver always liable [FACT] | Driver always liable [FACT] | Driver always liable [FACT] | Manufacturer liable during L3 operation (but paused) [FACT] |
| **Industry rating** | IIHS: POOR [FACT] | MotorTrend 2025 Best Tech [FACT] | N/A | N/A |

### 5.2 Waymo as the L4 Benchmark

Waymo operates actual driverless robotaxis in Los Angeles. This is relevant because it provides a lived experience of what real autonomy looks like, which calibrates expectations for Tesla FSD.

| Attribute | Waymo (Los Angeles) | Tesla FSD |
|---|---|---|
| **Autonomy level** | L4 — no human driver [FACT] | L2 — human driver required at all times [FACT] |
| **Coverage area** | Santa Monica, DTLA, freeways (405/110/10/90 since Nov 2025) [FACT] | Anywhere the car can drive |
| **Notable gaps** | NOT available in Hermosa Beach [FACT]. Permitted for South Bay but no activation date [FACT] | N/A — driver handles gaps |
| **Pricing** | $5.37 base + $2.50/mi + $0.32/min [FACT] | $8,000 one-time or $99/mo (for FSD on your own car) |
| **Availability** | 24/7, no waitlist [FACT] | Whenever you drive your Tesla |
| **Scale** | 200K+ rides/week across all cities [FACT] | ~4M vehicles with FSD hardware |
| **Supervision required** | None — you are a passenger [FACT] | Constant — you are the safety driver [FACT] |

**Buyer note:** If you live in Waymo's coverage area, you can experience genuinely driverless transportation today for per-trip pricing. Tesla FSD, despite its name, requires your full attention at all times. These are fundamentally different products solving different problems. Waymo replaces your need to drive; Tesla FSD assists you while you drive.

### 5.3 Mercedes Drive Pilot: The L3 Cautionary Tale

Mercedes was the first to offer certified L3 driving in California [FACT]. However, it has **paused** Drive Pilot for 2026+ new models [FACT]. Key factors:

- Luminar, Mercedes' LiDAR supplier, entered bankruptcy [FACT]
- The ODD was extremely narrow: <40 mph, daylight only, mapped highways only [FACT]
- Replacement system: MB.Drive Assist Pro (L2++), coming 2026 [FACT]

**Buyer implication:** Even the most conservative, regulation-compliant L3 approach proved commercially unviable. This suggests the gap between L2 (Tesla) and true L3+ is enormous, and that Tesla's claims about imminent full autonomy should be weighed against Mercedes' retreat after actually achieving certification [INFERENCE].

### What we know
- Tesla FSD is the only system offering surface-street ADAS capability [FACT].
- Tesla FSD has the worst industry safety rating among major ADAS systems (IIHS: POOR) [FACT].
- GM Super Cruise is the only major L2 system that requires functional eye tracking to operate [FACT].
- Waymo is the only L4 robotaxi operating at scale in LA (200K+ rides/week all cities) [FACT].
- Mercedes retreated from L3, unable to sustain the technology and supply chain [FACT].

### What we don't know
- How Tesla FSD's actual collision and near-miss rate compares to GM Super Cruise or human driving on equivalent routes (no controlled study exists).
- Whether Waymo will expand to the South Bay (including Hermosa Beach) in 2026.
- Whether BMW or other OEMs will match Tesla's surface-street ADAS capability.
- How the FSD IIHS rating would change if Tesla submitted for re-evaluation after post-recall improvements.

### Best skeptic argument
Tesla FSD offers the broadest operational domain (all roads) but with the weakest safety validation (IIHS POOR, no disengagement data published, ongoing NHTSA investigations). GM Super Cruise works in a narrower domain but has better safety ratings and more robust driver monitoring. Waymo has proven that actual autonomy is possible, making Tesla's "Full Self-Driving" name increasingly misleading as consumers can directly compare the two experiences. You are paying $8,000 for a very capable L2 system that Tesla markets as if it were approaching L4.

### What would change my mind
Tesla achieving an IIHS rating above POOR, publishing verifiable per-mile safety data comparable to Waymo's safety reports, or demonstrating sustained unsupervised operation in a regulatory-approved pilot.

---

## 6. Regulatory & Safety Landscape

### 6.1 Active NHTSA Actions

| Investigation / Recall | Scope | Status | Key Details | Buyer Impact |
|---|---|---|---|---|
| **PE25012** (traffic violations) | 2.88M vehicles [FACT] | Open — most serious active investigation [FACT] | 80 violation reports, 8,313 potential violations under review [FACT]. **Deadline: Feb 23, 2026** [FACT] | Could result in mandatory recall, feature restrictions, or forced disengagement in certain scenarios |
| **23V-838** (2M recall) | ~2M vehicles [FACT] | Completed via OTA [FACT] | Resulted in larger alerts, stricter intersection monitoring, simplified activation [FACT] | Already applied to your vehicle if on recent software |
| **3 additional open investigations** | Various [FACT] | Open [FACT] | Details vary | Cumulative regulatory pressure |

**Five total open NHTSA investigations** as of Feb 2026 [FACT]. PE25012 is the most consequential, with a Feb 23, 2026 deadline and a scope covering nearly 3 million vehicles.

### 6.2 CA DMV Action

| Action | Date | Detail |
|---|---|---|
| Deceptive marketing ruling | Dec 2025 [FACT] | CA DMV found Tesla's FSD marketing deceptive [FACT] |
| Remedy deadline | 60 days from ruling [FACT] | Tesla must modify marketing or face 30-day sales suspension in California [FACT] |
| Potential consequence | ~Feb 2026 [INFERENCE] | If Tesla does not comply, California vehicle sales could be suspended for 30 days |

### 6.3 Federal Enforcement

| Action | Status | Detail |
|---|---|---|
| DOJ criminal investigation | Disclosed Oct 2023, believed ongoing [FACT] | Scope not fully public; likely related to Autopilot/FSD safety claims [INFERENCE] |
| Class action (N.D. Cal.) | Certified Aug 2025 [FACT] | Class certification is a significant procedural milestone; indicates court found common questions of fact [FACT] |

### 6.4 IIHS Safeguard Ratings

| System | Rating | Notes |
|---|---|---|
| Tesla Autopilot | **POOR** [FACT] | Lowest possible rating |
| Tesla FSD | **POOR** [FACT] | Lowest possible rating |
| Note | — | No retest conducted post-recall 23V-838 [FACT] |

### 6.5 Countervailing Regulatory Forces

| Factor | Direction | Assessment |
|---|---|---|
| Trump administration AV policy | Deregulatory [FACT] | Pushing deployment cap increases, national AV framework [FACT] |
| Potential federal preemption | Deregulatory [SPECULATION] | Could override state-level restrictions like CA DMV actions |
| Tesla behavioral pattern | Mixed signals [INFERENCE] | Complies with specific recalls via OTA while simultaneously pushing limits (e.g., reintroduced "Mad Max" mode the same week PE25012 opened) [FACT] |

### 6.6 Regulatory Risk Summary for Buyers

| Risk | Probability | Impact | Timeframe |
|---|---|---|---|
| PE25012 results in mandatory feature restriction | Medium [INFERENCE] | FSD capability reduced in certain scenarios | H1 2026 |
| CA DMV sales suspension | Low-Medium [INFERENCE] | Temporary sales halt; no impact on existing owners | Q1 2026 |
| DOJ investigation results in charges | Unknown [SPECULATION] | Unknown; could range from fines to operational restrictions | Unknown |
| Class action settlement/judgment | Medium [INFERENCE] | Potential refunds or credits for FSD purchasers | 2026-2028 |
| Federal deregulation overrides state actions | Medium [SPECULATION] | Reduces regulatory headwinds for Tesla | 2026-2027 |

### What we know
- Five NHTSA investigations are open, with PE25012 (traffic violations, 2.88M vehicles) being the most serious [FACT].
- The CA DMV has ruled Tesla's FSD marketing deceptive and given a 60-day remedy window [FACT].
- A DOJ criminal investigation was disclosed in Oct 2023 and is believed ongoing [FACT].
- A class action has been certified in N.D. Cal. [FACT].
- Both Autopilot and FSD received the lowest possible IIHS safeguard rating (POOR) [FACT].
- Tesla reintroduced "Mad Max" mode the same week PE25012 opened [FACT].

### What we don't know
- What specific remedies NHTSA will require if PE25012 finds violations.
- Whether the Trump administration's deregulatory stance will materially shield Tesla from NHTSA enforcement.
- The scope and current status of the DOJ criminal investigation.
- Whether Tesla will contest or comply with the CA DMV deceptive marketing ruling.
- Whether IIHS will conduct a post-recall retest of FSD.

### Best skeptic argument
Tesla faces an unprecedented convergence of regulatory actions: five open NHTSA investigations, a state-level deceptive marketing finding, a federal criminal investigation, and a certified class action — all simultaneously. The company's pattern of complying narrowly with specific recalls while immediately pushing new boundaries (Mad Max mode) suggests a corporate culture that treats regulatory compliance as a speed bump, not a guardrail. Buyers purchasing FSD today are buying into a product whose capabilities could be restricted by any of these actions, with no refund mechanism guaranteed.

### What would change my mind
NHTSA closing PE25012 with no action, the DOJ investigation concluding without charges, or Tesla voluntarily adopting a more conservative deployment strategy that reduces the regulatory attack surface.

---

## 7. Deprecation & Retrofit Risk

This section is critical for any buyer evaluating whether to purchase FSD today.

### 7.1 Historical Retrofit Record

| Transition | Retrofit Offered? | Cost | Physical Compatibility | Timeline to Complete | Completion Rate | Status |
|---|---|---|---|---|---|---|
| HW2.5 to HW3 | Yes [FACT] | Free for FSD owners; $1,000 for others [FACT] | Drop-in (same board size) [FACT] | 2+ years globally [FACT] | Unknown | Complete |
| HW3 to HW4 | Promised [FACT] | Musk said free for FSD owners (Q4 2024) [FACT] | **Not possible** — completely different form factor [FACT] | N/A | 0% | **Zero retrofits performed as of Feb 2026** [FACT] |
| HW4 to AI5 | No [FACT] | N/A | **Not possible** — different cooling and power requirements [FACT] | N/A | N/A | Explicitly ruled out (Q2 2025 earnings) [FACT] |

### 7.2 The HW3-to-HW4 Broken Promise

This deserves special attention:

| Date | Statement | Source |
|---|---|---|
| Jan 2023 | Musk says "no retrofit" from HW3 to HW4 [FACT] | Public statement |
| Q4 2024 | Musk reverses, promises free HW4 upgrade for FSD owners [FACT] | Public statement |
| Feb 2026 | **Zero retrofits have begun** [FACT] | Community tracking, no Tesla announcements |

**Buyer implication:** If you own an HW3 vehicle with FSD, your software is capped at v12.6.x [FACT] and no hardware upgrade has materialized despite a promise over a year ago. The physical incompatibility (different form factor) makes this retrofit logistically difficult and expensive for Tesla even if they intend to follow through [INFERENCE].

It is possible Tesla is waiting for an AI5-based retrofit solution rather than upgrading HW3 vehicles to soon-to-be-superseded HW4, but this is unconfirmed [SPECULATION].

### 7.3 What This Means for Today's Buyer

| If you buy today... | Your hardware is... | Upgrade path to next gen | FSD software trajectory |
|---|---|---|---|
| Any new Tesla (2026) | HW4 / AI4 [FACT] | **None.** AI5 retrofit explicitly ruled out [FACT] | Will receive software updates as long as Tesla supports AI4 |
| Used Tesla (HW3) | HW3 / AI3 [FACT] | **None delivered.** Promised but 0 completed [FACT] | Capped at v12.6.x [FACT] |
| Used Tesla (HW2.5 or older) | HW2.5 or older | Obsolete | No FSD capability |
| Wait for AI5 vehicles | AI5 (H2 2026 limited, mid-2027 volume) [INFERENCE] | Current-gen at time of purchase | Latest software |

### 7.4 FSD Software Ceiling by Hardware

| Hardware | Max FSD Version | Key Limitations |
|---|---|---|
| HW3 / AI3 | v12.6.x (frozen) [FACT] | No further features. 1.2MP cameras limit perception distance. 144 TOPS limits model complexity |
| HW4 / AI4 | Current and future (unknown ceiling) | 5MP cameras, 300+ TOPS. Unknown when Tesla will announce end-of-support |
| AI5 | Future | Not yet in any vehicle [FACT] |

### What we know
- HW2.5-to-HW3 was a successful drop-in retrofit [FACT].
- HW3-to-HW4 retrofit was promised but zero have been performed in 14+ months [FACT].
- HW4-to-AI5 retrofit is explicitly impossible [FACT].
- HW3 vehicles are permanently capped at FSD v12.6.x [FACT].
- Every new Tesla sold today ships with HW4 [FACT].

### What we don't know
- Whether Tesla will ever fulfill the HW3-to-HW4 upgrade promise.
- How long Tesla will continue to support and improve FSD on HW4 before focusing exclusively on AI5.
- Whether AI4's ~300+ TOPS is sufficient for the level of autonomy Tesla is targeting, or whether meaningful features will be gated behind AI5.
- What happens to FSD licenses on HW3 vehicles — will Tesla offer trade-in credits, refunds, or simply let the capability stagnate?

### Best skeptic argument
Tesla has a documented pattern of promising upgrades it does not deliver. The HW3-to-HW4 retrofit was promised over a year ago with zero units completed. The HW4-to-AI5 retrofit is impossible. This means every Tesla sold today has a hardware ceiling with no upgrade path. Buyers paying $8,000 for FSD are making a bet that HW4 will be sufficient for the useful life of their vehicle — a bet Tesla has given no concrete assurance on. Meanwhile, HW3 FSD owners who paid up to $15,000 are stuck on frozen software with a broken upgrade promise.

### What would change my mind
Tesla beginning actual HW3-to-HW4 retrofits at scale (not "coming soon" — actual installations with VIN tracking). Or Tesla providing a clear, time-bound commitment on HW4's software support horizon.

---

## 8. FSD Pricing & Ownership Economics

### 8.1 Current Pricing (as of Feb 2026)

| Option | Price | Notes |
|---|---|---|
| **One-time purchase** | $8,000 [FACT] | **Being eliminated after Feb 14, 2026** [FACT] |
| **Monthly subscription** | $99/month [FACT] | Cancel anytime |
| **Subscription (EAP owners)** | $49/month [FACT] | For owners who previously purchased Enhanced Autopilot |

### 8.2 Critical Ownership Terms

| Term | Detail | Buyer Impact |
|---|---|---|
| **Tied to VIN** | FSD purchase is tied to the vehicle, not the owner [FACT] | If you sell your car, the buyer gets FSD. You do not carry it to a new Tesla |
| **Trade-in stripping** | Trading in to Tesla may result in FSD being stripped from the vehicle [FACT] | Your $8,000 investment may vanish on trade-in |
| **Transfer windows** | Transfer to a new Tesla only possible during limited periodic windows [FACT] | You cannot transfer FSD at will; Tesla controls the timing |
| **Autosteer removed from base** | New vehicles no longer include Autosteer in standard Autopilot [FACT] | Basic highway lane-keeping now requires FSD subscription |

### 8.3 Purchase vs. Subscription Break-Even

| Scenario | Purchase ($8,000) | Subscription ($99/mo) | Break-even |
|---|---|---|---|
| Keep vehicle with FSD active full-time | $8,000 once | $1,188/year | ~6.7 years |
| Use FSD 6 months/year (seasonal) | $8,000 once | $594/year | ~13.5 years |
| Sell vehicle after 3 years | $8,000 (may lose on trade-in) | $3,564 total | Subscription wins |
| Keep vehicle 8+ years | $8,000 once | $9,504+ total | Purchase wins (if FSD not stripped and hardware not deprecated) |

### 8.4 The Autosteer Removal Trap

Tesla has removed Autosteer from standard Autopilot on new vehicles [FACT]. This means:

- **Before:** Basic Autopilot included adaptive cruise + lane keeping (Autosteer) at no extra cost
- **Now:** Basic Autopilot is adaptive cruise only. Lane keeping requires FSD subscription ($99/mo) [FACT]

This effectively increases the minimum cost of highway ADAS from $0/month to $99/month for new Tesla buyers [INFERENCE]. This is a significant change that makes Tesla's baseline ADAS offering less competitive than most competitors, which include lane keeping standard.

### What we know
- The $8,000 purchase option is ending Feb 14, 2026 [FACT].
- FSD is tied to VIN and may be stripped on trade-in [FACT].
- Transfers to new Teslas are only allowed during limited windows Tesla controls [FACT].
- Autosteer has been removed from standard Autopilot on new vehicles [FACT].

### What we don't know
- What will replace the $8,000 purchase option after Feb 14, 2026 (higher price? subscription-only?).
- Whether Tesla will ever make FSD transferable between vehicles as a standard policy.
- How trade-in FSD stripping is determined (is it systematic or inconsistent?).
- Whether the Autosteer removal will face regulatory scrutiny as a degradation of standard safety features.

### Best skeptic argument
Tesla's FSD pricing structure is designed to maximize revenue extraction while minimizing buyer flexibility. The VIN-lock means your $8,000 depreciates with the car. Trade-in stripping means Tesla can resell the same software twice. Transfer windows are controlled by Tesla, not the buyer. And now removing Autosteer from base Autopilot forces buyers into a $99/month subscription for features that were previously free and are included standard by most competitors. The purchase option ending Feb 14 creates artificial urgency. This is not buyer-friendly pricing; it is rent-seeking behavior enabled by a captive ecosystem.

### What would change my mind
Tesla making FSD permanently transferable between vehicles owned by the same person, eliminating trade-in stripping, or restoring Autosteer to standard Autopilot.

---

## 9. Buyer Decision Framework

### 9.1 Should You Buy/Subscribe to FSD Today?

| Buyer Profile | Recommendation | Reasoning |
|---|---|---|
| **New Tesla buyer who drives highways daily** | Subscribe monthly ($99/mo), do not purchase | Purchase option ends soon with no clarity on future terms. VIN-lock and trade-in stripping make purchase risky. Subscription preserves flexibility |
| **New Tesla buyer, mostly city driving** | Subscribe to evaluate, then decide | FSD's surface-street capability is unique but inconsistent. A month of real-world testing ($99) is far cheaper than a regretful $8,000 purchase |
| **Existing HW3 owner with FSD** | Do not spend further money | Your FSD is capped at v12.6.x. The promised HW4 upgrade has not materialized. Wait for concrete retrofit action, not promises |
| **Existing HW4 owner without FSD** | Subscribe monthly if interested | HW4 runs current FSD well since v13.2. But no upgrade path to AI5 exists, so avoid the $8,000 purchase lock-in |
| **Buyer considering waiting for AI5** | Wait if you can | AI5 vehicles are the only way to get next-gen hardware. But limited availability H2 2026 and volume mid-2027 means a long wait [INFERENCE] |
| **Buyer who wants true autonomy** | Use Waymo where available | Waymo is L4 with no supervision required, operating 24/7 in parts of LA. Tesla FSD is L2 requiring constant supervision. They are not comparable products |

### 9.2 Key Risk Matrix for FSD Purchase Decision

| Risk | Likelihood | Severity | Mitigation |
|---|---|---|---|
| HW4 deprecated before vehicle end-of-life | Medium [INFERENCE] | High — FSD stops improving | Subscribe monthly; do not purchase |
| Regulatory action restricts FSD features | Medium [INFERENCE] | Medium — temporary or permanent capability reduction | No mitigation available to buyer |
| FSD price increases after Feb 14, 2026 | High [INFERENCE] | Low — subscription still available | Lock in purchase before deadline only if you plan 7+ year ownership |
| FSD stripped on trade-in | High [FACT-based pattern] | High — total loss of $8,000 | Subscribe monthly; never purchase |
| AI5 delivers meaningful capability leap | Medium [SPECULATION] | High — HW4 buyers locked out | Wait for AI5 vehicles or subscribe monthly on HW4 |

### 9.3 The Bottom Line

**For most buyers, the monthly FSD subscription ($99/mo) is the rational choice.** It provides:

- Full FSD capability without $8,000 upfront commitment
- Flexibility to cancel if regulatory actions degrade the product
- No trade-in stripping risk
- No hardware deprecation lock-in
- Ability to evaluate month-to-month as the product evolves

**The $8,000 purchase makes sense only if:**

- You plan to keep this specific vehicle for 7+ years [INFERENCE]
- You will not trade in to Tesla (avoiding strip risk)
- You accept that HW4 has no upgrade path to AI5 [FACT]
- You are comfortable with the regulatory uncertainty [FACT]

**If you want hands-free, eyes-off driving today:** Tesla FSD does not offer this. GM Super Cruise offers hands-free L2 on highways. Waymo offers fully driverless L4 in select cities.

---

## Appendix A: Source Quality Notes

This dossier draws from the following source categories, listed in descending order of reliability:

| Source Type | Reliability | Examples Used |
|---|---|---|
| Regulatory filings (NHTSA, CA DMV) | High | Investigation numbers, recall details, deadlines |
| Tesla SEC filings and earnings calls | High (for factual statements) | Hardware specs, timeline claims, pricing |
| Independent teardowns | High | Board-level hardware comparisons |
| Tesla public statements (Musk, executives) | Medium — forward-looking claims have poor track record | AI5 timeline, retrofit promises, autonomy predictions |
| Industry analyst reports | Medium | TOPS estimates, production timelines |
| Community tracking (VIN databases, fleet data) | Medium | HW4 rollout timeline, emulation mode discovery |
| Competitor filings and press releases | Medium-High | Waymo pricing, Super Cruise specs, Mercedes status |

---

## Appendix B: Glossary

| Term | Definition |
|---|---|
| **TOPS** | Tera Operations Per Second — measure of AI inference compute throughput |
| **HBM3** | High Bandwidth Memory, 3rd generation — fast memory used for AI workloads |
| **EUV** | Extreme Ultraviolet lithography — advanced semiconductor manufacturing process |
| **ODD** | Operational Design Domain — the specific conditions under which an ADAS/AV system is designed to function |
| **SAE Level** | Society of Automotive Engineers autonomy classification (L0-L5) |
| **OTA** | Over-the-Air software update |
| **USS** | Ultrasonic Sensors |
| **ISP** | Image Signal Processor |
| **FSD** | Full Self-Driving (Tesla's branded L2 ADAS product) |
| **EAP** | Enhanced Autopilot (legacy Tesla ADAS tier) |
| **Shadow Mode** | Tesla's fleet data collection system where vehicles passively record driving scenarios |
| **VIN-lock** | FSD license tied to Vehicle Identification Number, not transferable to owner |

---

*End of dossier. Last updated 2026-02-08.*
