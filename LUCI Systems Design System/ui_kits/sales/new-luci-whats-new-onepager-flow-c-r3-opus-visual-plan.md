# New LUCI What's New one-pager — Flow C **R3** · Opus visual plan

- **Status:** Hard visual direction for GLM. Copy + structure locked (r2). Implement exactly; do not re-open layout decisions.
- **Target files:** `ui_kits/sales/new-luci-whats-new-onepager-flow-c.html` → then overwrite `ui_kits/sales/new-luci-whats-new-onepager.html` with the same file (stable IMP preview).
- **Format:** one US Letter sheet, 816 × 1056 px, `overflow:hidden`, print-safe.
- **Craft reference:** `luci-website` — `HomeMesh.astro` (hero-c layering), `CaseStudyYaamava.astro` `.cs-hero` (full hero + directional scrim), `HomeLedger.astro` (numeral scale), `SectionBlock` lockup (40×3 mint rule). This sheet is held to the **website's** craft bar, not to older sparse sales-print habits.

---

## 0. THESIS — one idea, no options

> **The sheet is a hero, not a header.** The full mesh+floorplan hero owns the top third and every element below it hangs off the **same two vertical axes** the hero establishes. The left column is never abandoned, because the right column is *populated* (a date plate on the dense mesh), and the reader is pulled into promise 01 by a **numeral spine** that the hero's mint rule hands off into — the heaviest rule on the page sits directly above `01`.

Three rejections, three fixes, one mechanism each:

| Jane's rejection | Root cause in the r2 file | R3 fix |
|---|---|---|
| Wrong "mesh" — lines only | `mast__mesh` = `luci-e-mesh-header-transparent.svg` at `width:62%`, right-pinned | **Full-bleed** `luci-bg-hero-with-plan-transparent-1920x1080.svg` (mesh **+** floorplan), `inset:0`, `object-fit:cover` (§A) |
| Header text is weird / big left gap | 32px headline capped at `20ch` inside a full-width flex column, with a lone `justify-content:flex-end` date row below it → ~45% of every line-box empty and nothing on the right to hold it | **Explicit 2-column masthead grid** (1fr / 188px). Headline up to 42px filling a 430px measure across 3 lines; the date becomes a designed **plate** in the right rail (§B) |
| No compelling design pulling into the 3 Promises | Middle title at 17px (a label, not a chapter), 27px numerals, uniform 1px hairlines everywhere → a wireframe under a fancy header | **Threshold step + 24px chapter title + 40px numeral spine + a graded rule hierarchy** that makes the entry to `01` the loudest rule on the sheet (§C) |

---

## 1. Page frame + the two axes (memorize these numbers)

```
.sheet { width: 816px; height: 1056px; overflow: hidden; display: flex; flex-direction: column;
         background: var(--off-white); }
--pad: 52px;              /* flat px, not 0.55in — the grid math below depends on it */
```

| Axis | x (px) | Carries |
|---|---:|---|
| **A1 — page axis** | `52` | wordmark, announce kicker, headline, subhead, middle title + its 40×3 rule, the `01/02/03` numerals, close rule, footer wordmark |
| **A2 — feature-name axis** | `296` | every feature name in all 3 rows (`52 + 214 + 30`) |
| **A3 — teaser axis** | `494` | every feature teaser in all 3 rows (`296 + 178 + 20`) |
| **A4 — right edge** | `764` | kicker (top right), date plate right edge, row hairline ends, footer micro-label |

Live measure = **712px**. Four axes, zero drift between rows. That alignment discipline — not gridlines — is what makes the ledger read as a built table.

**Vertical budget (target, ±8px):**

| Block | Height |
|---|---:|
| Masthead (full hero) | **380** |
| Threshold + middle title lockup | **84** |
| Ledger row 01 | ~118 |
| Ledger row 02 | ~118 |
| Ledger row 03 (4 features) | ~146 |
| Slack (breathing room before close) | 40–70 |
| Close | ~120 |
| Footer | **40** |
| **Total** | **≤ 1056** |

Slack rule: `.middle { justify-content: flex-start; padding-bottom: 20px }` and `.close { margin-top: auto }`. **Never `space-between`** — it dumps all slack into one gap and overflows (see `luci-sales-document-system.mdc`, footer-clearance learning).

---

## A. FULL HERO BACKGROUND — mesh **+** floorplan, full bleed

**Asset (only this one):** `assets/textures/luci-bg-hero-with-plan-transparent-1920x1080.svg`

It is already transparent over navy: a full-canvas floorplan `<image>` under a mint `#68E3BE` mesh (opacity 0.15–0.31), plus port rings and four `#E8D8A4` accent dots. **Forbidden on this sheet:** `luci-e-mesh-header-transparent.svg`, `luci-bg-hero-mesh-lines-*`, any circuit texture.

### Layer stack (bottom → top)

```css
.mast {
  position: relative; height: 380px; overflow: hidden;
  padding: 40px var(--pad) 34px;
  background: linear-gradient(152deg, #10232D 0%, #0A161C 62%, #06121A 100%);
  color: var(--off-white);
}
/* z0 — base navy gradient above */

/* z1 — the hero, as an <img> for print stability (NOT a CSS background) */
.mast__hero {
  position: absolute; inset: 0; width: 100%; height: 100%;
  object-fit: cover; object-position: 62% 46%;
  opacity: 0.92; z-index: 0; pointer-events: none;
}

/* z2 — directional scrim: dense + vivid at the right, muted (never dead) at the left */
.mast__scrim {
  position: absolute; inset: 0; z-index: 1; pointer-events: none;
  background:
    radial-gradient(74% 82% at 22% 44%,
      rgba(8,18,24,0.78) 0%, rgba(8,18,24,0.52) 38%, rgba(8,18,24,0.18) 64%, transparent 84%),
    linear-gradient(100deg,
      rgba(8,18,24,0.90) 0%, rgba(8,18,24,0.84) 32%, rgba(8,18,24,0.54) 58%,
      rgba(8,18,24,0.18) 82%, rgba(8,18,24,0.06) 100%);
}

/* z3 — mint handoff rule: the hero's last gesture, and the ledger's first */
.mast__rule {
  position: absolute; left: 0; right: 0; bottom: 0; height: 4px;
  background: var(--mint); z-index: 3;
}
```

**Why `0.90` and not `1.0` on the left:** the r2 scrim went to solid `var(--navy-deep)` at 0% and `0.92` at 46%, which is exactly what killed the left third — an opaque navy panel with a skinny text column on it. At `0.90/0.84` the mesh and one or two plan walls read *faintly through* the headline column. That's what the website does (`.home-entry.hero-c::after` fades to transparent and adds a radial cloud only behind `.home-entry__copy`), and it is the difference between "type on a finished background" and "type on a void."

**Crop math (don't guess):** source is 1920×1080 (1.78:1); the box is 816×380 (2.15:1). `cover` scales to width 816 → height 459 → 79px trimmed vertically. `object-position: 62% 46%` puts the mesh's dense right-hand cluster (the `1382`/`1737` verticals and the port rings around `x≈1382`) in the right third of the visible crop, behind the date plate, and keeps the plan's strongest wall runs off the headline.

**Print, non-negotiable:**
- **No `mix-blend-mode`, no `mask-image`.** The website uses `screen` blending and radial masks; both are soft-mask paths that corrupt or drop in Chrome print/PDF. Translate them to plain gradient scrims as specified above. The asset's own transparency makes blending unnecessary.
- Add `.mast`, `.mast__hero`, `.mast__scrim`, `.mast__rule`, `.mast__date-gold`, `.middle__step`, `.foot` to the `print-color-adjust: exact` list.
- Keep the `@media print { .mast { background: var(--navy-deep) !important } }` fallback if the `<img>` drops.

---

## B. MASTHEAD COMPOSITION — kill the left gap

```css
.mast__grid {
  position: relative; z-index: 2; height: 100%;
  display: grid;
  grid-template-columns: 1fr 188px;
  grid-template-rows: auto auto 1fr auto;
  column-gap: 32px;
}
```

| Cell | Content | Spec |
|---|---|---|
| r1 · span 2 | wordmark **+** `WHAT'S NEW` kicker, `justify-content:space-between` | logo 132×24 at A1; kicker Space Grotesk 700 / **10px** / `0.22em` / uppercase / `rgba(104,227,190,0.85)`, right-aligned to **A4** |
| r2 · c1 | `A NEW VERSION OF LUCI IS COMING` | Space Grotesk 700 / **10px** / `0.20em` / uppercase / `var(--mint)`; `margin-top:22px` |
| r2 · c2 | — | empty (the date plate starts at r3 so it aligns to the headline, not the kicker) |
| r3 · c1 | **Headline** | Space Grotesk 700 / **42px** / lh `1.06` / `-0.03em` / `var(--off-white)` / `max-width:430px` / `margin-top:12px`. `<em>programming</em>` → `font-style:normal; color:var(--mint)` |
| r3 · c2 | **Date plate** (see below) | `align-self:start; margin-top:14px` |
| r4 · c1 | **Subhead** | Inter 400 / **13px** / lh `1.62` / `rgba(235,245,248,0.82)` / `max-width:430px`; `border-top:1px solid rgba(104,227,190,0.16); padding-top:16px` |
| r4 · c2 | — | empty by design — dense mesh + plan reads here, held above by the plate |

**Headline fills its measure.** 45 characters at Space Grotesk 700 / 42px over a 430px measure breaks ~20 / ~15 / ~10 → three lines, 134px tall. That is the fix: the left column is now a **block**, not a ribbon. Do not set `max-width` in `ch`; use `430px` so it cannot drift with font metrics.

### The date plate (the right rail's anchor)

```
[ 188×1px  rgba(104,227,190,0.42) ]
RELEASE DATE          ← Space Grotesk 700 · 9.5px · 0.22em · uppercase · rgba(235,245,248,0.62) · mt 10
JANUARY 19            ← Space Grotesk 700 · 26px · lh 1.0 · -0.02em · var(--mint) · mt 6
[ 56×2px  var(--gold) ]   ← mt 10 — the ONE gold moment on the sheet
```

Right-align the plate's text to **A4**. `RELEASE DATE · JANUARY 19` from the locked copy is rendered as label + value on two lines; no ordinal, no abbreviation.

**Accent discipline:** headline accent and all structure are **mint** (opener = mint only, `luci-dual-accent-system.mdc`). Gold appears exactly once — the 56×2px plate underline. The bottom handoff rule stays **solid mint** full-width; do **not** copy the website's mint→gold split rule here, because gold is already spent.

### 3-second eye path

1. **Headline**, 42px mint-accented, three lines, left block — the only display-scale type on the sheet.
2. **JANUARY 19**, 26px mint — the second-largest type, deliberately across the fold on the mesh side, so the eye crosses the hero instead of falling off the left column.
3. **Subhead**, above its own mint hairline.
4. Down the mint rule into `01`.

The announce kicker is the entry stamp, not a competitor. Nothing else in the masthead is above 13px.

---

## C. COMPEL THE 3 PROMISES — the main craft ask

The promises are the reason this sheet exists. Three mechanisms, applied together.

### C.1 Threshold — the dark→white handoff (never a flat cliff)

Directly under the 4px mint rule:

```css
.middle__step {                    /* full-bleed contrast step, 22px */
  height: 22px; flex: 0 0 22px;
  background: linear-gradient(to bottom, #E4EDF0 0%, var(--off-white) 100%);
}
```

This is the print translation of the site's section handoff: the reader leaves navy through a mint rule and lands on a **graded** light band that resolves into the page white. 22px, full bleed, no border.

### C.2 The chapter title (not a label)

```css
.middle { flex: 1 1 auto; display: flex; flex-direction: column;
          padding: 26px var(--pad) 20px; justify-content: flex-start; }
.middle__title { font-family: var(--font); font-weight: 700; font-size: 24px;
                 line-height: 1.14; letter-spacing: -0.02em; color: var(--ink-strong); }
.middle__rule  { width: 40px; height: 3px; background: var(--accent-light);
                 margin: 12px 0 18px; }
```

**17px → 24px.** At 17px it read as a caption under the hero; at 24px it reads as the sheet's second headline and the 40×3 mint rule under it is the same lockup gesture every website `SectionBlock` opens with. Left-aligned on A1. No role/subhead line — the locked copy doesn't have one, and don't invent one.

### C.3 The numeral spine + graded rule hierarchy (this is the pull)

```css
.row { display: grid; grid-template-columns: 214px 1fr; column-gap: 30px;
       padding: 20px 0; border-top: 1px solid rgba(53,79,92,0.16); }
.row:first-of-type { border-top: 2px solid var(--accent-light); }   /* ← the loudest rule on the page */
.row:last-of-type  { border-bottom: 1px solid rgba(53,79,92,0.16); }
.row__lead { align-self: start; min-width: 0; }

.ledger__num  { display: block; font-family: var(--font); font-weight: 700;
                font-size: 40px; line-height: 1; letter-spacing: -0.02em;
                color: var(--accent-light); margin-bottom: 8px; }
.row__name    { font-family: var(--font); font-weight: 700; font-size: 16.5px;
                line-height: 1.2; letter-spacing: -0.015em; color: var(--ink-strong);
                margin-bottom: 8px; }
.row__benefit { font-family: var(--font-body); font-weight: 400; font-size: 11.5px;
                line-height: 1.5; color: var(--navy-muted); max-width: 190px; }
```

Three deliberate craft moves:

1. **Numerals 27px → 40px.** `01 / 02 / 03` in `#2b9e80` at 40px, stacked on axis A1, become a visible **spine** — the second-loudest voice on the sheet after the headline, and the thing the eye lands on when it comes off the mint rule. This is `HomeLedger`'s `clamp(28px, 3.2vw, 38px)` numeral scale, rendered at letter size. Anything under ~36px dissolves into the body and the middle goes flat again — that is precisely the r2 failure.
2. **Graded rules, not uniform hairlines.** The entry to `01` is a **2px `#2b9e80`** rule; rows 02 and 03 open on **1px `rgba(53,79,92,0.16)`**; features separate on **1px `rgba(53,79,92,0.09)`**. Three weights = an unmistakable start point and a clear descending hierarchy. The r2 file used one hairline weight for both rows and features, so nothing said "begin here."
3. **Equal header weight, honest row heights.** All three `.row__name` are identical in size and weight; only row 03 is taller because it carries four features (locked copy). `align-self:start` keeps each lead block top-aligned to its row rule so the three numerals read as one column, not three floating marks.

### C.4 The 70% feature field

```css
.features { min-width: 0; display: flex; flex-direction: column; }
.feature  { display: grid; grid-template-columns: 178px 1fr; column-gap: 20px;
            align-items: baseline; padding: 6.5px 0;
            border-top: 1px solid rgba(53,79,92,0.09); }
.feature:first-child { border-top: none; padding-top: 1px; }
.feature:last-child  { padding-bottom: 0; }
.features__name   { font-family: var(--font-body); font-weight: 600; font-size: 11.5px;
                    line-height: 1.3; color: var(--ink-strong); }
.features__teaser { font-family: var(--font-body); font-weight: 400; font-size: 11px;
                    line-height: 1.4; color: var(--navy-muted); }
```

- Every feature name starts at **A2 = 296px**; every teaser at **A3 = 494px**. Identical in all three rows. No card, no box, no equal columns — one compact line per feature, hairline-separated, letter density held.
- `align-items: baseline` so a two-line name (`Video/LED wall layout sync`) still sits on the teaser's first baseline.
- Feature names are Inter 600, not Space Grotesk: they are list copy, not heads (`luci-visual-design.mdc`). The only Space Grotesk in the ledger is the numerals, the promise names, and the middle title.

### C.5 Why this pulls

Contrast steps in order down the page: 42px navy-field headline → mint 4px rule → graded light step → 24px chapter title + 40×3 mint rule → **2px mint rule** → 40px `01`. Each step is smaller and lighter than the last except the one that matters: the rule above `01` is heavier than the rule above `02` and `03`. The reader is handed a start point and then a rhythm, and the rhythm is the same three-beat structure the website uses to move a reader from a dark hero into a white content band.

---

## D. CLOSE + FOOTER

```css
.close { margin-top: auto; padding: 0 var(--pad) 18px; }
.close__rule    { width: 40px; height: 3px; background: var(--accent-light); margin-bottom: 12px; }
.close__info    { font-family: var(--font-body); font-size: 11.5px; line-height: 1.5; color: var(--ink); }
.close__info strong { font-family: var(--font); font-weight: 700; color: var(--ink-strong); }
.close__url     { font-family: var(--font); font-weight: 600; color: var(--accent-light); }
.close__contact { margin-top: 8px; font-family: var(--font-body); font-size: 10.5px;
                  line-height: 1.5; color: var(--navy-muted); }
.close__contact strong { font-family: var(--font); font-weight: 700; color: var(--ink-strong); }
```

The close's 40×3 mint rule intentionally rhymes with the middle title's rule — open and close on the same mark. Information close, **not** a CTA: no button, no panel, no fill.

**Footer — drop the mesh echo.** 40px, `background: var(--navy-deep)`, `border-top: 1px solid rgba(235,245,248,0.06)`, mint wordmark at A1, micro-label right to A4, both Space Grotesk 9.5px / `0.14em` / uppercase. **Delete `.foot__mesh` and `.foot__scrim` entirely.** One background moment per sheet; a second faint mesh strip at the bottom cheapens the hero and was part of the lines-only pass being rejected.

---

## E. HARD CONSTRAINTS FOR GLM

1. **816 × 1056, `overflow:hidden`, one sheet.** Run `python3 scripts/fit-check.py ui_kits/sales/new-luci-whats-new-onepager-flow-c.html` and confirm a **negative `over`**. A clipped page renders as a plausible finished page — verify, never eyeball.
2. **If it overflows,** take it out in this order: row padding `20 → 16`, masthead height `380 → 356`, threshold step `22 → 16`. **Never** reduce type sizes below the values above, and **never** trim copy — copy is locked (r2) and only Jane changes it. If a headline or teaser line breaks badly, **flag it**; don't rewrite it.
3. **Background:** the with-plan SVG only, as an `<img>`, full bleed. No lines-only mesh, no circuit textures, no second mesh instance anywhere on the sheet.
4. **No `mix-blend-mode`, no `mask-image`, no CSS filters** — print/PDF safety. Gradient scrims only.
5. **Fonts:** `../../assets/fonts/luci-brand-fonts.css` only. No Google Fonts `<link>`, no inline `<style data-luci-fonts>`. **No Syncopate** anywhere — Space Grotesk (heads, labels, numerals) + Inter (all copy).
6. **Accents:** mint `#68E3BE` on dark; `#2b9e80` on light (every light-surface accent, `#176B54` retired). Gold `#EDD086` **once** — the date-plate underline. No bright mint or bright gold on light.
7. **Copy + structure locked:** new-version masthead + January 19, one subhead, "The 3 Promises of New LUCI", split ledger (promise left / features+teasers right), thin Guide URL + contact footer. No upgrade-path steps, no download CTA, no metrics, no client names.
8. **After the HTML is done:** overwrite `ui_kits/sales/new-luci-whats-new-onepager.html` with the same file (stable IMP preview), then commit both.

### Measurable QA probes (not opinions)

| # | Probe | Pass |
|---|---|---|
| 1 | `.mast__hero` src | ends `luci-bg-hero-with-plan-transparent-1920x1080.svg`; `inset:0`; `object-fit:cover` |
| 2 | Occurrences of `e-mesh` / `mesh-lines` / `circuit` in the file | **0** |
| 3 | Left-third emptiness | headline box ≥ 3 lines tall and ≥ 420px wide; scrim left stop ≤ `0.90` alpha |
| 4 | Right rail populated | date plate top edge within 20px of headline top; plate right edge = 764px |
| 5 | Axis drift | all 10 feature names start at x = 296px; all 10 teasers at x = 494px |
| 6 | Spine | `.ledger__num` computed font-size = 40px in all three rows; all three at x = 52px |
| 7 | Rule hierarchy | row 01 top border 2px `#2b9e80`; rows 02/03 1px `rgba(53,79,92,0.16)`; features 1px `0.09` |
| 8 | Gold count | exactly one `--gold` use (date-plate underline) |
| 9 | Footer | no `.foot__mesh` / `.foot__scrim` in markup |
| 10 | Fit | `fit-check.py` → negative `over`; last content block clears the footer by ≥ 24px |

---

## F. Website patterns cited (and how each was translated to print)

| Website | Pattern | Translation on this sheet |
|---|---|---|
| `CaseStudyYaamava.astro` `.cs-hero` | full `luci-bg-hero-1920x1080.svg` under a `to right` scrim that stays vivid at the right edge; 4px accent rule at the bottom | §A — same directional scrim logic, with the **with-plan** asset, as an `<img>`, and a solid-mint bottom rule |
| `HomeMesh.astro` `.home-entry.hero-c` | mesh at full opacity, a radial mask, and a **radial cloud behind the copy block only** — never an opaque left panel | §A — the radial cloud becomes the first gradient stop in `.mast__scrim`; the mask is dropped (print-unsafe) |
| `HomeMesh.astro` `.home-ledger__rail::before` | localized dark cloud so type stays legible on a live background | §A — folded into the same scrim rather than a second layer |
| `HomeLedger.astro` | numerals at `clamp(28px, 3.2vw, 38px)` carrying the section's rhythm | §C.3 — 40px numeral spine on axis A1 |
| `SectionBlock` lockup (§3.5) | big name → 40×3px mint rule → small role | §C.2 / §D — 24px title → 40×3 `#2b9e80` rule, opened and closed the same way |
| Site section handoffs | dark band → graded light band, never a hard cut | §C.1 — 22px `#E4EDF0 → #F5F8FA` threshold step |

---

## SUMMARY (5 lines)

1. **Asset:** full-bleed `luci-bg-hero-with-plan-transparent-1920x1080.svg` (mesh **+** floorplan) as an `<img>` at `inset:0`, `object-fit:cover`, `object-position:62% 46%`, under a two-gradient directional scrim that tops out at `0.90` alpha on the left so the mesh reads *through* the type instead of sitting beside a navy void — no blend modes, no masks, print-safe.
2. **Masthead fix:** the left gap was a `20ch` headline in a full-width flex column with an orphan right-aligned date; replaced by an explicit `1fr / 188px` grid — 42px headline filling a 430px measure across three lines on axis A1, and a populated right rail carrying a `RELEASE DATE / JANUARY 19` plate (26px mint, 56×2px gold underline — the sheet's only gold).
3. **The pull:** mint 4px handoff rule → 22px graded light threshold → 24px chapter title with a 40×3 `#2b9e80` rule → a **2px mint rule** above promise 01 that is the heaviest rule on the page → a 40px `01/02/03` numeral spine on the same axis as everything else.
4. **Ledger discipline:** four locked axes (52 / 296 / 494 / 764), three graded rule weights (2px entry, 1px row, 1px-at-0.09 feature), Inter 600 names + Inter 400 teasers on one compact line each, equal header weight, honest row heights, no cards — and the footer mesh echo deleted so the hero is the sheet's one background moment.
5. **Constraints:** 816×1056 `overflow:hidden`, `fit-check.py` must report negative `over`, copy locked (flag, never trim), no Syncopate, mint-on-dark / `#2b9e80`-on-light / gold once, then overwrite `new-luci-whats-new-onepager.html` with the same file.
