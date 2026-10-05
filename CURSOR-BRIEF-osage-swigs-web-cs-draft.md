CURSOR BRIEF
Repo: design (`luci-design` only — write here; do NOT edit `luci-website`)
Branch: existing luci-design working branch
Model: GPT (`luci-cursor --role gpt`)
Why not GLM: unlocked case-study spine / copy draft; Jane reviews options before any website implement
Mode: execute

Outcome Jane will see:
A self-contained HTML review page she opens in her browser with two full draft options for the Osage Casino Hotel – Ponca City / Swigs web case study, plus a sourced fact sheet. Draft only. No website publish, no deploy, no Webflow, no ActiveCampaign.

Where she looks:
- `case-studies/osage-ponca-swigs/osage-swigs-web-cs-draft-options.html` (open via file://)
- `case-studies/osage-ponca-swigs/osage-swigs-fact-sheet.md`

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

Section structure to follow in each draft option:
1. Hero (headline + dek)
2. At-a-glance / facts
3. Challenge
4. Approach / what we built (+ scope list)
5. Results
6. Quote (or placeholder)
7. What's next
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

---

## Sources (primary factual spine — SOURCE WINS)

All under `case-studies/osage-ponca-swigs/sources/`:

1. **Primary:** `swigs-osage-ponca-city-spotlight.txt` (and .docx) — Brian's project write-up. Two passes in one doc: technical spotlight + guest-experience version. Anchor every number/claim here.
2. **Context:** `10-05-osage-case-study-transcript.txt` (and .docx) — Jane/team Oct 5 context call. Use for ownership framing (tribal multi-property Oklahoma operator; LUCI 4+ years) and light "what's next" only if supported. Do NOT turn unfinished work (Tulsa event center, ballrooms) into the story spine.

Ermintrude (Editorial) is writing a shortened Signal/newsletter version from the same sources in parallel — facts must be traceable.

---

## Job-specific locks (Jane — include / enforce)

### Subject
Swigs, the bar / live entertainment venue at **Osage Casino Hotel – Ponca City**. LED + audio + LUCI control integration.

### Facts to anchor (verify each against the spotlight; source wins if different)
- Three-plane ~20ft LED display
- 60 cabinets / 480 panels
- Native resolution 3840×1296
- Design LED 1.56mm CoB
- NovaStar H5 processor
- 4 operational presets
- 7 LG set-top boxes
- QSC + JBL audio zones (QSC CX-Q 8K8 amp; 5 JBL stage speakers, 2 JBL subs, 3 JBL in-ceiling; two new audio zones)
- LUCI control integration of new AV endpoints alongside existing property tech
- 25.5 hours install with a 4-person onsite team (originally scheduled four full working days; Thursday reduced to three-item punch list)

### Framing
- May briefly situate Osage as a multi-property tribal operator in Oklahoma with LUCI in its properties for 4+ years (transcript supports "at least four years").
- The piece is **Swigs / Ponca**, NOT a portfolio tour.
- Do NOT center unfinished properties (Tulsa event center, ballrooms). At most a light "what's next" line if the transcript supports it.

### Claims / quotes / people
- Never invent quotes, numbers, outcomes, or customer names.
- Quote block: use only a quote that actually appears in the sources; otherwise a clearly marked `[Quote TBD — Jane to source]` placeholder.
- Anonymize individuals (e.g. "the LUCI install lead", "the property's team") unless Jane says otherwise.
- Results: only what the sources state; mark anything unsupported as TBD rather than inventing.

### Partner / vendor naming
- Marketing typically does not name partners/vendors in body copy.
- Keep hardware specs (Design LED, NovaStar, LG, QSC, JBL) to a **spec/facts block only**.
- Flag partner-naming in body vs facts-block as an **Open Decision for Jane**.

### Naming / slug — LOCKED by Jane (RESOLVED, not an Open Decision)
- Name and URL are **Osage Casino Hotel – Ponca City (Swigs)**. Website slug: `osage-ponca-swigs`.
- It is **NOT Sand Springs** — that property has not been done yet. Never write "Sand Springs" anywhere in the HTML or the fact sheet.
- Jane: the work done at Ponca City is **Swigs and Swizzle, plus the ballroom**. The draft stays focused on **Swigs**.
- Swizzle and the ballroom may get at most a light mention as other LUCI work at the property, and only to the extent the sources support it. Invent no details about them (no sizes, dates, scope); mark anything unsupported TBD. (Note: the transcript's "swallows/follows/snakes" are likely mis-transcriptions of Swizzle — treat transcript specs for that first wall as unverified/TBD, do not use them in copy.)
- Do NOT list naming/slug as an Open Decision.

### Forbidden
- Phrase: `property-by-property`
- The words `Sand Springs` (anywhere in deliverables)
- Claim that LUCI **replaces** other technology
- Editing `luci-website`
- Deploy, publish, Webflow, ActiveCampaign
- Committing anything outside `luci-design`

---

## Deliverables (all in `case-studies/osage-ponca-swigs/`)

### a) `osage-swigs-fact-sheet.md`
- Every fact/number used in the drafts, each with: source file name + short supporting excerpt
- Plus a list of items the sources do **not** support (TBD)

### b) `osage-swigs-web-cs-draft-options.html`
ONE self-contained, simply styled review page (inline CSS, readable typography, no external deps) that Jane opens in her browser.

Contents:
1. **Option A** — full draft with a technical/operator spine led by the build (alignment across three planes, install hours, presets, control integration). Follow case-study section structure.
2. **Option B** — full draft with a guest-experience/venue spine led by what it feels like in Swigs (flexible entertainment destination, daypart/event modes). Follow same section structure. Genuinely different spine from A — not a light paraphrase.
3. Each option includes: headline, dek, at-a-glance facts, challenge, what we built (approach + scope list), results, quote or `[Quote TBD — Jane to source]`, what's next, suggested photo slots described by subject (may reference filenames listed above).
4. **Open Decisions** list for Jane at the end of the page (include at minimum: partner/vendor names in body vs facts-only; quote sourcing; whether/how to mention Swizzle + ballroom; any other forks you hit — naming/slug is RESOLVED, do not list it).
5. Clear **TBD** markers where sources are silent.
6. No photos embedded required.

---

## Git / board

- Commit in `luci-design` of just these new files + this brief is fine.
- Do **not** commit or touch `luci-website`.
- After deliverables exist, update Active jobs row `osage-swigs-web-cs` on `LUCI Systems Design System/agent-handbook/shared/CURRENT-WORK-BOARD.md`:
  - Stage = Jane review
  - Waiting on Jane = yes
  - Artifact = absolute path to the HTML
  - Next = Jane picks option

---

## Definition of done

1. Both deliverable files exist under `case-studies/osage-ponca-swigs/`
2. Every number in the HTML is traceable to the spotlight (or marked TBD)
3. No invented quotes; no "replaces"; no "property-by-property"
4. Hardware vendor names confined to facts/spec blocks (or flagged Open Decision)
5. Two genuinely different option spines
6. Board row updated for Jane review
7. Return paths + option headlines + Open Decisions list

Handoff when done: Consuelo (Case Studies). Draft only — Jane reviews before any website implement. Do not ping Jane from Cursor.
