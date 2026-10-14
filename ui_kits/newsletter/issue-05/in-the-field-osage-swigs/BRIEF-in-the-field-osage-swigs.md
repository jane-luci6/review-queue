# BRIEF: The Signal Issue 05 — In the Field (shortened case study)

**Client:** Jane Haynie, Director of Marketing, LUCI Systems  
**Writer role:** GPT via luci-cursor (`--role gpt --repo design`)  
**Issue:** The Signal Issue 05 · October 2026  
**Section:** In the Field  
**Subject:** Swigs at Osage Casino Hotel — Ponca City, Oklahoma  
**Status:** DRAFT for Jane HTML review only — do NOT publish, do NOT touch Webflow or ActiveCampaign.

---

## Deliverables (write both into this same folder)

Work folder (already created; write outputs here):
`/Users/janehaynie/Documents/Cursor Projects/luci-design/ui_kits/newsletter/issue-05/in-the-field-osage-swigs/`

1. **`osage-swigs-in-the-field-DRAFT.html`** — single self-contained, clean, readable HTML review page in LUCI newsletter style.
2. **`NOTES.md`** — short fact ledger: every fact used + its source file and line (or section heading).

---

## Length & structure (Signal In the Field — NOT the full web case study)

- **Word count target:** roughly **180–280 words** of story body (headline + opener + narrative + soft link; exclude HTML chrome / captions / NOTES).
- **Required shape:**
  1. Kicker: `In the field`
  2. **Headline** (benefit-led, warm, specific)
  3. **Cold-reader opener** — 1–2 sentences: who, where, what venue (Swigs / Osage Casino Hotel / Ponca City, Oklahoma)
  4. Short narrative (architecture challenge → install/control outcome → guest experience)
  5. Compact **stat row or bullets** for hard numbers where that reads better
  6. Soft closing link line to the full case study with placeholder URL marked **TBD** (e.g. `href="#TBD-full-case-study"` or visible text `Full case study → TBD`)
- Include **1–2 photo slots** as placeholders with caption exactly: `Photo TBD: Osage Project Media`

---

## Primary sources (in this folder — USE THESE ONLY)

1. **PRIMARY facts:** `swigs-osage-ponca-city-spotlight.txt` (Brian’s write-up). Prefer this for all numbers and technical claims.
2. **Portfolio background only:** `10-05-osage-case-study-transcript.txt` (Oct 5 team call). Team decision: *“Just talk about Ponca then. We can mention the other stuff.”* Story focus = Ponca City Swigs; a **light nod** to the longer Osage relationship is fine (LUCI has worked with Osage across several Oklahoma properties for years — Tulsa, Bartlesville, Sand Springs, Ponca City, Skiatook, Pawhuska). Do not make Sand Springs the story.
3. **Tone/length reference:** `_ref-issue04-shell.html` — Issue 04 In the Field (Aliante) for structure, voice, and visual language. Issue 04’s project log already mentioned Swigs/Ponca in passing; this piece is the deeper In the Field feature — **do not rehash the Issue 04 proj-log blurb** (phases, “six properties,” “Swigs Stage” wording). Tell the Swigs LED/audio story fresh.

**Hard rule:** Use only facts from the sources. Do **not** invent quotes, numbers, names, or partner claims. If something is ambiguous, omit it from the HTML and flag it in NOTES.md.

---

## Facts that MUST match the long web case study (Consuelo owns that one)

Confirm each against the spotlight source and state accurately:

- Three-plane LED wall
- Nearly 20 ft wide (7′ 10½″ center + two 5′ 10¾″ angled wings)
- Design LED 1.56mm-pitch CoB *(see partner-naming note below)*
- 60 cabinets / 480 panels
- 3840 × 1296 native resolution
- **25.5 hours** — spotlight states this is **total working time** from installation to completion (originally scheduled for four full working days; primary install/programming in first two days; Thursday reduced to a three-item punch list). State it accurately as working time / install-to-completion working hours — not “calendar days.”
- LUCI control (new A/V endpoints and zones integrated into LUCI / centralized control alongside existing property technology)
- Audio zones (two new audio zones; QSC amp + JBL speakers appear in source — include only if they fit the short length; do not invent)

Optional supporting facts from spotlight if space allows: four operational presets; seven LG set-top boxes as independent video sources; four-person onsite team.

---

## Brand locks (non-negotiable)

- Active voice; specific and concrete.
- Warm, human tone with a little lightness — never stiff corporate.
- Spell it **A/V** (never `AV` without the slash).
- Never say LUCI **“replaces”** other tech. LUCI works with and absorbs other A/V tech so it’s all managed through a **single interface**.
- Don’t call LUCI a **“layer”**.
- Never use the phrase **“property-by-property”**.
- Never imply reduced LUCI support or partnership.
- Marketing normally doesn’t name partner brands. **Design LED:** keep out of the headline and stat row; mention at most once in body if needed for the pitch fact; if unsure, omit the brand name and say “1.56mm-pitch CoB” / fine-pitch CoB. Flag the choice in NOTES.md.
- Avoid naming QSC / JBL / NovaStar / LG in the headline or stat row; body mention only if essential and space allows — prefer focusing on outcomes (audio zones, multi-source layouts, LUCI control).
- Do not use banned words anywhere: `replaces`, `layer`, `property-by-property`, `AV` (unsashed).

---

## HTML style (self-contained review page)

Borrow fonts and colors from Issue 04 shell:

- Fonts: Google Fonts `Syncopate:700` + `Space Grotesk:400;500;600;700`
- CSS vars:
  - `--navy-deep:#0A161C; --navy:#10232D; --navy-mid:#314955; --navy-muted:#49616E;`
  - `--mint:#68E3BE; --mint-dark:#2b9e80;`
  - `--sand:#E5E3DF; --off-white:#F5F8FA; --white:#FFFFFF; --rule-light:#D4D9DC;`
  - `--display:'Syncopate',...; --body:'Space Grotesk',...;`
- Visual register: sand/light In the Field treatment (kicker, headline, property line, stat row, narrative on light canvas) — suitable for Jane to review in a browser as a standalone page.
- Title the browser tab something like: `DRAFT · In the Field · Swigs / Osage Ponca City · Signal 05`
- Mark the page clearly as DRAFT (small banner is fine).
- Photo placeholders: dashed boxes, caption `Photo TBD: Osage Project Media`.
- Soft case-study link at end with TBD URL.

---

## NOTES.md requirements

List every factual claim in the HTML with source pointer, e.g.:

- `3840 × 1296` — spotlight.txt line ~3 / “From 60 Cabinets…”
- `25.5 hours` = total working time — spotlight “25.5 Hours From Installation to Completion”
- Design LED naming decision
- Any ambiguity you deliberately omitted
- Confirmation you avoided Issue 04 proj-log phrasing overlap

---

## Execute

Write the two deliverables into the work folder now. Keep copy tight, benefit-led, and source-faithful.
