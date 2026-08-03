# LUCI brand assets — build context

Read this before using anything in this folder. It is written for a coding agent;
the rules below prevent the most likely mistakes.

## What these are

Dark, technical background art: a connected node/line mesh over a faded venue
floorplan. The visual idea is LUCI as the connective tissue orchestrating a
venue. Backgrounds contain **no logo and no text** — place those yourself.

## Palette

| Token | Hex | Use |
|---|---|---|
| `--luci-bg-deep` | `#070F14` | page background, and the fallback behind every background image |
| `--luci-bg-lift` | `#10232C` | centre of the background wash |
| `--luci-mint` | `#68E3BE` | primary accent, mesh lines, links, focus rings |
| `--luci-gold` | `#E8D8A4` | sparing accent only — a few nodes and one highlighted phrase |
| `--luci-white` | `#F5F8FA` | headings and body text on dark |

Always set `background-color: #070F14` alongside a background image. The SVGs do
not paint the full frame at every aspect ratio, and a white flash before load
looks broken against this palette.

## Which background file

| File | Use | Notes |
|---|---|---|
| `backgrounds/luci-bg-hero-1920x1080.svg` | 16:9 hero, general page background | default choice |
| `backgrounds/luci-bg-wide-2560x800.svg` | wide section band, CTA strip, footer | shallow layout |
| `backgrounds/luci-bg-portrait-1080x1920.svg` | mobile hero, portrait panels | use below ~700px viewport |
| `backgrounds/luci-bg-hero-mesh-only-1920x1080.svg` | any of the above, lighter | 10 KB, no floorplan, recolourable |
| `backgrounds/luci-plan-texture-1920x1080.png` | optional | floorplan alone, transparent, for layering |

Every SVG has `preserveAspectRatio="xMidYMid slice"`, so it crops to fill like
`background-size: cover` rather than distorting. **Never** override this, and
never set `width`/`height` in a way that changes the aspect ratio.

## Usage

```css
.hero {
  background: #070F14 url("/backgrounds/luci-bg-hero-1920x1080.svg")
              center / cover no-repeat;
  min-height: 60vh;
}
@media (max-width: 700px) {
  .hero { background-image: url("/backgrounds/luci-bg-portrait-1080x1920.svg"); }
}
```

As an element behind content:

```html
<div class="hero">
  <img class="hero-bg" src="/backgrounds/luci-bg-hero-1920x1080.svg" alt="" aria-hidden="true">
  <h1>…</h1>
</div>
```
```css
.hero    { position: relative; isolation: isolate; }
.hero-bg { position: absolute; inset: 0; width: 100%; height: 100%;
           object-fit: cover; z-index: -1; }
```

Backgrounds are decorative: `alt=""` and `aria-hidden="true"`. Do not describe
them to screen readers.

## Text over the background

Contrast is not the constraint. Measured on the 1920×1080 hero, 0–255 luma:

| Region | Mean | p95 | `#F5F8FA` contrast |
|---|---|---|---|
| Top third | 24.2 | 44 | 16.6:1 |
| Middle third | 25.4 | 31 | — |
| Lower half | 22.1 | 28 | 17.0:1 |
| Overall | 23.4 | 32 | — |

White text clears WCAG AA everywhere on these backgrounds by a wide margin —
roughly 17:1 against a 4.5:1 requirement. Body text and headings are safe
anywhere.

The actual constraint is **busyness, not brightness**. The top third holds the
floorplan, and its p95 is 44 against 28 for the lower half — same average, more
fine detail. Small text over that detail reads as cluttered even though it is
legible. So:

- Headlines: fine anywhere, including the top third
- Body copy and anything below ~16px: prefer the lower two-thirds
- If small text must sit over the top third, add a scrim:
  `background: linear-gradient(transparent, rgba(7,15,20,.85))`

## Recolouring

Every group carries a class: `.luci-mesh`, `.luci-node`, `.luci-port`,
`.luci-accent`, `.luci-plan`.

To restyle, **inline the SVG** — paste the markup, or use an SVG loader
(`vite-plugin-svgr`, `@svgr/webpack`, Next.js `dangerouslySetInnerHTML`). Any CSS
rule from the page beats the built-in colour, because presentation attributes
lose to stylesheet rules:

```css
.hero svg .luci-mesh { stroke: #7FF0CC; }
.hero svg .luci-node,
.hero svg .luci-port { fill: #7FF0CC; stroke: #7FF0CC; }
```

This does **not** work through `<img>` or `background-image` — those render in an
isolated context. Inline it if you need to restyle.

Two things you cannot change in CSS:

- The floorplan layer is a pre-tinted embedded raster. Its opacity is adjustable
  (`#plan { opacity: … }` when inlined) but not its hue.
- The background wash is a `<radialGradient>` with literal stops.

Do not rewrite the SVGs to use `var()` for colour. It was tried and removed: in a
non-browser renderer, `var()` in a presentation attribute renders blank in one
form and crashes the parser in another. Browsers are fine with it; build
pipelines, optimisers and PDF exporters are not.

## Logo

| File | Use |
|---|---|
| `logo/luci-logo-full-480w.png` | header lockup, 1x |
| `logo/luci-logo-full-960w.png` | header lockup, 2x — pair via `srcset` |
| `logo/luci-mark-96.png` / `-192.png` | compact nav, avatar, favicon source |
| `logo/luci-mark-512.png` | app icon, `og:image` source |

Lockup aspect ratio is **4.1804** — set `width` and `height` attributes to
matching values to reserve space and avoid layout shift. Never stretch it, never
recolour it, never add a container shape (circle, badge, rounded square) around
the mark. Clear space around the lockup should be at least the height of the icon.

**These are PNG, not SVG.** No vector logo was available. Ask the brand owner for
an SVG before launch — a raster logo in a site header will look soft on high-DPI
displays at large sizes. The PNGs above are sized for their intended use and will
be fine at those sizes, but do not scale them up.

## Tagline

> The **Orchestration Engine** for Enterprise Multimedia

Set as live text, not an image. "Orchestration Engine" is emphasised in
`--luci-gold` at a heavier weight; the rest is `--luci-white` at light weight.
Reference typeface is Lato (Light for body, Semibold for the emphasis); substitute
a similar humanist sans if Lato is not in the stack.

## Performance

| File | Size |
|---|---|
| hero | 79 KB |
| wide | 58 KB |
| portrait | 137 KB |
| mesh only | 10 KB |
| plan texture PNG | 164 KB |

The floorplan is embedded as base64 WebP, which is why the full versions are
larger than the mesh-only one. If the hero is above the fold, preload it:

```html
<link rel="preload" as="image" href="/backgrounds/luci-bg-hero-1920x1080.svg">
```

If you need to cut weight, use the mesh-only SVG and layer the plan texture as a
separate, lazily-loaded image — or drop the plan entirely on mobile.

Serve SVGs gzipped or brotli'd. The mesh geometry is plain text and compresses
well; the embedded WebP does not compress further.

## Do not

- Do not stretch, skew, or change the aspect ratio of any asset
- Do not tile or repeat the backgrounds — they are compositions, not patterns
- Do not place the logo on the busy top third of a background without a scrim
- Do not use gold for anything other than a small accent
- Do not re-encode the SVGs through a lossy optimiser without visually checking
  the result; the embedded raster and the `preserveAspectRatio` behaviour are
  both easy to break
- Do not use these backgrounds behind long-form body copy at full strength; fade
  or scrim them first

## Provenance

The floorplan is traced from a real venue plan. Labels and zone highlights were
removed, but the footprint is authentic and could be recognised by someone who
knows the property. Confirm with the brand owner before using it on public
marketing pages.

`demo.html` in this folder shows all of the above working in a page.
