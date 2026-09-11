# Card 02 — "Across more than 40 acres" — one-off card

**Rendered:** 11 Sep 2026 · GLM · per `../BODY-TREATMENT-LOCK.md` rev 2 (N-class plate geometry)

This is a **one-off card** — not part of the c02–c19 sequence in `../titles.md`. It lives in `cards/`, separate from `previews/` which holds the c02 series. Jane asked for this single card with her own line (no period).

## Files

| File | What it is |
|---|---|
| `card-02-across-40-acres-transparent.png` | Transparent 1920×1080 overlay — bed + plate + single-line narrative (**no mint rule**; all text off-white Medium) |
| `card-02-across-40-acres-preview.jpg` | Same overlay composited over a frame from `../../timeline/003-s03-Casino 3-gaming-acres.mp4` (~2.0s) |

## Copy (verbatim — Jane's line; no period)

`Across more than 40 acres`

No trailing period. Word order preserved. Not in `titles.md` — this is Jane's new line for this card only. (The `titles.md` c03 string `Across more than 40 acres.` has a period; this one-off card does not.)

## Per-card override of BODY-TREATMENT-LOCK.md (NOT a house-rule change)

This card overrides one clause in `../BODY-TREATMENT-LOCK.md` **for this card only**:

- §3.1 / §1 / §7: the 56×3 mint rule is **removed**. Jane removed it on card 01 — looked weird; do not bring it back. The plate top edge stays at the N-class `y=728`; the headroom above the text reads as margin, which is correct per lock §3.3.

No mint type appears on this card — consistent with lock §2 ("Type is off-white, never mint. Body cards get mint only as the 3px rule"). Since the rule is removed and there is no display-numeral ask, all words are off-white Medium, including `40`.

The lock still governs every other body card (c02–c19) unchanged — the no-rule override is not promoted to a house rule. Only Jane can promote a preference to a universal rule (per the learned-preferences rule, 11 Sep).

## Type spec

| Element | Font | Size | Tracking | Color / opacity | Baseline |
|---|---|---|---|---|---|
| `Across more than 40 acres` (single line) | SpaceGrotesk-Medium | 52 | +0.01em | off-white `#F5F8FA` 100% | y=920 (anchor) |

**Layout:** one calm line. The string measures 684px at Medium 52 (+0.01em), right edge `x=844` — well inside the 864 measure (limit `x=1024`). No second line needed.

**Size choice:** 52px sits inside the brief's ~48–56 range and matches card 01's body-text size (52) for consistency across the one-off cards in `cards/`. The lock's N-variant default is 48; the brief authorized the range and emphasized readability.

## Plate / bed spec (from BODY-TREATMENT-LOCK.md rev 2 — N-class)

| Element | Spec |
|---|---|
| Bed (layer 1) | `#0A161C`, alpha 0.00 @ y=380 → 0.45 @ y=1080, quadratic ease; horizontal falloff 1.00 → 0.30 at x=1920; full-bleed, no edges |
| Plate (layer 2) | `#0A161C` @ 0.62; y=728→1080, x=0→1536; bleeds left + bottom; top edge hard at y=728, radius 0, 8px feather; full density to x=1024, quadratic ease to 0.00 at x=1536 |
| ~~Mint rule~~ | **Removed on this card** (per-card override). Plate top edge stays at y=728; headroom reads as margin. |
| Shadow | `#0A161C` @ 50%, offset (0,3), blur 22 — soft, no stroke |
| Anchor | left x=160, last baseline y=920 |
| Measure | 864 (right edge x=1024) — line right edge x=844, inside |
| Composite order | footage → bed → plate → type (with shadow) — **mint rule step removed** |

## Verification (mechanical — 11 Sep)

- Both files 1920×1080 (transparent RGBA / preview RGB) ✓
- **Mint rule region (x=160–216, y=791–794): 0 mint pixels** — rule is gone ✓
- **Tight mint check (within 30 of #68E3BE): 0 px anywhere in overlay** — no mint type, no mint rule ✓
- Text is off-white: 6,026 pure off-white px in type zone; bright text avg RGB (219,223,225) — off-white, not mint ✓
- Top-right corner max alpha = 0 (transparent, open frame, iMovie-ready) ✓
- Plate-zone mean alpha: ~0.725 (within 0.62–0.80 target) ✓
- Plate top edge steps up at y=728 (N-class): 0.106 @ y=724 → 0.384 @ y=728 → 0.663 @ y=732 ✓
- Left bleed (y900–1080, x0–4) mean alpha 0.750; bottom bleed 0.787 — plate bleeds off left + bottom ✓
- Single line, right edge x=844, inside measure 864 ✓
- No pill, no radius, no centered text, no second ornament ✓
- Copy byte-identical to brief: `Across more than 40 acres` (no period) ✓

## Build script

`../build_card_02_across_40_acres.py` — re-runnable. Does not touch `build_card_01_with_100k.py`, `build_backed_c02.py`, `build_previews.py`, `build_revised_c02.py`, source media, `titles.md`, Jane's title (`c00`/`c01`), or the `previews/` folder.
