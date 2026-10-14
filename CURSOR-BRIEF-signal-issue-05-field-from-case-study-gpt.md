CURSOR BRIEF
Repo: design (`luci-design` only)
Model: GPT (`luci-cursor --role gpt`)
Mode: execute
Job: Rewrite Signal Issue 05 "In the Field" as a SHORTENED VERSION of the published Osage web case study. Copy only. Edit only the text inside the two In the Field sections of the Issue 05 HTML.

## Source of truth (read first)
- Web case study text: `LUCI Systems Design System/ui_kits/newsletter/issue-05/in-the-field-osage-swigs/osage-case-study-web-2026-10-08.txt`
  (same content as `../luci-website/src/data/caseStudyOsagePoncaSwigs.ts` if you can read it)
- This REPLACES the r2 Field draft and the current Issue 05 Field copy as the basis. Do not carry over facts that are not in the case study.

## File to edit IN PLACE
`LUCI Systems Design System/ui_kits/newsletter/the-signal-issue-05-october-2026.html`
Scope: ONLY `<section ... id="field-story">` and the following `<section class="sec sec--light" aria-labelledby="field-story-title">` (ends just before `<!-- DESIGN WITH LUCI -->`). Touch nothing else in the file.

## Size and structure: match Issue 04's In the Field
Reference: `LUCI Systems Design System/ui_kits/newsletter/the-signal-issue-04-september-2026.html` (section id="field-story" + its light body section).
Use the same blocks and classes Issue 04 uses, at roughly the same length (about 330–420 words of body copy total, excluding stats and list):
1. `field-opener__title` = the case study headline: "One foundation" + mint span "for every property expansion". Keep it exactly.
2. `field-opener__dek` = a 1–2 sentence condensation of the case study's thesis paragraph ("We installed the LUCI platform ... instead of making each new project another system to manage.").
3. `field-property` = "Osage Casino Hotel — Ponca City" · "Ponca City, Oklahoma".
4. `field-stats__row--4` = the case study's four inventory stats EXACTLY as written: 4+ / years growing on LUCI; 4 / connected projects; 2 / venue phases in the latest expansion; 98 / endpoints on LUCI. Remove the current [TBD] stats and the "Ponca City / This year's focus" stat.
5. Story blocks (`field-num` with `field-num__head` + `h3.field-num__title`, like Issue 04): three blocks following the case study's arc, using its section titles:
   - "The project was never just one room" (challenge: complexity accumulates project by project; original install put the platform and operating standard in place; the team returned for each phase).
   - "Four phases. One relationship." (original install → ballroom → Swizzle → Swigs; the software expands instead of resetting; the team returns with context). Place this block BEFORE the existing slider/photo figure.
   - "The latest project — Swigs" (inside the existing `field-pair`, left column): nearly 20-foot LED canvas across three planes; 60 cabinets / 480 panels / one continuous 3840 × 1296 display; four-person onsite team backed by the home office; installation and primary programming in 25.5 working hours; four operating presets, seven independent video sources; two new audio zones; the room changes modes, the operating standard does not.
6. `field-runs` list (right column of `field-pair`): title "What Ponca City runs now". 4 items drawn from the case study's "What the relationship made possible" bullets / scope (shorten lightly, keep facts and numbers exactly). Keep the existing `field-runs__item--icon` markup and reuse Issue 04's four icon SVGs in order.
7. `field-readmore`: remove the "There's more to this one..." line (do not replace it with an equivalent). Keep one link: text "Read the full case study", `href="http://10.10.1.37/resources/case-studies/osage-ponca-swigs/"`, followed by a small yellow note `<mark class="tbd">[Swap to live URL at publish]</mark>`. Remove the old `[CASE STUDY URL — TBD]` line.
8. Leave the photo slots exactly as they are (the `field-scale` band and the `figure.field-slider-figure` placeholder). A separate GLM pass fills them. Do not add images.

## Hard rules
- Keep the case study's headline, thesis, arc, and facts. Use ONLY facts and numbers that appear in the case study. Do not invent stats. If the case study has a placeholder (e.g. "[TBD] Audio zones"), either leave that item out or keep it exactly as written inside `<mark class="tbd">…</mark>`. Never fill it in.
- Naming: use the case study's names exactly: "Osage Casino Hotel — Ponca City", "Ponca City", "ballroom", "Swizzle", "Swigs". If anything in the existing Issue 05 copy conflicts with the web page, follow the web page and list the conflict in your notes file.
- Brand locks: active voice. Spell it "A/V". Never "layer". Never "property-by-property". Never imply LUCI replaces other tech. No vendor or tech-partner names (no LED, processor, amp, speaker, or set-top brands). No pricing, POs, deposits, or deal status.
- Issue 05's newsletter voice may say "LUCI" / "the LUCI team" where the case study says "we".
- Keep `<mark class="tbd">` for anything still TBD.
- Don't deploy, push, or edit other files except the notes file below.

## Output
1. The edited HTML (Field sections only).
2. `LUCI Systems Design System/ui_kits/newsletter/issue-05/in-the-field-osage-swigs/NOTES-r3-from-case-study.md`: a 10–20 line note listing: word count, which case-study paragraphs each block condenses, every stat used with its case-study line, anything dropped, and any naming/stat conflicts found versus the previous Issue 05 Field copy.
