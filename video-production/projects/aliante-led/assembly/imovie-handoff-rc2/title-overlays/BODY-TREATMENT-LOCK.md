# Body treatment lock — Aliante RC2 onscreen text

**Locked:** 11 Sep 2026 · `design-direction-open` pass · applies to every onscreen text card **except** the opening title slide (`c00`, `c01`), which Jane owns.

**Canvas:** 1920 × 1080, 24 fps. All numbers below are pixels at that canvas.

**What GLM does next:** render one revised **c02** preview from this lock (transparent PNG + composite over `timeline/002-s02-Casino 1-gaming-100k.mp4`). Nothing else until Jane approves.

---

## 1. Thesis — an anchored type block, not a caption

The rejected pass failed because it was a *caption*: a rounded translucent pill hugging one centered line of white SemiBold, floating in the middle of the lower frame. Rounded pill + centered sentence + same backing as the title is the iMovie/YouTube subtitle default, and it reads as cheap no matter how good the type inside it is.

The fix is not a better box. **It is no box.** Onscreen text becomes a left-anchored editorial block hung off the frame's bottom-left corner, legible because of a shapeless gradient in the footage, not because of a container. This is the de-boxed LUCI language already canon in the design system (hairline + whitespace, sharp geometry, no rounded chrome) applied to motion.

Three moves carry it:

1. **Anchor, don't float.** Every card hangs from one fixed point — left margin `x=160`, last baseline `y=920`. The block grows upward from there. Nothing is centered, nothing is vertically guessed per shot. Consistency across 17 cards is what makes it read as designed rather than typed.
2. **Backing has no edges.** A full-width bottom gradient replaces the pill. A gradient can't look cheap because there is no shape to judge — it reads as a graded frame, which is how documentary lower-thirds have always worked.
3. **One ornament, and it's structural.** A 56 × 3 mint rule above the first line, on the left margin. That is the only graphic element. It is the same lockup accent rule the site uses, so the video inherits the brand without new language.

**Hierarchy inside the card is what makes it sophisticated.** The rejected version set every card at one size, so a scope stat and a full sentence looked identical. Two related variants fix that: stats get a display numeral with a receding qualifier; sentences get a single calm measure. Same anchor, same rule, same scrim — one system, two registers.

---

## 2. Tokens

| Token | Value | Use |
|---|---|---|
| Type — primary | `#F5F8FA` (off-white) @ 100% | first line of every card |
| Type — secondary | `#F5F8FA` @ 80% | qualifier / second-tier line |
| Accent rule | `#68E3BE` (mint) @ 100% | the 56 × 3 rule only |
| Scrim | `#0A161C` (navy-deep), gradient alpha | legibility |
| Font — emphasis | `SpaceGrotesk-SemiBold.ttf` | numerals, first tier |
| Font — everything else | `SpaceGrotesk-Medium.ttf` | narrative lines, qualifiers |

Fonts: `LUCI Systems Design System/assets/fonts/`. **Only Medium and SemiBold exist — do not synthesize a Bold or a Light.** Weight contrast comes from Medium vs SemiBold plus scale, not from faux weights.

**Type is off-white, never pure `#FFFFFF`, and never mint.** Mint type belongs to Jane's title. Body cards get mint only as the 3px rule.

Space Grotesk for this onscreen copy is Jane's lock for this beat. Do not "correct" it to Inter — the design-system body-copy rule governs running document copy, not video type.

---

## 3. Geometry — shared by every variant

| Element | Spec |
|---|---|
| Left margin (all text + rule) | `x = 160` |
| Last baseline of the block | `y = 920` (160 from bottom edge) |
| Stack direction | upward from `y = 920` |
| Max line width | `1120` (right edge `x = 1280`; the right third of frame stays open) |
| Max lines | 2 (variant N/S) · 3 (variant M) |
| Alignment | left, ragged right — **never centered, never justified** |
| Mint rule | `56 × 3`, at `x = 160`, bottom edge `28` above the cap-top of line 1 |
| Type shadow | `#0A161C` @ 50%, offset `(0, 3)`, blur `22` — soft, shapeless, no stroke/outline |

### Scrim

Vertical gradient of `#0A161C`, eased (quadratic, not linear — a linear ramp shows a visible start line):

- alpha `0.00` at `y = 430`
- alpha `0.62` at `y = 1080`

Multiplied by a horizontal falloff so the frame breathes on the right:

- multiplier `1.00` from `x = 0` to `x = 980`
- easing down to `0.35` at `x = 1920`

Full-bleed to all four relevant edges. **No radius, no blur pass, no visible boundary anywhere.**

Peak alpha may move within `0.40–0.68` when a shot demands it — drop toward `0.40` over already-dark footage, push toward `0.68` over a blown-out casino floor. Never remove the scrim (consistency across cards) and never exceed `0.68` (it starts reading as a black bar). **Hold `0.62` for the c02 preview.**

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

### M — multi-stat stack (c16 only)

Three fragments, one per line, all at `56` Medium / `-0.01em` / `76` baseline-to-baseline. Within each line, set the numeral in **SemiBold at off-white 100%** and the following word in **Medium at off-white 80%** — same size, so the stack stays a clean three-line column while the counts still lead. Periods kept verbatim.

### E — end card (c19)

The end card is navy with the LUCI logo — no footage, no competing title, so it is the one exception to left-anchoring.

| Spec | Value |
|---|---|
| Font / size | Medium `44` |
| Tracking | `+0.06em` |
| Color | off-white 88% |
| Alignment | centered under the logo lockup |
| Scrim | none (card is already `#0A161C`) |
| Mint rule | none |

---

## 5. Worked example — c02, copy verbatim

**String (`titles.md`, unchanged):** `100,000+ square feet of gaming.`
**Variant:** S (begins with a numeral, 5 words).
**Break:** `100,000+` / `square feet of gaming.`

| Element | Value |
|---|---|
| Scrim | `#0A161C`, alpha 0.00 @ `y=430` → 0.62 @ `y=1080`, eased; horizontal falloff 1.00 to `x=980` → 0.35 at `x=1920`; full-bleed, no edges |
| Line 2 — `square feet of gaming.` | SpaceGrotesk-Medium `40`, `+0.02em`, `#F5F8FA` @ 80%, left `x=160`, **baseline `y=920`** |
| Line 1 — `100,000+` | SpaceGrotesk-SemiBold `128`, `-0.03em`, `#F5F8FA` @ 100%, left `x=160`, baseline `y=867` (cap-top ≈ `y=775`) |
| Mint rule | `#68E3BE`, `x = 160→216`, `y = 744→747` |
| Shadow | both lines: `#0A161C` @ 50%, offset `(0,3)`, blur `22` |
| Block extent | `y ≈ 744–920`, left-anchored at `x=160`; right two-thirds of frame unobstructed above `y=430` |

Baselines are derived from the anchor: last baseline `y=920`, everything stacks up. If a renderer's cap-height metrics differ slightly from the estimates above, **hold `y=920` and the `160` left margin** and let the top of the block float — the anchor is the lock, the cap-top numbers are arithmetic.

---

## 6. How this stays clear of Jane's title

The title slide keeps its own treatment untouched. The body system differs on five axes at once, so there is no ambiguity about which is the display moment:

| | Jane's title (`c00`) | Body cards |
|---|---|---|
| Family | Syncopate | Space Grotesk |
| Case | ALL CAPS | sentence case as written |
| Color | mint type | off-white type; mint only as a 3px rule |
| Alignment | centered | left-anchored at `x=160` |
| Position | optical center | bottom-left, baseline `y=920` |

Shared, deliberately: the navy-deep value and mint as the accent. That is brand continuity, not competition. **Nothing after the title slide is ever centered over footage, and nothing after it sets type in mint.** The title remains the only display moment in the cut.

---

## 7. Do not — explicitly against the rejected pass

- **No pill, no rounded rectangle, no card, no capsule** behind text. No `border-radius` of any kind. If it has a corner, it's wrong.
- **No blurred-edge scrim shape.** The gaussian-blurred halo in `build_previews.py` (`soft_dark_backing`) is retired for body cards — replace it with the §3 gradient. Do not reuse that function.
- **No backing that hugs the text.** The scrim is full-bleed and shapeless; its size never depends on the length of the string.
- **No centered body text.** Ever, over footage.
- **No single flat size for all cards** — a scope stat and a sentence must not render identically.
- **No pure white**, no mint type, no gold anywhere in these cards.
- **No outline, stroke, or hard drop shadow** on type. Soft shadow only, per §3.
- **No copy changes** — no rewording, no dropped periods, no added punctuation, no uppercasing.
- **No per-shot repositioning.** The anchor is fixed. Shots are adapted to with scrim alpha, not with new positions.
- **No animated text** — no typewriter, no slide-in, no letter reveal. If the overlay fades, plain cross-dissolve, 8 frames (`0.33s`) in and out.

---

## 8. Pre-ship check

1. Left margin `160` and last baseline `y=920` on every card (variant E excepted).
2. Correct variant per the §4 test; c16 is M, c02 and c12 are S.
3. Copy byte-identical to `titles.md`, including periods.
4. Only Medium and SemiBold used; no faux weights.
5. Type off-white; mint appears only as the `56 × 3` rule.
6. Scrim is a gradient with no visible edge; peak alpha within `0.40–0.68`.
7. Max 2 lines (3 for M); no orphans; numbers unbroken from their units.
8. Nothing centered over footage; no rounded geometry anywhere.
9. Everything inside the 5% title-safe area (`x ≥ 96`, `y ≤ 984`).

---

## 9. Out of scope / open

- **`c00` and `c01`** — the opening title slide is Jane's. Not redesigned here. `c01` ("A sportsbook renovation with LUCI Systems", role `title2`) sits on the same shot as `c00` and reads as part of that slide, so this lock deliberately leaves it alone. If Jane wants `c01` pulled into the body system instead, it becomes a one-line variant N and that needs her call.
- **Per-shot scrim alpha** for c03–c19 — set during render against each frame, within the `0.40–0.68` band.
