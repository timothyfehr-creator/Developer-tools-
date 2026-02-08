# Hermosa Beach Lived Driving Experience
## Route-Class Simulation for Tesla FSD — Current (HW4/v14) and Projected Early 2027

**Status:** COMPLETE
**Last updated:** 2026-02-08
**Claim tagging:** All non-trivial claims tagged [FACT], [INFERENCE], or [SPECULATION]
**Hardware assumed:** HW4 / AI4 (current production). AI5 is not expected in your vehicle by Q1 2027.
**Software assumed:** Current = FSD v14.2. Projected = v15/v16 era.

---

## 1. Your Driving Profile

| Attribute | Detail |
|---|---|
| Home | Hermosa Beach, CA |
| Local trips | 5–8 mi: Redondo, Manhattan Beach, Torrance. Surface streets + short freeway hops. Daily. |
| Medium trips | Hermosa ↔ Santa Monica (~15 mi), Hermosa ↔ DTLA (~22 mi). A few times/month. |
| Road trips | Palm Springs, Ojai, Central CA, San Diego. ~1×/quarter. |
| Priority | Techy feel + max practical automation + low annoyance. Will supervise. Wants workload reduction, not WTF moments. |

## 2. Scoring Rubric

| Score | Intervention Rate (per trip) | Annoyance | Feel |
|---|---|---|---|
| **5** (excellent) | 0–1 minor | Rare nags, no phantoms | Relaxing — you forget you're supervising |
| **4** (good) | 1–2 minor | Occasional nag, rare phantom | Comfortable — occasional glance-checks |
| **3** (acceptable) | 2–4 minor OR 1 significant | Noticeable nags | Alert but not stressed |
| **2** (mediocre) | 4+ minor OR 2+ significant | Frequent nags/phantoms | Vigilant — hands hovering |
| **1** (poor) | Frequent significant | Constant | Stressful — why bother? |

**Definitions:**
- *Minor intervention:* Steering nudge, gentle brake tap, verbal "come on." No safety risk.
- *Significant intervention:* Full takeover required to avoid unsafe outcome or major routing error.

---

## 3. Route Class Assessments

### Class A: Local Surface (Hermosa Errands, 5–8 mi)

**Typical route:** Home → PCH → Artesia Blvd → Torrance Target → return via Sepulveda

**Where you'd engage FSD:**
- Arterials (PCH, Sepulveda, Artesia, Hawthorne Blvd): Yes — these are FSD's strongest surface-street domain [INFERENCE]
- Residential streets: Engage but expect occasional awkwardness at stop signs and tight corners [INFERENCE]
- Parking lots: Disengage. FSD v14 has improved parking lot navigation but tight retail lots (Riviera Village, Del Amo Fashion Center) remain unreliable [INFERENCE]

**Where you'd proactively disengage:**
- Riviera Village / downtown Hermosa (narrow streets, parallel parking, pedestrians in roadway) [INFERENCE]
- School zones near Hermosa Valley School (unpredictable pedestrians, crossing guards) [SPECULATION]
- Del Amo Fashion Center parking structure (tight turns, low clearance, dim lighting) [INFERENCE]

**Intervention rate:**

| Scenario | Est. Interventions (5-mi trip) | Type | Reasoning |
|---|---|---|---|
| Current (v14, 2026) | 2–4 minor, 0–1 significant | Minor: hesitation at unprotected lefts, stop-sign timing. Significant: parking lot | [INFERENCE] v14 is dramatically improved on arterials but still hesitant on residential streets with ambiguous right-of-way |
| Projected S1 (v15/v16, 2027) | 1–3 minor, 0 significant | Minor: reduced hesitation | [INFERENCE] Improvement trajectory suggests 25–35% reduction in minor interventions |
| Projected S2 (optimistic) | 0–2 minor, 0 significant | — | [SPECULATION] |

**Critical intervention hotspots:**
- Unprotected left from PCH onto Pier Ave (heavy pedestrian traffic, bikes, no protected signal) [INFERENCE]
- Artesia Blvd / Hawthorne Blvd intersection (complex multi-lane, heavy truck traffic) [INFERENCE]
- Parking lot entries/exits at South Bay Galleria or Del Amo [INFERENCE]

**Annoyance factors:**
- Cabin camera nag if wearing sunglasses (improved in v12.5.4 but not perfect) [FACT]
- Overly cautious stop-sign behavior in residential areas (full 3-second stops when human drivers do a California roll) [INFERENCE]
- Speed limit issues: Hermosa residential streets have 25 mph limits; FSD may go exactly 25 when traffic flows at 30 [INFERENCE]

**Feel scores:**

| Scenario | Score | Notes |
|---|---|---|
| Current (v14) | **3/5** | Alert but not stressed. FSD handles arterials well but you'll take over for parking and tricky turns. |
| Projected S1 | **3.5/5** | Minor improvement. Still need to park yourself. Arterials smoother. |
| Projected S2 | **4/5** | Approaching comfortable if parking lot handling improves. |

**Operating tips:**
- Engage on arterials, disengage for parking lots and narrow residential streets
- Set to "Chill" speed profile if you want less aggressive acceleration on PCH [FACT — v12.6.3+ feature]
- Keep sunglasses that are compatible with IR gaze tracking (dark polarized lenses can trigger torque-nag fallback)

---

### Class B: Short Freeway Hop (5–10 mi)

**Typical route:** PCH → 405 N → Rosecrans Ave exit → destination in El Segundo

**Where you'd engage FSD:**
- Entire route. This is FSD's best domain [INFERENCE]
- 405 merge from PCH is the stress point [INFERENCE]

**Where you'd proactively disengage:**
- Rarely needed. Perhaps if construction is active on 405 near LAX [INFERENCE]

**Intervention rate:**

| Scenario | Est. Interventions | Type | Reasoning |
|---|---|---|---|
| Current (v14) | 0–1 minor, 0 significant | Minor: merge timing | [INFERENCE] Highway FSD is the strongest capability. v14 community data: ~0.97 critical DE per 10K miles |
| Projected S1 (2027) | 0 minor, 0 significant | — | [INFERENCE] Highway performance near-perfect in clear weather by 2027 |
| Projected S2 | 0 | — | — |

**Critical intervention hotspots:**
- 405 N merge from PCH (short merge lane, speed differential from 35→65 mph) [INFERENCE]
- LAX construction zone (if active — frequent lane closures near Century Blvd) [INFERENCE]
- Rosecrans off-ramp exit speed (FSD sometimes brakes late for tight exits) [INFERENCE]

**Annoyance factors:**
- Minimal. Highway FSD is the lowest-annoyance mode [INFERENCE]
- One nag possible if trip is <10 minutes and you glance at phone [FACT]

**Feel scores:**

| Scenario | Score | Notes |
|---|---|---|
| Current (v14) | **4.5/5** | Near-excellent. You mostly ride. Merge is the only watch point. |
| Projected S1 | **5/5** | Excellent. Near-zero intervention expected. |
| Projected S2 | **5/5** | — |

**Operating tips:** Engage FSD before the merge ramp so it has time to plan the lane change. Don't engage mid-merge.

---

### Class C: Hermosa → Santa Monica (~15–20 mi)

**Typical route:** PCH → 405 N (or stay on PCH) → exit Santa Monica Blvd → SM surface streets → destination

**Where you'd engage FSD:**
- 405 freeway segment: Yes, excellent domain [INFERENCE]
- PCH route alternative: Yes, but PCH through El Segundo/Playa del Rey has unprotected turns and cyclist hazards [INFERENCE]
- Santa Monica surface streets (Wilshire, Santa Monica Blvd, Ocean Ave): Engage with awareness — busy pedestrian areas, bike lanes, Uber/Lyft stops [INFERENCE]
- Parking: Disengage. SM parking structures are tight and FSD struggles [INFERENCE]

**Where you'd proactively disengage:**
- SM parking structures (especially 4th/Broadway structure, Santa Monica Place)
- Ocean Ave near Palisades Park (heavy pedestrian crossing, street performers, tour buses) [INFERENCE]
- If taking PCH: disengage at Temescal Canyon / Sunset Blvd merge area (complex geometry) [SPECULATION]

**Intervention rate:**

| Scenario | Est. Interventions (full trip) | Type | Reasoning |
|---|---|---|---|
| Current (v14) | 2–4 minor, 0–1 significant | Minor: SM surface street hesitation, speed oscillation in 405 crawl. Significant: rare — maybe a wrong lane choice approaching SM | [INFERENCE] |
| Projected S1 (2027) | 1–3 minor, 0 significant | Fewer hesitations, better navigation | [INFERENCE] |
| Projected S2 | 0–2 minor, 0 significant | — | [SPECULATION] |

**Critical intervention hotspots:**
- 405 N through Culver City (chronic stop-and-go, aggressive lane-cutters, FSD may brake hard for cutters) [INFERENCE]
- SM Blvd / Lincoln Blvd intersection (complex multi-lane, buses, bikes) [INFERENCE]
- Montana Ave / Ocean Ave (pedestrians crossing mid-block near restaurants) [INFERENCE]
- Parking (disengage entirely) [INFERENCE]

**Annoyance factors:**
- 405 congestion: FSD may oscillate between following close and leaving too much gap, inviting cut-ins [INFERENCE]
- Speed in SM residential zones: FSD may go strictly 25 in 25 zones when locals go 30–35 [INFERENCE]
- Routing: FSD may take suboptimal route into SM (e.g., Pico instead of Olympic) [INFERENCE]

**Feel scores:**

| Scenario | Score | Notes |
|---|---|---|
| Current (v14) | **3.5/5** | Highway segment is great. SM surface streets are hit-or-miss. Parking is manual. Overall: comfortable with occasional alert moments. |
| Projected S1 | **4/5** | Highway near-perfect. SM surface streets improved. Parking still manual. |
| Projected S2 | **4.5/5** | Close to "set and forget" except parking. |

**Operating tips:**
- 405 route is better for FSD than PCH (fewer conflict points, better lane markings)
- In SM, switch to manual 1–2 blocks before your parking destination
- If going to Main Street / Abbot Kinney area (Venice border), expect more cyclist interactions

---

### Class D: Hermosa → DTLA (~22–25 mi)

**Typical route:** 405 N → 110 N → DTLA exit (e.g., 6th St, 4th St) → downtown grid

**Where you'd engage FSD:**
- 405 segment: Yes [INFERENCE]
- 110 N: Engage but with elevated awareness — 110 is an old freeway with narrow lanes, sharp curves, no shoulders, and aggressive merges [INFERENCE]
- DTLA grid: Engage on major streets (Figueroa, Grand, Olympic). Expect more interventions than SM [INFERENCE]

**Where you'd proactively disengage:**
- 110 N construction zones (chronic near DTLA)
- DTLA one-way streets with confusing signage [INFERENCE]
- Uber/Lyft/delivery vehicle double-parking zones (Spring St, Broadway) [INFERENCE]
- Any parking structure in DTLA [INFERENCE]

**Intervention rate:**

| Scenario | Est. Interventions (full trip) | Type | Reasoning |
|---|---|---|---|
| Current (v14) | 3–6 minor, 0–1 significant | Minor: 110 curve hesitation, DTLA pedestrian stops, one-way confusion. Significant: possible wrong-way turn or missed exit on 110 | [INFERENCE] |
| Projected S1 (2027) | 2–4 minor, 0 significant | 110 handling improved, DTLA navigation better | [INFERENCE] |
| Projected S2 | 1–3 minor, 0 significant | — | [SPECULATION] |

**Critical intervention hotspots:**
- **110 N between 105 and DTLA** — narrow lanes, tight curves near Dodger Stadium exit, old infrastructure with minimal shoulders [INFERENCE]. This is the hardest freeway segment on any of your regular routes.
- **110 N merge from 405** — short merge ramp, high speed differential [INFERENCE]
- **DTLA grid at rush hour** — jaywalking pedestrians, cyclists, scooters, Uber stops, food delivery bikes [INFERENCE]
- **Figueroa / 7th St** — extremely busy intersection with pedestrians, transit, bikes [INFERENCE]

**Annoyance factors:**
- 110 N curves: FSD may slow unnecessarily or oscillate in lane position [INFERENCE]
- DTLA: frequent phantom braking or over-cautious stops for pedestrians who aren't crossing [INFERENCE]
- One-way streets: FSD occasionally attempts turns onto wrong-way streets in DTLA grid [INFERENCE — PE25012 investigation includes wrong-way turns]

**Feel scores:**

| Scenario | Score | Notes |
|---|---|---|
| Current (v14) | **2.5/5** | The 110 keeps you vigilant. DTLA is hands-hovering territory. Overall: you're doing real supervisory work. |
| Projected S1 | **3/5** | 110 handling better, DTLA still complex. You can relax on 405 but tense up on 110 and downtown. |
| Projected S2 | **3.5/5** | Approaching acceptable for routine DTLA trips. |

**Operating tips:**
- On 110 N, stay in the right 2 lanes — FSD handles straight sections better than the leftmost curve-hugging lanes [INFERENCE]
- Disengage 2–3 blocks before your DTLA destination, especially if parking involves a tight structure
- If going to Arts District or Little Tokyo, expect narrower streets and more pedestrian interactions
- Evening return via 110 S is easier (less congestion, fewer merges)

---

### Class E: Hermosa → Palm Springs (~120 mi)

**Typical route:** 405 N → 105 E → I-10 E → Palm Springs exits

**Where you'd engage FSD:**
- Entire freeway segment. This is FSD's strongest use case: long highway cruise [INFERENCE]
- Palm Springs surface streets at destination: engage with awareness [INFERENCE]

**Where you'd proactively disengage:**
- I-10 construction zones (frequent through Inland Empire and Cabazon area) [INFERENCE]
- Palm Springs resort streets if navigating into hotel/resort parking [INFERENCE]

**Intervention rate:**

| Scenario | Est. Interventions (120 mi) | Type | Reasoning |
|---|---|---|---|
| Current (v14) | 1–3 minor, 0 significant | Minor: construction zone speed, Cabazon wind-induced lane drift?, destination navigation | [INFERENCE] Community data: ~1-2 per 100 highway miles for minor interventions |
| Projected S1 (2027) | 0–2 minor, 0 significant | Even fewer | [INFERENCE] |
| Projected S2 | 0–1 minor, 0 significant | Near-zero | [SPECULATION] |

**Critical intervention hotspots:**
- **I-10 through Inland Empire** — construction zones are chronic (Ontario to Redlands). Lane closures, narrowed lanes, concrete barriers close to travel lanes [INFERENCE]
- **Cabazon wind corridor** — strong crosswinds can affect vehicle stability and FSD lane-keeping, especially if buffeted by trucks [INFERENCE]
- **Sun glare** — eastbound morning, westbound afternoon. Camera-only system has no radar fallback in direct sun [FACT]
- **Palm Springs city streets** — resort area with pedestrians, golf carts, unexpected obstacles [INFERENCE]

**Annoyance factors:**
- Long highway cruise = minimal nags (cabin camera is primary; torque nags only if camera fails) [FACT]
- Speed limit handling: I-10 speed limit varies (65–70) but traffic flows at 75–80. FSD speed offset setting matters [INFERENCE]
- Wind: occasional lane-position adjustment feels slightly less confident than calm conditions [INFERENCE]

**Feel scores:**

| Scenario | Score | Notes |
|---|---|---|
| Current (v14) | **4/5** | Genuinely relaxing for 80%+ of the trip. Highway cruise is FSD's bread and butter. Construction zones and arrival streets require attention. This is where FSD delivers the most workload reduction. |
| Projected S1 | **4.5/5** | Construction zone handling likely improved. Near-cruise-ship-level relaxation for most of the drive. |
| Projected S2 | **5/5** | Essentially autopilot (in the aviation sense) for the highway portion. |

**Operating tips:**
- Set speed offset to +5 or +10 mph to match traffic flow (stock FSD tracks speed limit too closely for I-10) [INFERENCE]
- Keep sunglasses IR-compatible for the desert sun
- On windy days, you may want to keep hands lightly on wheel even though FSD is handling it — psychologically reassuring
- Engage FSD before 405→105 interchange (complex merge, let FSD plan it)

---

### Class F: Hermosa → Ojai / Central CA (80–200 mi)

**Typical routes:** 405 → 101 N → Ojai (via 33 N), or 405 → 101 N → further north

**Where you'd engage FSD:**
- 101 N freeway: Yes, strong domain [INFERENCE]
- Highway 33 to Ojai: Mixed. Two-lane mountain road with curves, limited passing zones [INFERENCE]
- Route 1 (PCH) sections: Engage with awareness — coastal cliffs, narrow lanes, cyclists [INFERENCE]

**Where you'd proactively disengage:**
- Highway 33 tight curves above Ventura (limited visibility, no centerline in spots) [INFERENCE]
- Single-lane rural sections with no lane markings [INFERENCE]
- Ojai town center (narrow, pedestrian-heavy, diagonal parking) [INFERENCE]

**Intervention rate:**

| Scenario | Est. Interventions (100-mi trip) | Type | Reasoning |
|---|---|---|---|
| Current (v14) | 2–5 minor, 0–1 significant | Minor: curve speed on 33, rural intersection timing. Significant: possible lane departure on unmarked curves | [INFERENCE] Two-lane roads are FSD's weakest highway domain |
| Projected S1 (2027) | 1–4 minor, 0 significant | Modest improvement on two-lane roads | [INFERENCE] |
| Projected S2 | 1–3 minor, 0 significant | — | [SPECULATION] |

**Critical intervention hotspots:**
- **Highway 33 above Casitas Springs** — winding mountain road, oncoming traffic, no center barrier, limited markings [INFERENCE]
- **101 N through Ventura** — construction zones, exits to 33 [INFERENCE]
- **PCH sections** — cyclists, cliff-edge curves, tourist traffic [INFERENCE]
- **Rural intersections with no signals** — FSD struggles with T-intersections without clear stop signs [INFERENCE]

**Feel scores:**

| Scenario | Score | Notes |
|---|---|---|
| Current (v14) | **3/5** | 101 freeway segment is comfortable. Mountain roads require active supervision. You're a co-pilot on Highway 33, not a passenger. |
| Projected S1 | **3.5/5** | 101 segment near-perfect. Mountain roads slightly better. |
| Projected S2 | **3.5/5** | Two-lane roads are hardware-limited (camera FOV, no radar for blind curves). |

**Operating tips:**
- Use FSD on 101 freely. Disengage before Highway 33 gets twisty (above the lake)
- On PCH, engage in straight sections, disengage for tight cliff curves near Big Sur (if going further north)
- Set to "Chill" for mountain roads — reduces aggressive acceleration out of curves

---

### Class G: Hermosa → San Diego (~120 mi)

**Typical route:** 405 S → I-5 S → San Diego exits

**Where you'd engage FSD:**
- Entire I-5 corridor: Yes, excellent domain [INFERENCE]
- San Diego surface streets: Engage with awareness [INFERENCE]

**Where you'd proactively disengage:**
- San Clemente / Camp Pendleton construction (if active) [INFERENCE]
- Downtown SD parking [INFERENCE]

**Intervention rate:**

| Scenario | Est. Interventions (120 mi) | Type | Reasoning |
|---|---|---|---|
| Current (v14) | 1–2 minor, 0 significant | Minor: construction zones, SD arrival navigation | [INFERENCE] I-5 is wide, well-marked, predictable |
| Projected S1 (2027) | 0–1 minor, 0 significant | Near-zero | [INFERENCE] |
| Projected S2 | 0 | — | — |

**Critical intervention hotspots:**
- **I-5 through Camp Pendleton** — long monotonic stretch, but construction zones near Oceanside [INFERENCE]
- **I-5 / I-805 merge near Del Mar** — multi-lane merge in heavy traffic [INFERENCE]
- **Carlsbad / Encinitas curves** — I-5 has gentle curves that occasionally confuse lane-keeping in older FSD versions, mostly resolved in v14 [INFERENCE]
- **Downtown SD** — Gaslamp Quarter is pedestrian-heavy, narrow streets, rideshare chaos [INFERENCE]

**Feel scores:**

| Scenario | Score | Notes |
|---|---|---|
| Current (v14) | **4.5/5** | One of the best FSD road trips you can do. Wide highway, good markings, gentle curves. Arrival in SD requires attention but is manageable. |
| Projected S1 | **5/5** | Essentially stress-free except SD parking. |
| Projected S2 | **5/5** | — |

**Operating tips:**
- I-5 to SD is the ideal FSD road trip — enjoy it
- Set speed offset to match I-5 traffic flow (~70–75 mph)
- If destination is in Gaslamp Quarter, disengage at the freeway exit and navigate yourself

---

## 4. Personalized Scorecard

### Current System (HW4, FSD v14, Early 2026)

| Route Class | Feel Score | Interventions (per trip) | Annoyance | Would You Use FSD? |
|---|---|---|---|---|
| A: Local surface (5–8 mi) | **3/5** | 2–4 minor | Moderate (parking, stop signs) | Yes on arterials, no in parking lots |
| B: Short freeway hop | **4.5/5** | 0–1 minor | Low | Yes, always |
| C: → Santa Monica | **3.5/5** | 2–4 minor | Moderate (405 crawl, SM streets) | Yes on freeway, cautious in SM |
| D: → DTLA | **2.5/5** | 3–6 minor, 0–1 significant | High (110, DTLA grid) | Yes on 405, vigilant on 110/DTLA |
| E: → Palm Springs | **4/5** | 1–3 minor | Low | Yes, the ideal use case |
| F: → Ojai/Central CA | **3/5** | 2–5 minor | Moderate (mountain roads) | Yes on 101, partial on rural |
| G: → San Diego | **4.5/5** | 1–2 minor | Low | Yes, always |
| **Weighted average** | **3.6/5** | | | |

### Projected Early 2027 — Base Scenario (HW4, v15/v16)

| Route Class | Feel Score | Interventions | Annoyance | Delta from Current |
|---|---|---|---|---|
| A: Local surface | **3.5/5** | 1–3 minor | Moderate (parking still manual) | +0.5 |
| B: Short freeway hop | **5/5** | 0 | Low | +0.5 |
| C: → Santa Monica | **4/5** | 1–3 minor | Low–Moderate | +0.5 |
| D: → DTLA | **3/5** | 2–4 minor | Moderate | +0.5 |
| E: → Palm Springs | **4.5/5** | 0–2 minor | Low | +0.5 |
| F: → Ojai/Central CA | **3.5/5** | 1–4 minor | Moderate | +0.5 |
| G: → San Diego | **5/5** | 0–1 minor | Low | +0.5 |
| **Weighted average** | **4.1/5** | | | **+0.5** |

### What Improves Most by Early 2027

| Route Class | Current → Projected | Confidence | Key Driver |
|---|---|---|---|
| B: Short freeway | 4.5 → 5.0 | **High** | Highway is already near-perfect; incremental gains finish the job |
| G: → San Diego | 4.5 → 5.0 | **High** | Same as above — long highway cruise |
| E: → Palm Springs | 4.0 → 4.5 | **High** | Construction zone handling improves modestly |
| C: → Santa Monica | 3.5 → 4.0 | **Medium** | 405 handling smoother; SM streets slowly improve |
| D: → DTLA | 2.5 → 3.0 | **Medium** | 110 and DTLA are hard problems; improvement is real but limited |
| A: Local surface | 3.0 → 3.5 | **Medium** | Arterials improve; parking lots remain manual |
| F: → Ojai | 3.0 → 3.5 | **Low** | Two-lane mountain roads are hardware-limited |

---

## 5. Narrated Drives

### Drive A: Rush-Hour Hermosa → Santa Monica (Tuesday, 5:30 PM)

#### Version 1: Current System (HW4, FSD v14, Early 2026)

**5:30 PM — Departure from Hermosa Beach**
You pull out of your driveway on a residential street. Engage FSD. It handles the 25 mph residential zone fine but does a full 3-second stop at every stop sign — you'd normally do a California roll. Mildly annoying but correct behavior [INFERENCE].

**5:33 PM — PCH northbound**
FSD merges onto PCH smoothly. Traffic is moderate. It holds speed at 40 mph in the 40 zone. A cyclist appears in the bike lane — FSD gives them a wide berth, drifting slightly left. Good behavior. No intervention needed [INFERENCE].

**5:37 PM — PCH → 405 N on-ramp**
The merge onto 405 N from PCH is tight. FSD accelerates from 35 to 60 mph and slots into the right lane. Smooth. This is where FSD earns its keep [INFERENCE].

**5:40 PM — 405 N through Culver City**
Stop-and-go traffic. FSD handles it well — smooth acceleration and braking. However, an aggressive BMW cuts in with about 2 car-lengths of space. FSD brakes harder than you would. **Minor intervention: you override the brake with gas pedal** to maintain flow and avoid rear-end risk from the truck behind you [INFERENCE]. This is the classic "FSD is too polite in LA traffic" moment.

**5:48 PM — 405 N approaching SM exits**
Traffic loosens slightly. FSD holds the #2 lane at 55 mph. It signals and moves right for the Wilshire exit. Clean execution [INFERENCE].

**5:52 PM — Wilshire Blvd in Santa Monica**
FSD handles the wide boulevard well. It navigates the Wilshire / 26th St light correctly. **Minor intervention: at Wilshire / 14th, FSD hesitates on a right turn** when a pedestrian is on the far sidewalk, not crossing. You lightly steer through the turn [INFERENCE].

**5:56 PM — Ocean Ave**
FSD slows to 25 mph on Ocean Ave. Pedestrians are everywhere near Palisades Park. FSD is cautious — maybe too cautious, stopping for a jaywalker who has already passed. **Minor intervention: you tap the accelerator** [INFERENCE].

**5:58 PM — Parking**
You disengage FSD and park yourself in a garage on 2nd Street. FSD parking in these tight structures is not reliable [INFERENCE].

**Trip summary:**

| Metric | Value |
|---|---|
| Total distance | ~16 mi |
| Total time | ~28 min |
| FSD engaged | ~85% of trip |
| Interventions (minor) | 3 |
| Interventions (significant) | 0 |
| Nags | 1 (glanced at phone in 405 traffic) |
| Phantom events | 0 |
| Overall feel | **3.5/5** |
| "WTF moments" | 0 |

**Verdict:** Solid. The 405 segment is relaxing. SM surface streets require attention but aren't stressful. The main value is workload reduction in stop-and-go — you arrive noticeably less fatigued than manual driving [INFERENCE].

---

#### Version 2: Projected Early 2027 (Base Scenario, HW4, v15/v16)

**Key differences from 2026:**

**5:40 PM — 405 N through Culver City**
Same stop-and-go, but FSD v15/v16 handles cut-ins more smoothly. **The aggressive BMW cuts in — FSD brakes slightly but proportionally.** No intervention needed. Gap management is better [INFERENCE — based on continued improvement trajectory in v13→v14].

**5:52 PM — Wilshire Blvd**
FSD no longer hesitates on the right turn with a distant pedestrian. Improved pedestrian intent prediction [INFERENCE].

**5:56 PM — Ocean Ave**
FSD still cautious with jaywalkers but doesn't full-stop for a pedestrian who has already passed. One less minor intervention [INFERENCE].

**Trip summary — projected 2027:**

| Metric | 2026 | 2027 (base) | Delta |
|---|---|---|---|
| Interventions (minor) | 3 | 1 | -2 |
| Interventions (significant) | 0 | 0 | — |
| Nags | 1 | 1 | — |
| Overall feel | 3.5/5 | **4/5** | +0.5 |
| "WTF moments" | 0 | 0 | — |

**Verdict:** Noticeably better. The trip feels more like "the car drives, you supervise" rather than "you drive with AI assistance." The 405 segment is approaching hands-off trust. SM streets are smoother. You still park yourself [INFERENCE].

---

### Drive B: Weekend Hermosa → Palm Springs (Saturday, 8:00 AM)

#### Version 1: Current System (HW4, FSD v14, Early 2026)

**8:00 AM — Departure**
Engage FSD on residential streets. Full stops at every sign. Fine, it's Saturday, no rush [INFERENCE].

**8:03 AM — PCH → 405 N**
Short hop to 405 N on-ramp. Light Saturday traffic. FSD merges cleanly [INFERENCE].

**8:06 AM — 405 N → 105 E interchange**
Multi-lane interchange. FSD navigates it smoothly — signals, lane changes, merges. This is textbook FSD territory [INFERENCE].

**8:10 AM — 105 E → I-10 E**
Another interchange. FSD handles it. You're settling in. Check mirrors, relax hands on lap (cabin camera is watching, not the wheel) [INFERENCE].

**8:15 AM — I-10 E through Inland Empire**
Open highway. 70 mph. FSD is in cruise mode. This is the best FSD experience available — long, straight, well-marked highway. You watch the desert landscape. Interventions: zero [INFERENCE].

**8:45 AM — I-10 construction zone near Ontario**
Lane narrows, concrete barriers, reduced speed to 55. **FSD handles it but drifts slightly right toward the barrier** — you instinctively nudge the wheel left. **Minor intervention.** FSD recovers and tracks center [INFERENCE].

**9:15 AM — Cabazon area**
Wind picks up through the San Gorgonio Pass. FSD adjusts steering slightly for crosswind. No intervention needed, but you notice the car working harder to stay centered. Slightly unsettling in strong gusts [INFERENCE].

**9:25 AM — I-10 E approaching Palm Springs exits**
FSD signals for the exit. Speed drops smoothly from 70 to 35. Clean execution [INFERENCE].

**9:30 AM — Palm Springs surface streets**
FSD navigates the resort-area streets. Speed is 35–40 mph. A golf cart crosses from a resort entrance — **FSD stops smoothly.** No intervention. Impressive [INFERENCE].

**9:35 AM — Resort/hotel arrival**
You disengage FSD as you enter the resort driveway. Park yourself [INFERENCE].

**Trip summary:**

| Metric | Value |
|---|---|
| Total distance | ~120 mi |
| Total time | ~1 hr 35 min |
| FSD engaged | ~95% of trip |
| Interventions (minor) | 1 (construction zone drift) |
| Interventions (significant) | 0 |
| Nags | 0 |
| Phantom events | 0 |
| Overall feel | **4/5** |
| "WTF moments" | 0 |

**Verdict:** This is FSD at its best. You arrive at Palm Springs noticeably fresher than if you'd driven manually for 90+ minutes. The construction zone was the only moment requiring attention. The wind was noticeable but handled. This trip alone makes FSD worth the $99/month subscription for you [INFERENCE].

---

#### Version 2: Projected Early 2027 (Base Scenario)

**Key differences:**

**8:45 AM — Construction zone**
FSD v15/v16 handles the narrow lane better — improved construction zone detection from training on more fleet-collected construction zone data [INFERENCE]. **No intervention needed.** The slight right drift is gone.

**9:15 AM — Cabazon wind**
Same crosswind performance — this is physics-limited (wind force vs. vehicle mass), not software-limited [INFERENCE]. Feels the same as 2026.

**Trip summary — projected 2027:**

| Metric | 2026 | 2027 (base) | Delta |
|---|---|---|---|
| Interventions (minor) | 1 | 0 | -1 |
| Interventions (significant) | 0 | 0 | — |
| Overall feel | 4/5 | **4.5/5** | +0.5 |
| "WTF moments" | 0 | 0 | — |

**Verdict:** Near-perfect road trip experience. FSD handles the entire drive door-to-destination-driveway with zero interventions. You arrive genuinely rested. The improvement from 2026 to 2027 is real but incremental — 2026 was already excellent for this route [INFERENCE].

---

## 6. Comparative Context

### Waymo for Your Santa Monica Trip

| Dimension | Waymo | Tesla FSD (current) | Tesla FSD (projected 2027) |
|---|---|---|---|
| Available for this route? | **Partial.** Serves SM and freeways [FACT]. Does NOT pick up in Hermosa Beach [FACT]. You'd need to get yourself to a Waymo coverage area first. | Yes — your car, your route | Yes |
| Approximate cost | ~$45–55 one-way [INFERENCE based on distance/pricing] | $99/mo subscription (unlimited trips) | $99/mo+ |
| Supervision required? | **None.** You're a passenger. Read, work, nap. [FACT] | **Yes.** Constant supervision required. [FACT] | Still yes. L2 supervision required. |
| Door-to-door? | **No.** Can't pick up in Hermosa. | **Yes.** | **Yes.** |
| Experience quality | Premium — but you're in someone else's car, someone else's schedule [INFERENCE] | Your car, your schedule, your music, your stuff. But you're driving. | Same. |
| Practical for this persona? | **No for daily use** (coverage gap). Useful for occasional SM/DTLA trips if you're already in coverage area. | **Yes** — primary use case | **Yes** |

**Bottom line:** Waymo is irrelevant for your daily Hermosa Beach life until it covers the South Bay. For occasional SM/DTLA trips where you're already in the area, it's a genuine alternative — but you'd still need to drive or rideshare to get to coverage. It's not a substitute for car ownership; it's a supplement [INFERENCE].

### Super Cruise for Your Palm Springs Trip

| Dimension | GM Super Cruise | Tesla FSD (current) | Tesla FSD (projected 2027) |
|---|---|---|---|
| Works on I-10? | **Yes.** I-10 is fully mapped. [FACT] | Yes | Yes |
| Hands-free? | **Yes.** No touch required while engaged. [FACT] | **No.** Hands on wheel or strikeout. [FACT] | Still no. |
| Eye-tracking monitoring? | **Yes.** IR camera. Strict — looks away and it disengages. [FACT] | Cabin camera (less strict fallback to torque). [FACT] | Same. |
| Surface streets at destination? | **No.** Highway only. [FACT] Disengages at exit ramp. | **Yes.** Full route including PS streets. [FACT] | Yes. |
| Overall highway feel | Truly hands-free. Slightly more relaxing than Tesla on highway. [INFERENCE] | Hands on wheel required. Effective but not hands-free. | Same. |
| Construction zone handling | Disengages. You take over. [FACT] | Attempts to handle — sometimes poorly (drift). [INFERENCE] | Improved but still imperfect. |
| Vehicle options | Equinox EV (~$35K+), Blazer EV, Lyriq, Celestiq [FACT] | Any Tesla with HW4 [FACT] | Same. |

**Bottom line:** If your primary FSD use case were highway-only road trips, Super Cruise would be competitive — it's hands-free, well-monitored, and works on your I-10/I-5 routes. But it does nothing on surface streets, which is where you spend most of your driving time. Tesla FSD is the only system that works on your entire driving domain [INFERENCE].

---

## 7. Buyer Strategy

### Decision Matrix

| Strategy | Best If... | Risk | Key Signal to Watch |
|---|---|---|---|
| **Buy Tesla now, subscribe FSD ($99/mo)** | You want a Tesla anyway and want to evaluate FSD month-by-month | HW4 has no upgrade path to AI5. $99/mo adds up over years | Monthly FSD quality improvements via OTA |
| **Buy Tesla now, purchase FSD ($8,000 before Feb 14)** | You will keep this car 7+ years, will NOT trade in to Tesla, and accept HW4 ceiling | $8,000 locked into a depreciating VIN. No AI5 upgrade possible. FSD may be stripped on trade-in | Nothing — this is a sunk-cost bet |
| **Wait for AI5 vehicles** | You don't need a car until H2 2027+ and want the latest hardware | 12–18 month wait minimum. AI5 will run in emulation mode initially (see HW4 precedent) | FCC filings, teardowns, Model Y/3 VIN changes |
| **Buy competitor + Waymo supplement** | You want hands-free highway (Super Cruise) + true autonomy where available (Waymo) | Two systems, neither covers your full driving domain. Waymo doesn't serve Hermosa | Waymo South Bay expansion announcement |
| **Buy Tesla now, skip FSD, wait for Waymo** | You drive yourself on surface streets, use Waymo where available | Waymo may never cover Hermosa. You miss out on FSD workload reduction | Waymo coverage map updates |

### Recommended Strategy for Your Profile

**Buy a Tesla with HW4 now. Subscribe to FSD at $99/month. Do NOT purchase the $8,000 option.**

Reasoning:

1. **You want a techy car with maximum automation** — Tesla FSD on HW4 is the only system that covers your full driving domain (surface streets + highway + road trips) [FACT]
2. **FSD subscription preserves optionality** — you can cancel any month, no sunk cost, no trade-in stripping risk [FACT]
3. **HW4 software is your improvement path** — software updates (v15/v16) will meaningfully improve your experience by early 2027 without any hardware change [INFERENCE]
4. **AI5 is irrelevant to you until mid-2027 at earliest** — and even then, early AI5 vehicles will run in emulation mode [INFERENCE]
5. **The $8,000 purchase makes no sense** at your likely ownership horizon (3–5 years). At $99/mo, you'd pay $5,940 over 5 years with full flexibility vs. $8,000 locked into the VIN [FACT — arithmetic]
6. **Regulatory uncertainty is real** — if PE25012 results in feature restrictions, you want the ability to cancel your subscription rather than sitting on an $8,000 sunk cost [INFERENCE]

### Recommended Configuration

| Choice | Recommendation | Reasoning |
|---|---|---|
| Model | Model Y (or Model 3 if sedan preferred) | Highest utility for South Bay lifestyle; best FSD support |
| FSD | **Subscribe monthly ($99)** | Flexibility, no lock-in, evaluates month-by-month |
| Autopilot note | New vehicles no longer include Autosteer for free [FACT]. FSD subscription is now required for highway lane-keeping. This makes the $99/mo feel more necessary than before. |
| Color / trim | Personal preference — no impact on FSD |

### Watch List: Signals That Change This Recommendation

| Signal | Where to Monitor | Check Frequency | Triggers What Action |
|---|---|---|---|
| AI5 FCC filing | fcc.gov, NotATeslaApp | Monthly | Indicates AI5 vehicles within ~9 months. Start considering wait. |
| AI5 teardown appears | NotATeslaApp, Munro Live | Monthly | Confirms AI5 in production vehicles. Evaluate trade-in timing. |
| PE25012 enforcement action | NHTSA.gov | Feb 23, 2026 deadline, then ongoing | If feature restriction: evaluate if FSD still worth $99/mo |
| Waymo South Bay expansion | Waymo app, Waymo blog | Quarterly | If Hermosa covered: reduce FSD reliance for SM/DTLA trips |
| FSD subscription price increase | Tesla.com | Monthly | If >$149/mo: reassess value proposition |
| HW3→HW4 retrofits begin | NotATeslaApp, Tesla forums | Monthly | Signals Tesla is serious about HW upgrades (positive for ecosystem trust) |
| FSD v15/v16 release notes | NotATeslaApp, TeslaFi | Per release | Track improvement trajectory — are gains continuing or plateauing? |

### What we know
- HW4 + FSD subscription is the rational choice for a buyer in your position today [INFERENCE based on all evidence].
- AI5 is not relevant to your purchase decision for at least 18 months [INFERENCE].
- Software improvement is your primary value driver, and the trajectory is strong [FACT — community data].
- Regulatory uncertainty is the biggest wild card for your FSD experience [FACT].

### What we don't know
- How long Tesla will actively improve FSD on HW4 before shifting resources to AI5.
- Whether PE25012 will result in meaningful feature restrictions that degrade your experience.
- Whether Waymo will reach Hermosa Beach (would change the competitive calculus significantly).
- Whether FSD subscription pricing will increase (Musk has said prices will rise "as capabilities improve").

### Best skeptic argument
You're paying $99/month for a fancy L2 system that requires your constant attention and is one NHTSA recall away from losing features. Meanwhile, Waymo runs actual robotaxis 15 miles north of you. Tesla has promised full autonomy for 10 years and never delivered it. The subscription is a treadmill — you'll keep paying because each update is "almost there," but you'll never stop supervising. At $1,188/year, that's a meaningful recurring cost for what is essentially a driver-assistance system dressed up with the word "Self-Driving" in its name.

### What would change my mind
Tesla achieving genuine unsupervised operation in a regulatory-approved pilot program (not marketing claims — actual approval). Or FSD subscription including Autosteer as a base feature again, making the value proposition clearer. Or AI5 enabling a demonstrable capability that HW4 cannot match, with a confirmed upgrade or trade-in program.

---

## 8. Extended Horizon: Late-2027 AI5 Trip Simulations

> **Context:** You're considering waiting until mid-to-late 2027 to buy a Tesla equipped with AI5 hardware. These simulations project three specific trips on a late-2027 AI5 vehicle running FSD v16/v17.
>
> **The critical insight:** AI5 hardware will run in **AI4 emulation mode** at launch (see [forecast report §10](a15_stack_forecast_early_2027.md#10-extended-horizon-what-if-you-wait-until-mid-to-late-2027)). The driving experience is determined by software (v16/v17), not the underlying hardware. A late-2027 AI5 vehicle drives identically to a 2024 HW4 vehicle that has received 18 months of OTA software updates.
>
> **Hardware assumed:** AI5 (2,000–2,500 TOPS, HBM3) running in AI4 emulation mode
> **Software assumed:** FSD v16 or v17 — approximately 12–18 months beyond current v14.2

### Trip 1: Grocery Run on PCH (Hermosa → Vons/Ralphs, ~3 mi each way)

**Route:** Home → residential streets → PCH south → Torrance grocery store → return

#### Narrated Drive (Late 2027, AI5 + FSD v16/v17)

**Departure — residential streets**
You pull out and engage FSD. The residential zone behavior is refined — v16/v17 still does full stops at stop signs (legally required [FACT]) but the timing feels more natural. The acceleration from stops is smoother, less robotic than current v14 [INFERENCE]. On narrow residential streets with parked cars on both sides, FSD confidently threads the gap at ~20 mph. This was a hesitation point on v14; v16 handles it without slowing to a crawl [INFERENCE].

**PCH southbound**
FSD merges onto PCH smoothly. Speed holds at 40 mph in the 40 zone. A cyclist appears in the bike lane — FSD gives appropriate clearance without the exaggerated swerve that earlier versions sometimes produced [INFERENCE]. A pedestrian steps into the crosswalk at a mid-block crossing near Hermosa Ave — FSD yields cleanly and proceeds when clear [INFERENCE].

**Parking lot arrival**
This is where the biggest improvement shows. v16/v17 has better parking lot navigation [SPECULATION] — it can handle the Vons/Ralphs lot entry, navigate to an open spot in the main aisle, and pull in. It's not perfect: tight end-cap spots and spots flanked by large SUVs still cause hesitation [INFERENCE]. But the "disengage at the parking lot entrance" rule from 2026 is now "disengage if the lot is unusually tight."

**Return trip**
Essentially the same experience in reverse. Total round-trip interventions: 0–1 minor.

#### Scorecard

| Metric | Current (v14, 2026) | Late 2027 (AI5 + v16/v17) | Delta |
|---|---|---|---|
| Interventions (minor) | 2–4 | 0–2 | -2 |
| Interventions (significant) | 0–1 | 0 | -0.5 |
| Parking lot handling | Disengage at entrance | Engage through main aisles, disengage for tight spots | Meaningful improvement |
| Feel score | **3/5** | **4/5** | **+1.0** |
| Key improvement source | — | Software (v16/v17), not AI5 hardware [INFERENCE] | — |

**AI5 hardware contribution:** Negligible for this trip. The grocery run is low-speed, well-mapped surface streets. AI4-class compute handles this comfortably. The improvements you feel are entirely from software maturation [INFERENCE].

---

### Trip 2: Hermosa → Santa Monica (Rush Hour, ~16 mi)

**Route:** Home → PCH → 405 N → Wilshire exit → SM surface streets → destination

#### Narrated Drive (Late 2027, AI5 + FSD v16/v17)

**405 N through Culver City — rush hour stop-and-go**
The biggest improvement over 2026: gap management. v16/v17 handles aggressive cut-ins without the hard braking that v14 sometimes produced [INFERENCE]. When the inevitable BMW cuts in with 2 car-lengths of space, FSD eases off the accelerator proportionally rather than stomping the brake. The truck behind you doesn't get a scare. **Zero interventions on the 405 segment** [INFERENCE]. This is the single biggest quality-of-life improvement for your commute pattern.

**Santa Monica surface streets**
Wilshire Blvd: smooth. The hesitation at right turns with distant pedestrians (a v14 quirk) is gone [INFERENCE]. FSD navigates the Wilshire/Lincoln intersection confidently. On Ocean Ave, FSD handles the heavy pedestrian zone with appropriate caution — slowing but not stopping for pedestrians who are clearly on the sidewalk [INFERENCE]. The jaywalker false-stop problem from 2026 is largely resolved, though FSD still errs on the side of caution (correctly so, given PE25012 pressure) [INFERENCE].

**One remaining friction point:** Speed in SM residential zones. FSD still tracks the speed limit closely (25 in a 25) when local traffic flows at 30–35. This is likely a permanent behavior due to regulatory constraints [INFERENCE — PE25012 makes Tesla conservative about speed violations].

**Parking**
You still park yourself in the 2nd Street garage. Parking structures with tight multi-level spirals remain beyond FSD's reliable capability [INFERENCE]. This may be the last frontier — parking structures are adversarial environments (dim lighting, tight clearances, unpredictable pedestrians) that resist software improvement [SPECULATION].

#### Scorecard

| Metric | Current (v14, 2026) | Late 2027 (AI5 + v16/v17) | Delta |
|---|---|---|---|
| Interventions (minor) | 2–4 | 0–1 | -2.5 |
| Interventions (significant) | 0–1 | 0 | -0.5 |
| 405 stop-and-go handling | Good but occasional hard brake on cut-ins | Excellent — proportional responses | Major improvement |
| SM surface streets | Hit-or-miss | Mostly smooth, occasional speed-limit annoyance | Clear improvement |
| Parking | Manual | Manual | No change |
| Feel score | **3.5/5** | **4.5/5** | **+1.0** |
| Key improvement source | — | Software (v16/v17) — 405 gap management + pedestrian intent prediction [INFERENCE] | — |

**AI5 hardware contribution:** Minimal. The 405/SM route is well within AI4 compute capabilities. The improvements are from 18 months of neural network training on fleet data, not from 7× more TOPS [INFERENCE].

---

### Trip 3: Weekend Trip to Ojai (~80 mi, includes Highway 33)

**Route:** Home → 405 N → 101 N → Highway 33 N → Ojai → return

This trip has three distinct segments with very different FSD characteristics:

#### Segment 1: Freeway (405 → 101, ~55 mi) — Feel: 5/5

Identical to the current excellent freeway experience, just slightly more polished. v16/v17 on the 101 through Ventura is essentially autopilot-grade. You read, glance up occasionally, arrive at the 33 exit rested. **Zero interventions expected** [INFERENCE].

#### Segment 2: Highway 33 — The Mountain Section (~20 mi) — Feel: 2.5–3/5

**This is where the trip gets interesting — and where AI5 hardware hits its limits.**

Highway 33 above Casitas Springs is a two-lane mountain road with:
- Blind curves with no center barrier [FACT]
- Sections with faded or absent lane markings [INFERENCE]
- Oncoming traffic inches away on tight curves [FACT]
- Limited sight distance on switchbacks [FACT]
- Cyclists on shoulders (weekend recreation traffic) [FACT]
- Rock debris and road damage [INFERENCE]

**What v16/v17 improves over v14:**
- Better curve speed prediction — less jerky speed oscillation going into turns [INFERENCE]
- Improved handling of faded lane markings (uses road-edge detection when center line is absent) [INFERENCE]
- Slightly more confident on two-lane passing zones [INFERENCE]

**What v16/v17 CANNOT fix (hardware-limited):**
- **Camera physics on blind curves.** You cannot see around a mountain curve with a forward-facing camera, regardless of compute. The car cannot perceive oncoming traffic until it's visible. This is a fundamental sensor limitation, not a software limitation [FACT].
- **Night mountain driving.** 5MP cameras in low light on an unlit mountain road have fixed photon collection. AI5's 2,500 TOPS doesn't help if the camera can't see the road [FACT].
- **Steep grades with loose surface.** Traction is mechanical, not computational [FACT].

**What AI5 could theoretically help with (but doesn't in emulation mode):**
- Faster inference on degraded road marking inputs (currently compute-constrained on AI4 when multiple cameras have ambiguous input simultaneously) [SPECULATION]
- Larger occupancy network for predicting road geometry beyond visible range [SPECULATION]
- But in emulation mode, none of this is active [INFERENCE]

**Realistic Highway 33 experience:**
You engage FSD on the straighter sections below Casitas Springs. As the road tightens above the lake, you take over for the switchbacks — FSD can technically handle them but its lane-centering feels uncertain on unmarked curves, and you don't trust it with oncoming traffic inches away. You re-engage on the straight descent into Ojai. **1–3 minor interventions, 0–1 significant** on the mountain section [INFERENCE].

#### Segment 3: Ojai Town (~5 mi) — Feel: 3.5/5

Ojai's downtown is a charming small-town grid: low speed (25 mph), pedestrians, diagonal parking, cyclists, the Sunday farmers market crowd [FACT]. FSD handles the grid adequately — it's a simple road geometry. Diagonal parking spots are the main challenge; you'll park yourself at the destination [INFERENCE]. 0–1 minor interventions [INFERENCE].

#### Full Trip Scorecard

| Segment | Distance | Feel Score 2026 | Feel Score Late 2027 | Delta | Bottleneck |
|---|---|---|---|---|---|
| Freeway (405 → 101) | 55 mi | 4.5/5 | **5/5** | +0.5 | None — FSD's best domain |
| Highway 33 (mountain) | 20 mi | 2.5/5 | **2.5–3/5** | +0–0.5 | **Camera physics** — blind curves, no markings |
| Ojai town | 5 mi | 3/5 | **3.5/5** | +0.5 | Diagonal parking, pedestrians |
| **Trip overall** | **80 mi** | **3/5** (weighted) | **3.5/5** (weighted) | **+0.5** | Highway 33 drags down the average |

**AI5 hardware contribution:** Effectively zero for this trip. Highway 33 is limited by camera physics (you can't see around blind mountain curves), not compute. The freeway and Ojai town segments don't need more than AI4 compute. This is the trip where the "AI5 makes everything better" narrative breaks down — the bottleneck is sensors and road geometry, not processing power [INFERENCE].

**Honest assessment:** The Ojai trip in late 2027 feels ~0.5 points better than today, driven entirely by software improvements to curve handling and small-town navigation. Highway 33's mountain section remains the one part of your regular driving life where FSD provides minimal value and you're essentially driving manually. This won't change until Tesla adds additional sensing modalities (radar, lidar) or significantly longer-range cameras — none of which are in the AI5 hardware spec [INFERENCE].

---

### Summary: Late-2027 AI5 Vehicle Across All Three Trips

| Trip | Feel (2026) | Feel (Late 2027 AI5) | Delta | AI5 Hardware Impact |
|---|---|---|---|---|
| Grocery on PCH | 3/5 | **4/5** | +1.0 | Negligible |
| → Santa Monica (rush) | 3.5/5 | **4.5/5** | +1.0 | Negligible |
| → Ojai (weekend) | 3/5 | **3.5/5** | +0.5 | Zero |
| **Average** | **3.2/5** | **4.0/5** | **+0.8** | **Negligible — all gains from software** |

### The Bottom Line for the "Wait for AI5" Buyer

The late-2027 AI5 experience is **genuinely good** — a 4/5 average across your regular trips is comfortable, low-stress driving where FSD handles 85–95% of the work. But this improvement comes from **18 months of software maturation**, not from AI5 hardware. A buyer who purchased an HW4 vehicle in early 2026 and received the same OTA updates would have an essentially identical driving experience.

The AI5 hardware is an investment in 2029–2030, when native software unlocks:
- Full simultaneous 5MP × 8 camera processing
- Larger neural networks with better edge-case handling
- Potentially sub-100ms photon-to-control latency

If you plan to keep the car 5+ years, AI5 is the better long-term bet. If you plan to keep it 3–4 years, the hardware difference is irrelevant to your ownership experience.

---

*End of lived experience report. Last updated 2026-02-08.*
