# New LUCI What's New one-pager — Flow C R2 · Opus visual plan

Implementation note for GLM. Copy and structure are locked (`new-luci-whats-new-onepager-flow-c-r2-copy.md`). This note covers **eye path, hierarchy, e-mesh, and ledger craft only**. Target: `new-luci-whats-new-onepager-flow-c.html`, one US Letter sheet.

Fixes Jane's two rejections: **circuit texture → e-mesh**, and **weak hierarchy → a directed read**.

## 1. Eye path (letter leave-behind, held at arm's length)

1. **Theme headline** in the navy masthead — the largest thing on the sheet, and the first thing that resolves at arm's length. The gold `<em>` on "programming" is the single point of color contrast in the top field, so the eye lands mid-headline, not at the top-left corner.
2. **Date** — deliberately the second stop, not the last. Pull it out of the paragraph flow into a right-aligned or hairline-set marker on the masthead baseline so it catches on the way out of the headline.
3. **Announcement + subhead** — read on the rebound, one beat below the headline. They confirm the news; they don't announce it.
4. **"The 3 Promises of New LUCI"** — the handoff from dark to white. The canvas flip does the work; the title just labels the section.
5. **The three numerals 01 / 02 / 03** — a vertical spine down the left 30% that sets the rhythm before any feature text is read. Eye travels down the numbers first, then back up to enter row 01.
6. **Per row: promise header → features.** Left-to-right inside each row, then down to the next numeral. Feature names carry the horizontal scan; teasers are read only on the second pass.
7. **Close block** — URL and contact, last and quietest.
8. **Footer wordmark** — terminal, not a stop.

The two things a reader must retain if they look for three seconds: **the headline and January 19.** Everything else is designed to be found on the second pass.

## 2. Hierarchy — what dominates, what recedes

Dominant (one tier, no competition):
- **Theme headline** — Space Grotesk 700, ~30–34px, line-height 1.08, tracking −0.025em, off-white with a `--gold` `<em>`. This is the only element at this size on the sheet.
- **Date** — Space Grotesk 700, ~13px, tracked ~0.18em uppercase, `--mint`. Small but isolated, so it reads as loud. Give it its own line with a short mint hairline above or a 1px top rule; never trailing the subhead as a sentence.

Structural (second tier, equal to each other):
- **Promise headers** (`.row__name`) — Space Grotesk 700, ~15–16px, `--ink-strong`, tracking −0.01em. All three identical; row 03's extra feature must not make its header feel heavier.
- **Numerals** (`.ledger__num`) — Space Grotesk 700, ~26–28px, `--accent-light` `#2b9e80`. Sized to build the spine but kept **below** the promise header in visual weight by using the accent color rather than ink, so the header still wins the word-level read.
- **Middle title** — Space Grotesk 700, ~16–17px, ink, over the existing 40×3px mint rule. Label, not headline. Do not let it approach the masthead headline's scale.

Recede (third tier):
- **Announcement** (`.mast__announce`) — 10px Space Grotesk, tracked 0.2em uppercase, `--mint`. Kicker weight, sits above the headline.
- **Subhead** — Inter 400, ~12.5px, line-height 1.55, `rgba(235,245,248,0.8)`, capped at ~58ch so it never runs the full masthead width.
- **Promise leads** (`.row__benefit`) — Inter 400, ~11.5px, `--navy-muted`, max ~30ch so the left column stays a column.
- **Feature names** — Inter 600, ~11.5px, ink. **Feature teasers** — Inter 400, ~11px, `--navy-muted`. The weight step between them is the only separation needed; no color accent on either.
- **Close + footer** — Inter, 10–11px. `[UPGRADE GUIDE URL]` in `#2b9e80` so the placeholder reads as a link slot, contact lines in muted ink.

Spacing carries the hierarchy more than size does: **masthead ~34% of the sheet, ledger ~52%, close+footer ~14%.** Gaps on the 8px scale — 32px between masthead and middle title, 24px between ledger rows, 16px above the close rule.

## 3. E-mesh integration

- **Masthead:** `assets/textures/luci-e-mesh-header-transparent.svg` as an `<img>` layer over `--navy-deep`, `object-fit: cover`, pinned right (`object-position: right center`). Right-weighted like `HomeMesh.astro` and the case-study heroes — the mesh is vivid in the right third, and a horizontal scrim `linear-gradient(90deg, var(--navy-deep) 0%, rgba(10,22,28,0.92) 46%, transparent 78%)` mutes it behind the headline and subhead. Mesh at ~0.5 opacity overall; the existing `.mast__glow` mint radial stays as the warm-up at top-left.
- **Footer:** the same file, much quieter — ~0.22 opacity, right-pinned, scrim from the left. It should read as the masthead's echo, not a second event.
- **White middle: no texture at all.** The ledger is the reading zone and needs the cleanest canvas on the sheet. Mesh on light would also force a non-brand tint. The dark/light/dark rhythm (mesh → clean → mesh) is what makes the middle feel intentional.
- **Do not use** `texture-circuit-header-mintgold`, `texture-circuit-navy-mint`, or `band-circuit-baked.jpg`. Remove the `.band-circuit-print` image and both circuit `background-image` rules.
- **Print stability:** Chrome print-to-pdf drops CSS backgrounds unreliably, so the mesh must ship as a real `<img>` element (not a `background-image`) with `print-color-adjust: exact` on `.mast` and `.foot`. The transparent SVG over a solid navy fill prints correctly and stays vector — no raster bake needed. Keep the existing `@media print` navy `!important` fallbacks so a dropped image still prints as solid navy rather than white.
- `luci-bg-hero-mesh-lines-1920x1080.svg` is the fallback if the header variant's density reads too busy at letter scale; it carries its own navy wash, so if you use it, drop the scrim's opaque end.

## 4. Ledger / middle craft

- **Alignment is the whole trick.** One shared left edge for the numerals, one for the promise headers and leads, one for the feature names, one right edge for the teasers. Four vertical lines the eye can trust across all three rows.
- **Separators:** a 1px `rgba(53,79,92,0.14)` hairline **between ledger rows only**, full-bleed across both columns. Inside the feature stack, a lighter hairline (`0.08` alpha) between feature lines, with none after the last line in each row. No boxes, no cards, no vertical rule between the 30/70 columns — the gap does that.
- **Row rhythm:** 24px above and below each hairline. Row 03 is taller by one feature line; absorb that with slightly tighter feature line-height across all rows rather than compressing row 03 alone.
- **Feature lines:** name left, teaser right, both baseline-aligned on one line, ~14–16px line box. Let the gap between them flex; do not dot-leader or right-align the names.
- **Breathing room:** ~28px between the promise lead column and the feature column. If the sheet runs tight, take it from the masthead's bottom padding and the close block — never from the gaps between ledger rows, which is what makes the section read as a ledger instead of a list.
- **Numeral treatment:** number sits above the promise header with ~6px between them, not inline. That stacked start is what turns the left 30% into a spine.

## 5. Hard constraints

- True 8.5×11: `.sheet` stays `816×1056px`, one page, `overflow: hidden`. **Overflow is silently clipped and looks finished** — run `python3 scripts/fit-check.py` and confirm a negative `over` before calling it done.
- Copy is locked. Micro fit flex (a hyphen, a line-break hint) is allowed but must be flagged back to Jane; no rewording, no dropped teasers.
- No circuit textures anywhere in the file, including print fallbacks.
- Mint is primary and structural (rules, date, masthead accent bar, numerals via `#2b9e80` on light); gold appears once, on the headline `<em>`, on dark only.
- Body copy is Inter throughout; Space Grotesk only for heads, labels, numerals. No Syncopate on this sheet.
- No structure changes: no promise index, no upgrade path, no download CTA, no invented metrics or client names.
