# CURSOR BRIEF — Platform page mockup, round 3 (GLM)

**Repo:** `luci-website`
**Owner:** GLM (build) · design direction by Claude · copy by GPT/Jane
**Supersedes:** the "What LUCI is" section in `~/.cursor/plans/how_luci_works_04b3f80a.plan.md` (§ Platform page, section 2). Every other section of that plan stays as written.

Jane reviewed `http://10.10.1.37/mockup-platform.html` and asked for four changes:

1. The rack is **one rack**, not half a rack.
2. The top of the mockup doesn't match the other pages. It reads too tall.
3. The LUCI/Systems explainer under the diagram needs a real design.
4. The explainer headings should be **The Orchestration Platform** and **The Embedded Team**. Don't repeat "LUCI" and "Systems" (the diagram already names them), and show that the embedded team is covered in detail on another page.

---

## 1. Rebuild the mockup on the real site components (fixes the header)

The current mockup is a hand-built HTML file with a fake header, fake chapter nav, and a gold banner. That's why it doesn't match. Stop patching it.

- **Create** `src/pages/previews/platform-mockup.astro`.
- Wrap it in `BaseLayout` with `noindex` and `darkHeader`, exactly as `src/pages/platform.astro` does. This gives the real site header (96px), real logo, real chapter nav, and real footer.
- Use the real components: `PlatformChapterNav`, `PlatformHeroStage`, `SectionBlock`, `PlatformArchitectureStage`, and `PlatformOrbit` (the real interactive orbit, not a placeholder box).
- No mockup banner. Put "Preview" in the page `title` only.
- **Do not edit any live data file** (`features.ts`, `site.ts`, `integrations.ts`, `Header.astro`). Keep all preview-only copy inline in the preview page. The live `/platform` must not change until Jane approves.
- The header will still read "Platform" in this preview. The "What is LUCI?" rename ships with the real build. Jane has already approved it.
- When the preview is live, **delete** `luci-website/mockup-platform.html` and `luci-website/public/mockup-platform.html`.

Preview URL after deploy: `http://10.10.1.37/previews/platform-mockup/`

**Hero:** `PlatformHeroStage` unchanged. Same min-height, photo, scrim, and Syncopate lockup as `/platform` and `/platform/services`. Only the deck changes (copy in § 4).

**"What LUCI is" lockup:** the role line was too long and read as a second headline. Shorten it to **The platform and the team behind it**.

## 2. "What LUCI is" — section structure

`SectionBlock` with `id="what-luci-is"`, `tone="deep"`, `wide`. Keep the existing padding override and the global mesh/veil CSS from `platform.astro` (copy those rules into the preview page's global style block, keyed to `#what-luci-is`).

In order:

1. Lockup and deck (copy in § 4).
2. The **original diagram, unchanged:** `<img src="/images/diagrams/luci-what-luci-is.dark.svg?v=1">` inside `<figure class="diagram-block diagram-block--parent diagram-reveal">`, `max-width: 860px`, exactly as on the live page. Do not edit, crop, or redraw the SVG. It is a canonical asset.
3. The **new explainer** (§ 3), directly under the diagram at the same 860px width, so it reads as the diagram's caption system rather than a separate block.

## 3. The explainer — design spec

### Concept

The explainer continues the diagram. Two columns split at the diagram's "+". Each column centers under its own diagram label. A short mint drop-line runs from each label down into its column, so the eye reads diagram, then definition, top to bottom.

```
        [ rack + devices ]           +        [ team / gear ]
             LUCI                                Systems
   THE ORCHESTRATION PLATFORM            THE EMBEDDED OPERATION
               |                       |              |
         WHAT RUNS YOUR A/V            |   INCLUDED IN EVERY SUBSCRIPTION
     The Orchestration Platform        |        The Embedded Team
     Orchestration software and        |   Plans the environment with you,
     one rack of standardized ...      |   coordinates architects, ...
     Built on IP distribution ...      |
     See the technology →              |   How the embedded team works →
```

### Geometry (why these numbers)

The diagram SVG's `viewBox` is `6 0 560 300`. The LUCI label is centered at x=177, the "+" at x=350, and Systems at x=462. As fractions of the width: LUCI ≈ 30.5%, "+" ≈ 61.4%, Systems ≈ 81.4%.

A grid split at 61.4% puts the left column's center at 30.7% and the right column's center at 80.7%, within about 1% of each label. Use this split. Don't use 50/50, which would put the right column visibly off-center from "Systems".

### Markup

```html
<div class="luci-explain diagram-reveal">
  <div class="luci-explain__col luci-explain__col--platform">
    <p class="luci-explain__eyebrow">What runs your A/V</p>
    <h3 class="luci-explain__title">The Orchestration Platform</h3>
    <p class="luci-explain__body">…</p>
    <p class="luci-explain__body luci-explain__body--strong">…</p>
    <a class="luci-explain__link" href="#technology">See the technology <span aria-hidden="true">&rarr;</span></a>
  </div>
  <div class="luci-explain__col luci-explain__col--team">
    <p class="luci-explain__eyebrow luci-explain__eyebrow--gold">Included in every subscription</p>
    <h3 class="luci-explain__title">The Embedded Team</h3>
    <p class="luci-explain__body">…</p>
    <a class="luci-explain__link" href="/platform/services">How the embedded team works <span aria-hidden="true">&rarr;</span></a>
  </div>
</div>
```

### CSS (desktop, ≥ 760px)

```css
.luci-explain {
  display: grid;
  grid-template-columns: 61.4fr 38.6fr;
  max-width: 860px;
  margin-top: var(--space-3);
}
.luci-explain__col {
  position: relative;
  padding: var(--space-5) var(--space-4) 0;   /* top room for the drop-line */
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
}
/* Mint drop-line from the diagram label into the column */
.luci-explain__col::before {
  content: '';
  position: absolute;
  top: 0;
  left: 50%;
  width: 1px;
  height: 24px;
  background: linear-gradient(to bottom, rgba(104, 227, 190, 0), rgba(104, 227, 190, 0.55));
}
/* Vertical hairline at the "+" split */
.luci-explain__col--team {
  border-left: 1px solid rgba(104, 227, 190, 0.16);
}
.luci-explain__eyebrow {
  font-family: var(--font-head);
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  line-height: 1.4;
  color: var(--mint);
  margin: 0 0 var(--space-1);
}
.luci-explain__eyebrow--gold { color: var(--gold); }
.luci-explain__title {
  font-family: var(--font-head);
  font-size: clamp(20px, 2.2vw, 24px);
  font-weight: 700;
  line-height: 1.15;
  letter-spacing: -0.015em;
  color: var(--off-white);
  margin: 0 0 var(--space-2);
}
.luci-explain__body {
  font-family: var(--font-body);
  font-size: 15px;
  line-height: 1.65;
  color: rgba(245, 248, 250, 0.78);
  max-width: 40ch;
  margin: 0;
}
.luci-explain__body + .luci-explain__body { margin-top: var(--space-2); }
.luci-explain__body--strong { color: rgba(245, 248, 250, 0.94); }
.luci-explain__link {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  min-height: 44px;
  margin-top: auto;            /* both links sit on the same baseline */
  padding-top: var(--space-3);
  font-family: var(--font-head);
  font-size: 15px;
  font-weight: 600;
  color: var(--mint);
  text-decoration: none;
  transition: gap 0.15s ease;
}
.luci-explain__link:hover,
.luci-explain__link:focus-visible { gap: 12px; text-decoration: underline; text-underline-offset: 4px; }
```

Notes:

- `margin-top: auto` on the links plus the grid's equal-height columns keeps both links aligned on one line, even though the left column has more copy.
- The `.diagram-reveal` class on `.luci-explain` reuses the page's existing bloom script. Give it `style="--i:1"` so it reveals just after the diagram.
- The left column's IP line (`--strong`) is the one sentence that previews the Technology section. It gets the slightly brighter color, but no bold and no accent color.
- Gold appears only on the right column's eyebrow, as the secondary accent. Mint stays primary everywhere else.

### Mobile (< 760px)

```css
@media (max-width: 759px) {
  .luci-explain { grid-template-columns: 1fr; }
  .luci-explain__col {
    padding: var(--space-4) 0 0;
    text-align: left;
    align-items: flex-start;
  }
  .luci-explain__col::before { display: none; }
  .luci-explain__col--team {
    border-left: 0;
    border-top: 1px solid rgba(104, 227, 190, 0.16);
    margin-top: var(--space-4);
  }
  .luci-explain__link { margin-top: 0; }
}
```

On mobile the diagram shrinks, so the drop-lines no longer line up with anything. Drop them, left-align the text, and stack the columns with a hairline between them.

### Don't

- No boxes, cards, backgrounds, or icons in the explainer.
- No "LUCI" or "Systems" in the explainer headings or eyebrows. The diagram already names them.
- Don't remove the old `.luci-def*` classes by hand-editing the old mockup. The old mockup gets deleted.

## 4. Copy for this round

The only copy changes from the round 2 mockup are below. GPT/Jane may refine wording later; build with these.

**Hero deck:** LUCI is software for operating every display, source, audio zone, and connected system across a property from one interface.

**What LUCI is**
- Lockup name: **What LUCI is**
- Lockup role: **The platform and the team behind it**
- Deck: **Every LUCI subscription combines the platform that runs your A/V with the embedded team that plans, deploys, and supports it. Both are included from day one.**

**Left column**
- Eyebrow: **What runs your A/V**
- Title: **The Orchestration Platform**
- Body: **Orchestration software and one rack of standardized hardware. Together they run your property's A/V and give your team one interface to control it.**
- Strong line: **Built on IP distribution, so content reaches any display on the property without a dedicated source player behind each one.**
- Link: **See the technology →** (`#technology`)

**Right column**
- Eyebrow: **Included in every subscription**
- Title: **The Embedded Team**
- Body: **Plans the environment with you, coordinates architects, integrators, vendors, and trades around one operating standard, and stays accountable through deployment and support, so the A/V is built right from the start.**
- Link: **How the embedded team works →** (`/platform/services`)

**Rack count everywhere:** the platform runs on **one rack**. Search the preview for "half" and "1/2" and remove both. The architecture callouts and FAQ already say one standardized rack; keep that.

## 5. Rest of the page

Build every other section exactly as specified in the plan file (Capabilities, Technology, The team is part of LUCI, FAQ on mid, CTA), using the real components. Specifically:

- **Capabilities:** the real `feature-grid` markup and CSS from `platform.astro`, with the six updated card strings inline.
- **Technology:** the real `PlatformArchitectureStage`, the `tech-intro` block and pull line, the hardware note, and the three callouts with the new icons (SVG markup is in the plan).
- **Team section:** the real `PlatformOrbit`. Link label: **See the embedded services included with LUCI →**

## 6. QA, then deploy

- `npm run build` passes, and no lint errors in the new page.
- Compare `/previews/platform-mockup/` with `/platform/services/` at 1440px: the header, chapter nav, and hero heights match.
- The explainer columns center under the diagram's "LUCI" and "Systems" labels at 1280px and 1440px (eyeball it; within a few pixels).
- Both explainer links sit on the same line on desktop.
- The explainer stacks cleanly at 375px.
- Reduced motion: the diagram and explainer show their end state immediately.
- Copy: "A/V" never "AV", "one rack" (no "half"), and no "layer" for LUCI.
- Deploy with `./deploy.sh`, then confirm `http://10.10.1.37/previews/platform-mockup/` returns 200 and the two old mockup files return 404.
- Commit: `Platform preview r3: real components, original diagram + aligned explainer, one rack`.
- Send Jane the preview URL and remind her to hard-refresh (Cmd+Shift+R). **Do not touch `/platform` until she approves.**
