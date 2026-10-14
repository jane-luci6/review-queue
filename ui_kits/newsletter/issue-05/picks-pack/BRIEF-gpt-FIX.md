# FIX BRIEF: Update Signal Issue 05 picks pack (do not start from scratch)

**Repo / folder:** `ui_kits/newsletter/issue-05/picks-pack/`  
**Update in place:** `issue-05-titles-advice-mwm-DRAFT.html` + `NOTES.md`  
**Keep** existing Theme title options, Advice names/blurbs, and MwM outlines/quotes/recommended spine unless they violate brand locks. Improve scannability only if needed.

Jane has locked two more sections since the first draft. Fold them into the SAME browser pack.

---

## A) Quick Tip — LOCKED = calendar collision (NOT admin PIN)

- QT is **locked**: today’s behavior only — when two presets share the same TVs, **the next one wins** (Mike consult **06-26**).
- Do **NOT** tease New LUCI lockout / Staging-Apply as the tip.
- Parked wording CoS ok’d: **don’t stack a drawing on a daypart without a plan.**
- Add a short **2–3 sentence QT draft blurb** labeled **draft → approve** so Jane can approve wording.
- **Drop/demote** the admin PIN article gate from the top status bar (PIN is no longer the QT). PIN may remain as a one-line parked note in NOTES only if useful — not in the HTML top bar.

## B) What’s Coming — LOCKED = Reporting & Analytics

Draft a short What’s Coming body for **Reporting & Analytics** — feature spotlight for Signal, benefit-led, active voice.

Framing: **Beta / new-version ONLY — never “we launched.”**

Include a **promo callout** for the **What’s New two-pager** (first published piece on new LUCI) — soft invite to open/read it in this issue.

Brand locks: spell **A/V**; never `layer`; never `LUCI replaces` / `replaces`; never `property-by-property`; don’t imply reduced LUCI partnership. If you nod to New LUCI theme: **putting the power of programming in your hands.**

### Claims — align to Upgrade Guide (do not invent UI)

From `luci-website/src/data/upgradeGuide.ts` · Reporting & Analytics:
- One-liner spirit: Review incidents, latency, command results, and preset activity across the last 24 hours, 7 days, or 30 days.
- Paragraph spirit: Turns day-to-day system activity into a view of how the property has been running. Review incident volume/duration, command success/failure, latency, and preset activity across those windows. Overview to spot patterns, then move into the relevant device, command, or automation record.
- Live monitoring = now; audit trails = who/what/when; Reporting & Analytics = patterns across time.

Do **not** invent chrome claims beyond what the visual tabs show.

### Visual — REQUIRED in What’s Coming / R&A section

Fan PNG already copied next to the HTML:
`signal-05-reporting-analytics-fan.png` (same folder as the HTML — use **relative** `src`)

Caption/context Jane approved for the asset:
- Overlapping fan of **4 Analytics tabs: Overview, Commands, Automation, Reliability**
- Scrubbed “Realtime degraded” / “Establishing connection”
- Skipped Systems + Device Incidents

Show the fan image **in the What’s Coming / Reporting & Analytics section next to the draft copy**. Label section for Jane reply: **What’s Coming draft → approve / edit / reject**.

Optional note listing preferred placements from Mac screenshots folder (for Jane):  
`luci-design/richard-oct5-upgrade-followups/ui-screenshots/` — `06-analytics-overview.png`, `05-analytics-commands.png`, `04-analytics-automation.png`, `03-analytics-reliability.png` (fan already composites these four). Do not claim Systems or Device Incidents in the Signal visual.

## C) Top status strip — refresh

Must say:
- What’s Coming body = **Reporting & Analytics draft in this pack → approve** (no longer “ON HOLD until feature pick”)
- Quick Tip = **calendar collision LOCKED** (draft blurb in pack)
- Field = Osage Ponca City Swigs draft already in review
- Design services still yours next
- Admin PIN tip **not** the QT (demoted/removed from top bar)

## D) Keep Sections 1–3 from prior brief

Theme titles (6–8; reject “One Thread from Plan to Floor”), Advice blurbs + 2–3 section names, MwM outlines + verbatim quotes + recommended spine — retain unless broken. Jane reply codes stay: Theme C, Advice name 2, MwM spine 1, plus **QT approve**, **What’s Coming approve**.

## E) NOTES.md updates

Add/replace:
- QT locked: calendar collision Mike 06-26 (next preset wins); parked wording; no New LUCI lockout tease
- PIN demoted (was gated; no longer QT)
- What’s Coming locked: Reporting & Analytics; UG claim alignment; fan asset path + four tabs
- CoS typo 09-08 → 09_28 still noted
- Speaker accuracy basement = Mike 09_28

## Execute

Rewrite `issue-05-titles-advice-mwm-DRAFT.html` as one complete self-contained pack with all sections. Keep LUCI newsletter fonts/colors. Relative img for the fan PNG.
