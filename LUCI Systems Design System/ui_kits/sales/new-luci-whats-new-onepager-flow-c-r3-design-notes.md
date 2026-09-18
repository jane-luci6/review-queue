# New LUCI What's New one-pager — Flow C R3 · design notes (full hero pass)

**Built:** 18 September 2026 · GLM · rebuild per `CURSOR-BRIEF-new-luci-whats-new-flow-c-r3-glm-fullmesh.md`.
**Design lock:** `new-luci-whats-new-onepager-flow-c-r3-opus-visual-plan.md` (Opus r3 visual plan — full hero, masthead grid, numeral spine, graded rules).
**Copy lock:** `new-luci-whats-new-onepager-flow-c-r2-copy.md`. **No copy was rewritten.** No teaser was dropped. Zero copy flags.

## Jane rejection fixed (all three, per Opus r3 plan §0)

| Rejection | Root cause in r2 | R3 fix |
|---|---|---|
| Wrong "mesh" — lines only | `luci-e-mesh-header-transparent.svg` right-pinned at 62% width | Full-bleed `luci-bg-hero-with-plan-transparent-1920x1080.svg` (mesh **+** floorplan) as an `<img>` at `inset:0`, `object-fit:cover`, `object-position:62% 46%` |
| Header text weird / big left gap | 32px headline capped at `20ch` in a full-width flex column; orphan right-aligned date row | Explicit `1fr / 188px` masthead grid — 42px headline filling a 430px measure across 3 lines; date becomes a designed plate in the right rail |
| No compelling pull into the 3 Promises | 17px middle title (a label), 27px numerals, uniform 1px hairlines | 24px chapter title + 40px numeral spine + graded rule hierarchy (2px mint entry rule above 01, 1px rows, 1px-at-0.09 features) |

## Full hero (per Opus r3 plan §A)

- **Asset:** `assets/textures/luci-bg-hero-with-plan-transparent-1920x1080.svg` — the only background moment on the sheet. Transparent over navy: full-canvas floorplan `<image>` under a mint `#68E3BE` mesh, plus port rings and four `#E8D8A4` accent dots.
- **Layer stack (bottom → top):**
  - z0: `.mast` base navy gradient `linear-gradient(152deg, #10232D 0%, #0A161C 62%, #06121A 100%)`
  - z1: `.mast__hero` — the hero as a real `<img>` (print stability, NOT CSS background), `inset:0`, `object-fit:cover`, `object-position:62% 46%`, `opacity:0.92`
  - z2: `.mast__scrim` — two-gradient directional scrim: a radial cloud at 22% 44% (dense behind the headline, fading right) + a linear `100deg` gradient topping out at `0.90` alpha on the left (so the mesh reads *through* the type, not beside a navy void)
  - z3: `.mast__rule` — solid mint 4px bottom handoff rule (the hero's last gesture, the ledger's first)
- **No `mix-blend-mode`, no `mask-image`, no CSS filters** — print/PDF safety. The asset's own transparency makes blending unnecessary.
- **Print fallback:** `@media print { .mast { background: var(--navy-deep) !important } }` if the `<img>` drops.
- **Forbidden textures removed:** zero occurrences of `e-mesh`, `mesh-lines`, or `circuit` in the file (grep-verified). The footer mesh echo from r2 is deleted entirely — one background moment per sheet.

## Masthead grid (per Opus r3 plan §B)

- **Grid:** `grid-template-columns: 1fr 188px; grid-template-rows: auto auto 1fr auto; column-gap: 32px` — kills the left gap by giving the headline a real measure and the right rail a real anchor.
- **r1 (span 2):** wordmark (132×24 at A1) + `WHAT'S NEW` kicker (right-aligned to A4), `justify-content:space-between`.
- **r2 c1:** `A NEW VERSION OF LUCI IS COMING` — Space Grotesk 700 / 10px / 0.20em / uppercase / mint.
- **r3 c1:** Headline — Space Grotesk 700 / **42px** / lh 1.06 / -0.03em / off-white / `max-width:430px`. `<em>programming</em>` → mint (not gold — opener is mint-only per `luci-dual-accent-system.mdc`). Fills 430px across 3 lines (134px tall, probe-verified).
- **r3 c2:** Date plate — `RELEASE DATE` label (9.5px, 0.22em, rgba(235,245,248,0.62)) + `JANUARY 19` (26px, -0.02em, mint) + 56×2px **gold** underline (the sheet's only gold moment). Right-aligned to A4 (764px, probe-verified). Plate top edge within 2px of headline top (probe-verified).
- **r4 c1:** Subhead — Inter 400 / 13px / lh 1.62 / rgba(235,245,248,0.82) / `max-width:430px`, with mint hairline top border.

## The pull — 3 Promises (per Opus r3 plan §C)

- **C.1 Threshold step:** 16px full-bleed `linear-gradient(to bottom, #E4EDF0 0%, #F5F8FA 100%)` — the dark→white handoff, graded not flat. (Reduced from 22px per overflow fix order; see below.)
- **C.2 Chapter title:** Space Grotesk 700 / **24px** (up from r2's 17px) / -0.02em / `--ink-strong`. Left-aligned on A1. 40×3px `#2b9e80` rule below — the same `SectionBlock` lockup gesture the website uses.
- **C.3 Numeral spine + graded rules:**
  - Numerals **27px → 40px** — `01/02/03` in `#2b9e80` at 40px, stacked on axis A1 (x=52, probe-verified), become a visible spine.
  - **Graded rule hierarchy:** row 01 opens on a **2px `#2b9e80`** rule (the heaviest rule on the page, the start point); rows 02 and 03 open on **1px `rgba(53,79,92,0.16)`**; features separate on **1px `rgba(53,79,92,0.09)`**. Three weights = unmistakable start + descending hierarchy (probe-verified).
  - Equal header weight: all three `.row__name` identical in size/weight (16.5px Space Grotesk 700). Row 03 is taller only because it carries four features.
- **C.4 Feature field:** 178px name column + 1fr teaser, 20px gap, baseline-aligned, 6.5px padding, hairline-separated. Feature names Inter 600 (list copy, not heads); teasers Inter 400. No cards, no boxes.
- **Axis discipline (probe-verified):** A1=52 (numerals), A2=296 (all 10 feature names), A3=494 (all 10 teasers), A4=764 (right edge). Four axes, zero drift between rows.

## Close + footer (per Opus r3 plan §D)

- **Close:** `margin-top:auto`, 40×3px `#2b9e80` rule (rhymes with the middle title's rule — open and close on the same mark). Information close, not a CTA. `[UPGRADE GUIDE URL]` in `#2b9e80`, contact lines in muted ink. Padding-bottom 24px for footer clearance.
- **Footer:** 40px navy `--navy-deep`, `border-top: 1px solid rgba(235,245,248,0.06)`. Mint wordmark at A1, micro-label right to A4, both Space Grotesk 9.5px / 0.14em / uppercase. **`.foot__mesh` and `.foot__scrim` deleted entirely** — one background moment per sheet (grep-verified: 0 occurrences).

## Overflow fix applied (per Opus r3 plan §E.2)

Initial build overflowed by +78px. Applied the plan's fix order:
1. Row padding 20 → 16 (saved 24px)
2. Masthead height 380 → 356 (saved 24px)
3. Threshold step 22 → 16 (saved 6px)
4. Middle padding 26/20 → 18/14 (saved 14px)
5. Middle rule margin 12/18 → 8/12 (saved 10px)

**No type sizes were reduced. No copy was trimmed.** Final: `fit-check.py` → nat=1056px, over=0, no overflow. Visual clearance between last close content and footer = 24px (close padding-bottom).

## Accent discipline (per `luci-dual-accent-system.mdc`)

- Mint `#68E3BE` on dark (hero kicker, announce, headline `<em>`, date value, 4px bottom rule).
- `#2b9e80` on light (middle title rule, numeral spine, row 01 entry rule, close rule, close URL).
- Gold `#EDD086` **exactly once** — the 56×2px date-plate underline (probe-verified: 1 `var(--gold)` use). No bright mint or bright gold on light.
- No Syncopate anywhere (grep-verified: 0 occurrences). Space Grotesk for heads/labels/numerals; Inter for all copy.

## Print verification (this pass)

- **Headless Chrome `--print-to-pdf`:** 1 page, US Letter (612×792 pts = 8.5×11in), ~351 KB.
- **`fit-check.py`:** natural content height **1056px** vs 1056px target → **over=0** (no overflow, no clipping). One `.doc-page` detected.
- `@page { size: letter; margin: 0 }`; `.sheet` locked to `816px × 1056px` with `overflow: hidden`.
- `print-color-adjust: exact` on `.mast`, `.mast__hero`, `.mast__scrim`, `.mast__rule`, `.mast__date-gold`, `.mast__date-top`, `.middle__step`, `.foot`, `.ledger__num`, `.close__rule`.

## QA probe results (all pass)

| # | Probe | Result |
|---|---|---|
| 1 | `.mast__hero` src / inset / object-fit | `luci-bg-hero-with-plan-transparent-1920x1080.svg` / `0px` / `cover` ✅ |
| 2 | `e-mesh` / `mesh-lines` / `circuit` in file | 0 / 0 / 0 (grep-verified) ✅ |
| 3 | Headline box | 430px wide, 134px tall (3 lines) ✅ |
| 4 | Date plate | top within 2px of headline top, right edge = 764px ✅ |
| 5 | Axis drift | 10 names at x=296, 10 teasers at x=494, all aligned ✅ |
| 6 | Numeral spine | 3 numerals at x=52, all 40px ✅ |
| 7 | Rule hierarchy | row 01: 2px #2b9e80; rows 02/03: 1px rgba(53,79,92,0.16) ✅ |
| 8 | Gold count | 1 `var(--gold)` use (date-plate underline) ✅ |
| 9 | Footer | 0 `foot__mesh` / 0 `foot__scrim` (grep-verified) ✅ |
| 10 | Fit | nat=1056px, over=0; visual clearance = 24px ✅ |

## Copy lock — no changes

- Every locked string verbatim (HTML entities for apostrophes/dashes/middots render identically).
- **No micro fit flex was needed** — no hyphens added, no line-break hints, no teaser shortened. Zero copy flags.
- Placeholders retained: `[UPGRADE GUIDE URL]`, `[NAME]`, `[TITLE]`, `[EMAIL]`, `[PHONE]`.
- No invented metrics, no client names.
- No structure changes: no promise index, no upgrade path, no download CTA.

## Files

- `ui_kits/sales/new-luci-whats-new-onepager-flow-c.html` — rebuilt per Opus r3 (source of truth).
- `ui_kits/sales/new-luci-whats-new-onepager.html` — overwritten with the same file (stable IMP preview).
- `ui_kits/sales/new-luci-whats-new-onepager-flow-c-r3-design-notes.md` — this file.

## How to open / print

Open in a browser (or Cursor's in-editor preview). Print → Save as PDF: US Letter, margins none, scale 100%, background graphics ON.
