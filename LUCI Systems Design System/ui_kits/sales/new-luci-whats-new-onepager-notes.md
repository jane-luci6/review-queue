# New LUCI — What’s New one-pager · status notes

**Built:** 16 Sep 2026 · GLM (maker) · from locked copy in `new-luci-whats-new-onepager-copy.md`
**Files:**
- `new-luci-whats-new-onepager.html` — the handout (self-contained; links `../../assets/fonts/luci-brand-fonts.css`)
- `new-luci-whats-new-onepager-copy.md` — locked copy (verbatim source)

## What’s built

A single-page What’s New handout for the upcoming New LUCI platform release, for LUCI customers and prospects. Uses **Option 1 — Three promises** (Jane, 16 Sep; logged in `DECISION-LOG.md`), presented **creatively** as a staggered release announcement rather than an equal-column feature sheet.

### How the creative three-promises presentation works

The headline dominates the top of the page, then the three promises **unfold in a staggered sequence — left → center → right** — so they read as one continuous release narrative instead of three parallel columns:

- **Promise 1 · Operate — leans LEFT.** Body copy + feature-in-focus card on the left; UI capture frame on the right.
- **Promise 2 · Make it yours — CENTERED.** Narrower column, centered, with the UI capture frame stacked beneath. The centering gives this (the leanest pillar — one feature, one proof) its own quiet moment.
- **Promise 3 · See and secure — leans RIGHT.** Mirror of Promise 1: UI capture frame on the left, body + feature-in-focus on the right.

Each pillar keeps **identical component structure** (number · name · argument · lead · feature-in-focus · more-proof · UI capture), so strategic weight stays equal even though scale and placement differ. The UI captures are **part of each pillar’s narrative moment**, not parked in a separate screenshot gallery (per the layout notes).

### Visual system

LUCI sales tokens from the existing sales UI kit: navy `#10232D` / `#0A161C`, mint `#68E3BE` (dark) / `#2b9e80` (light), gold `#EDD086` (dark) / `#CEB06E` (light). Space Grotesk structure · Syncopate display (masthead “What’s New” + promise numbers only) · Inter body. Off-white canvas, near-black ink, hairline separation, soft mint feature-in-focus cards, dashed mint UI-capture frames. Print-friendly: scrolls on screen, flows to ~2 US Letter sheets in print (`@page` + `break-inside: avoid` on promises/captures; `print-color-adjust: exact` on dark/filled surfaces).

## Open locks for Jane

- **`[RELEASE DATE]`** — placeholder in the masthead, mint text. Replace when the date is locked.
- **CTA — Jane locks later.** Option A (`See New LUCI in action.`) is the **working default** shown in mint in the CTA band. Option B (`Schedule a New LUCI walkthrough.`) is shown beside it. Both are present per the copy file; Jane picks one.
- **UI CAPTURE slots (3).** Each pillar has one labeled placeholder frame (dashed mint, “UI Capture” tag + the verbatim capture description from the copy + a “drop in Jane’s New LUCI capture” note). Capture descriptions:
  1. *Venue panel controlling a single space*
  2. *Property-branded interface beside its live floor-plan map*
  3. *Live monitoring view with activity and session controls*
- **Proof strip — empty.** No approved, anonymous launch-level consolidation metric was found, so the slot is left empty with a labeled note (`Add consolidation metric — no client names`). No number or client name was invented.

## Content fidelity (self-check)

All copy applied **verbatim** from the locked copy file:
- Masthead: “WHAT’S NEW” + “A new LUCI platform release is on the way.”
- Headline: “Putting the power of programming in your hands” (mint accent on *programming*)
- Benefit line, audience line, release date line — all verbatim
- Three pillars in locked order: Operate · Make it yours · See and secure
- Each pillar’s argument, lead, feature-in-focus (name + text), and more-proof items — verbatim
- CTA Option A (working default) + Option B — both present
- Proof strip left empty per copy file

## Out of scope (per brief — not done)

- No invented metrics, client names, screenshots, or features
- No IT sidebar / technical catalog
- No “property-by-property” language; no retired operational-precision lead
- No Webflow publish / ActiveCampaign / Send
- No deploy (brief did not require it; this is a design-system handout HTML, not a website/portal change)
- UI images not invented — labeled placeholder frames only, for Jane’s captures

## To review

Open `new-luci-whats-new-onepager.html` directly in a browser, or serve the `sales/` folder (`python3 -m http.server`) and visit the file. Print to PDF (US Letter) to check the print flow.
