# Card 01 — "With 100,000+ square feet of gaming," — one-off card

**Rendered:** 11 Sep 2026 · GLM · per `../BODY-TREATMENT-LOCK.md` rev 2 (S-class plate geometry)
**Revised:** 11 Sep 2026 · GLM · Jane's two visual tweaks (see "Jane's rev (this card)" below).

This is a **one-off card** — not part of the c02–c19 sequence in `../titles.md`. It lives in `cards/`, separate from `previews/` which holds the c02 series. Jane asked for this single card with new copy and a type adjustment, then locked two further visual tweaks for this card only.

## Files

| File | What it is |
|---|---|
| `card-01-with-100k-transparent.png` | Transparent 1920×1080 overlay — bed + plate + two-line lockup (**no mint rule**; numeral in mint) |
| `card-01-with-100k-preview.jpg` | Same overlay composited over a frame from `../../timeline/002-s02-Casino 1-gaming-100k.mp4` (~2.0s) |

## Copy (verbatim — Jane's new line)

`With 100,000+ square feet of gaming,`

Trailing comma preserved. Word order preserved. Not in `titles.md` — this is Jane's new line for this card only.

## Jane's rev (this card — 11 Sep)

Two visual tweaks Jane locked for this card only:

1. **Remove the green mint rule** (the 56×3 line). She finds it weird on this card.
2. **Set `100,000+` in LUCI mint `#68E3BE`** (bright mint on the dark plate — correct for dark plate; passes contrast).
3. `With` and `square feet of gaming,` stay **off-white Medium 52 @ 95%** — readable, unchanged from the prior render.

### Per-card override of BODY-TREATMENT-LOCK.md (NOT a house-rule change)

This card overrides two clauses in `../BODY-TREATMENT-LOCK.md` **for this card only**:

- §2: *"Type is off-white, never mint. Mint type belongs to Jane's title. Body cards get mint only as the 3px rule."*
- §6: *"Nothing after the title slide sets type in mint."*

On this card, **mint goes on the numeral and there is no rule**. The lock still governs every other body card (c02–c19) unchanged — mint as type is not promoted to a house rule. Only Jane can promote a preference to a universal rule (per the learned-preferences rule, 11 Sep).

## Type spec

| Element | Font | Size | Tracking | Color / opacity | Baseline |
|---|---|---|---|---|---|
| `With` (line 1, lead-in) | SpaceGrotesk-Medium | 52 | +0.01em | off-white 95% | y=868 |
| `100,000+` (line 1, numeral) | SpaceGrotesk-SemiBold | 128 | -0.03em | **mint `#68E3BE` 100%** | y=868 (shared) |
| `square feet of gaming,` (line 2) | SpaceGrotesk-Medium | 52 | +0.01em | off-white 95% | y=920 (anchor) |

**Layout:** two lines. Line 1 mixes `With` (Medium 52) + `100,000+` (SemiBold 128, mint) on a shared baseline — the small lead-in sits at the bottom of the numeral's height, a standard editorial pattern. Line 2 is the qualifier on the anchor baseline.

**Hierarchy:** numeral 128px vs surrounding text 52px = 2.46× font-size ratio (cap-height ~92px vs ~37px = 2.49×). Clearly larger; surrounding words clearly readable. The mint color adds a second emphasis axis on top of the scale.

## Plate / bed spec (from BODY-TREATMENT-LOCK.md rev 2 — S-class, unchanged)

| Element | Spec |
|---|---|
| Bed (layer 1) | `#0A161C`, alpha 0.00 @ y=380 → 0.45 @ y=1080, quadratic ease; horizontal falloff 1.00 → 0.30 at x=1920; full-bleed, no edges |
| Plate (layer 2) | `#0A161C` @ 0.62; y=680→1080, x=0→1536; bleeds left + bottom; top edge hard at y=680, radius 0, 8px feather; full density to x=1024, quadratic ease to 0.00 at x=1536 |
| ~~Mint rule~~ | **Removed on this card** (Jane's rev). Plate top edge stays at y=680; the headroom above the numeral now reads as margin, which is correct per lock §3.3. |
| Shadow | `#0A161C` @ 50%, offset (0,3), blur 22 — soft, no stroke |
| Anchor | left x=160, last baseline y=920 |
| Measure | 864 (right edge x=1024) — line 1 right edge x=860, line 2 right edge x=744, both inside |
| Composite order | footage → bed → plate → type (with shadow) — **mint rule step removed** |

## Verification (mechanical — 11 Sep rev)

- Both files 1920×1080 (transparent RGBA / preview RGB) ✓
- **Mint rule region (x=160–216, y=747–750): 0 mint pixels** — rule is gone ✓
- **Numeral `100,000+` is mint `#68E3BE`**: 14,016 mint px / 0 off-white px in numeral zone ✓
- `With` is off-white (1,328 off-white px / 0 mint px) ✓
- `square feet of gaming,` is off-white (5,046 off-white px / 0 mint px) ✓
- Mint confined to numeral bbox only (x=303–873, y=777–873) — no stray mint anywhere else in the overlay ✓
- Top-right corner max alpha = 0 (transparent, open frame, iMovie-ready) ✓
- Plate-zone mean alpha: ~0.737 (within 0.50–0.74 band) ✓
- Numeral cap-height 92px vs qualifier cap-height 37px = 2.49× (clearly larger) ✓
- Both lines inside measure 864 (right edges 860 and 744) ✓
- No pill, no radius, no centered text, no second ornament ✓

## Build script

`../build_card_01_with_100k.py` — re-runnable. Does not touch `build_backed_c02.py`, `build_previews.py`, `build_revised_c02.py`, source media, `titles.md`, Jane's title (`c00`/`c01`), or the `previews/` folder.
