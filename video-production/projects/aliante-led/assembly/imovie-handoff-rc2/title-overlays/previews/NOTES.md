# Title-overlay previews — Aliante RC2 iMovie handoff

Two preview treatments for Jane's visual approval before any full overlay set.
Rendered 11 Sep 2026 from `../titles.md` (copy verbatim).

## Files in this folder

| File | What it is |
|---|---|
| `01-main-title-c00-transparent.png` | Transparent 1920×1080 overlay — main title (c00) |
| `01-main-title-c00-preview.jpg` | Same overlay composited over a frame from timeline clip `001-s01-…` |
| `02-space-grotesk-c02-transparent.png` | Transparent 1920×1080 overlay — first body card (c02) |
| `02-space-grotesk-c02-preview.jpg` | Same overlay composited over a frame from timeline clip `002-s02-…` |

## Copy used (verbatim from `titles.md`)

- **c00** — source string `Aliante Casino + Hotel` → rendered **ALL CAPS** as `ALIANTE CASINO + HOTEL`
- **c02** — `100,000+ square feet of gaming.` (exact string, sentence case)

## Type & placement choices

### 01 — Main title (c00), the one display moment
- **Font:** Syncopate Bold, 72px
- **Case:** ALL CAPS (per Jane's locked rule for this beat)
- **Color:** LUCI mint `#68E3BE` — primary accent on dark for the display moment
- **Placement:** centered horizontally and vertically on screen
- **Backing:** soft translucent dark pill (`#0A161C` ~140α), rounded rectangle with gaussian-blurred edges — a cinematic scrim, not a hard caption box

### 02 — Body card (c02), first regular Space Grotesk treatment
- **Font:** Space Grotesk SemiBold, 42px
- **Case:** sentence case (copy verbatim)
- **Color:** white `#FFFFFF`
- **Placement:** lower-third, centered horizontally, ~160px up from bottom
- **Backing:** same soft translucent dark pill treatment as the title — consistent across the system

## Composite frames

- `01-…-preview.jpg` — frame grabbed at ~2.5s into `001-s01-Casino 2-title-open-casino.mp4` (title window in the cut is ~1.5–4.0s, which maps to clip 001)
- `02-…-preview.jpg` — frame grabbed at ~2.0s into `002-s02-Casino 1-gaming-100k.mp4` (title window in the cut is ~6.3–9.7s; clip 001 is 6.0s, so this maps to ~0.3–3.7s into clip 002)

## Scope

Only these two treatments were rendered. No other overlay cards (c01, c03–c19) were generated.
Source media, the rough cut, and `titles.md` were not modified.

## Build script

`../build_previews.py` — re-runnable; reads `titles.md` copy via the constants in the script and the LUCI brand fonts from `LUCI Systems Design System/assets/fonts/`.

---

## Revised c02 — de-boxed body overlay (11 Sep 2026)

The `02-space-grotesk-c02-*` files above are the **rejected** first pass (centered
white SemiBold in a rounded translucent pill). They are kept for comparison only.

The **revised** c02 implements `../BODY-TREATMENT-LOCK.md` (Claude
`design-direction-open` lock, 11 Sep) — a left-anchored editorial block with no
box, no pill, no radius. Legibility comes from a shapeless full-bleed gradient
scrim, not a container.

| File | What it is |
|---|---|
| `03-body-c02-revised-transparent.png` | Transparent 1920×1080 overlay — scrim + mint rule + two-line stat lockup |
| `03-body-c02-revised-preview.jpg` | Same overlay composited over a frame from timeline clip `002-s02-…` |

### Spec (from BODY-TREATMENT-LOCK.md §3 + §5 worked example)

- **Variant S** (stat lockup): numeral SemiBold 128 / qualifier Medium 40 @ 80%
- **Copy verbatim:** `100,000+ square feet of gaming.` → break `100,000+` / `square feet of gaming.`
- **Anchor:** left `x=160`; last baseline `y=920` (line 2); line 1 baseline `y=867`
- **Mint rule:** 56×3 at `x=160→216`, `y=744→747` — the only graphic element
- **Scrim:** `#0A161C`, alpha 0.00 @ `y=430` → 0.62 @ `y=1080`, quadratic ease; horizontal falloff 1.00 → 0.35 at `x=1920`; full-bleed, no edges
- **Shadow:** `#0A161C` @ 50%, offset `(0,3)`, blur `22` — soft, no stroke
- **Fonts:** `SpaceGrotesk-SemiBold.ttf` + `SpaceGrotesk-Medium.ttf` only (no faux weights)
- **No pill, no radius, no centered text, no `soft_dark_backing`**

### Build script

`../build_revised_c02.py` — re-runnable; does not touch `build_previews.py`,
source media, `titles.md`, or the rejected preview files.

---

## Rev 2 backed c02 — corner plate + bed (11 Sep 2026)

The `03-body-c02-revised-*` files above are the **rev 1** pass (gradient-only
scrim). Over the c02 frame — a lit ceiling, a purple carpet field, and a
fully illuminated slot sign behind the numeral — a 0.62 bottom gradient
barely registers and the mint rule vanishes. Rev 2 adds the **corner plate**.

The `04-body-c02-backed-*` files implement `../BODY-TREATMENT-LOCK.md` **rev 2**
(Jane approved, 11 Sep) — a two-layer build: a full-bleed gradient **bed**
(layer 1) plus a hard-edged bottom-left corner **plate** (layer 2). The plate
bleeds off the left and bottom frame edges, draws exactly one edge (the top),
and dissolves to the right. It is a plane in the frame's architecture, not a
box around the text.

| File | What it is |
|---|---|
| `04-body-c02-backed-transparent.png` | Transparent 1920×1080 overlay — bed + plate + mint rule + two-line stat lockup |
| `04-body-c02-backed-preview.jpg` | Same overlay composited over a frame from timeline clip `002-s02-…` |

### Spec (from BODY-TREATMENT-LOCK.md rev 2 — §3.2 bed, §3.3 plate, §5 worked example)

- **Variant S** (stat lockup): numeral SemiBold 128 / qualifier Medium 40 @ 80%
- **Copy verbatim:** `100,000+ square feet of gaming.` → break `100,000+` / `square feet of gaming.`
- **Anchor:** left `x=160`; last baseline `y=920` (line 2); line 1 baseline `y=868`
- **Mint rule:** 56×3 at `x=160→216`, `y=747→750` — the only graphic element
- **Bed (layer 1):** `#0A161C`, alpha 0.00 @ `y=380` → 0.45 @ `y=1080`, quadratic ease; horizontal falloff 1.00 → 0.30 at `x=1920`; full-bleed, no edges
- **Plate (layer 2):** `#0A161C` @ `0.62`; `y=680→1080`, `x=0→1536`; bleeds left and bottom; top edge hard at `y=680`, radius 0, 8px feather; full density to `x=1024`, quadratic ease to 0.00 at `x=1536`
- **Measure:** 864 (right edge `x=1024`) — rev 2 tightening
- **Shadow:** `#0A161C` @ 50%, offset `(0,3)`, blur `22` — soft, no stroke
- **Composite order:** footage → bed → plate → mint rule → type (with shadow)
- **Fonts:** `SpaceGrotesk-SemiBold.ttf` + `SpaceGrotesk-Medium.ttf` only (no faux weights)
- **No pill, no radius, no centered text, no `soft_dark_backing`, no second ornament, no plate without the bed**

### Verification (mechanical, against §8 pre-ship checklist)

- Both files 1920×1080 (transparent RGBA / preview RGB)
- Effective alpha behind type block: ~0.80 (within 0.62–0.80 target)
- Plate-zone mean alpha 04 (bed+plate) ~0.74 vs 03 (bed only) ~0.39 — plate clearly denser
- Plate top edge hard at `y=680` with 8px feather; full density to `x=1024`, dissolved by `x=1536`
- Mint rule present, mint-colored, legible on the plate
- Bed present under the plate (grade, not the legibility device)
- Left + bottom bleed off frame; top-right corner carries bed grade only
- Type off-white; left-anchored at `x=160` (not centered)

### Build script

`../build_backed_c02.py` — re-runnable; supersedes `build_revised_c02.py` for
the rev 2 output. Does not touch `build_previews.py`, `build_revised_c02.py`,
source media, `titles.md`, Jane's title (`c00`/`c01`), or the prior preview files.
