# Aliante LED — Paper Edit (Cursor)

**Stage:** Paper edit — A/B test variant (Cursor)
**Purpose:** Match the approved copy and narrative beats to the strongest available footage. This is an editorial paper edit only — no typography, transitions, animation, color, music, or graphic design decisions.
**Owner:** Cursor
**A/B test note:** This is the Cursor variant of the paper edit. It does not overwrite any shared artifact. STATE.json is not modified during this test.

---

## Approved copy (locked — do not rewrite)

The following copy was approved by Jane with ChatGPT and is locked for this stage. Cursor is not authorized to rewrite, polish, shorten, improve, or substitute it.

```
Aliante Casino + Hotel
A multimedia transformation orchestrated by LUCI

106 feet of curved LED.
2,000 square feet of display.

The hard part is building at this scale.
LUCI makes running it the easy part.

Aliante's legacy system filled 15 racks.
With LUCI, everything now runs from 2.

[Optional, only if pacing and evidence support it:]
More than 20 legacy projectors came out, too.

A 150-foot LED ticker wraps the sportsbook bar.

And the sportsbook is only part of it.
Across Aliante:
266 displays. 89 zones. 7+ technologies.
All orchestrated through LUCI.

Aliante runs its multimedia environment through LUCI.

End card:
Absurdly simple AV for complex properties.
```

**Copy rules (from Jane):**
- 10 words maximum per onscreen slide/card (ceiling, not target)
- Do not add explanatory copy just because footage exists
- Some stretches should contain no text at all
- Do not turn factual lines into slogans
- Do not add VO

---

## Claim verification

All approved factual lines verified against `analysis/project-intelligence.md` claim ledger:

| Approved line | Claim # | Status | Notes |
|---|---|---|---|
| 15 legacy racks | #5 | ✅ confirmed | "15 racks → 2 LUCI racks" — V0026, EJ transcript, written case study |
| 2 current LUCI racks | #5 | ✅ confirmed | Same as above. V0026 says "two and a half"; use "2" per approved copy |
| 20+ projectors | #6 | ✅ confirmed | "20+ projectors removed" — written case study |
| 106-foot wall | #1 | ✅ confirmed | "106-foot curved LED wall" — V0026, EJ transcript, written case study |
| 2,000 square feet | #3 | ✅ confirmed | "~2,000 square feet" — written case study (106×20=2,120; "roughly 2,000") |
| 150-foot ticker | #8 | ✅ confirmed | "150 ft bar ticker" — written case study inventory |
| 266 displays | #22 | ✅ confirmed | "266 displays" — written case study ledger |
| 89 zones | #22 | ✅ confirmed | "89 audio zones" — approved copy shortens to "zones" (same fact) |
| 7+ technologies | #22 | ✅ confirmed | "7+ technologies orchestrated" — written case study ledger |

**No claim ledger conflicts found.** All approved factual lines are verified.

---

## Voice rule flag (for Jane — do not rewrite copy)

The approved end card reads: `Absurdly simple AV for complex properties.`

Two voice-rule conflicts:
1. **"AV" vs "A/V"** — `luci-messaging-voice.mdc` requires "Always write A/V — never AV or A-V." The approved copy uses "AV."
2. **"Absurdly simple"** — `luci-messaging-voice.mdc` lists "absurdly simple / easy to use / intuitive" under Retired terms.

Jane explicitly approved this copy, so it is not rewritten. **Flagged for Jane's awareness.** If she wants it changed, she will direct the change; Cursor will not substitute it.

---

## Footage gap: empty rack positions

Jane's instruction references "the footage showing the 13 empty racks." The deep media review did not identify footage of 13 empty rack positions specifically. Available rack-room footage:

- **V0048** — decommissioned projectors on floor (dusty, detached lenses, cable spools). Shows legacy equipment removed, not empty rack positions.
- **V0053** — decommissioned rack units on floor (Tier 3, brief). Shows removed units, not empty positions.
- **V0051** — completed LUCI racks (three racks with active blue displays). The "after."
- **V0052** — alternate completed racks (cable management).
- **I0078** — LUCI IPTV ENCODER NX-5 close-up.
- **V0049** — LUCI hardware being installed (progress, technician present).
- **V0050** — LUCI rack with technician (progress).

**Gap:** No footage of 13 empty rack positions (where the old racks were, now empty). The paper edit uses V0048 (decommissioned legacy equipment) as the "before" and V0051 (completed LUCI racks) as the "after." The subtraction is implied by the contrast between decommissioned equipment and the 2 LUCI racks, not by showing empty positions. **Flagged for Jane.** If footage of empty rack positions exists in the source library but was not flagged during deep review, a targeted re-inspection could find it.

---

## Paper edit sequence

### SECTION 1 — OPENING (two variants)

Both variants use the same approved copy. They converge into the same common body at Section 2.

---

#### Opening A — Finished-first

| # | Beat | Visual purpose | Primary asset | In/out range | Est. duration | Onscreen copy | No-text? | Alternate | Notes |
|---|---|---|---|---|---|---|---|---|---|
| A1 | Hook / scale | Establish the finished wall at full scale, people for scale | V0036 | 00:10.0–00:17.6 | ~8s | `Aliante Casino + Hotel` | No | V0041 (alt hero) | Best hero pull-back. Let the wall breathe before the thesis line. |
| A2 | Hook / thesis | Continue the hero reveal, land the thesis | V0040 | 00:11.0–00:20.0 | ~9s | `A multimedia transformation orchestrated by LUCI` | No | V0036 (reprise) | Use the comprehensive journey (bar + ticker + wall). The thesis line lands as the camera reaches the main wall. |
| A3 | Hook / scale | Hold on the wall, land the scale | I0065 | static | ~4s | `106 feet of curved LED.` | No | I0066 (alt still) | Freeze-frame hold on the definitive hero still. Let the viewer read the scale. |
| A4 | Hook / scale | Brief hold, second scale line | I0065 (hold) or V0041 | static / 00:08.3–00:11.0 | ~3s | `2,000 square feet of display.` | No | — | Quick second super. Can hold on I0065 or cut to V0041 for motion. |

**Opening A total: ~24s.** Then converges to Section 2 (build).

---

#### Opening B — Tease-and-build (Jane's current preference)

| # | Beat | Visual purpose | Primary asset | In/out range | Est. duration | Onscreen copy | No-text? | Alternate | Notes |
|---|---|---|---|---|---|---|---|---|---|
| B1 | Hook / title | Brief glimpse — the finished wall, but only a tease | V0036 | 00:10.0–00:13.0 | ~3s | `Aliante Casino + Hotel` | No | V0040 (alt tease) | Hold on the hero for only 3s — enough to establish visual quality, not enough to satisfy. Cut away before the full reveal. |
| B2 | Hook / thesis | Cut to the thesis line over a different visual | V0028 | 00:01.7–00:05.0 | ~3s | `A multimedia transformation orchestrated by LUCI` | No | V0021 (COMING SOON) | The thesis lands over construction — the viewer immediately knows this is about LUCI, not about construction. |
| B3 | Hook / scale | Land the scale over construction context | V0028 | 00:05.0–00:08.0 | ~3s | `106 feet of curved LED.` | No | — | The scale line over installation footage — the viewer sees the build and reads the size simultaneously. |
| B4 | Hook / scale | Second scale line, still in build | V0027 | 00:01.0–00:04.0 | ~3s | `2,000 square feet of display.` | No | — | Continue the build tease. The full hero reveal is saved for later. |

**Opening B total: ~12s.** Then converges to Section 2 (build). The full hero wall payoff is deferred to Section 8 (wall payoff).

**Why B is currently preferred:** It establishes visual quality immediately (the 3s tease confirms the wall is real) without spending the hero reveal. The thesis lands over construction, which prevents the "construction video" read from the first frame. The full hero payoff is saved for later, giving the ending a genuine visual reward.

---

### SECTION 2 — THE BUILD (common body)

Both openings converge here. The build footage communicates scale, physical effort, precision, and panel installation.

| # | Beat | Visual purpose | Primary asset | In/out range | Est. duration | Onscreen copy | No-text? | Alternate | Notes |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Build / complexity | Installation scale — workers on scissor lift, green test panels, wall under construction | V0028 | 00:01.7–00:11.7 | ~10s | `The hard part is building at this scale.` | No | V0027 (alt install) | The strongest installation footage. The copy names the effort. Let the viewer watch workers on lifts. |
| 2 | Build / precision | LED modules going up against green test pattern, workers on boom lift | V0027 | 00:04.0–00:10.0 | ~6s | — (no text) | **Yes** | V0028 (reprise) | A no-text stretch. Let the precision and physical work speak. The green test pattern is visually striking. |
| 3 | Build / commissioning | Technicians at base of completed wall, commissioning phase | V0035 | 00:07.3–00:12.5 | ~5s | — (no text) | **Yes** | — | Transition from construction to commissioning. The wall is nearly done. No text — the viewer watches the work. |

**Build total: ~21s.**

**5-photo progression placeholder:** Between shots 1 and 2 (or after shot 3), the human-curated 5-photo progression (I0054 → I0059 → I0062 → I0008 → I0027) could appear as a brief construction progression — the wall building itself from scaffolding to completed state. Duration: ~4-6s depending on treatment (dissolve, flipbook, or crop/reframe — not determined here). This is optional; if the video installation footage (V0028, V0027) carries the build sufficiently, the progression can be omitted. **Do not generate or animate it yet.**

---

### SECTION 3 — THE LUCI TURN

The key turn from "effort to build" to "simplicity to operate." This must land where the viewer understands LUCI is the reason operation becomes simple. Do not place it over generic construction footage.

| # | Beat | Visual purpose | Primary asset | In/out range | Est. duration | Onscreen copy | No-text? | Alternate | Notes |
|---|---|---|---|---|---|---|---|---|---|
| 4 | LUCI turn | Visual connection to LUCI — the completed LUCI racks or hardware. The turn from build to operation. | V0051 | 00:00.5–00:04.0 | ~4s | `LUCI makes running it the easy part.` | No | I0078 (LUCI hardware close-up) | The viewer sees the completed LUCI racks — the thing that runs the wall — and reads the turn. This is the bridge from construction to simplification. The rack-room proof follows immediately. |

**LUCI turn total: ~4s.**

**Why V0051 here:** The viewer has just watched the build (V0028, V0027, V0035). Now they see the completed LUCI racks — the hardware that runs what they just watched being built. The super "LUCI makes running it the easy part" lands over the thing that does the running. This is the visual/narrative connection to LUCI that the instruction requires.

---

### SECTION 4 — RACK ROOM (before/after)

Major visual proof point. The viewer should visually understand the subtraction.

| # | Beat | Visual purpose | Primary asset | In/out range | Est. duration | Onscreen copy | No-text? | Alternate | Notes |
|---|---|---|---|---|---|---|---|---|---|
| 5 | Rack before | Legacy equipment removed — decommissioned projectors, dusty, detached lenses | V0048 | 00:01.1–00:08.0 | ~7s | `Aliante's legacy system filled 15 racks.` | No | V0053 (alt decommissioned) | The "before." The viewer sees what came out. The copy names what it was. **Gap:** No footage of 13 empty rack positions — V0048 shows decommissioned equipment, not empty positions. See "Footage gap" above. |
| 6 | Rack after | Completed LUCI racks — clean, active, blue displays | V0051 | 00:02.0–00:06.5 | ~5s | `With LUCI, everything now runs from 2.` | No | V0052 (alt completed) | The "after." The contrast with shot 5 IS the simplification proof. The copy names the subtraction. |
| 7 | Rack detail | LUCI hardware close-up — the equipment that runs it | I0078 | static | ~3s | — (no text) | **Yes** | V0052 (alt rack) | A no-text hardware detail shot. Let the viewer see the LUCI branding and the clean rack. The proof is already made; this is the punctuation. |

**Rack room total: ~15s.**

---

### SECTION 5 — PROJECTOR LINE (optional — CUT RECOMMENDED)

| # | Beat | Visual purpose | Primary asset | In/out range | Est. duration | Onscreen copy | No-text? | Alternate | Notes |
|---|---|---|---|---|---|---|---|---|---|
| 8 | Projector (optional) | Additional decommissioned evidence — projectors on floor | V0048 | 00:08.0–00:11.6 | ~4s | `More than 20 legacy projectors came out, too.` | No | — | **CUT RECOMMENDED.** Reason: V0048 already appeared in shot 5 (rack "before"). Reusing the same footage for a second decommissioning line is redundant — the viewer has already seen the legacy equipment. The rack contrast (shots 5-6) already makes the subtraction visible. Adding the projector line slows the story without adding new visual evidence. If the edit needs the projector number for completeness, it can appear as a secondary super over shot 5 (rack "before") rather than as a separate shot. |

**Projector: CUT RECOMMENDED.** If kept, ~4s additional.

---

### SECTION 6 — WALL PAYOFF (no text)

At least one stretch of excellent finished-wall footage with no onscreen copy, allowing the completed environment to breathe.

| # | Beat | Visual purpose | Primary asset | In/out range | Est. duration | Onscreen copy | No-text? | Alternate | Notes |
|---|---|---|---|---|---|---|---|---|---|
| 9 | Wall payoff | The completed wall in full — let it breathe | V0036 | 00:10.0–00:17.6 | ~8s | — (no text) | **Yes** | V0040 (alt hero) | No text. The viewer has just seen the rack room (the simplification). Now they see the wall again — but understand what's behind it. In Opening B, this is the first full hero reveal (the payoff the viewer has been waiting for). In Opening A, this is a reprise with deeper meaning. |
| 10 | Wall payoff / environment | Comprehensive journey — bar, ticker, seating, main wall | V0040 | 00:18.0–00:27.3 | ~9s | — (no text) | **Yes** | V0041 (alt hero) | Continue the no-text stretch. The most comprehensive hero footage. Let the music carry the viewer through the finished environment. |

**Wall payoff total: ~17s.**

---

### SECTION 7 — TICKER

The finished ticker as part of the expansion beyond the main wall. Do not use testing footage (V0031) as finished footage.

| # | Beat | Visual purpose | Primary asset | In/out range | Est. duration | Onscreen copy | No-text? | Alternate | Notes |
|---|---|---|---|---|---|---|---|---|---|
| 11 | Ticker | Finished bar ticker reveal — pull-back with patrons | V0039 | 00:05.8–00:13.8 | ~8s | `A 150-foot LED ticker wraps the sportsbook bar.` | No | V0044 (alt ticker) | The completed ticker. The copy names the scale. Do NOT use V0031 (testing data) here — it shows test numbers, not finished content. |

**Ticker total: ~8s.**

---

### SECTION 8 — PROPERTY-WIDE EXPANSION

The transition from sportsbook-specific footage into the larger Aliante property. Use only the strongest B-roll. Do not dilute with generic casino footage.

| # | Beat | Visual purpose | Primary asset | In/out range | Est. duration | Onscreen copy | No-text? | Alternate | Notes |
|---|---|---|---|---|---|---|---|---|---|
| 12 | Expansion transition | Bridge from sportsbook to the broader property | V0010 | 00:02.0–00:08.0 | ~6s | `And the sportsbook is only part of it.` | No | V0004 (alt bridge) | The strongest B-roll — casino bar with gaming terminals, sports on TV. Shows LUCI-managed A/V in operational context. The copy marks the expansion. |
| 13 | Property-wide | Food court with digital signage — LUCI-managed endpoints | V0004 | 00:00.6–00:06.7 | ~6s | `Across Aliante:` | No | V0002 (alt property) | The copy introduces the property scope. The food court signage is a visible LUCI-managed endpoint. |
| 14 | Property-wide | Casino floor — gaming atmosphere, scale of property | V0002 | 00:01.6–00:08.0 | ~6s | `266 displays. 89 zones. 7+ technologies.` | No | V0014/V0016 (alt property) | The scope line over the broadest property shot. Three numbers communicate scale and breadth. Do not add more stats. |
| 15 | Property-wide / orchestration | Hotel lobby or high-limit lounge — hospitality context | V0014 | 00:00.4–00:05.0 | ~5s | `All orchestrated through LUCI.` | No | V0016 (alt lobby) / V0007 (high-limit lounge) | The orchestration line lands over a distinct environment — the viewer sees the breadth of what LUCI runs. |

**Property-wide total: ~23s.**

---

### SECTION 9 — ENDING

Return to the strongest finished environment. Then the end card.

| # | Beat | Visual purpose | Primary asset | In/out range | Est. duration | Onscreen copy | No-text? | Alternate | Notes |
|---|---|---|---|---|---|---|---|---|---|
| 16 | Closing | Return to the finished wall — the bookend | V0040 | 00:20.0–00:27.3 | ~7s | `Aliante runs its multimedia environment through LUCI.` | No | V0036 (alt closing) | Return to the strongest finished-environment footage. The viewer sees the wall one final time, now understanding what's behind it. |
| 17 | End card | LUCI end card | — (graphic) | — | ~4s | `Absurdly simple AV for complex properties.` | No | — | End card over a held frame or fade to a LUCI brand card. **Voice rule flag:** "AV" should be "A/V" and "absurdly simple" is a retired term per `luci-messaging-voice.mdc`. Jane approved this copy — flagged, not rewritten. |

**Ending total: ~11s.**

---

## Five-photo progression — provisional placement

**Location:** Between shots 1 and 2 in the build section (Section 2), or after shot 3 (commissioning).

**Sequence:** I0054 (IMG_4216, scaffolding) → I0059 (IMG_4334, early build) → I0062 (IMG_4367, later pre-install) → I0008 (IMG_4806, LED installation underway) → I0027 (IMG_4872, completed wall).

**Duration:** ~4-6s depending on treatment.

**Function:** Shows the wall building itself from scaffolding to completed state. In Opening A, it can serve as the rewind mechanism (the wall "unbuilds" from the finished reveal into the build). In Opening B, it can serve as a construction progression within the build section.

**Treatment:** Not determined. Candidate treatments (soft dissolve, flipbook, crop/reframe, longer hold on payoff) remain in `visual-analysis.json`. Do not generate or animate yet.

**If omitted:** The video installation footage (V0028, V0027, V0035) carries the build sufficiently without the photo progression. It is a useful device, not a structural dependency.

---

## Runtime estimate

| Section | Duration |
|---|---|
| Opening A (finished-first) | ~24s |
| Opening B (tease-and-build) | ~12s |
| Build (common) | ~21s |
| LUCI turn | ~4s |
| Rack room | ~15s |
| Projector (optional — CUT RECOMMENDED) | ~4s (if kept) |
| Wall payoff (no text) | ~17s |
| Ticker | ~8s |
| Property-wide expansion | ~23s |
| Ending | ~11s |

**Opening A total (with projector cut): ~24 + 21 + 4 + 15 + 17 + 8 + 23 + 11 = ~123s (~2:03)**
**Opening B total (with projector cut): ~12 + 21 + 4 + 15 + 17 + 8 + 23 + 11 = ~111s (~1:51)**

**Leanest coherent version: ~111-123s (~1:51-2:03).** This is lean. If it feels too long, the first cut candidates are:
1. Projector line (Section 5) — already CUT RECOMMENDED (~4s saved)
2. One of the two no-text wall payoff shots (Section 6, shot 9 or 10) — keep one, cut the other (~8s saved)
3. One of the property-wide B-roll shots (Section 8, shot 13 or 15) — keep three, cut one (~6s saved)

**Do not cut copy to shorten.** Cut redundant shots or optional proof points first.

---

## Video clips used in the common body

**Unique video assets in the common body (excluding openings):**
V0028, V0027, V0035, V0051, V0048, V0036, V0040, V0039, V0010, V0004, V0002, V0014

**Unique image assets in the common body:**
I0078

**Total unique assets in common body: 13 (12 videos + 1 image)**

**Opening A additional: V0036, V0040, I0065 (V0041 alternate)**
**Opening B additional: V0036, V0028, V0027 (reused in common body)**

---

## Continuity / edit notes

- **V0036 → V0040:** Both are hero pull-backs of the completed wall. If both appear (Opening A uses them early, Section 6 uses them as payoff), vary the in/out points so the viewer doesn't feel they're seeing the same shot twice. Use V0036's 00:10-00:13 in Opening A and 00:13-00:17 in Section 6.
- **V0028 → V0027:** Both show installation with workers on lifts. V0028 is the stronger (scissor lift, green test panels). V0027 is the alternate (boom lift, green test pattern). Use V0027 as a different angle of the same work, not a repeat.
- **V0048 → V0051:** The rack-room contrast. Cut from dusty decommissioned projectors to clean blue LUCI racks. The cut IS the argument. Music can bridge the visual quality gap.
- **V0039 → V0010:** The ticker-to-property transition. V0039 is the bar ticker (sportsbook-specific). V0010 is the casino bar (broader property). The cut marks the expansion from "the sportsbook" to "Aliante."
- **No-text stretches:** Shots 2, 3, 7, 9, 10 are no-text. ~26s of no-text footage in a ~2:00 video. The music carries these stretches. Do not add text just because footage exists.

---

## A/B test compliance

- This artifact is `editorial/paper-edit-cursor.md` — it does not overwrite `editorial/paper-edit.md`.
- STATE.json is not modified during this test.
- No shared analysis, narrative, or copy artifacts were altered.
- The only new project artifact created is this file.
