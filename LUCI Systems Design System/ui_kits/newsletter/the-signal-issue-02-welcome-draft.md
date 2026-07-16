# The Signal — Issue 02 · July 2026

**Working file:** `the-signal-issue-02-july-2026.html`  
**Target ship:** July 15, 2026

---

## Issue theme

**The Version of Tomorrow We Haven't Yet Met**

---

## Article checklist

| # | Section | Status | Notes |
|---|---------|--------|-------|
| — | Welcome | ✅ Seeded | Updated bridge mentions Tachi |
| 01 | In the field · Tachi Palace | ✅ Cinematic build | Three-act story, highlight reel, before/after slider |
| 02 | What's coming | ⬜ TBD | August release feature preview + transition plan |
| — | Quick tip | ⬜ TBD | Rotate (June = mobile control) |
| 03 | Inside LUCI | ⬜ TBD | New playbook — not morning reset again |
| — | Support portal | ✅ Evergreen | Keep as-is |
| 04 | Beyond the platform | ✅ Mostly done | Services list kept; intro updated for mid-year |

---

## Tachi Palace assets

**Folder:** `assets/tachi-palace/` (web-optimized `-web.jpg` + `tachi-reel-web.mp4`)

| File | Use in issue |
|------|----------------|
| `01-hero-web.jpg` | Cinematic hero (2:1, overlaid headline) |
| `02-before-bays-web.jpg` | Act I — empty wall bays |
| `03-install-web.jpg` | Act II — install bleed |
| `03b-install-detail-web.jpg` | Act II — two-up install detail |
| `03c-config-web.jpg` | Act II — two-up config candid |
| `build-pano-web.jpg` | Act II — mid-build panorama band |
| `04-rack-before-web.jpg` / `04-rack-after-web.jpg` | Act II — rack before/after pair |
| `tachi-reel-web.mp4` | Highlight reel (poster: `tachi-reel-poster-web.jpg`) |
| `slider-before-web.jpg` / `slider-after-web.jpg` | Act III — interactive before/after slider |
| `05-bingo-wall-web.jpg` | Act III — live BINGO wall detail |
| `06-team-web.jpg` | Close — team portrait |

**Webflow note:** The reel + slider require the cinematic CSS block and inline `<script>` to be carried into the Webflow embed split at publish (same as Issue 01 head/body split).

---

## Publish workflow (same as Issue 01)

1. Finish remaining TBD sections
2. Delete the draft banner at top
3. Split into Webflow embeds when copy is locked — include cinematic CSS + slider JS
4. Publish to Webflow at `/the-signal/issue-02`
5. Update hub cards
6. Build email teaser
7. Ship via ActiveCampaign

---

## Future issues — logged ideas

- **Lightning-strike safety announcement (Aug or Sep issue).** A client routes a live lightning-strike feed (strikes within ~10 miles of the property) to an automatic pool-zone evacuation announcement through LUCI — an audio-announcement + weather-data trigger, not a lighting story. Strong showcase of the scripting engine responding to external events, and a natural bridge to the agentic / self-healing capabilities in the August release. **Before running:** confirm with Mike which client/property and whether we can name it, and whether there's a specific real incident worth telling. Sourced from the 06-26 casino consultation transcript (~00:05:00). Possible homes: a short lead-in to a Platform/release section, or its own "In the field"-style showcase.
