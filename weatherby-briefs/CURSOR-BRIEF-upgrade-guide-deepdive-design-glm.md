# CURSOR BRIEF — Upgrade Guide feature deep-dive design (GLM)

**Model:** GLM  
**Repo:** website (`--repo website`)  
**Mode:** execute  
**Why not GPT:** design/CSS only — no copy rewrite.  
**Review:** http://10.10.1.37/luci-upgrade-guide/#ug-features (Jane: Cmd+Shift+R)

## Jane locks (do exactly — design first, NO transcript/copy rewrite)

Scope = section **"Feature deep-dive"** (`#ug-features` / `.ug-deepdive`) only.

Minimalism OK as a base — **refine, don’t scrap**. Do not invent features. Do not change deep-dive copy text (names, one-liners, paragraphs, benefits) in substance.

### 1) Section header — navy background (not a light bare label)

Match site/sales navy header treatment (SectionBlock `tone="deep"` / `--navy` / `--navy-deep` / sales `--header-navy` family — **brand tokens only**, do not invent a new color system).

- Feature deep-dive section header must sit on **black/navy** like other LUCI materials.
- Preferred: set SectionBlock `tone="deep"` for `#ug-features` so lockup uses existing deep lockup styles (off-white name, mint rule/role).
- If accordion must stay light-on-light for readability, nest `.ug-deepdive` in a light raised panel (`--off-white` / white) inside the deep section — do not leave the lockup as a light bare label on `tone="light"`.

### 2) Accordion open state — body placement / alignment

Open panel body text is oddly placed / doesn’t align with the feature header.

- Add design so open panels feel properly placed: spacing, alignment axis with header, rule/padding/inset.
- **Brand tokens only.**
- Known bug: `.ug-feature__body` uses `padding-left: minmax(160px, 220px)` which is **invalid CSS** (minmax is not a padding value). Fix by matching the summary grid axis on ≥720px:
  - Summary grid: `minmax(160px, 220px) 1fr 24px` (name | liner | chev).
  - Open body content should align under the **liner** column (column 2), with sensible top padding under the summary and bottom padding before the next rule.
- Keep closed-state summary layout; refine open-state inset/rule so it feels intentional.

### 3) Fix double hairlines under 01

Pillar group head has `border-bottom` and first `.ug-feature` has `border-top` → double rule under **01**.

- One clean rule only (remove one of the stacked borders; prefer a single rule between head and feature list).

### 4) Leave alone (do not touch)

- Hero: keep `center 72% / 125% auto`
- Pillars fills + support full-width row
- Intro first-sentence
- Deep-dive copy text (substance unchanged)
- Other sections (technical, path, FAQ, CTA)

## Files

- `src/pages/luci-upgrade-guide.astro` — Feature deep-dive SectionBlock tone + `.ug-deepdive` / accordion CSS (and minimal markup if a light panel wrapper is needed)
- Do **not** rewrite `src/data/upgradeGuide.ts` feature copy

## Out of scope

- Copy/transcript edits
- New features, new color system, new accordion interaction model
- Hero / pillars / support / intro

## Required

1. Implement navy header + accordion placement + single rule under 01 exactly as locked.
2. Commit message: `Upgrade guide: feature deep-dive design (navy header + accordion)`
3. `./deploy.sh`
4. Update board Active jobs: add/update `upgrade-guide-deepdive-design` → deployed (hash); Waiting Jane Cmd+Shift+R.  
   Board: `luci-design/LUCI Systems Design System/agent-handbook/shared/CURRENT-WORK-BOARD.md`

## Definition of done

Live `.37` `/luci-upgrade-guide/`: HTTP 200; navy deep-dive section header present; accordion open body aligned with feature header axis; single clean rule under 01 (no double); hero still `center 72% / 125% auto`; pillar fills + support row still present; deep-dive copy text unchanged in substance; commit hash returned.
