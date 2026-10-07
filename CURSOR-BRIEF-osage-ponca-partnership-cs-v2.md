CURSOR BRIEF
Repo: design (`luci-design` only — write here; do NOT edit `luci-website`)
Branch: existing luci-design working branch
Model: GPT (`luci-cursor --role gpt`)
Why not GLM: unlocked case-study spine / copy draft; Jane reviews before any website implement
Mode: execute

Outcome Jane will see:
A self-contained HTML review page she opens in her browser with **revised** draft options for the Osage Casino Hotel – Ponca City web case study, rebuilt around the **multi-year LUCI partnership** (not a three-plane LED / screen-size spotlight), plus an updated sourced fact sheet. Draft only. No website publish, no deploy, no Webflow, no ActiveCampaign.

Where she looks:
- `case-studies/osage-ponca-swigs/osage-swigs-web-cs-draft-options.html` (open via file:// — **replace in place**; keep this filename so IMP/preview paths stay stable)
- `case-studies/osage-ponca-swigs/osage-swigs-fact-sheet.md` (**update in place**)

---

## Canon / voice (READ — do not recap in deliverables)

Point yourself at handbook canon in this repo; do not paste brand/voice lectures into the HTML:

- `LUCI Systems Design System/agent-handbook/canon/channel-playbooks.md`
- `LUCI Systems Design System/agent-handbook/canon/messaging-voice.md`
- `LUCI Systems Design System/agent-handbook/roles/case-studies.md`
- Any other voice/claims canon under `agent-handbook/canon/`

Standing claim lock (already on the work board): NEVER say LUCI **replaces** other technology. LUCI works with and absorbs other tech so everything is managed through one interface.

Active voice. Do not use the phrase **property-by-property**.

---

## Pattern references (READ only — do NOT edit luci-website)

Read these for section structure and tone patterns. Do not modify them:

- `../luci-website/src/data/caseStudyAliante.ts`
- `../luci-website/src/components/CaseStudyAliante.astro`
- `../luci-website/src/data/caseStudyOsagePoncaSwigs.ts` (shell, slug `osage-ponca-swigs`)
- `../luci-website/src/components/CaseStudyOsagePoncaSwigs.astro` (shell)

Section structure to follow in each draft option (adapt labels to the partnership arc — do not force an LED-install story):
1. Hero (headline + dek) — relationship / value-over-time thesis, NOT screen dimensions
2. At-a-glance / facts — **relationship-oriented placeholders** (see Stats locks)
3. Challenge (why an ongoing partnership / embedded control platform matters)
4. Approach / what we built across the relationship timeline (+ scope list where sourced)
5. Results / consolidation — placeholders for Jane’s numbers; no invented outcomes
6. Quote (or placeholder)
7. What's next (light, only if sourced; unfinished portfolio work is not the spine)
8. Suggested photo slots (describe by subject; no embedded photos required)

Existing photos you may reference as slot suggestions (list only — do not copy files):
`../luci-website/public/images/case-studies/osage-ponca-swigs/`
- osage-hero-wall-finished-web.jpg
- osage-wall-build-web.jpg
- osage-wall-build-2-web.jpg
- osage-wall-cavity-before-web.jpg
- osage-bar-logo-screens-web.jpg
- osage-exterior-dusk-web.jpg
- osage-gaming-floor-web.jpg

Also READ and revise from the **prior** (now wrong-framing) artifacts in this folder:
- `case-studies/osage-ponca-swigs/osage-swigs-web-cs-draft-options.html` — discard LED/spotlight as the lead spine; keep useful review-page pattern (options + Open Decisions + TBD markers)
- `case-studies/osage-ponca-swigs/osage-swigs-fact-sheet.md` — update for new relationship/timeline claims; mark unsupported items TBD

---

## Sources (primary factual spine — SOURCE WINS)

All under `case-studies/osage-ponca-swigs/sources/`:

1. **Context / relationship timeline (REQUIRED for this rebuild):** `10-05-osage-case-study-transcript.txt` (and .docx) — Jane/team Oct 5 call. Use for the multi-year arc and Signal thesis framing. Soft language where dates/names are fuzzy; do not invent precision.
2. **Technical depth for latest chapter only:** `swigs-osage-ponca-city-spotlight.txt` (and .docx) — Brian’s Swigs project write-up. Anchor Swigs technical numbers here. These specs are **secondary detail** in a facts block — not hero stats.

Ermintrude owns the Signal In the Field short separately — web CS is yours; facts must stay traceable so both pieces match.

---

## Job-specific locks (Jane — Oct 7 scope lock — ENFORCE)

### Rebuild thesis (this is the job)
**STOP** framing this as a three-plane LED / screen-size spotlight.

Rebuild around the **whole multi-year relationship** with **Osage Casino Hotel – Ponca City**.

**Required story arc (all options must follow this order):**
1. Several years ago — original LUCI install
2. Then bringing the ballroom in
3. Then the two Swig / Swallow (Swizzle) LEDs and upgrades

**Strategic thesis:** Ongoing partnership with LUCI — value over time; depth and breadth of partnerships and services; clear demonstration of Signal’s newsletter theme: **why having an embedded stronghold in your org is incredibly valuable.**

Osage may be named as the case-study subject. Ponca City only — not a portfolio tour of other Osage properties.

### Stats / callouts — HARD LOCK
- **Consolidation / at-a-glance section = placeholders only.** Jane will supply the numbers. Use clear markers like `[TBD — Jane: years with LUCI]`, `[TBD — Jane: projects at this property]`, etc.
- **Do NOT lead with LED screen sizes as the hero stats.** If sizes appear at all, they are **secondary detail** only (e.g. in a labeled “Latest chapter — Swigs specs” facts block).
- Prefer highlighting length of relationship, number of projects, phases of work, etc. — **placeholders OK** until Jane sends numbers.
- Never invent revenue, attendance, dwell, satisfaction, uptime, tap-counts, or other outcome metrics.

### Timeline claims — source honesty
From the Oct 5 transcript (soft language; mark exact years TBD unless Jane locks numbers):
- LUCI was installed in Osage properties previously; team confirms **“at least four years”** — use as relationship floor, or placeholder if you want Jane to set the published number.
- Then LUCI returned for **ballroom** work (projectors / ballroom solution brought onto LUCI) — transcript supports ballroom as a later phase; do not invent wall sizes or exact dates for ballroom.
- Then **this year’s** Ponca City LED / venue work: transcript says **Swallows first**, then the Swigs expansion stage LED (Brian’s spotlight). Jane’s words for the venues: **Swigs and Swizzle**, plus the ballroom. Treat transcript “swallows/follows/snakes” as likely mis-transcriptions of **Swizzle** — do **not** publish unverified first-wall pixel sizes from the transcript in body copy; put those in TBD or omit.
- Spotlight facts for **Swigs only** (cabinets, 3840×1296, Design LED 1.56mm CoB, NovaStar H5, 4 presets, 7 LG STBs, QSC + JBL audio zones, LUCI integration, 25.5 hrs / 4-person team) may appear as **secondary** technical detail if useful — never as the hero.

### Naming / geography — LOCKED
- Name and URL framing: **Osage Casino Hotel – Ponca City** (Swigs / Swizzle + ballroom as chapters of one property relationship). Website slug stays `osage-ponca-swigs` (do not rename slug in this job).
- **NOT Sand Springs** — never write “Sand Springs” in the HTML or fact sheet.
- Do NOT list naming/slug as an Open Decision.

### Claims / quotes / people
- Never invent quotes, numbers, outcomes, or customer names beyond what’s sourced.
- Quote block: only a quote that actually appears in the sources; otherwise clearly marked `[Quote TBD — Jane to source]`.
- Anonymize individuals (“the LUCI install lead”, “the property’s team”) unless Jane says otherwise.
- Results: only what sources state; unsupported → TBD.

### Partner / vendor naming
- Marketing typically does not name partners/vendors in body copy.
- Keep hardware specs (Design LED, NovaStar, LG, QSC, JBL) to a **spec/facts block only** if included.
- Flag partner-naming in body vs facts-block as an **Open Decision for Jane**.

### Forbidden
- Framing the piece as primarily a three-plane LED / screen-size spotlight
- LED dimensions (width, resolution, cabinet/panel counts) as **hero** or at-a-glance lead stats
- Phrase: `property-by-property`
- The words `Sand Springs` (anywhere in deliverables)
- Claim that LUCI **replaces** other technology (works with / absorbs / integrates only)
- Editing `luci-website`
- Deploy, publish, Webflow, ActiveCampaign
- Committing anything outside `luci-design`
- Invented quotes, years, project counts, or business outcomes

---

## Deliverables (all in `case-studies/osage-ponca-swigs/`)

### a) `osage-swigs-fact-sheet.md` — UPDATE IN PLACE
- Every fact/number used in the drafts, each with: source file name + short supporting excerpt
- Explicit section for **relationship / timeline** claims (original install → ballroom → Swig/Swizzle LEDs) with source excerpts
- Plus a list of items the sources do **not** support (TBD) — include Jane’s consolidation numbers, Swizzle publishable specs, exact year of original install, quote, business outcomes
- Note source conflicts if any (e.g. speaker-count aggregate vs itemized in spotlight)

### b) `osage-swigs-web-cs-draft-options.html` — REPLACE IN PLACE (same filename)
ONE self-contained, simply styled review page (inline CSS, readable typography, no external deps) that Jane opens in her browser.

Contents:
1. **Option A** — full draft with a **partnership / relationship-first** emphasis (embedded stronghold; value over years; depth and breadth of services). Must still walk the required three-beat arc.
2. **Option B** — full draft with a **venue evolution across projects** emphasis (how Ponca City’s spaces grew under one control platform: original install → ballroom → Swig/Swizzle LEDs). Genuinely different spine from A — not a light paraphrase. Same required arc.
3. If sources only honestly support one strong spine, deliver **one** full option and say so in an opener — prefer two if both can be honest.
4. Each option includes: headline, dek, at-a-glance (**relationship placeholders**, not LED sizes), challenge, approach across the timeline (+ scope list where sourced), results/consolidation (**placeholders**), quote or `[Quote TBD — Jane to source]`, what's next, suggested photo slots by subject.
5. Optional labeled block: “Latest chapter — Swigs (secondary technical detail)” for sourced Swigs specs — never the hero.
6. **Open Decisions** list for Jane at the end (include at minimum: which option leads; partner/vendor names in body vs facts-only; quote sourcing; how to name Swizzle vs transcript “Swallows”; which consolidation stats Jane will supply; any other forks — naming/slug and “not Sand Springs” are RESOLVED, do not list them).
7. Clear **TBD** markers where sources are silent.
8. Banner at top noting: **Oct 7 Jane lock — rebuilt around multi-year Ponca City partnership; prior LED-spotlight drafts superseded.**
9. No photos embedded required.

---

## Git / board

- Commit in `luci-design` of the updated fact sheet, HTML, and this brief is fine.
- Do **not** commit or touch `luci-website`.
- After deliverables exist, update Active jobs row `osage-swigs-web-cs` on `LUCI Systems Design System/agent-handbook/shared/CURRENT-WORK-BOARD.md`:
  - Jane asked = rebuild web CS around multi-year Ponca City partnership (Oct 7 lock)
  - Stage = Jane review
  - Waiting on Jane = yes
  - Model = GPT
  - Artifact = absolute path to the HTML + note Oct 7 partnership spine
  - Next = Jane reviews HTML / picks option

---

## Definition of done

1. Both deliverable files updated under `case-studies/osage-ponca-swigs/`
2. Both options (or one strong spine) follow original → ballroom → Swig/Swizzle arc
3. Hero / at-a-glance do **not** lead with LED screen sizes; consolidation stats are placeholders
4. Every timeline claim and number is traceable to sources (or marked TBD)
5. No invented quotes; no “replaces”; no “property-by-property”; no “Sand Springs”
6. Hardware vendor names confined to facts/spec blocks (or flagged Open Decision)
7. Board row updated for Jane review
8. Return paths + option headlines + Open Decisions list

Handoff when done: Consuelo (Case Studies). Draft only — Jane reviews before any website implement. Do not ping Jane from Cursor. Do not update .37 preview (Weatherby later).
