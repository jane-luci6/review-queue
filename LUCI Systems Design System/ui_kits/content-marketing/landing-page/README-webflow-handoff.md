# LUCI social landing page — Webflow handoff

**Target URL:** `lucisystems.com/luci`
**Files:** `index.html`, `webflow-HEAD.html`, `webflow-BODY.html`, `/images`

A condensed version of the new homepage, cut to one job: walk a visitor through
the LUCI solution and get them to request a demo. Open `index.html` in a browser
to review it.

---

## Page flow

| # | Section | id | Source |
|---|---|---|---|
| 1 | Nav — logo + one CTA | `section-nav` | Homepage, stripped to a single action |
| 2 | Hero — "Control your whole property." + floor map | `section-hero` | Homepage hero |
| 3 | Silos → "run them all" | `section-silos` | Homepage |
| 4 | Control / Automate / Execute | `section-interface` | Homepage + brochure p1 |
| 5 | Less hardware, fewer vendors (comparison) | `section-consolidation` | Homepage |
| 6 | Why properties move to LUCI (4 cards) | `section-capabilities` | Homepage + brochure p1 |
| 7 | Trusted on live floors (logos) | `section-proof` | Homepage |
| 8 | Next step — demo form | `demo` | New |
| 9 | Footer | `section-footer` | Homepage |

**Deliberately dropped from the homepage:** the "Running on floors like yours"
industry carousel, the "How will LUCI support you?" role cards, the Ameristar case
study strip, and the "Go deeper" blog/resources block. Each of those sends people
sideways; on a page whose only job is the demo, they cost conversions. The case
study is the one worth reconsidering — it's strong proof — but it needs a
destination, and the site isn't live yet.

**Nav is intentionally one CTA, no site navigation.** Standard landing-page
practice: every nav link is an exit without converting. It also sidesteps the
problem of linking to the current site while the rebrand is in flight.

---

## What still needs your input

Ten `[TODO]` markers in `index.html`, in three groups:

**1. The comparison table** (`#section-consolidation`). I could read `4+ → 1`,
`40 Gb → 1 Gb`, `$1,000s → Included` and `Locked → Yours` off your screenshot, but
not the row labels, and not the `5+ / 12+ / 100+` rows. Send me that copy and I'll
finish it. Built as real HTML rather than an exported image on purpose, so the
numbers stay editable in Webflow.

**2. Property logos** (`#section-proof`). Three placeholder slots. The homepage
shows Chinook Winds, Snoqualmie and a third I couldn't make out. Logo files aren't
in this project — export them from the Webflow build.

**3. The hero image.** Currently `floor-map.jpg`, generated from
`map-final-v7.png`. Your new homepage uses a different, wider floor map render
that looks better in that slot. If you can export it, drop it in `/images` and
I'll swap it.

Note on `map-final-v7.png`: the "Hotel Lobby" label was rebuilt in v7 — the pill
had drifted off its text when the red offline-zone overlays were removed from the
original screenshot. Use v7 or later, never v6.

---

## Porting order

1. **Variables first.** Every colour and size is a CSS custom property in `:root`.
   Recreate those as Webflow variables before building anything else. Palette was
   sampled from the sales brochure PDF: navy `#10232D`, mint `#68E3BE`, gold
   `#EDD086`, cream `#F3F7F8`, plus `--slate:#2C4956` for the band between dark
   sections.
2. **Font.** Space Grotesk (400/500/600/700), Google Fonts. Add under Project
   Settings → Fonts. Syncopate is *not* used here — that was specific to the social
   carousel.
3. **Paste the two files.** `webflow-HEAD.html` → Page Settings → Inside `<head>`
   tag. `webflow-BODY.html` → a single HTML Embed. Head is ~11K characters; if
   Webflow rejects it for size, move the CSS to a hosted stylesheet.
4. **Images.** Three in use: `floor-map.jpg`, `luci-logo-white-mint.png`,
   `texture-isometric.png`. Upload to Webflow assets and relink. Alt text is
   already written — keep it. (`post-001-orchestration.jpg` and `zone-access.jpg`
   are leftovers from an earlier version and can be deleted.)
5. **The form.** Replace the whole `<form id="demoForm">` with your ActiveCampaign
   embed, then **delete the inline `<script>`** at the bottom of the file — it only
   fakes a success state for preview and is not a backend.

   In AC, set the post-submit behaviour under *Website → your form → Edit Design →
   Options → On Submit*: either "Show Thank You" with a message, or "Open URL" to
   redirect. Worth checking the existing site form's setting too — if it's on the
   default and showing nothing, that's the same fix.

6. **Icons.** Inline SVG, no icon library. Paste into Embed elements or swap for
   Webflow's icon handling. Strokes are mint `#68E3BE` on the dark cards.

---

## Design conventions carried over

- Mint eyebrow with wide letter-spacing above each section headline.
- One accent word per headline — mint or gold, never both in the same headline.
- Gold reserved for accent words and numerals. Never body copy.
- Big translucent mint numerals bottom-right of the capability cards.
- Isometric texture as a low-opacity wash (7–10%) on dark sections only.
- Full-bleed mint bar closing the footer.
- Dark navy throughout, with one lighter `--slate` band at the silos section for
  rhythm, matching the homepage.

---

## Before launch

- **The carousel CTA points here.** Slide 4 of social post 001 links to
  `lucisystems.com/luci`. Don't publish that post until this page is live.
- Decide where AC submissions route, and who gets notified.
- Footer address and phone came from page 5 of the sales brochure — sanity-check
  they're current.
- No analytics, favicon or OG share image is set. For OG, slide 1 or 4 of the
  carousel would work.
