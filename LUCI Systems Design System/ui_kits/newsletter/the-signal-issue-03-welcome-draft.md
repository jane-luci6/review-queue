# The Signal — Issue 03 · August 2026

**Working file:** `the-signal-issue-03-august-2026.html`  
**Target ship:** August 15, 2026

---

## Issue theme

**EDIT — Issue theme goes here**

---

## Article checklist

| # | Section | Status | Notes |
|---|---------|--------|-------|
| — | Welcome | ⬜ TBD | Bridge from July (Command Trail shipped, Tachi field story) |
| 01 | In the field | ⬜ TBD | Cinematic build — same pattern as Issue 02 |
| 02 | LUCI Quick Tip | ⬜ TBD | Rotate (July = lighting on the map) |
| 03 | What's coming | ⬜ TBD | Next release after August ship — agentic / self-healing? |
| 04 | Inside LUCI | ⬜ TBD | New playbook — not revert preset again |
| — | Support portal | ✅ Evergreen | Keep as-is |
| 05 | A Minute with Mike | ⬜ TBD | Recurring column |

---

## Logged ideas (from Issue 02 planning)

- **Lightning-strike safety announcement.** A client routes a live lightning-strike feed (strikes within ~10 miles) to an automatic pool-zone evacuation announcement through LUCI — audio-announcement + weather-data trigger. Strong showcase of the scripting engine responding to external events; natural bridge to agentic capabilities. **Before running:** confirm with Mike which client/property and whether we can name it. Sourced from 06-26 casino consultation transcript (~00:05:00).

---

## Assets folder

Create when the field story is locked:

**Folder:** `assets/issue-03/` (or property-specific name, e.g. `assets/ameristar/`)

| File | Use in issue |
|------|----------------|
| `*-web.jpg` | Web-optimized photos (hero, before/after, install) |
| `reel-web.mp4` | Optional highlight reel + poster |
| `slider-before-web.jpg` / `slider-after-web.jpg` | Optional before/after slider |

---

## Publish workflow (same as Issues 01–02)

1. Finish TBD sections; delete the draft banner at top
2. Split into Webflow embeds when copy is locked — include cinematic CSS + slider JS
3. Publish to Webflow at `/the-signal/issue-03`
4. Update hub cards (`the-signal-hub.html`)
5. Build email teaser (`ui_kits/email/email-signal-issue-03-teaser.html`)
6. Ship via ActiveCampaign

---

## Structure reference

Same spine as Issue 02 (July):

**Masthead → Welcome → TOC → In the field (marquee) → Quick tip (dark) → What's coming → Inside LUCI → Support portal → A Minute with Mike → Closing → Footer**
