# Card 02 — "Across more than 40 acres" — one-off card

**Rendered:** 11 Sep 2026 · GLM · per `../BODY-TREATMENT-LOCK.md` rev 2 (N-class plate geometry)
**Revised:** 11 Sep 2026 · GLM · Jane's highlight revise — `40 acres` in mint display scale matching card 01's `100,000+` pattern (see "Jane's rev (this card)" below).

This is a **one-off card** — not part of the c02–c19 sequence in `../titles.md`. It lives in `cards/`, separate from `previews/` which holds the c02 series. Jane asked for this single card with her own line (no period), then locked a highlight treatment matching card 01.

## Files

| File | What it is |
|---|---|
| `card-02-across-40-acres-transparent.png` | Transparent 1920×1080 overlay — bed + plate + two-line lockup (**no mint rule**; lead-in off-white Medium, `40 acres` mint SemiBold 128) |
| `card-02-across-40-acres-preview.jpg` | Same overlay composited over a frame from `../../timeline/003-s03-Casino 3-gaming-acres.mp4` (~2.0s) |

## Copy (verbatim — Jane's line; no period)

`Across more than 40 acres`

No trailing period. Word order preserved. Not in `titles.md` — this is Jane's new line for this card only. (The `titles.md` c03 string `Across more than 40 acres.` has a period; this one-off card does not.)

## Jane's rev (this card — 11 Sep)

Jane locked a highlight treatment for this card matching card 01's numeral pattern:

1. **`40 acres` in LUCI mint `#68E3BE`** — SpaceGrotesk-SemiBold, display scale 128px (same size and color as card 01's `100,000+`).
2. **`Across more than` stays off-white Medium 52 @ 95%** — readable lead-in, same hierarchy as `With` on card 01.
3. **No mint rule** — Jane removed it on card 01; do not bring it back.
4. **Keep plate + bed (rev 2), left-anchored.**

### Layout — two lines (shared baseline exceeded measure)

The brief's preferred layout was a shared baseline (`Across more than` + `40 acres` on one line). At 128px the combined width is 982px — exceeds the 864 measure (right x=1142, limit 1024). Per the brief's "break cleanly if measure needs it" fallback, the card breaks to two lines:

- **Line 1:** `Across more than` — Medium 52, off-white 95%, baseline y=800
- **Line 2:** `40 acres` — SemiBold 128, mint 100%, baseline y=920 (anchor)

Word order preserved; `40` stays with `acres` on one line (never split). The numeral sits on the anchor at the same 128px display scale as card 01's `100,000+`, in the same mint. A 30px gap separates line 1's baseline from the numeral's cap-top (y=830). S-class plate (top y=680) matches card 01's geometry for consistency across the two one-off cards.

### Per-card override of BODY-TREATMENT-LOCK.md (NOT a house-rule change)

This card overrides three clauses in `../BODY-TREATMENT-LOCK.md` **for this card only**:

- §2: *"Type is off-white, never mint. Mint type belongs to Jane's title. Body cards get mint only as the 3px rule."* — mint goes on `40 acres` here.
- §3.1 / §1 / §7: the 56×3 mint rule is **removed**. Jane removed it on card 01; do not bring it back. The plate top edge stays at y=680 (S-class); headroom reads as margin.
- §6: *"Nothing after the title slide sets type in mint."* — mint type appears on this card.

The lock still governs every other body card (c02–c19) unchanged — mint as type is not promoted to a house rule. Only Jane can promote a preference to a universal rule (per the learned-preferences rule, 11 Sep).

## Type spec

| Element | Font | Size | Tracking | Color / opacity | Baseline |
|---|---|---|---|---|---|
| `Across more than` (line 1, lead-in) | SpaceGrotesk-Medium | 52 | +0.01em | off-white `#F5F8FA` 95% | y=800 |
| `40 acres` (line 2, highlight) | SpaceGrotesk-SemiBold | 128 | -0.03em | **mint `#68E3BE` 100%** | y=920 (anchor) |

**Hierarchy:** numeral 128px vs lead-in 52px = 2.46× font-size ratio (cap-height 91px vs 35px = 2.60×). Same scale ratio as card 01 (2.46× font-size, 2.49× cap-height). The mint color adds a second emphasis axis on top of the scale, matching card 01 exactly.

## Plate / bed spec (from BODY-TREATMENT-LOCK.md rev 2 — S-class, matching card 01)

| Element | Spec |
|---|---|
| Bed (layer 1) | `#0A161C`, alpha 0.00 @ y=380 → 0.45 @ y=1080, quadratic ease; horizontal falloff 1.00 → 0.30 at x=1920; full-bleed, no edges |
| Plate (layer 2) | `#0A161C` @ 0.62; y=680→1080, x=0→1536; bleeds left + bottom; top edge hard at y=680, radius 0, 8px feather; full density to x=1024, quadratic ease to 0.00 at x=1536 |
| ~~Mint rule~~ | **Removed on this card** (per-card override). Plate top edge stays at y=680; headroom reads as margin. |
| Shadow | `#0A161C` @ 50%, offset (0,3), blur 22 — soft, no stroke |
| Anchor | left x=160, last baseline y=920 |
| Measure | 864 (right edge x=1024) — line 1 right edge x=609, line 2 right edge x=670, both inside |
| Composite order | footage → bed → plate → type (with shadow) — **mint rule step removed** |

## Verification (mechanical — 11 Sep rev)

- Both files 1920×1080 (transparent RGBA / preview RGB) ✓
- **Mint rule region (x=160–216, y=788–797): 0 mint px** — rule is gone ✓
- **`40 acres` is mint `#68E3BE`**: 15,740 mint px in highlight zone; 0 stray mint outside bbox (x=164–690, y=829–920) ✓
- `Across more than` is off-white (4,005 off-white px, bbox x=162–596, y=764–799) ✓
- Mint (line 2) below off-white (line 1): mint y-min 829 > off-white y-min 764 ✓
- Top-right corner max alpha = 0 (transparent, open frame, iMovie-ready) ✓
- Plate-zone mean alpha: ~0.760 (within 0.62–0.80 target) ✓
- Plate top edge steps up at y=680 (S-class): 0.078 @ y=676 → 0.365 @ y=680 → 0.651 @ y=684 ✓
- Both lines inside measure 864 (right edges 609 and 670, limit 1024) ✓
- Font-size ratio 128/52 = 2.46× (matches card 01 exactly) ✓
- Numeral cap-height 91px vs lead-in cap-height 35px = 2.60× (clearly larger) ✓
- Copy byte-identical to brief: `Across more than 40 acres` (no period) ✓
- No pill, no radius, no centered text, no second ornament ✓

## Build script

`../build_card_02_across_40_acres.py` — re-runnable. Does not touch `build_card_01_with_100k.py`, `build_backed_c02.py`, `build_previews.py`, `build_revised_c02.py`, source media, `titles.md`, Jane's title (`c00`/`c01`), or the `previews/` folder.
