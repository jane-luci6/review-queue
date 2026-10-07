# CURSOR BRIEF — Upgrade Guide "Your path to the new LUCI": 3 design options (GLM)

**Repo:** `luci-website` · branch base `persona-hero-subhead-gold`
**Owner:** GLM (sample builds) · plan by Claude · Jane picks A/B/C
**Page:** `src/pages/luci-upgrade-guide.astro` → live at `http://10.10.1.37/luci-upgrade-guide/#ug-upgrade`
**Data:** `src/data/upgradeGuide.ts` → `upgradePath` (lines ~717–757)

Jane: the section "is not very visually appealing and it's really difficult to navigate." Build three sample directions on three branches so she can compare. These are direction probes, not final polish.

---

## 1. What's wrong with it today

Current order (markup ~lines 258–297, CSS `.ug-upgrade*` ~lines 1556–1720):

1. Long intro paragraph (`upgradePath.intro`, ~60 words).
2. Two-cell timing strip with a **mint left bar** (Release date · Pace). Jane already called the mint left bar overused.
3. Rollout note that repeats the Pace line ("coordinated sequence — not all at once").
4. Subhead "How your upgrade works" plus another paragraph that repeats the intro (preconfigured laptop, current system untouched).
5. Four steps as a narrow vertical list: 28px circle numbers, 14px titles, 13.5px body, `max-width: 48ch`.

Problems:
- **No visual anchor.** It's all small text in one column. Nothing reads as "this is a process with four stages."
- **The same idea shows up three times.** The intro, the how-intro and step 03 all say "your current system stays online." Pace and rollout note say the same thing twice.
- **The key facts are buried.** The things a client actually wants (when, how long the cutover takes, will my system go down, does it cost anything) are scattered through paragraphs. Some, like cost, only live in the FAQ.
- **Steps are too small** to scan, and there's no sense of sequence or who does what.

## 2. Ground rules for all three variants

- **Don't change copy in `upgradeGuide.ts`.** Every variant renders the existing fields. If a variant needs a short label (e.g. "Cutover"), put it inline in the markup and list it in the build notes for Jane to approve.
- **Restating existing facts is OK, inventing them is not.** The fact chips below lift wording that's already on the page (intro, step 04, FAQ). No new claims, no percentages, always **A/V**.
- **Hide duplicates, don't delete them.** Each variant may stop rendering `timing.rolloutNote` and `whatIsInvolved.paragraph` (both are duplicates). Leave them in the data file. Jane decides on the copy trim after she picks.
- **Only touch** the `UPGRADE PATH` markup block and the `.ug-upgrade*` CSS. Don't touch the frozen pillar tabs, features, FAQ, nav or CTA.
- **Brand rules:** mint is primary, gold secondary. `#2b9e80` (`--accent-light`) for accents on light. Heads in Space Grotesk, all body copy in Inter. 8px spacing scale. No new mint left bars. Use the §5.1 soft-icon tile + duotone icon pattern if icons are used (reference: `ui_kits/sales/capabilities-document.{html,css}` in `luci-design`).
- **Accessibility:** keyboard reachable, visible focus rings, `prefers-reduced-motion` fallback, and a sensible mobile stack at <640px.

### Shared "key facts" chips (A and B use these; C can too)

Four short facts, each a label plus a value, sourced from existing copy:

| Label | Value | Source |
|---|---|---|
| Release | December 2026 | `timing.releaseDate` |
| Rollout | Coordinated weekly groups | `timing.paceLine` (shortened, flag for Jane) |
| Cutover | About one to two hours | step 04 body |
| Your current system | Stays online until you switch | intro + step 03 |

Optional fifth: **Cost: Included under your current contract** (FAQ). Flag it in the notes; don't ship it as a default.

---

## 3. The three options

### Option A — Horizontal timeline ("the road")

**Idea:** make the four steps the hero of the section. They read left to right on a connected track, like a shipping tracker.

```
 Your path to the new LUCI
 For existing LUCI clients
 [intro paragraph, max 60ch]

 ┌──────────┬──────────────┬──────────┬──────────────────────┐
 │ RELEASE  │ ROLLOUT      │ CUTOVER  │ YOUR CURRENT SYSTEM  │   ← fact strip, hairline-divided,
 │ Dec 2026 │ Weekly groups│ ~1–2 hrs │ Stays online         │     no box, no left bar
 └──────────┴──────────────┴──────────┴──────────────────────┘

   (01)━━━━━━━━━━━━(02)━━━━━━━━━━━━(03)━━━━━━━━━━━━(04)        ← gold→mint low-opacity gradient track
   Schedule        Your laptop     Plug in         Switch when
   with LUCI       ships preloaded and verify      you are ready
   body…           body…           body…           body…
```

- Numbered nodes about 44px, Space Grotesk 700, `--accent-light` ring; node 04 filled mint as the destination.
- Connector: a thick (about 4px), low-opacity gold→mint gradient line through the node centers (per §5.1 flow connectors).
- Step titles 17–18px Space Grotesk 700; body Inter 15px, `--navy-muted`.
- Four equal columns at ≥1024px, 2×2 at 640–1024px. Below 640px it becomes a **vertical** track: line on the left, nodes stacked.
- Optional reveal: nodes and the line draw in left to right on scroll (300–400ms, with a reduced-motion fallback).

**Why it might win:** it instantly reads as a process with an end point. Lowest navigation burden, since everything is visible at once.
**Risk:** four bodies side by side are dense at ~1100px. Keep the bodies as they are, but check that each column holds about 28–34ch.

### Option B — Facts rail + step cards ("the brief")

**Idea:** split the section into **what you need to know** (left, sticky) and **what happens** (right). Same split-rail logic as the feature deep-dive above it, so it feels native to the page.

```
 ┌───────────────────────┐  ┌───────────────┐ ┌───────────────┐
 │ AT A GLANCE           │  │ [icon] 01     │ │ [icon] 02     │
 │ Release   Dec 2026    │  │ Schedule with │ │ Your laptop   │
 │ Rollout   Weekly grps │  │ LUCI          │ │ ships preload │
 │ Cutover   ~1–2 hours  │  │ body…         │ │ body…         │
 │ Current   Stays on    │  └───────────────┘ └───────────────┘
 │ system                │  ┌───────────────┐ ┌───────────────┐
 │                       │  │ [icon] 03     │ │ [icon] 04     │
 │ [Questions? → FAQ]    │  │ Plug in and   │ │ Switch when   │
 └───────────────────────┘  │ verify        │ │ you are ready │
     sticky on ≥900px       └───────────────┘ └───────────────┘
```

- Left rail: soft grey gradient card (same family as the pillar tabs, `#E8EEF2 → #F3F6F8`), **no mint left bar**. Facts as a de-boxed definition list with hairline rows. A small "Questions about your upgrade? See the FAQ ↓" link at the bottom jumps to `#ug-faq`.
- Rail sticky top must clear the main nav: use `top: 100px` (the frozen pillar tabs are out of view by this section; verify).
- Right: 2×2 step cards using the **§5.1 soft-icon tile** (54px tile, mint gradient, duotone icon with one gold accent). Icon ideas: calendar (01), shipping box or laptop (02), plug or check (03), switch/arrow (04). Numbers go in the small corner label, Space Grotesk 700, tracked.
- Intro paragraph sits full-width above both columns.
- Mobile: rail first (not sticky), then cards stacked.

**Why it might win:** the answers clients scan for are pinned and always visible. It matches the feature section's visual language. It also gives a natural bridge to the FAQ.
**Risk:** the busiest of the three. Keep the cards airy (24–32px padding) and the icons distinct.

### Option C — Interactive stepper ("one step at a time")

**Idea:** the strongest navigation fix. A clickable progress bar where each step opens one focused panel, with "Next step →" to move forward. Reads like an onboarding flow.

```
 [intro paragraph]
 [fact strip, same as A, but compact, inline]

  ●━━━━━━━━━━━━○━━━━━━━━━━━━○━━━━━━━━━━━━○
  01 Schedule   02 Ships     03 Verify     04 Switch           ← clickable tabs (role="tablist")

 ┌──────────────────────────────────────────────────────────────┐
 │ STEP 01 OF 04                                                │
 │ Schedule with LUCI                          [large step art  │
 │ Your account team reviews site readiness,    or soft-icon    │
 │ confirms the upgrade schedule, and …         tile, 96px]     │
 │                                                              │
 │ ← Previous                                     Next step →   │
 └──────────────────────────────────────────────────────────────┘
```

- Progress bar fills mint up to the active step. Completed nodes are filled; upcoming ones are outlined.
- Short step labels in the bar (Schedule · Ships · Verify · Switch) are **new inline labels**. Flag them for Jane. Full titles appear in the panel.
- Panel: soft grey gradient card, step title 24–28px Space Grotesk 700, body Inter 17px at 60ch, one large duotone icon on the right (§5.1 at 2× scale). Prev/Next buttons are pills; Next is mint-filled.
- Keyboard: arrow keys move between step tabs (same ARIA tab pattern as the pillar tabs). Without JS, all four panels show stacked so no content is hidden.
- Mobile: bar becomes four numbered dots; panel full-width.

**Why it might win:** one idea on screen at a time, big readable type, an obvious "what's next" action. It solves "hard to navigate" most directly.
**Risk:** content is hidden behind clicks, so a skimmer sees only step 01. Mitigate with the fact strip above, and by showing all four short labels in the bar.

---

## 4. Build instructions (per `luci-visual-options-workflow.mdc`)

1. In `luci-website`, confirm `persona-hero-subhead-gold` is clean and committed.
2. Create three branches off it: `upgrade-path-variant-a`, `upgrade-path-variant-b`, `upgrade-path-variant-c`. One direction per branch, built in minutes, not hours.
3. On each branch, edit only the UPGRADE PATH block and `.ug-upgrade*` CSS in `luci-upgrade-guide.astro`. Add JS for C inside the existing inline `<script>` IIFE, using its `reduceMo` flag.
4. `npm run build` on each and fix any errors.
5. Preview: `.37` can only show one branch at a time. For each branch, build, then capture screenshots of the `#ug-upgrade` section at **1440px and 390px** widths. Headless Chrome needs a unique `--user-data-dir` each run (old shared profiles hung last time). Save them as `/tmp/upgrade-path-{a,b,c}-{1440,390}.png`.
6. Deploy **Option A** to `.37` with `./deploy.sh` so Jane has one live to click through, unless she asks for another.
7. Commit each branch: `Upgrade path variant <X>: <direction>`.
8. Report back to Jane with the three screenshots labeled A/B/C, the branch names, the live URL, and the **flagged copy/label items** listed below. Don't merge. Jane picks.

## 5. Items to flag for Jane (decide after she picks)

- Remove the duplicate `rolloutNote` and `whatIsInvolved.paragraph` permanently?
- Approve the shortened fact values ("Coordinated weekly groups", "About one to two hours", "Stays online until you switch").
- Add "Cost: Included under your current contract" as a fact?
- Option C only: approve the short step labels (Schedule · Ships · Verify · Switch).

## 6. Don't

- Don't change `upgradeGuide.ts` copy or step order.
- Don't add a mint left bar, a deep-green bar+label divider, or dark navy icon tiles on the light canvas.
- Don't use flex-wrap pill/chip rows. Chrome produced a sub-pixel artifact on wrapped rows in the "Also in this upgrade" section. Use grid.
- Don't touch the frozen pillar tabs, feature rails, FAQ, or nav.
