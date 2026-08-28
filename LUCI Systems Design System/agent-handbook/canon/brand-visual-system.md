# Canon — brand and visual system

**Snapshot:** 28 August 2026  
**Sources (read these in Cursor for full text):**  
`luci-modern-design-guidelines.mdc`, `luci-visual-design.mdc`, `luci-dual-accent-system.mdc`, `luci-mint-primary-gold-secondary.mdc`, `luci-website-pattern-standard.mdc`, `luci-image-prompt-rules.mdc`, `luci-canonical-assets.mdc`, `assets/fonts/luci-brand-fonts.css`

This file is the Grok-portable summary. If a rule file is newer, the rule wins.

---

## Design Direction owns this file

Nothing is built until Jane or CoS settles direction. Maker applies tokens; Maker does not invent colors, type, or a new pattern.

**Jane’s Design Direction one-liner:** Navy, mint on dark only, Syncopate for short display, Space Grotesk for real type, sharp, de-boxed, proof over stat grids.

---

## Palette

| Token | Hex | Use |
|---|---|---|
| Navy deep | `#0A161C` | Heroes, bookends, footer |
| Navy | `#10232D` | Dark panels |
| Mint | `#68E3BE` | Accent **on dark only** |
| Light accent | `#2b9e80` | **The** accent on white/off-white/light — kickers, labels, links, bars, icons |
| Gold | `#EDD086` | Text/accent **on dark only** |
| Gold deep | `#CEB06E` | **Non-text** on light (icon strokes, tints) |
| Sand | `#E5E3DF` | Warm light panels |
| Off-white | `#F5F8FA` | Reading canvas (not pure `#FFF`) |
| Body ink | `#354F5C` | Body on light |

**Retired:** `#176B54`; Jackpot Red as brand accent; dark gold text (`#c9a24e`, `#6F5521`, etc.) on light.

**Mint vs gold:** Mint is primary (lockup rules, eyebrows, primary CTAs, structure). Gold is secondary (watermarks, duotone details, sand callout bars). Do not paint lockup name/rule/role gold.

**Atmosphere tints** (website, one per section, not competing with a mint hero): Harbor `#4A7285`, Clay `#B8926A`, Dusk `#8A7FA6` at low opacity.

**Contrast:** Body ≥ 4.5:1. Bright mint on sand is forbidden (~1.23:1). `#2b9e80` on off-white is the accepted light accent (~3.1).

---

## Type

| Tier | Face | Role |
|---|---|---|
| 1 Display | Syncopate 700 | Masthead, 1–3 word title, large numerals, tiny tracked labels. **Hard limit:** ≤3 words AND ≤~25 characters AND single line. If it wraps, it is not Syncopate. |
| 2 Structure | Space Grotesk 700 | Real headlines, section titles, brand names, metric numerals, kickers |
| 3 Body / recede | Inter 400 | **All running copy** — paragraphs, decks, notes, tables, diagram labels/captions |

One display-scale moment per asset. Section headers on the website (not homepage) use the SectionBlock **lockup**: big name (Space Grotesk) → 40×3px mint rule → small tracked role. Shorter string = name; longer = role.

---

## Layout and separation

- Spacing: **8px** scale (4px only for tight type).
- Reading measure: body **60–70ch**.
- De-boxed: space and hairlines, not stacked boxes. Sharp corners are a brand trait on core brand surfaces.
- 4px mint bar: true callouts and pull quotes — not every element.
- Tracks by copy density: **A** interactive/web (dark OK); **B** slides/social; **C** long documents (light required).
- New assets follow modern guidelines. Do not silently restyle old newsletters unless Jane asks.

**Soft-icon tiles on light (canonical for icon-led points):** ~54px, radius 16px, soft mint gradient, inset mint hairline, duotone icon (mint strokes + one gold accent). Not dark navy icon tiles. Not deep-green bar + uppercase label as a section divider.

---

## Website circuit pattern (webpages only)

One file: `/images/textures/texture-circuit-header-mintgold.png`. **Never tile.** Cover, no-repeat, center. `mix-blend-mode: lighten; opacity: 0.22` + navy veil. Dark sections only. First dark content band after hero (homepage exception: HomeDifferentiator + HomeWhyItMatters). **Not** on case studies, blog, newsletter, FAG, resources.

---

## Case study visual template (case studies only)

Do **not** copy this header treatment onto newsletters, sales docs, or the marketing site chrome.

- Hero: navy-deep, 4px mint bottom border, kicker “Case Study”, split title (Space Grotesk lead-in + Syncopate `<em>` mint).
- Sam’s Town is the standing visual template: photo-band with horizontal scrim, inline photo, mid-section mint radial wash, scope-story title mint + white “to date”.
- Narrative: see messaging canon + `luci-case-studies.mdc`.

---

## Diagrams

- Master: `LUCI Systems Design System/assets/diagrams/<name>.svg` — edit **content**, never canvas size to fit a consumer.
- Each asset copies and crops its own file. Relative path + `?v=N`.
- Never paste inline SVG markup into a document.
- Propagate only when Jane says propagate / ship / lock in.

Key masters: `luci-what-luci-is`, `luci-system-architecture`, `luci-consolidation-ledger`, `embedded-operation-orbit`.

---

## Photography / image prompts

Look like LUCI commissioned the photo. Kill AI tells (HDR, plastic skin, purple haze, perfect symmetry). Practical light. Specific materials. Casino = ops infrastructure, not roulette/chips. **Before** shots: no LUCI branding. **After:** LUCI can appear. People: candid, not smiling-at-camera.

Negative prompt (default): `generic stock photo, polished, sterile, perfect symmetry, cinematic, epic, futuristic, blue haze, purple haze, HDR, oversaturated, illustration, 3D render, posed model, stock-photo cliché, smiling at camera, watermark, text overlay`

Reference real client environments in OneDrive Project Media. Website `public/images/industries/` AI images are **not** ground truth.

---

## Open visual work (do not relitigate parked items)

- Ticker NFL names on homepage photo: parked. No blur, no card-over.
- E-mesh: SVG done; CTA/footer pending Jane.
- Yaamava layout variant on capabilities/retrofit: waiting Jane pick.
- Sam’s Town section spatial variants: untracked preview on website 28 Aug — Design Direction, then Jane, then Maker.
