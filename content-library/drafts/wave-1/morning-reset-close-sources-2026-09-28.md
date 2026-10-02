# Morning-reset spotlight close — source findings
**For:** Jane Haynie  
**Date:** 28 Sep 2026 (PT)  
**Purpose:** Source material only for rewriting the close of Wave 1 spotlight `spotlight-morning-reset`. Do not invent stories.

---

## A) Locked / boilerplate — what LUCI is

### Verbatim (Messaging Guide / handbook — do not paraphrase)

| Line | Quote | Path |
|---|---|---|
| **Tagline** | `The Orchestration Engine for Enterprise Multimedia` | `luci-design/LUCI Systems Design System/agent-handbook/canon/messaging-voice.md` (also `00-LUCI-ORGANIZATIONAL-CONTEXT.md`; `luci-website/src/data/site.ts` → `site.tagline`; Messaging Guide HTML) |
| **Sub-tagline** | `One interface to control, automate, and execute the entire guest experience.` | Same set; `site.subTagline` |
| **Guide instruction** | “The tagline and value prop are exact; use them as written.” | `luci-design/.../ui_kits/review/messaging/messaging-guide.html` (§ TAGLINE) |

Handbook framing Jane will recognize (not slogan dump, but locked category language):

> **LUCI Systems** sells an **orchestration engine for enterprise multimedia** — software, hardware, operating model, and an **embedded engineering team** (LUCI FDE) delivered as one system. Properties run A/V, signage, and related infrastructure from **one interface**, with a team that stays.

— `agent-handbook/00-LUCI-ORGANIZATIONAL-CONTEXT.md`

> LUCI is a fully managed A/V operating platform — software, hardware, operating model, and an embedded engineering team — deployed as a complete system your team takes over from day one.

— `luci-website/src/data/site.ts` → `oneOffering.offering`

> One platform, one embedded team, one outcome.

— `site.ts` → `oneOffering.summary`

### Site pillars (official website copy — prefer these over paraphrase)

From `luci-website/src/data/pillars.ts` (and Messaging Guide “MESSAGE PILLARS”):

1. **Complete visibility and control across your property** — “One interface surfaces every endpoint, zone, and system across your property. Every team sees the same picture and acts from the same place.”
2. **Align your teams by default** — “LUCI connects every team to the same system…”
3. **Fully activate the guest experience** — “Turn passive screens into purposeful moments…”
4. **Invest in the only A/V that scales and improves** — “Traditional A/V depreciates and expires. LUCI doesn't…”

Canon short pillar titles also in `messaging-voice.md` § Four message pillars.

### Homepage Control / Automate / Execute (already names morning reset)

From `luci-website/src/data/homeIntro.ts` Automate step:

> Build scenes once — game time, happy hour, **morning reset** — and fire them on schedule or trigger.

### Hard rules Jane will expect in the close

- Always **A/V**. Never call LUCI a “**layer**.” (`messaging-voice.md`, org context, Wave 1 prompt)
- Approved nouns/verbs: orchestration engine · platform · infrastructure · orchestrates / runs / operates / integrates / consolidates / refines
- Named clients in public only when the piece is an approved case study (spotlights: anonymize)

### “Absorbs A/V” — Wave 1 series lock, NOT Messaging Guide tagline lock

**Do not treat “LUCI works with and absorbs…” as official tagline/sub-tagline boilerplate.**

It **is** locked for the Wave 1 content pack as a series constraint:

> LUCI works with and absorbs the systems already on the floor. It does not replace them. Do not name partners or competitors. Never call LUCI a layer.

— `luci-design/content-library/CURSOR-WAVE-1-PROMPT.md` (+ every Wave 1 brief under `content-library/briefs/`; email scaffolds `NET-ACQ-02`, `PULSE-02`)

It appears in the current morning-reset draft close and sibling spotlights. If Jane wants the close to sound like **official what-LUCI-is**, prefer **tagline + sub-tagline + pillars / one interface**, and either keep absorb as a short non-replacement sentence (Wave 1 consistency) or replace it with sub-tagline substance — her call. It is **not** in the Messaging Guide TAGLINE / VALUE PROPOSITION verbatim block.

### Value-prop boilerplate — use with care

Messaging Guide still prints (stale spelling / “layer” wording):

> LUCI Systems orchestrates every layer of technology running your property — AV, signage, building, and operational infrastructure — from a single interface…

— `messaging-guide.html` VALUE PROPOSITION callout

`site.ts` `valueProp` is the same idea with **A/V** spelling fixed, but still says “orchestrates every layer of technology…”  
Handbook flags `_project-context.md` “orchestrates every layer” as **retired** when it names LUCI a layer; describing *client* stack accumulation is OK. For a spotlight close, **safer locked lines** are tagline, sub-tagline, `oneOffering`, and pillars — not the long valueProp dump (also too brochure-y for early-funnel per Jane’s prior close notes).

---

## B) Morning-reset stories (attributable sources only)

**Search coverage:** `luci-design`, `luci-website`, OneDrive LUCI (Marketing / Sales / Meetings / Recordings), Wave 1 drafts, Signal Issue 01, Field Activation Guide, case-study TS + PDFs, Downloads transcripts.  
**Not found:** OneDrive `Recordings/` and `Meetings/` were empty of usable files; no Clearwater / Aliante / Yaamava / Sam’s Town / Tachi / Boyd transcript that discusses *morning reset* as a deployed habit. Sep 28 internal upgrade transcript discusses preset *bugs* at properties, not morning-reset success stories.

### Story 1 — Ameristar Council Bluffs (strongest attributable)

| Field | Content |
|---|---|
| **Internal name (Jane only)** | Ameristar Council Bluffs (Penn Entertainment; land + riverboat casino, Council Bluffs, IA) |
| **Public-safe phrasing** | “a casino customer” / “a riverboat casino property preparing a land-side transition” / “our customer” — do **not** name Ameristar in a non–case-study spotlight |
| **What happened** | After a full A/V retrofit onto LUCI, published results list **automated resets and scheduling**; body copy says built-in automation lets ops perform **daily system resets**, scheduled adjustments, and system-wide changes with significantly less hands-on intervention. Same property also runs ~146 video endpoints / 50 audio zones from one interface (scope from case study). |
| **Proof point (1–2 sentences, anonymized)** | On one casino property, after consolidating A/V onto LUCI, operations gained automated daily system resets and scheduled adjustments — so restoring a known opening state stopped being a hands-on morning checklist across separate systems. |
| **Sources** | `luci-website/src/data/caseStudyAmeristar.ts` (`results.bullets`, `results.paragraphs`); Signal Issue 01 field story `luci-website/src/assets/the-signal/issue-01-body.html` (§ council-bluffs); PDF `luci-website/public/downloads/LUCI-Case-Study-Ameristar-Council-Bluffs.pdf`; OneDrive `Marketing - Documents/Content/Case Studies/LUCI-CS-Ameristar-Council-Bluffs.pdf` |
| **Caveat** | Copy says **“daily system resets” / “automated resets and scheduling”** — not the product phrase “morning reset.” Same capability family; do not overclaim a quoted “morning reset” from Ameristar staff. No customer quote about resets (install quote only: Facilities Manager, seamless install). |

### Story 2 — Sales / product pattern (Mike Epstein) — **not a named customer**

| Field | Content |
|---|---|
| **Internal label** | Mike Epstein demo pitch pattern (“Judge Judy”) — used as “one of the most widely used” morning-reset stories in sales |
| **Public-safe phrasing** | Frame as **industry pattern / what floors see**, never “at [named casino]”: late ballgame at the pits → only pit boss has A/V control → morning team finds the wrong show on screens → scheduled morning reset stops that |
| **What happened** | On 21 Jul 2026 prospect demo (Morgan / entertainment buyer referral), Mike: creates preset → scheduler → daily morning fire; explicitly: “One of the most widely used ones is our morning reset… somebody watching a ballgame at the pits… Judge Judy’s playing on the TV.” Also: teams that otherwise “run around every morning” checking TVs/channels/music/sources. |
| **Proof point (anonymized)** | Across casino floors, overnight channel and volume drift is common enough that LUCI treats a scheduled morning reset as one of the most-used automations — so the property opens on the planned look instead of last night’s leftovers. |
| **Sources** | `/Users/janehaynie/Downloads/07-21 Customer Consultation_ Casino AV_IT Unified IPTV Platform Pitch (Lucy Systems)-transcript.docx` (~00:26:58–00:28:49); same anecdote published as tip (no customer name) in Signal Issue 01 “Set a morning reset” — `issue-01-body.html`; Field Activation Guide GM UC02 — `luci-design/.../sales/field-activation-guide-*.html` / Downloads `LUCI-Field-Activation-Guide.pdf` (local news / wrong input / 5–7am quiet window) |
| **Caveat** | **Do not invent** a property name for Judge Judy. It is LUCI’s own recurring illustration (demo + Signal + FAG), not a case-study attribution. Fine as color in an early-funnel close if labeled as the operational problem pattern, not “our customer at X.” |

### Story 3 — Field Activation Guide use case (productized, not a customer case)

| Field | Content |
|---|---|
| **Internal** | FAG § General Management UC02 |
| **Public-safe** | Same as instructional: TV flipped to local news / wrong input; scheduled reset in 5–7am window; floor already correct before traffic |
| **Proof point** | Only as **how the feature is taught to GMs**, not as a named deployment win |
| **Source** | FAG HTML/PDF paths above; Atlassian Event Scheduler article linked from FAG |
| **Caveat** | Not a customer story. Do not present as “our casino customer did X.” |

### Story 4 — Near-misses (related presets, **not** morning reset)

| Property (internal) | What exists | Why it does **not** count |
|---|---|---|
| Tachi Palace | Bingo-winner presets fire walls + audio | Immersive win moment, not scheduled open restore — `caseStudyTachi.ts` |
| Sam’s Town | Six wall presets / sportsbook | Layout switching, not morning restore — `caseStudySamsTown.ts` |
| Aliante / Yaamava / Boyd / Clearwater | Case + sales assets exist | **No** morning-reset / daily-reset anecdote found in searchable copy or transcripts |
| Client Testimonies (Valley View, Osage) | General praise | No reset language — OneDrive `.../Client Testimonies/LUCI Client Testimonies.docx` |

---

## C) Recommendation for early-funnel spotlight close

**Use at most one soft proof beat + official “what LUCI is” bridge — not a case-study dump.**

1. **Primary (if any customer color):** **Story 1 (Ameristar), anonymized** — only property with published, attributable “daily system resets / automated resets and scheduling.” Fits early funnel as one concrete floor outcome without naming the account. Keep to 1–2 sentences; do not paste Ameristar retrofit narrative into a feature spotlight.
2. **Optional color (problem pattern, not proof of a named win):** **Story 2 Judge Judy / overnight drift** — already in Signal tip language; matches the article’s problem. Use as *why* resets matter, not as “our customer told us.”
3. **Skip for this close:** FAG as if it were a case study; Tachi/Sam’s Town presets; inventing Clearwater/Boyd/etc.

**Boilerplate for the “what LUCI is” sentence:** prefer **sub-tagline substance** (“one interface to control, automate, and execute…”) or a short orchestration-engine line from org context / `oneOffering` — **not** a slogan dump of both taglines plus all four pillars. Pillars 1 + 3 map cleanly to this feature (shared control point; guest experience on purpose).

**On “absorbs”:** for Jane’s rewrite from “LUCI works with and absorbs…” — treat absorb as **Wave 1 series continuity**, optional; official locked identity is tagline/sub-tagline/pillars. If she drops absorb, replace with sub-tagline + non-replacement of existing A/V (same idea, Messaging Guide vocabulary).

---

## D) What’s missing (thin inventory — do not invent)

- **No** call recording / FDE note that says “[Named property] set a morning reset at X am and got Y outcome.”
- **No** customer quote about morning reset (Ameristar quote is install-only).
- **No** Clearwater / Aliante / Yaamava / Tachi / Sam’s Town / Boyd morning-reset anecdotes in repos or OneDrive text searched.
- Ameristar is closest proof but uses **“daily system resets”** wording, not “morning reset.”
- Judge Judy is **sales/editorial pattern**, not attributable to a named account.
- To get 2–4 *real* named-customer morning-reset stories Jane can anonymize, need: FDE / Mike / Mark confirmation of which live properties run a scheduled morning preset, or a short interview note. Until then, inventory is **1 attributable published proof + 1 reusable problem pattern**.

---

## Quick cite pack (paths only)

- Tagline/sub-tagline: `.../agent-handbook/canon/messaging-voice.md`; `luci-website/src/data/site.ts`; `.../messaging/messaging-guide.html`
- Pillars: `luci-website/src/data/pillars.ts`
- Wave 1 absorb lock: `luci-design/content-library/CURSOR-WAVE-1-PROMPT.md`
- Current draft close: `luci-design/content-library/drafts/wave-1/spotlight-morning-reset.md`
- Prior close notes: `.../EDIT-NOTES-morning-reset-close.md`
- Ameristar: `luci-website/src/data/caseStudyAmeristar.ts`; Signal `issue-01-body.html`
- Mike morning-reset pitch: `Downloads/07-21 Customer Consultation_...transcript.docx`
- FAG UC02: `luci-design/.../sales/field-activation-guide-web-published.html` (and PDF in Downloads)
