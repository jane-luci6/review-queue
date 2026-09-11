# Body treatment lock — Aliante RC2 onscreen text

**Locked:** 11 Sep 2026 · `design-direction-open` pass · applies to every onscreen text card **except** the opening title slide (`c00`, `c01`), which Jane owns.
**Revised:** 11 Sep 2026 — rev 2. Jane approved the left-anchored editorial direction and asked for real dark backing behind the type ("some kind of faded black box or something behind the text") because the gradient alone loses to busy property footage. Rev 2 adds the **corner plate** (§3) and tightens the measure to `864`. Type system, anchor, variants, and copy are unchanged.

**Canvas:** 1920 × 1080, 24 fps. All numbers below are pixels at that canvas.

**What GLM does next:** render one revised **c02** preview from this lock — `previews/04-body-c02-backed-preview.jpg` plus the transparent PNG — composited over `timeline/002-s02-Casino 1-gaming-100k.mp4`. Nothing else until Jane approves.

---

## 1. Thesis — a plate in the frame, not a box around the text

Two things have been tried and one was rejected. Getting rev 2 right means holding both lessons at once.

**Rejected (pass 1):** a rounded translucent pill hugging one centered line of white SemiBold. It failed because it was a *caption* — a floating object with four visible sides, soft corners, and a width that shrink-wrapped the sentence. That is the iMovie/YouTube subtitle default and it reads as cheap regardless of the type inside it.

**Insufficient (rev 1):** a shapeless full-bleed gradient and nothing else. It solved the cheapness but not the job. Over the c02 frame — a lit ceiling, a purple carpet field, and a fully illuminated slot sign directly behind the numeral — a 0.62 bottom gradient barely registers. The mint rule vanished completely. Legibility is not optional on 17 cards cut across an entire property, and a treatment that only works over dark footage is not a system.

**Rev 2 — the corner plate.** Onscreen text sits on a hard-edged plane of navy-deep anchored into the frame's **bottom-left corner**. What separates a plate from the rejected pill is not density, it is geometry:

| | Rejected pill | Corner plate |
|---|---|---|
| Sides visible | 4 | **1** (the top edge) |
| Corners | 4, rounded | **0** |
| Relation to frame | floats inside it | **bleeds off left and bottom** — part of the frame's architecture |
| Width | shrink-wraps the string | **fixed per variant class**; never derived from copy length |
| Right side | hard edge | **dissolves over 512px** — there is no right edge to judge |
| Read | a container holding a caption | a graded plane the frame's corner is cut into |

A shape with one authored edge and no corners cannot read as a box, because a box is a thing you see the sides of. What the viewer sees is a horizontal boundary at the left of frame that tapers away to the right — the same sharp, left-anchored, horizontal-rule language the design system already uses, moved into motion.

**The plate is a second plane, not a cut-out.** The full-bleed gradient from rev 1 stays underneath. Its job changes: it is no longer the legibility device, it is the grade that keeps the plate from sitting on bright footage like a sticker. At the plate's top edge the footage above has already been graded to roughly `0.08–0.12`; the plate steps it to `~0.65`. A step between two tinted planes reads as deliberate tonal design. A hard `0.00 → 0.65` cut into raw bright footage would read as a mis-keyed matte or a letterbox bar — that is the failure mode the two-layer build exists to prevent. **Never ship the plate without the bed.**

Three moves still carry the system, unchanged from rev 1:

1. **Anchor, don't float.** Every card hangs from one fixed point — left margin `x=160`, last baseline `y=920`. The block grows upward. Nothing is centered, nothing is vertically guessed per shot. Consistency across 17 cards is what makes it read as designed rather than typed. The plate anchors to the same corner.
2. **Hierarchy inside the card is what makes it sophisticated.** The rejected version set every card at one size, so a scope stat and a full sentence rendered identically. Stats get a display numeral with a receding qualifier; sentences get a single calm measure. Same anchor, same rule, same plate — one system, two registers.
3. **One ornament, and it's structural.** A 56 × 3 mint rule above the first line, on the left margin. It is the only graphic element, and on the plate it is finally legible. Do **not** add a second ornament — no mint hairline along the plate's top edge, no corner tick, no logo bug. That was considered and rejected: the plate's edge is already doing the structural work, and a mint line on it would turn a tonal plane into chrome.

---

## 2. Tokens

| Token | Value | Use |
|---|---|---|
| Type — primary | `#F5F8FA` (off-white) @ 100% | first line of every card |
| Type — secondary | `#F5F8FA` @ 80% | qualifier / second-tier line |
| Accent rule | `#68E3BE` (mint) @ 100% | the 56 × 3 rule only |
| Plate | `#0A161C` (navy-deep) @ `0.62` | the bottom-left corner plane — primary legibility |
| Bed | `#0A161C` (navy-deep), gradient alpha | the grade under the plate — never omitted |
| Font — emphasis | `SpaceGrotesk-SemiBold.ttf` | numerals, first tier |
| Font — everything else | `SpaceGrotesk-Medium.ttf` | narrative lines, qualifiers |

Fonts: `LUCI Systems Design System/assets/fonts/`. **Only Medium and SemiBold exist — do not synthesize a Bold or a Light.** Weight contrast comes from Medium vs SemiBold plus scale, not from faux weights.

**Type is off-white, never pure `#FFFFFF`, and never mint.** Mint type belongs to Jane's title. Body cards get mint only as the 3px rule.

Space Grotesk for this onscreen copy is Jane's lock for this beat. Do not "correct" it to Inter — the design-system body-copy rule governs running document copy, not video type.

---

## 3. Geometry

### 3.1 Type block — shared by every variant

| Element | Spec |
|---|---|
| Left margin (all text + rule) | `x = 160` |
| Last baseline of the block | `y = 920` (160 from bottom edge) |
| Stack direction | upward from `y = 920` |
| Max line width | `864` (right edge `x = 1024`) — **rev 2: was `1120`** |
| Max lines | 2 (variant N/S) · 3 (variant M) |
| Alignment | left, ragged right — **never centered, never justified** |
| Mint rule | `56 × 3`, at `x = 160`, bottom edge `28` above the cap-top of line 1 |
| Type shadow | `#0A161C` @ 50%, offset `(0, 3)`, blur `22` — soft, shapeless, no stroke/outline |

The measure tightened from `1120` to `864` so that every line finishes inside the plate's full-density zone. Verified against the real fonts: every string in `titles.md` fits at `864`, and the widest rendered line in the whole set is `768` (c04, line 2). Locked breaks are in the appendix. Keep the shadow even though the plate carries most of the contrast — it earns its keep where the plate eases off to the right.

**Measured cap-height ratio is `0.708` of the point size** (`PIL` bbox on the shipped TTFs: `34` at `48`, `40` at `56`, `90` at `128`). Descender is `0.20`. Every vertical number below is derived from those, not estimated — if a renderer disagrees, hold the anchor and re-derive.

### 3.2 Bed — full-bleed gradient (layer 1)

Vertical gradient of `#0A161C`, eased (quadratic, not linear — a linear ramp shows a visible start line):

- alpha `0.00` at `y = 380`
- alpha `0.45` at `y = 1080`

Multiplied by a horizontal falloff so the frame breathes on the right:

- multiplier `1.00` from `x = 0` to `x = 980`
- easing down to `0.30` at `x = 1920`

Full-bleed to all four relevant edges. **No radius, no blur pass, no visible boundary anywhere.** The bed is a grade, not the legibility device — do not raise it to compensate for a weak plate.

### 3.3 Plate — bottom-left corner plane (layer 2)

Flat `#0A161C` at alpha `0.62`, composited over the bed.

| Property | Spec |
|---|---|
| Color | `#0A161C` |
| Density | `0.62` (tunable band `0.50–0.74`) |
| Bleeds | **left** (`x = 0`) and **bottom** (`y = 1080`) — no edge is drawn on either |
| Top edge | hard, **radius `0`**, with an `8` px vertical feather |
| Top edge `y` | per variant class — see table below |
| Full density | `x = 0 → 1024` |
| Right falloff | quadratic ease `1.00` at `x = 1024` → `0.00` at `x = 1536`; nothing right of `1536` |

**Top edge by variant class** (fixed per class, never per string — this is what keeps it from hugging):

| Variant | Line-1 cap-top | Mint rule | Plate top edge | Padding above rule |
|---|---|---|---|---|
| **S** — stat lockup | `y = 778` | `y = 747 → 750` | `y = 680` | `67` |
| **N** — narrative line | `y = 822` | `y = 791 → 794` | `y = 728` | `63` |
| **M** — multi-stat stack | `y = 728` | `y = 697 → 700` | `y = 632` | `65` |
| **E** — end card | — | none | **none** | — |

Padding lands `63–67` rather than a flat `64` because the plate's top edge stays on the 8px grid. The grid wins; the small variance is invisible and the numbers stay checkable.

N uses the **two-line** height for every N card, including one-liners. A one-line N card therefore carries extra headroom inside the plate; that reads as margin, which is correct, and it means fourteen cards share one plate geometry instead of fourteen slightly different ones.

**Notes on the numbers.**
- The `8` px feather is banding and ringing control for video compression, not a soft-chrome effect. At 1080p it reads as a clean line. Do not raise it past `12`, and do not drop it to `0` — a mathematically hard cut on a flat plane will ring under H.264.
- Padding is asymmetric by design and mostly supplied by the frame: `160` left (the margin, then bleed), `64` above the mint rule, roughly `150` below the last descender (then bleed). Right-side clearance is at least `~250` on every card in `titles.md`.
- The full-density edge at `x = 1024` and the falloff end at `x = 1536` are absolute. **Never derive either from the rendered text width.**
- The top edge tapers out with the right falloff, so no top-right corner ever forms.

### 3.4 Combined density — the thing to actually verify

Bed and plate composite to an effective alpha behind the type of roughly `0.65–0.72` (at `y = 800`: `1 − (1 − 0.10)(1 − 0.62) ≈ 0.66`).

**Target: `0.62–0.80` effective alpha measured behind the type block.** Sample the actual frame rather than trusting the arithmetic. Move the **plate** density inside `0.50–0.74` to hit it — toward `0.50` over already-dark footage, toward `0.74` over a blown-out casino floor or a lit sign. Leave the bed alone. Never exceed `0.74` on the plate: past that the footage stops reading through and the plane becomes a black bar. Never drop the plate below `0.50` — consistency across cards matters more than any single shot. **Hold `0.62` for the c02 preview.**

---

## 4. Variants

Variant selection is mechanical. Apply the test in order; first match wins.

| Variant | Test on the `titles.md` string | Cards |
|---|---|---|
| **M — multi-stat stack** | contains 3+ period-separated fragments | c16 |
| **S — stat lockup** | begins with a numeral **and** is ≤ 5 words | c02, c12 |
| **N — narrative line** | everything else | c03–c11, c13–c15, c17, c18 |
| **E — end card** | role `end` in `titles.md` | c19 |

### S — stat lockup

The quantity becomes display scale; the rest of the string recedes. Split the verbatim string at the end of the leading numeric token — no words added, removed, or reordered.

| Line | Font | Size | Tracking | Color | Leading |
|---|---|---|---|---|---|
| 1 — numeral | SemiBold | `128` | `-0.03em` | off-white 100% | — |
| 2 — qualifier | Medium | `40` | `+0.02em` | off-white 80% | `24` gap, line-1 baseline → line-2 cap-top |

Keep sentence case and keep the trailing period — copy is verbatim. **Do not uppercase body cards.** ALL CAPS belongs to Jane's Syncopate title; caps here would put the two in the same register.

### N — narrative line

| Spec | Value |
|---|---|
| Font / size | Medium `48` |
| Tracking | `+0.01em` |
| Baseline-to-baseline | `64` |
| Color | off-white 100% (both lines) |
| Lines | 1 preferred, 2 maximum |

Line-break rules:

- Break at a clause or prepositional boundary, not wherever the measure runs out.
- Never orphan a final line shorter than 4 characters or one word.
- Never break a number from its unit — `150-foot`, `14,200-square-foot`, `100,000+`, `7+` stay whole on one line.
- Never break `LUCI` or `A/V` across lines.
- Roughly balance the two lines; a long line over a 3-word line looks accidental.
- With the measure at `864`, most N strings now take two lines. That is expected — two balanced lines inside the plate beat one long line running into the falloff.

### M — multi-stat stack (c16 only)

Three fragments, one per line, all at `56` Medium / `-0.01em` / `76` baseline-to-baseline. Within each line, set the numeral in **SemiBold at off-white 100%** and the following word in **Medium at off-white 80%** — same size, so the stack stays a clean three-line column while the counts still lead. Periods kept verbatim.

### E — end card (c19)

The end card is navy with the LUCI logo — no footage, no competing title, so it is the one exception to left-anchoring **and the one card with no plate**.

| Spec | Value |
|---|---|
| Font / size | Medium `44` |
| Tracking | `+0.06em` |
| Color | off-white 88% |
| Alignment | centered under the logo lockup |
| Bed / plate | none (card is already `#0A161C`) |
| Mint rule | none |

---

## 5. Worked example — c02, copy verbatim

**String (`titles.md`, unchanged):** `100,000+ square feet of gaming.`
**Variant:** S (begins with a numeral, 5 words).
**Break:** `100,000+` / `square feet of gaming.`

| Element | Value |
|---|---|
| Bed | `#0A161C`, alpha 0.00 @ `y=380` → 0.45 @ `y=1080`, quadratic ease; horizontal falloff 1.00 to `x=980` → 0.30 at `x=1920`; full-bleed, no edges |
| Plate | `#0A161C` @ `0.62`; occupies `y = 680 → 1080` and `x = 0 → 1536`; bleeds left and bottom; **top edge hard at `y = 680`, radius 0, 8px feather**; full density to `x = 1024`, quadratic ease to 0.00 at `x = 1536` |
| Line 2 — `square feet of gaming.` | SpaceGrotesk-Medium `40`, `+0.02em`, `#F5F8FA` @ 80%, left `x=160`, **baseline `y=920`**; cap-top `y=892`, descenders to `y=928`, right edge `x=620` (width `460`) |
| Line 1 — `100,000+` | SpaceGrotesk-SemiBold `128`, `-0.03em`, `#F5F8FA` @ 100%, left `x=160`, baseline `y=868`; cap-top `y=778`, right edge `x=720` (width `560`) |
| Mint rule | `#68E3BE`, `x = 160→216`, `y = 747→750` |
| Shadow | both lines: `#0A161C` @ 50%, offset `(0,3)`, blur `22` |
| Type block extent | `y = 747–928`, `x = 160–720` — inside the plate's full-density zone with `304` of right clearance |
| Effective alpha behind type | ≈ `0.66` — inside the `0.62–0.80` target |
| Open frame | everything above `y = 680`, and everything right of `x = 1536`, carries bed grade only |

Composite order: footage → bed → plate → mint rule → type (with shadow).

Baselines are derived from the anchor: last baseline `y=920`, everything stacks up; the plate's top edge is derived from the mint rule. If a renderer's cap-height metrics differ slightly from the estimates above, **hold `y=920`, the `160` left margin, and the plate's `x` values**, and let the mint rule and plate top float with the measured cap-top. The anchor and the plate's horizontal geometry are the lock; the vertical cap-top numbers are arithmetic.

---

## 6. How this stays clear of Jane's title

The title slide keeps its own treatment untouched. The body system differs on six axes at once, so there is no ambiguity about which is the display moment:

| | Jane's title (`c00`) | Body cards |
|---|---|---|
| Family | Syncopate | Space Grotesk |
| Case | ALL CAPS | sentence case as written |
| Color | mint type | off-white type; mint only as a 3px rule |
| Alignment | centered | left-anchored at `x=160` |
| Position | optical center | bottom-left, baseline `y=920` |
| Backing | its own soft centered scrim | bottom-left corner plate, hard top edge, bleeds two frame edges |

Shared, deliberately: the navy-deep value and mint as the accent. That is brand continuity, not competition. **Nothing after the title slide is ever centered over footage, and nothing after it sets type in mint.** The title remains the only display moment in the cut.

---

## 7. Do not — explicitly against the rejected pass

- **No pill, no rounded rectangle, no capsule, no card** behind text. **No `border-radius` anywhere, on any layer.** If it has a rounded corner, it's wrong.
- **No four-sided shape.** The plate draws exactly one edge — the top. Left and bottom bleed off frame; the right dissolves. Drawing a right or left edge turns the plate back into the rejected box.
- **No backing sized from the copy.** The plate's `x` geometry is absolute (`1024` / `1536`) and its top edge comes from the variant class, not the string. It must never shrink-wrap a sentence.
- **No plate without the bed.** A hard-edged plane dropped straight onto ungraded footage reads as a letterbox bar or a mis-keyed matte. Two planes, always, in that order.
- **No blurred-edge scrim shape.** The gaussian-blurred halo in `build_previews.py` (`soft_dark_backing`) is retired for body cards. Do not reuse that function. The `8` px feather on the plate's top edge is compression control, not a blurred shape.
- **No second ornament.** No mint hairline on the plate edge, no corner tick, no bug, no gradient sheen inside the plate. The mint `56 × 3` rule is the only graphic element.
- **No centered body text.** Ever, over footage.
- **No single flat size for all cards** — a scope stat and a sentence must not render identically.
- **No pure white**, no mint type, no gold anywhere in these cards.
- **No outline, stroke, or hard drop shadow** on type. Soft shadow only, per §3.1.
- **No copy changes** — no rewording, no dropped periods, no added punctuation, no uppercasing.
- **No per-shot repositioning.** The anchor and the plate's geometry are fixed. Shots are adapted to with plate density inside `0.50–0.74`, nothing else.
- **No animated text and no animated plate** — no typewriter, no slide-in, no wipe-on. If the overlay fades, plate and type cross-dissolve together, 8 frames (`0.33s`) in and out.

---

## 8. Pre-ship check

1. Left margin `160` and last baseline `y=920` on every card (variant E excepted).
2. Correct variant per the §4 test; c16 is M, c02 and c12 are S.
3. Copy byte-identical to `titles.md`, including periods.
4. Only Medium and SemiBold used; no faux weights.
5. Type off-white; mint appears only as the `56 × 3` rule — and it is **visibly legible** on the plate.
6. Bed present under the plate; bed is a gradient with no visible edge.
7. Plate present: `radius 0`, bleeds left and bottom, one visible edge, top edge at the variant's `y`, full density to `x=1024`, dissolved to nothing by `x=1536`.
8. Effective alpha behind the type block sampled at `0.62–0.80`; plate density inside `0.50–0.74`.
9. Every text line finishes at or before `x = 1024`; max 2 lines (3 for M); no orphans; numbers unbroken from their units.
10. Nothing centered over footage; no rounded geometry anywhere on any layer.
11. Everything inside the 5% title-safe area (`x ≥ 96`, `y ≤ 984`).

---

## 9. Out of scope / open

- **`c00` and `c01`** — the opening title slide is Jane's. Not redesigned here, and it does **not** get the plate. `c01` ("A sportsbook renovation with LUCI Systems", role `title2`) sits on the same shot as `c00` and reads as part of that slide, so this lock deliberately leaves it alone. If Jane wants `c01` pulled into the body system instead, it becomes a one-line variant N and that needs her call.
- **Per-card plate density** for c03–c19 — set during render against each frame, inside the `0.50–0.74` band, to land the §3.4 effective-alpha target.
- **`build_revised_c02.py`** implements rev 1. GLM updates it (or supersedes it) to add the two-layer bed + plate and the `864` measure when rendering `previews/04-body-c02-backed-preview.jpg`.

---

## Appendix — locked line breaks at measure `864`

Copy is verbatim from `titles.md`; only the break points are authored here, per the §4 rules. Widths are measured on the shipped TTFs at the variant's size and tracking. Use these rather than re-breaking at render time.

| Card | Variant | Line 1 | Line 2 | Line 3 |
|---|---|---|---|---|
| c02 | S | `100,000+` — 560 | `square feet of gaming.` — 460 | — |
| c03 | N | `Across more than 40 acres.` — 647 | — | — |
| c04 | N | `Aliante set out to renovate its` — 714 | `14,200-square-foot sportsbook.` — 768 | — |
| c05 | N | `The renovation removed more` — 710 | `than 20 legacy projectors.` — 631 | — |
| c06 | N | `Aliante's A/V already ran` — 578 | `on the LUCI platform.` — 504 | — |
| c07 | N | `So LUCI Systems was the` — 589 | `obvious build partner.` — 522 | — |
| c08 | N | `For the wall and ticker.` — 541 | — | — |
| c09 | N | `The hard part is building` — 579 | `at this scale.` — 303 | — |
| c10 | N | `LUCI makes running it the easy part.` — 856 | — | — |
| c11 | N | `Aliante's legacy system` — 561 | `filled 15 racks.` — 336 | — |
| c12 | S | `13` — 131 | `now sit empty.` — 298 | — |
| c13 | N | `With LUCI, everything` — 510 | `now runs from 2.` — 397 | — |
| c14 | N | `A 150-foot LED ticker wraps` — 656 | `the sportsbook bar.` — 473 | — |
| c15 | N | `And the sportsbook is` — 523 | `only part of it.` — 342 | — |
| c16 | M | `266 displays.` — 350 | `89 zones.` — 253 | `7+ technologies.` — 441 |
| c17 | N | `All orchestrated through LUCI.` — 719 | — | — |
| c18 | N | `The wall, the ticker, and LUCI` — 681 | `are ready for game day.` — 568 | — |
| c19 | E | tagline, centered under logo, no plate | — | — |

c10 is the only long N string that stays on one line — it measures `856`, inside the `864` limit. Everything else over the measure is broken at a clause boundary with the two lines roughly balanced. **A one-line N card still uses the N plate height (`y = 728`);** the extra headroom is margin, not an error.
