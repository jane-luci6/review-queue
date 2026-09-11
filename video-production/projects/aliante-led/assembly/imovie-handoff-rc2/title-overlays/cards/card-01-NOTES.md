# Card 01 — "With 100,000+ square feet of gaming," — one-off card

**Rendered:** 11 Sep 2026 · GLM · per `../BODY-TREATMENT-LOCK.md` rev 2 (S-class plate geometry)

This is a **one-off card** — not part of the c02–c19 sequence in `../titles.md`. It lives in `cards/`, separate from `previews/` which holds the c02 series. Jane asked for this single card with new copy and a type adjustment.

## Files

| File | What it is |
|---|---|
| `card-01-with-100k-transparent.png` | Transparent 1920×1080 overlay — bed + plate + mint rule + two-line lockup |
| `card-01-with-100k-preview.jpg` | Same overlay composited over a frame from `../../timeline/002-s02-Casino 1-gaming-100k.mp4` (~2.0s) |

## Copy (verbatim — Jane's new line)

`With 100,000+ square feet of gaming,`

Trailing comma preserved. Word order preserved. Not in `titles.md` — this is Jane's new line for this card only.

## Type spec (Jane's note for THIS card — overrides old S qualifier)

Jane's directive: `100,000+` must be **larger** (display emphasis, SemiBold, same scale spirit as the approved S numeral). The rest must be **readable** — not the old 40px @ 80% whisper. Medium ~48–56, ~90–100% opacity.

| Element | Font | Size | Tracking | Color / opacity | Baseline |
|---|---|---|---|---|---|
| `With` (line 1, lead-in) | SpaceGrotesk-Medium | 52 | +0.01em | off-white 95% | y=868 |
| `100,000+` (line 1, numeral) | SpaceGrotesk-SemiBold | 128 | -0.03em | off-white 100% | y=868 (shared) |
| `square feet of gaming,` (line 2) | SpaceGrotesk-Medium | 52 | +0.01em | off-white 95% | y=920 (anchor) |

**Layout:** two lines. Line 1 mixes `With` (Medium 52) + `100,000+` (SemiBold 128) on a shared baseline — the small lead-in sits at the bottom of the numeral's height, a standard editorial pattern. Line 2 is the qualifier on the anchor baseline.

**Hierarchy:** numeral 128px vs surrounding text 52px = 2.46× font-size ratio (cap-height ~92px vs ~37px = 2.49×). Clearly larger; surrounding words clearly readable.

## Plate / bed spec (from BODY-TREATMENT-LOCK.md rev 2 — S-class)

| Element | Spec |
|---|---|
| Bed (layer 1) | `#0A161C`, alpha 0.00 @ y=380 → 0.45 @ y=1080, quadratic ease; horizontal falloff 1.00 → 0.30 at x=1920; full-bleed, no edges |
| Plate (layer 2) | `#0A161C` @ 0.62; y=680→1080, x=0→1536; bleeds left + bottom; top edge hard at y=680, radius 0, 8px feather; full density to x=1024, quadratic ease to 0.00 at x=1536 |
| Mint rule | `#68E3BE`, 56×3, x=160→216, y=747→750 — the only graphic element |
| Shadow | `#0A161C` @ 50%, offset (0,3), blur 22 — soft, no stroke |
| Anchor | left x=160, last baseline y=920 |
| Measure | 864 (right edge x=1024) — line 1 right edge x=860, line 2 right edge x=744, both inside |
| Composite order | footage → bed → plate → mint rule → type (with shadow) |

## Verification (mechanical)

- Both files 1920×1080 (transparent RGBA / preview RGB) ✓
- Mint rule: R=104 G=227 B=190 A=255 (mint, fully opaque) ✓
- Plate-zone mean alpha: 0.737 (within 0.50–0.74 band) ✓
- Effective alpha behind type block: 0.800 (at top of 0.62–0.80 target) ✓
- Top-right corner: 0.000 (transparent, open frame) ✓
- Numeral cap-height 92px vs qualifier cap-height 37px = 2.49× (clearly larger) ✓
- Both lines inside measure 864 (right edges 860 and 744) ✓
- No pill, no radius, no centered text, no second ornament ✓

## Build script

`../build_card_01_with_100k.py` — re-runnable. Does not touch `build_backed_c02.py`, `build_previews.py`, `build_revised_c02.py`, source media, `titles.md`, Jane's title (`c00`/`c01`), or the `previews/` folder.
