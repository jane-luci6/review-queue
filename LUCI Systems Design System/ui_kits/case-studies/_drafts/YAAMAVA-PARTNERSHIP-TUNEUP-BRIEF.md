# Yaamava' partnership case study — design tune-up brief (for GLM)

**From:** Claude design pass, reviewed with Jane · **Date:** 2026-11-04
**Build from:** `_drafts/yaamava-partnership-mockup-v1.html` (the approved-in-spirit mockup) → implement in canonical `ui_kits/case-studies/yaamava.html`, **not** as a new file.
**Photos are pre-staged** (web-ready, ≤1600px) in `assets/yaamava/partnership/`. Do not re-pull from OneDrive unless a slot below says so.

## 0. Ground rules (read first)

1. **Copy is locked.** Jane approved the wording in the mockup. Do **not** rewrite, trim, or "improve" any sentence. Everything in §6 marked ⚑ is an open question for Jane — leave the current text and flag it in your handoff note.
2. **Implement in the canonical template.** Reuse the `cs-*` classes already in `yaamava.html` / `sams-town.html`. New components get the same `cs-` prefix. Mockup CSS was written fast: **take the structure, not the CSS verbatim** (it has off-scale spacing, boxed callouts, and Google-Fonts loading that the canonical page doesn't use).
3. **Pipeline after the HTML is approved:** `yaamava.html` → `npm run build:review` mirror → `yaamava-webflow-body.html` (+ head) → `luci-website` Astro component/data (`CaseStudyYaamava.astro`, `caseStudyYaamava.ts`) → `./deploy.sh` → verify `http://10.10.1.37`. Commit in small chunks. Jane has **not** approved anything for Webflow yet.
4. Voice rules apply to anything you touch: **A/V** (never AV), never call LUCI a "layer," no percentage claims, no outcome/revenue stats.
5. This is a **web-first marketing page**. PDF is a derivative; don't let print constraints shape it.

## 1. The design goal: three speeds of reading

The page must work for three readers. Build every section so all three get something:

| Speed | Reader | What they see | Must be true |
|---|---|---|---|
| **5 seconds** | Skimming an email link | Hero title + dek → at-a-glance stats → timeline → photos | The whole story ("eight-year partnership that grew from integration to enterprise") is legible from the hero, the 3 stats, and the 5-row timeline alone. |
| **30 seconds** | Evaluating LUCI | + section headings, photo captions, one big-number or pull-line per section, the quote | Reading **only** headings + captions + callouts + quote tells a coherent story. |
| **3 minutes** | Buyer / procurement | + full paragraphs, the proof tier | Nothing is lost; detail sits under the skim layer, never replaces it. |

**Rule of thumb for every section:** (1) a heading that states the point, (2) one dominant visual with a caption, (3) one number or pull-line a skimmer can grab, (4) the paragraphs.

## 2. What's wrong with the mockup today (findings → fixes)

| # | Finding | Fix (see §4) |
|---|---|---|
| F1 | **Photos don't match the copy.** The 909 sportsbook photo sits under the 2018/COVID section; the gaming-floor photo sits above the 909 section; the 2018 foundation band shows a 2021 LED column. | Re-map every photo (§5). |
| F2 | **A paragraph appears twice.** "…the LUCI engineers supporting the next project already understand the systems in place, the decisions behind them…" is in both *What eight years has built* and *A partnership built for what's next* (the latter was reworded during the last round and duplicated it). | Keep it once, in "eight years." Fix "what's next" per §4.9. |
| F3 | **Placeholder image** still in the last section. No Palms/corporate/firehouse/school photography exists in the library. | Use staged lobby/909 photo + enterprise chip list (§4.9). Request Palms/corporate photos from Mike (⚑). |
| F4 | **The required "Consolidation you can see" section and the "Yaamava' on LUCI to date" ledger were dropped** by the rewrite. The case-study rule makes the former mandatory (verbatim H2, rack background Jane just had shipped). The page also lost its dark mid-page rhythm and its strongest subtraction proof. | Restore both as a "proof tier" (§4.7–4.8). Jane to confirm (⚑1). |
| F5 | **Hero lead-in is 7 words** and orphans "WITH" onto a second line. Rule: lead-in ≤ ~5 words. | Split title: lead-in "Built to grow with" + Syncopate `Yaamava'` (§4.0). |
| F6 | **No visual evidence of LUCI's role.** The story is "LUCI engineered alongside construction," yet there's no construction/before-after imagery. The library has a full shell → design → installed sequence. | Triptych + install pair (§4.4). |
| F7 | **Section titles wrap badly** (`max-width:24ch` leaves orphans: "…for a growing / property"). | `max-width: 32ch` + `text-wrap: balance` on `.cs-sec__title`. |
| F8 | **Big stats are small.** "1,000+ speakers" and "34 LED walls" are in 26px boxed callouts — the loudest facts on the page read like footnotes. | Big-numeral treatment, de-boxed (§3.2). |
| F9 | **Timeline leaves the right half empty** and has lost the "LUCI role" labels that carry the point of the whole page (the role grows). | Role chips in the right column (§4.2). |
| F10 | **Boxed callouts** (4-sided hairline + left bar) violate the de-boxed rule. | Left 4px mint bar only, or hairline top/bottom. |
| F11 | **Off-scale spacing** in mockup CSS (18/22/28/30/36px). | Snap to 8px scale (4px for tight type only). |
| F12 | **CTA reuses the hero photo** and drops the "About LUCI" boilerplate the other case studies carry. | New CTA photo; restore About LUCI (§4.10). |
| F13 | **Enterprise breadth is buried in a paragraph** ("Palms, corporate offices, conference rooms, firehouses, schools, banquet halls"). That's a scannable list. | Chip/list treatment (§4.9). |
| F14 | **Expansion scope is buried in a sentence** (gaming space, 17-story hotel, spa, pool deck, restaurants, bars, retail, meeting spaces). | Scan strip (§4.4). |
| F15 | **Page is all white/light** from top to CTA. Other case studies alternate light/dark. | Dark 909 band (keep) + dark proof tier (§4.7–4.8). |

## 3. Shared components (build once, reuse)

### 3.1 Skim line (section lede)
A short pull-line under or beside a heading. **Pulled from existing copy only** — do not author new sentences. Candidates already in the copy: *"One A/V backbone. Expanded across the resort."* (expansion), *"1,000+ speakers replaced in eight months"* (foundation), *"34 LED walls across seven venues"* (909). Style: Space Grotesk 600, `clamp(20px,2.4vw,26px)`, 40×3px mint rule above (house lockup rule).

### 3.2 Big-number callout (replaces the boxed callouts)
Layout: numeral left, text right, desktop one row; stacked on mobile.
- Numeral: Space Grotesk 700, `clamp(56px,9vw,88px)`, line-height 0.9, tracking −0.03em; `--accent-light` on light, `--mint` on dark.
- Label: Space Grotesk 700, 20–24px. Detail: Inter 15–16px, `--ink` / `rgba(235,245,248,.84)`.
- Separation: 4px mint left bar **or** hairline top+bottom. **No four-sided box.**
- Used for: **1,000+** (foundation), **34** (909).

### 3.3 Figure with caption
Every photo gets `<figure>` + `<figcaption>` (Inter 13px, `--navy-muted` / 70% white on dark, centered, per `.cs-figure figcaption`). Captions are one factual line, no adjectives. Alt text always descriptive and uses **A/V**.

### 3.4 Role chip (timeline)
Right-column tag: Space Grotesk 600, 11–12px, tracked 0.08em, uppercase; hairline `--rule-light`, ink text. Rows 4–5 get a `#E6F5EF` tint fill. **Never** gold-deep text on white (fails contrast).

### 3.5 Scan strip (chips / soft-icon row)
For lists that are already in the copy (expansion scope, enterprise sites). Follow §5.1 of `luci-modern-design-guidelines.mdc` (soft-icon tiles, duotone icons: mint primary, one gold accent) **or**, where icons would be forced, a plain hairline-separated inline list. One style per page.

## 4. Page spec — section by section

Final order (zones in brackets). Backgrounds follow the case-study rhythm rule (alternate dark/light).

| # | Section | Zone |
|---|---|---|
| 0 | Hero | dark |
| 1 | At a glance (logo + 3 partnership stats) | light |
| 2 | The partnership from start to today (timeline) | white |
| 3 | A new foundation for a growing property | photo band → light |
| 4 | Engineering alongside Yaamava's expansion | white |
| 5 | New venues. The same foundation. | **dark** (`cs-sec--mid`) |
| 6 | What eight years of partnership has built (+ quote) | white |
| 7 | Consolidation you can see — **restored** | **dark** (rack bg) |
| 8 | Yaamava' on LUCI to date — **restored** | **dark** (ledger) |
| 9 | A partnership built for what's next | light |
| 10 | CTA + About LUCI | dark |

### 4.0 Hero
- **Split title:** lead-in `Built to grow with` (4 words) + `<em>Yaamava'</em>`. Put Jane's full title **"A technology partnership built to grow with Yaamava'"** in `<title>`, `og:title`, and the Webflow SEO title so nothing is lost (⚑2).
- Background: `assets/yaamava/gaming-floor-led-web.jpg` under the standard hero scrim (86% → 10%, left to right). Keep the 4px mint→gold bottom bar.
- Dek: the single paragraph only. Kicker "Case Study". Property row unchanged.
- Optional phase 2: muted 6–8s hero loop from `Yaamava/YEV LED/yaamava_event_entry.mov` (93MB source — transcode to ≤2MB mp4 + poster). Not required for this pass.

### 4.1 At a glance
- One hairline grid directly under the hero (no separate kicker section, no dead whitespace): **[Yaamava' logo cell] | 8 years | 17-story | 10+**. Logo = `../../assets/logos/yaamava.png`, ~96px tall, as in the original glance block. 2×2 on mobile.
- Same `cs-inventory` treatment as the original stats bar (mint numerals, 1px hairline grid, white cells). 3-line stat: numeral / label / muted foot. Foot lines are Jane's wording (keep).
- Keep the *"The partnership at a glance"* kicker only if it fits inside the glance block; otherwise drop it.

### 4.2 Timeline — "The partnership from start to today"
- `<ol>`, not `<ul>`. Headline must not orphan (F7).
- Row = `node rail | body | role chip`. Body = year (Syncopate 12px label), milestone (Space Grotesk 700 18px), desc (Inter 15px, **no 54ch cap** — let it use the width). Role chip right-aligned (§3.4), dropping under the desc on mobile. Chip text is Jane's v1.1 wording: *Integration · Engineering & project management · Design & construction collaboration · New venue development · Enterprise technology partnership.*
- **Growth, per Jane's doc:** the 2021 milestone is the **strongest visual increase**; the line stays substantial afterward. Node diameters ≈ 10 / 16 / 30 / 32 / 36px; line width steps ≈ 3 / 5 / 12 / 14 / 16px, one continuous tapered stroke behind the nodes (white 4px ring on each node). Final "2023–Today" node is `--accent-light` with a soft ring. Thickness is qualitative — no axis, no numbers.
- Keep Jane's intro sentence ("As San Manuel's resorts has expanded…") directly under the H2 (⚑3: grammar).
- Reduced motion: static. Optional: line draws on scroll (≤400ms, one easing curve) behind `prefers-reduced-motion`.

### 4.3 A new foundation (2018–2020)
- Keep Jane's layout: photo band with left scrim, paras 1–2 on the left; para 3 (COVID) full width below. **Change the photo** — the LED column is a 2021 artifact.
  - Band image: `legacy-rack-before-web.jpg` (existing asset) **if Jane confirms it's Yaamava (⚑4)**; otherwise `partnership/p-headend-idf.jpg`.
  - Caption (only if the rack is confirmed): one factual line, no LUCI branding in the "before" image (before/after discipline).
- COVID paragraph full width → **big-number callout "1,000+ / speakers replaced in eight months"** (§3.2), with Jane's detail line. Optional soft-icon speaker tile.
- No photo exists of the speaker replacement — don't force one.

### 4.4 Engineering alongside the expansion (2021)
This is where LUCI's role is proven. Lead with the pictures.
1. H2.
2. **Triptych directly under the heading** (3-up, 2px gaps, same height; stacks on mobile). Left→right: `partnership/p-entry-1-structure.jpg` → `partnership/p-entry-2-design.jpg` (LUCI's LED design placed in the actual room) → `event-entry-led-web.jpg` (installed). Captions: **Structure · Design · Installed**. Small mint arrows between frames.
3. Scan strip (§3.5) — "What the expansion added": Expanded gaming space · 17-story hotel tower · Spa · Pool deck · Restaurants & bars · Retail · Meeting spaces (all words already in Jane's copy; leave the paragraph untouched).
4. Jane's two paragraphs.
5. Promote *"One A/V backbone. Expanded across the resort."* to the section's skim line (§3.1).
6. Optional second pair: `partnership/p-lobby-1-frame.jpg` → `partnership/p-lobby-2-installed.jpg`, caption "Lobby: LED frame → installed."
- Existing install photos (`install-led-cabinets-web`, `install-column-commission-web`, `install-head-end-web`, `install-lobby-frame-web`) are the LUCI-at-work shots. Use **one** as a small inline photo near the paragraphs; don't build a crew grid.

### 4.5 New venues. The same foundation. (2022 — The 909)
- Dark `cs-sec--mid` (keep). Open with a **full-bleed hero photo**: `partnership/p-909-halo.jpg` (or `p-909-archway.jpg`, see rights note ⚑8). **Remove the gaming-floor photo** that sat above this section.
- Three spec tiles under the photo (dark, mint numerals, hairline separators): **50′ × 12′ — Game Day display · 150+ — screens · LED archway** (50′×12′ and 150+ confirmed by the 2022-11-17 public press release and fact sheet; the archway tile uses an icon, not a number).
- Jane's two paragraphs. Then a 2-up: `partnership/p-909-bar.jpg` + `partnership/p-909-ceiling.jpg`, captions "The 909 bar and video ring" / "Ceiling LED over the sportsbook floor" (factual; adjust after Jane's look).
- **34** big-number callout (dark variant). The factual note stands: do **not** imply all 34 walls are at the 909 or from the 2021 expansion.

### 4.6 What eight years of partnership has built
- Jane's two paragraphs, then the **Toni Pepper quote directly under** (Jane's instruction), verbatim, in a larger pull-quote: Inter italic `clamp(22px,3vw,28px)`, 5px `--accent-light` bar, attribution Space Grotesk 700 12px tracked.
- **Remove the lightweight scope row** (290,000 / 1,000+ / 34) *if* §4.7–4.8 are restored — the ledger carries scope. If Jane declines the restore (⚑1), keep the row as is and file the ledger under "parked."

### 4.7 Consolidation you can see — RESTORE (required by `luci-case-studies.mdc`)
Take the section **verbatim from the current live `yaamava.html`** (H2 "Consolidation you can see", 4 rows, `assets/luci-rack-web.jpg` right-side rack background as shipped). Do not rewrite rows.
- ⚑ Optional stronger row 1 (needs Jane OK): *Six audio systems and four video systems → one control interface* (from Jane's own foundation copy; the most verifiable subtraction in the whole story).

### 4.8 Yaamava' on LUCI to date — RESTORE
Take the ledger block (`cs-ledger`: 420 displays / 34 LED walls / 284 audio zones / 92 DTV channels / 220 signage endpoints / 14 technologies → "One LUCI platform") **verbatim** from the live page. It is the denominator-first proof and the dark closing rhythm.

### 4.9 A partnership built for what's next
- Jane approved this heading. **Fix F2:** paragraph 2 currently duplicates "eight years." Replace it with Jane's own v1.1 sentence: *"Through ongoing maintenance, system improvements, and planning for future projects, LUCI continues supporting the enterprise as its needs evolve."* (⚑ Jane to confirm.)
- Add the **enterprise scan strip** (§3.5): Yaamava' Resort & Casino · Palms Casino Resort · Corporate offices · Conference rooms · Firehouses · Schools · Banquet halls. Every item is already in the copy.
- Photo: `partnership/p-lobby-2-installed.jpg` (the finished YAAMAVA' lobby LED) until Palms/corporate photography is supplied (⚑9). **No placeholder images may ship.**

### 4.10 CTA
- Photo: a *different* image from the hero — `partnership/p-909-archway.jpg` under the standard CTA scrim.
- Copy as written ("Your property's technology needs will change…"). Button "Talk to LUCI" → `https://www.lucisystems.com/contact`.
- **Restore the "About LUCI" boilerplate** from the live page (verbatim; it's the approved value-prop statement).

## 5. Photo map

All staged in `assets/yaamava/partnership/` unless noted ("existing" = already in `assets/yaamava/`).

| Slot | File | Source (OneDrive `Project Media/Yaamava/…`) | Note |
|---|---|---|---|
| Hero bg | existing `gaming-floor-led-web.jpg` | — | keep |
| Foundation band | existing `legacy-rack-before-web.jpg` **or** `p-headend-idf.jpg` | `IDF/AV4 IDF/IMG_2696.jpg` | ⚑4 provenance |
| Triptych 1 (structure) | `p-entry-1-structure.jpg` | `YEV LED/photos/Event Entry 4.jpg` (HEIC) | bare shell, cones |
| Triptych 2 (design) | `p-entry-2-design.jpg` | `YEV LED/photos/Event Entry 4 proposed.jpg` | LED overlay in magenta — it's a design visualization; caption says "Design" |
| Triptych 3 (installed) | existing `event-entry-led-web.jpg` | — | |
| Lobby pair | `p-lobby-1-frame.jpg`, `p-lobby-2-installed.jpg` | `Lobby LED/Lobby Frame.jpg`, `Lobby LED/IMG_3893.jpg` | optional |
| 909 hero | `p-909-halo.jpg` | `909 Sports Bar/909 Food Hall Opening/SBS-L-909HALL-1119-04TP-1.jpg` | client-supplied press photo (⚑8) |
| 909 2-up | `p-909-bar.jpg`, `p-909-ceiling.jpg` | `…/SBS-L-909HALL-1119-07TP-1.jpg`, `909 Sports Bar/For Review/IMG_1474.HEIC` | bar = press photo; ceiling = LUCI phone shot |
| 909 alt hero / CTA | `p-909-archway.jpg` | `909 Sports Bar/For Review/IMG_2479.HEIC` | LUCI-shot — no rights question |
| 909 sign | `p-909-sign.jpg` | `Yaamava' 909 Archway 8.png` | **680px only — small use only, do not stretch** |
| Install inline | existing `install-*-web.jpg` or `p-install-scaffold.jpg` | `Bar LED/IMG_4666.jpeg` | portrait; pick one |
| Enterprise / closer | `p-lobby-2-installed.jpg` | `Lobby LED/IMG_3893.jpg` | until Palms photos arrive |

**Not used on purpose:** grand-opening crowd/celebrity/mascot photos (identifiable people; not LUCI's story), food photos, the ~40 phone stills in `909 Sports Bar/For Review/` beyond those above, renderings (`San Manuel *.PNG`, `Yaamava LED *.PNG` — likely design renders; don't present as installed).
**Video available** (phase 2): `909 Archway.mov`, `909_grand_opening_b-roll_fa.mp4`, `LUCI LED Sportsbook.mp4`, `YEV LED/yaamava_event_entry*.mov`, `yaamava_lobby*.mov`.

## 6. Open questions for Jane ⚑ (GLM: leave current behavior, flag in handoff)

1. **Restore "Consolidation you can see" + ledger?** Recommended yes (rule-required; strongest proof; restores dark rhythm). Default if no answer: build them, keep behind a clearly-marked block so they can be removed in one edit.
2. **Hero title.** Her full title exceeds the canonical lead-in length. Recommendation: split title in the hero + full title in SEO/`<title>`.
3. **Grammar:** "As San Manuel's resorts **has** expanded" → "resort has" / "resorts have." Left as written.
4. **Is `legacy-rack-before-web.jpg` a Yaamava photo?** (Carried from the earlier rack-background round; unconfirmed.)
5. **2021 expansion date.** File timestamps suggest a 2021–22 build: bar LED shots June 2021, event-entry LED factory photos Jan 2022, The 909 opened **Nov 17, 2022**. The timeline's "2021" may want to read **2021–22**. Mike to confirm.
6. **"10+ venues & locations"** needs Mike's count (the copy lists ~7 named kinds of site).
7. **Resolved:** The 909 facts in the doc's verification note (50′×12′ Game Day display, 150+ screens, Nov 2022 opening) match the public press release/fact sheet. Still unconfirmed: individual LED-wall install dates; the 290,000 sq ft vs. wider resort footprint; endpoint total.
8. **Press-photo rights.** `SBS-L-909HALL-…` are client-supplied PR photos. Fine for the review mockup; confirm usage with Yaamava marketing before publishing, or swap to the LUCI-shot `p-909-archway` / `p-909-ceiling`.
9. **No Palms / corporate / firehouse / school photography** in the library. Ask Mike. Until then the closer uses the lobby shot.
10. **New-claim option:** a "0 new control systems" tile on the 909 band (derived from Mike's statement and Jane's copy). Not built unless Jane okays it.

## 7. Brand-standard delta checklist (mockup → canonical)

- [ ] Fonts via `../../assets/fonts/luci-brand-fonts.css` (embedded) — **no** Google Fonts `<link>`.
- [ ] Syncopate only for: kicker, hero `<em>`, year labels/tiny tracked labels. Headlines Space Grotesk 700; **all body Inter**.
- [ ] One display moment (the hero `<em>`).
- [ ] Mint = primary accent (lockup rules, eyebrows, CTA); gold = secondary (role dots, ledger numbers, section-title accent on dark). Never bright mint on light; light accent is `#2b9e80`; `#176B54` is retired.
- [ ] Sharp corners; no drop shadows on flat tiles; callouts de-boxed (F10).
- [ ] Spacing on the 8px scale; section padding `clamp(44px,6vw,72px) clamp(28px,6vw,64px)`; 60–64ch body measure.
- [ ] Section header: use the canonical `cs-sec__title` + accent span pattern already in `yaamava.html` (don't invent a new lockup).
- [ ] Contrast: body ≥ 4.5:1; no gold-deep text on white; scrims keep text ≥ 4.5:1 over photos.
- [ ] A11y: `<ol>` for timeline, `figure/figcaption`, descriptive alt, visible focus on CTA, 44px target, `prefers-reduced-motion` respected.
- [ ] "A/V" everywhere (incl. alt text/captions); never "layer" for LUCI.
- [ ] Per-slot cache-buster `?v=N` on every new image ref; images ≤ ~350KB, `loading="lazy"` below the fold, explicit `width/height`.

## 8. Implementation order & QA

1. Copy `partnership/` assets referenced into the review mirror build (`npm run build:review`) — verify paths resolve.
2. Edit canonical `yaamava.html`: hero → glance → timeline → foundation → expansion → 909 → eight years → restored proof tier → what's next → CTA. Commit after each pair of sections.
3. Screenshot at 1100 / 768 / 390px (headless Chrome is fine). Check: no orphan headings, triptych stacks, timeline chips reflow, scrims legible, no placeholder URLs, no Webflow-CDN/`placehold.co` URLs left in canonical HTML.
4. **5-second test:** screenshot only hero + glance + timeline — does it tell the story? **30-second test:** hide all `<p>` — do headings + captions + callouts + quote still read as a story?
5. Derive Webflow body/head (`.luci-cs` scoped; image URLs → Webflow CDN assets Jane uploads; flag the new images that need uploading) and the website component/data. Deploy to `.37`; post URL + hard-refresh note.
6. Do **not** push to Webflow. Hand Jane the review URL and the ⚑ list.

## 9. Handoff note GLM should return
Short list: what shipped, screenshots, any ⚑ item you hit, any image you had to substitute, and anything in this brief you couldn't do.
