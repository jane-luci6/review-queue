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
