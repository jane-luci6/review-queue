# LUCI Systems Design System

**Start here:** open [`index.html`](index.html) with Live Preview for the design system hub (nav left, live specimens right).

Workspace root is the parent **`luci-design`** folder — see [`../README.md`](../README.md).

## About LUCI Systems

LUCI Systems is an enterprise multimedia OS company serving the hospitality and gaming industry — casinos, resorts, and luxury hotels. Their software platform powers immersive guest experiences by allowing venue staff to manage all multimedia systems (TVs, audio, digital displays, content presets) from a single interface with one-touch simplicity.

**Core value propositions:**
- The Orchestration Engine for Enterprise Multimedia
- Powers immersive guest experiences
- Up to 90% reduction in hardware
- Drag-and-drop content management from any mobile device
- Unlimited users with customizable permissions
- Infinitely scalable, incredibly simple

**Founders:** Mike Epstein (CEO) and Nickolas Jensen (CIO) — 25+ years as integrators, owners, and operators.

**Key clients:** Osage Casino, Seneca Casino, Spirit Mountain Casino, Choctaw Casinos & Resort, Stanly Ranch, Valley View Casino & Hotel, Yamava Resort & Casino, Isleta Resort, etc.

---

## Sources

- **Figma file:** `LUCI - Web Design - External.fig` (mounted as VFS)
  - Page 1: `LUCI_digital_styleguide` — 26 frames covering colors, typography, CTAs, patterns, textures, components
  - Page 2: `Hi-Fi_microsite_V1` — 13 frames: full desktop + mobile microsite, 404 pages, demo modal
- **Uploaded assets:** logos (white/mint, black, mint, 500px), splash image, newsletter HTML mockup ("The Signal")

---

## CONTENT FUNDAMENTALS

### Voice & Tone
LUCI writes with authority and confidence — they are experts in a niche industry and speak like it. Copy is direct, technical-leaning but accessible. The brand is **serious but not stiff**.

### Casing
- **ALL CAPS** for all headers, subheaders, section labels, and CTAs — this is non-negotiable and rooted in the Syncopate typeface which is designed for uppercase
- **Sentence case** for body copy and descriptions
- **Title Case** for attribution, names, and partner/client names

### Person & Address
- Third person for company descriptions ("Our software powers…")
- First-person plural ("we design, implement, and support…")
- Direct address for CTAs ("request a demo", "learn about luci")

### Punctuation & Style
- No emoji anywhere in the brand
- En dashes used for ranges; no Oxford flourishes
- Short, punchy sentences for hero copy; longer explanation in body
- Numbers formatted large and bold for impact stats (e.g., "90%")
- Specific, operational language: "drag-and-drop," "one-touch," "unlimited users"

### Newsletter ("The Signal")
- A monthly customer newsletter. Tone is editorial — uses pull-quotes, case-study results, and short callouts.
- Section labels (department kickers) use SYNCOPATE all-caps centered between two short mint rules.
- Build new issues from `ui_kits/newsletter/the-signal-web-template.html`. Web issues live at `/the-signal/issue-NN`; the index is the Newsletter Hub.

#### Issue structure & editorial conventions *(decided Issue 01, Jun 2026)*
Every issue is built from two content types — **articles** and **callouts** — and they are treated differently:

- **Articles** are the substantive stories. They appear in the **"In this issue"** index, numbered (`01`, `02`, …) **in reading order**. Recurring article departments: *In the field* (field/case study), *What's coming* (platform/Platform), *Meet [name]* (team), *Inside LUCI* (how-to you can run in the platform), *Beyond the platform* (services).
- **Callouts** are short asides (e.g. *Quick tip*, *Support portal*). They are **NOT numbered and do NOT appear in the index.** Style them as contained navy blocks with a mint left bar on a white section (see "Callouts" under Visual Foundations) — never a full-bleed section flush against another colored section.
- **Order:** Welcome (CEO note) → **In this issue** (placed *after* the welcome) → **lead with the marquee story** (usually *In the field*) → remaining articles, with callouts interspersed as light beats between them → Closing → Footer.
- **Section color rhythm:** alternate `sec--white` and `sec--light` for reading sections so the eye keeps moving. Use `sec--marquee` (warm sand background + scaled headline) for the lead field story — it transitions cleanly from the dark TOC without a grey-on-navy clash. Callouts always sit on `sec--white`. Reserve `sec--deep` for the Closing (and Footer) — never for a mid-issue article, or it reads like the footer started early.
- The welcome note's preview of "what's in this issue" should match the actual article order.
- Keep team intros (*Meet [name]*) brief — a who/why, photo, and a "say hi" CTA. Don't pad.

### Examples of Copy in Use
- `"The Orchestration Engine for Enterprise Multimedia"`
- `"One interface to control, automate, and execute the entire guest experience."`
- `"YOUR MULTIMEDIA THOUGHT PARTNERS"`
- `"Scalable strategy and support to dazzle guests and optimize operations"`
- `"Trusted by Four-Star Destinations"`
- `"The operating solution for enterprise media systems"`

---

## VISUAL FOUNDATIONS

### Color System
See `colors_and_type.css` for CSS variables. Named palette (official brand names):

| Name | Hex | Usage |
|---|---|---|
| Pit Boss Blue | `#0A161C` | Deepest dark, hero backgrounds |
| Controlled Blue | `#10232D` | Primary dark background |
| Sportsbook Blue | `#314955` | Secondary dark sections |
| Immersive Slate | `#49616E` | Tertiary dark, client logo section bg |
| Loan Shark | `#A6B0B6` | Subdued borders, disabled |
| Integrayted | `#ABADB3` | Dividers, muted text |
| Unified Gray | `#535559` | Body text on light |
| The Sands | `#E5E3DF` | Primary light background |
| Ambient White | `#F5F8FA` | Cards, frosted glass elements |
| High Limit Mint | `#68E3BE` | Primary accent — interactive elements, section highlights |
| Jackpot Red | `#FA564C` | Secondary accent — key headers, founder names, attribution |

### Typography
- **Syncopate Bold** — All headers, subheaders, CTA labels, section names. Always UPPERCASE. No letter-spacing override (0%). Available on Google Fonts.
- **Space Grotesk** (Regular / Medium / Bold) — All body copy, descriptions, UI labels. Sentence case or Title Case. No letter-spacing override. Available on Google Fonts.
- **Montserrat Bold/Regular** — Used in some UI contexts (16px), secondary to Space Grotesk.

#### Type Scale
| Role | Font | Weight | Size |
|---|---|---|---|
| Hero Header | Syncopate | 700 | 55–96px |
| Section Header | Syncopate | 700 | 36–64px |
| Subheader | Syncopate | 700 | 24–32px |
| Label / CTA Large | Syncopate | 700 | 16–18px |
| Label / CTA Small | Syncopate | 700 | 14px |
| Body Large | Space Grotesk | 400 | 18px / 27px lh |
| Body Default | Space Grotesk | 400/500/700 | 16px / 21px lh |
| Body Small | Space Grotesk | 400 | 14px / 22px lh |

### Backgrounds & Texture
- Two primary background modes: **dark** (`#10232D`) and **light** (`#E5E3DF` The Sands).
- **Halftone/noise textures** (`assets/textures/`) overlaid at 50–94% opacity on hero and story sections. Apply with `mix-blend-mode: color-burn` over a flat-color base.
- **Isometric line patterns** (`assets/patterns/`) — geometric maze motif derived from the LUCI logomark. Available in 7 variants (PNG + SVG, for dark and light backgrounds).
- **Use sparingly.** One textured section and one patterned section per page is the maximum. Default to flat colors.
- No gradients — the brand avoids gradient backgrounds entirely.

### Borders & Dividers
- **1px solid** rules (`rgb(16,35,45)`) as primary section dividers — entire blocks are separated by hairline borders
- Full-width horizontal rules used inline to extend section labels (e.g., "what we do ——————")
- No gradient dividers; always hard lines

### Cards & Containers
- **Quote cards**: `border-radius: 4px`, `backdrop-filter: blur(15px)`, `background: rgba(245,248,250, 0.80)`, `box-shadow: 0 0 20px rgba(36,34,38, 0.7)` — frosted glass effect
- **Content cards**: `background: rgba(245,248,250, 0.65)`, same blur/shadow treatment
- **Person cards**: `border: 1.5px solid #10232D`, hard corners, no radius
- **All other containers**: sharp corners (`border-radius: 0`) — this is a defining brand trait

### Containment & Minimalism (de-boxed)
LUCI is a modern, edgy 2026 tech brand. **Whitespace, typography, and hairlines carry structure — not stacked containers.** Boxes are the exception, never the default. This is the standard for everything we design.

- **Separate with space + a single hairline**, not bordered boxes. Use one 1px divider (`rgba(255,255,255,0.1)` on dark, `--rule-light` on light) or generous padding.
- **Don't double up containment** — never wrap content in an outer border *and* add internal dividers; pick one.
- **Tabular data → de-boxed lists.** Render rows as a definition list / stacked rows with hairline separators, not an HTML `<table>` with cell borders (also avoids mobile horizontal scroll).
- **No spreadsheet grids** — avoid 1px-gap grids of filled cells for stats/results; use airy rows with mint numerals instead.
- **Reserve the 4px mint accent bar** for true callouts, pull quotes, and the masthead signature only — not every element.
- **No drop shadows on flat content tiles; no gradients.**
- Reference: `ui_kits/newsletter/the-signal-design-comparison.html` (Current vs Sharp de-boxed).

**Callouts (asides) — the sanctioned exception.** Tips, support prompts, and other asides *should* be contained, because an aside needs to read as separate from the article flow:
- A callout is a **contained block** with a 4px mint left bar, sharp corners, and real padding (`clamp(24px,4vw,32px)`) — typically a navy block sitting on a light section.
- **Bracket it with whitespace.** Never place a callout as a full-bleed section flush against another colored section (they bleed together). Let the surrounding section's padding frame it.
- Callouts are not numbered articles and don't appear in the "In this issue" index.

### CTAs (Buttons)
Three variants, all sharp-cornered:
- **Primary**: Filled `#10232D` bg, `#F5F8FA` text + arrow, Syncopate Bold, `padding: 20px` (large) or `13px 16px` (small)
- **Secondary**: Outlined `2px solid #0A161C`, transparent bg, dark text + arrow
- **Tertiary**: Text-only with inline arrow (`→`), Syncopate Bold, dark text. Used as accordion/section labels.
- **Text Link**: Space Grotesk Bold 15px, underlined, + optional `+` icon prefix
- Arrow treatment: horizontal line + arrowhead SVG, proportional to button size

### Icons
- Two primary icons: `icon_plus` (crosshair/plus) and `icon_carat` (chevron/caret pointing down)
- Hand-drawn SVG paths — minimal, geometric, 12–16px
- No icon library — bespoke SVG only
- Color matches context: dark on light, light on dark

### Animation & Interaction
- No animation system defined in Figma; static-first
- Hover states implied: opacity shifts, color darkening
- Frosted glass cards suggest subtle depth on hover

### Spacing & Layout
- **Desktop canvas**: 1440px wide, `padding: 0 64px` for content sections
- **Mobile canvas**: 390px wide, `padding: 0 24px`
- **Section vertical padding**: typically `64px` top/bottom
- **Gap scale**: 4, 8, 12, 16, 24, 36, 48, 64px

### Imagery
- Real hospitality/casino photography used in testimonial sections
- Product UI mockups (tablet/app wireframes) used in feature sections — line-art style with mint and red accent fills
- No illustrations; no stock-photo icons
- Images feel cool/moody — dark environments, premium hospitality

### Shadows
- Cards: `box-shadow: 0 0 20px rgba(36,34,38, 0.7)` (heavy) or `0 0 20px rgba(36,34,38, 0.2)` (light)
- No drop shadows on buttons or flat elements

---

## ICONOGRAPHY

LUCI uses **bespoke SVG icons only** — no third-party icon library or font.

**Core icons (copied to `assets/`):**
- `LUCI-logo.svg` — the logomark (geometric chevron/stack mark)
- Plus icon (`icon_plus`): crosshair `+` shape, 14×14px, 2px stroke paths
- Carat icon (`icon_carat`): downward chevron `∨`, 11×7px
- Arrow right: horizontal line + arrowhead, used exclusively inside CTA buttons

**Logo files** (`assets/logos/`):
- `luci-full-black.png` — Full lockup, black. Default on light bg.
- `luci-full-white.png` — Full lockup, white. Default on dark bg.
- `luci-full-mint.png` — Full lockup, mint. Accent on dark bg only.
- `luci-full-mintmark-blacktext.png` — Mixed: mint mark + black text. Use on light bg for emphasis.
- `luci-mark-black.png` · `luci-mark-white.png` · `luci-mark-mint.png` — Logomark only.
- `luci-mark-mint-square.png` (500×500) · `luci-social-icon.png` — Social avatars.
- `luci-wordmark-black.png` — Wordmark only (rare; use full lockup by default).
- `assets/LUCI-logo.svg` — Vector mark for any scale.
- `assets/luci-splash.jpg` — Brand splash photography.

**Usage rules:**
- Logo always appears centered in nav bar with extra optical padding to the right (use `logo_FOR_NAV` variant in Figma)
- Logomark used as a section indicator (small, ~20–38px) before section titles like "what we do"
- No emoji. No unicode symbols used decoratively.

---

## FILE INDEX

```
index.html                   ← Design system hub (open with Live Preview)
README.md                    ← You are here
colors_and_type.css          ← All CSS custom properties (colors + type)

assets/
  logo-white-mint.png        ← Logo: white + mint on dark bg
  logo-black.png             ← Logo: full black on light bg
  logo-mint.png              ← Logo: mint logomark only
  logo-500px.png             ← Logo: full color 500px
  LUCI-logo.svg              ← SVG logomark
  splash.jpg                 ← Hero splash image

preview/
  colors-neutrals.html       ← Neutral color swatches
  colors-brand.html          ← Brand accent + dark scale
  type-headers.html          ← Syncopate header specimens
  type-body.html             ← Space Grotesk body specimens
  ctas.html                  ← CTA button variants
  cards.html                 ← Card / container patterns
  spacing.html               ← Spacing + layout tokens
  brand-logos.html           ← Logo usage
  brand-textures.html        ← Texture / background patterns

ui_kits/
  website/
    README.md                ← Website UI kit notes
    index.html               ← Full microsite prototype
    Nav.jsx                  ← Navigation component
    Hero.jsx                 ← Hero section
    WhatWeDo.jsx             ← What we do section
    Benefits.jsx             ← Benefits section
    ProductOverview.jsx      ← Product overview grid
    Testimonials.jsx         ← Testimonial carousel
    Team.jsx                 ← Founders/team section
    ClientLogos.jsx          ← Client logo soup
    Stats.jsx                ← Quantified impact stats
    Footer.jsx               ← Footer component
    CTAs.jsx                 ← All CTA button components
```
