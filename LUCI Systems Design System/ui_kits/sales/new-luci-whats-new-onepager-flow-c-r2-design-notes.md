# New LUCI What's New one-pager — Flow C R2 · design notes (e-mesh pass)

**Built:** 17 September 2026 · GLM · rebuild per `CURSOR-BRIEF-new-luci-whats-new-flow-c-r2-glm-emesh.md`.
**Design lock:** `new-luci-whats-new-onepager-flow-c-r2-opus-visual-plan.md` (Opus visual plan — eye path, hierarchy, e-mesh, ledger craft).
**Copy lock:** `new-luci-whats-new-onepager-flow-c-r2-copy.md`. **No copy was rewritten.** No teaser was dropped.

## Jane rejection fixed

Prior pass used **circuit textures** (`texture-circuit-header-mintgold.png`, `texture-circuit-navy-mint.png`, `band-circuit-baked.jpg`, `texture-3.png` smoke base). Jane rejected the circuit read. **All circuit textures removed** — grepped the file: zero matches for `circuit`, `band-circuit`, or `texture-3`. The masthead and footer now use **e-mesh only**.

## E-mesh integration (per Opus plan §3)

- **Masthead:** `assets/textures/luci-e-mesh-header-transparent.svg` as a real `<img>` (`.mast__mesh`), `position:absolute; object-fit:cover; object-position:right center`, right-pinned at 62% width, opacity 0.5. A left-to-right scrim (`linear-gradient(90deg, navy-deep 0% → 0.92α at 46% → transparent at 78%)`) mutes the mesh behind the headline and subhead. The existing `.mast__glow` mint radial stays as warm-up at top-left. Mint 4px bottom rule retained.
- **Footer:** same e-mesh file (`.foot__mesh`), right-pinned at 55% width, **opacity 0.22** — the masthead's echo, not a second event. Scrim from the left.
- **White middle: no texture.** The ledger is the reading zone — cleanest canvas on the sheet.
- **Print stability:** mesh ships as real `<img>` elements (not CSS `background-image`) with `print-color-adjust:exact` on `.mast`, `.foot`, and the mesh layers. Chrome print-to-pdf renders the `<img>` correctly. `@media print` falls back to solid `--navy-deep` if the image drops.
- **Fallback asset** (not used this pass): `assets/textures/luci-bg-hero-mesh-lines-1920x1080.svg` — available if the header variant reads too dense at letter scale.

## Hierarchy — eye path applied (per Opus plan §1–§2)

**Dominant (one tier):**
- **Theme headline** — Space Grotesk 700, 32px, line-height 1.08, tracking −0.025em, off-white with **`--gold` `<em>`** on "programming." The single point of color contrast in the top field — eye lands mid-headline, not at the top-left corner. (Changed from `--mint` to `--gold` per Opus plan; gold on dark navy passes contrast.)
- **Date** — Space Grotesk 700, 13px, tracked 0.18em uppercase, `--mint`, **right-aligned** with a short mint hairline (120×1px) above it. Second stop on the eye path — catches on the way out of the headline. Moved out of paragraph flow; no longer trailing the subhead.

**Structural (second tier, equal):**
- **Promise headers** (`.row__name`) — Space Grotesk 700, 16px, `--ink-strong`, tracking −0.01em. All three identical weight; row 03's extra feature does not make its header heavier.
- **Numerals** (`.ledger__num`) — Space Grotesk 700, 27px, `--accent-light` `#2b9e80`. Stacked above the promise header with 6px gap (not inline). Sized to build the spine but kept **below** the promise header in visual weight by using the accent color rather than ink. (Changed from Syncopate 13px to Space Grotesk 27px per Opus plan.)
- **Middle title** — Space Grotesk 700, 17px, ink, over 40×3px mint rule. Label, not headline. Reduced from 20px so it doesn't approach the masthead headline's scale.

**Recede (third tier):**
- **Announcement** (`.mast__announce`) — 10px Space Grotesk, tracked 0.20em uppercase, `--mint`. Kicker above the headline.
- **Subhead** — Inter 400, 12.5px, line-height 1.55, `rgba(235,245,248,0.80)`, max 58ch. Sits below the date; read on the rebound.
- **Promise leads** (`.row__benefit`) — Inter 400, 11.5px, `--navy-muted`, max 30ch. Left column stays a column.
- **Feature names** — Inter 600, 11.5px, `--ink-strong`. **Feature teasers** — Inter 400, 11px, `--navy-muted`. Weight step is the only separation; no color accent on either. (Changed feature names from Space Grotesk 700 to Inter 600 per Opus plan.)
- **Close + footer** — Inter, 10.5–11.5px. `[UPGRADE GUIDE URL]` in `#2b9e80` (link slot), contact lines in muted ink.

## Ledger craft (per Opus plan §4)

- **One shared left edge** for numerals, one for promise headers + leads, one for feature names; teasers right-aligned on the same line as their name. Four vertical lines the eye trusts across all three rows.
- **Separators:** 1px `rgba(53,79,92,0.14)` hairline between ledger rows only (full-bleed). Inside the feature stack, lighter `0.08` alpha hairline between feature lines, none after the last line. No boxes, no cards, no vertical rule between the 30/70 columns — the 28px column gap does that.
- **Row rhythm:** 22px above and below each hairline. Row 03 is taller by one feature line; all three headers retain equal visual weight.
- **Feature lines:** name left, teaser right, baseline-aligned, 6px padding. No dot-leaders, no right-aligned names.
- **Breathing room:** 28px between the promise lead column and the feature column.

## Spacing budget (per Opus plan §2 — masthead ~34%, ledger ~52%, close+footer ~14%)

- Masthead padding: 0.36in top / 0.30in bottom (tightened from 0.42/0.34 to fit the sheet after the position fix).
- Middle padding: 0.32in top / 0.26in bottom.
- Close padding: 0.22in top / 0.18in bottom.
- All gaps on the 8px scale.

## Copy lock — no changes

- Every locked string verbatim (HTML entities for apostrophes/dashes/middots render identically).
- **No micro fit flex was needed** — no hyphens added, no line-break hints, no teaser shortened. Zero copy flags.
- Placeholders retained: `[UPGRADE GUIDE URL]`, `[NAME]`, `[TITLE]`, `[EMAIL]`, `[PHONE]`.
- No invented metrics, no client names.
- No structure changes: no promise index, no upgrade path, no download CTA.

## Print verification (this pass)

- **Headless Chrome `--print-to-pdf`:** 1 page, US Letter (612×792 pts = 8.5×11in), **90 KB** (down from 353 KB — no baked circuit JPG; e-mesh is vector SVG via `<img>`).
- **`fit-check.py`:** natural content height **1009px** vs 1056px target → **−47px** (underfill, no overflow, no clipping). One `.doc-page` detected.
- `@page { size: letter; margin: 0 }`; `.sheet` locked to `8.5in × 11in` with `overflow: hidden`.
- `print-color-adjust: exact` on `.mast`, `.foot`, mesh `<img>` layers, numerals, rules.

## Bug fixed during this pass

Initial rebuild overflowed by +412px because `.mast>*` and `.foot>*` catch-all rules set `position:relative` on ALL children, overriding `position:absolute` on the mesh/scrim/glow layers — the e-mesh `<img>` was in flow and expanded the layout. Fixed by replacing the catch-alls with explicit content-element selectors (`.mast__row`, `.mast__announce`, etc.) so the mesh layers keep `position:absolute`.

## How to open / print

Open in a browser (or Cursor's in-editor preview). Print → Save as PDF: US Letter, margins none, scale 100%, background graphics ON.
