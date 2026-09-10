# LUCI — organizational context

**For:** all Grok Bots  
**Snapshot:** 28 August 2026  
**Status of this file:** verified facts are marked; inferences are labeled. If this file conflicts with `shared/CURRENT-WORK-BOARD.md` or a Cursor rule newer than this date, those win.

---

## 1. Who we are

**LUCI Systems** sells an **orchestration engine for enterprise multimedia** — software, hardware, operating model, and an **embedded engineering team** (LUCI FDE) delivered as one system. Properties run A/V, signage, and related infrastructure from **one interface**, with a team that stays.

**Tagline (verbatim):** The Orchestration Engine for Enterprise Multimedia  
**Sub-tagline (verbatim):** One interface to control, automate, and execute the entire guest experience.

**What LUCI is:** an operating system that connects infrastructure; a platform that appreciates over time; software + hardware + operating model + embedded engineers accountable from design through refinement.

**What LUCI is not:** a control panel (one system at a time); a dashboard that only reports; a point solution that creates another integration problem; a vendor that hands off after install.

**Voice in one line:** Institutions, not adjectives. Lead with the customer’s accumulated complexity; stage LUCI as subtraction — fewer variables, vendors, interfaces — not as a feeling.

Jane owns marketing and design direction. She is **not** a developer. She works in Cursor in plain English. Mike owns demos, the feature list, and sales-doc customization. Mark owns personal cadence and cold outbound. Nick appears on portal/customization vision and older upgrade checklists.

---

## 2. How the work is organized

Two git repos on Jane’s Mac (not a monorepo):

| Repo | Job |
|---|---|
| **luci-design** | Design system, Cursor rules, sales HTML/PDF, Internal Marketing Portal, The Signal, emails, social production, case-study HTML, campaign plans, this handbook |
| **luci-website** | Astro 6 static site for the lucisystems.com **rebuild**. Review deploy to `10.10.1.37`. Intended public host: Netlify |

**Critical:** local git is far ahead of GitHub. luci-design `origin/main` lagged by **271** commits in this snapshot. luci-website GitHub `main` was still **16 June 2026**; the live working branch is **`persona-hero-subhead-gold`** (~472 commits ahead). **Never treat GitHub clone as current LUCI.**

Review surfaces Jane actually uses:

- Website: **`http://10.10.1.37`** (hard-refresh Cmd+Shift+R)
- Portal: **`http://10.10.1.17:8081`**
- Stakeholder review queue: built into the portal / review site from `review-queue.json`

Public lucisystems.com today still includes **legacy Webflow** for some live properties (Signal, Field Activation Guide, some case-study embeds). The Astro site is the rebuild, targeted for **fall 2026**. Do not tell Jane to look at `localhost:4321` as the deliverable.

---

## 3. Brand decisions that brought us here

These are **locked** unless Jane reopens them.

### Positioning
- Category: orchestration engine, not integrator theater, not signage vendor.
- **Platform + partnership** as one offering. Never split into competing nav destinations.
- Control / Automate / Execute. Oversee sits under Control.
- LUCI sits **above** endpoints (e.g. Q-SYS). Honesty Protocol: credit partners. Do not imply LUCI owns native zone logic that belongs to a third party. Parked: vendor-reduction language that sounds like dropping Q-SYS.

### Voice (always)
- Always write **A/V**. Never “AV”.
- Never **layer** as a noun for LUCI (“orchestration layer” is retired).
- Use: orchestration engine; LUCI orchestrates / runs / operates / integrates / consolidates / refines; platform; infrastructure.
- Retire: absurdly simple, easy, intuitive, revolutionize, transform, empower, best-in-class, game-changing, owner’s rep (use LUCI FDE or embedded team), percentage claims in brand copy, named clients in **public** materials (case studies are the exception when approved).
- Problem first. Accumulation and silos. Operational stakes (“not optional”). Team that stays. Built in, not bolted on.
- Marketing/web may be 2nd person. SOW/MSA/proposal: 3rd person, factual.
- Tagline and value-prop boilerplate: do not paraphrase when the guide requires verbatim.

### Visual
- **De-boxed:** whitespace and hairlines, not stacked containers. Sharp corners (`border-radius: 0`) on brand surfaces that use the visual-design rule; modern guidelines allow 12–24px on some new cards — **do not invent a new radius language**. Case studies and sales docs follow their own templates.
- **Three-tier type:** Syncopate = short display only (≤ ~3 words, ≤ ~25 characters, one line). Space Grotesk = headlines, labels, metric numerals. **Inter = all running body copy, always.**
- **Mint primary, gold secondary.** Bright mint `#68E3BE` and bright gold `#EDD086` on **dark only**. Light-surface accent is **`#2b9e80`** every time. `#176B54` retired. No dark gold text on light.
- Proof via case studies, quotes, named scope — **not spreadsheet stat grids**.
- Diagrams: one canonical SVG master; each asset gets its own resized copy. Never resize the master. Ask Jane: canonical vs local.
- Photography: look like LUCI shot it. Casino = operations (racks, sportsbooks, LED walls), not gambling glamour. No in-progress field photos on social (OSHA + grand-reveal).

### How Jane works with agents
- Small local commits in Cursor are the safety net. Grok directs; the Cursor agent it invokes through `luci-cursor` commits coherent production work.
- Open visual decisions: offer 2–3 **genuine** variants on branches; Jane picks; merge winner. Tiny tweaks: just do one.
- “Make a rule” is not automatically house-wide. Ask which assets.
- Phrasebook: she never types commands.

---

## 4. Chronology (verified)

### June 2026 — foundations
- luci-design repo and stakeholder review hub stand up.
- Messaging docs sync from OneDrive Word → review HTML.
- **16 Jun:** Website rebuild locked to **Astro + Netlify + GitHub**, no CMS, **no Webflow for the new site**. luci-website scaffolded. Strategy brief + IA wireframe written (`_project-context.md` — useful for history, **stale for copy**: it still contains “orchestrates every layer”).
- The Signal Issue 01 exists as flagship editorial (zoned canvas, three fonts). Later used as the modern-guidelines flagship reference.
- Ameristar Council Bluffs case study is the first public proof pattern to migrate.

### July 2026 — system and volume
- Internal Marketing Portal production moves to **`10.10.1.17:8081`**. Old hub on `.37:8080` is superseded (cleanup still parked).
- Mike’s workflow: paste portal URL into Cursor → customize client doc. Click-to-edit in Cursor preview. Locked pages stay locked unless Jane overrides.
- Sales document system canonized (brochure, capabilities, fit-check / page-count invariant — never clip a letter page; add a page instead of silently trimming).
- Mint primary / gold secondary canonized (23 Jul).
- Inter body-copy pass across sales library (~16 Jul).
- Social: production mode. Mike green-lights Jane posting without per-post approval. **In-progress field photos retired.**
- Signal Issue 02.
- Field Activation Guide prospect version approved; customer FAG published on lucisystems.com (~23 Jul).
- Visual-options workflow (2–3 branches) added as a rule.
- Portal long-term FastAPI/TipTap plan written — **not built**.
- Client document library deferred; Mike saves locally.

### August 2026 — proof, Signal 03, New LUCI, case-study template
- Image-prompt rules: custom photography, not AI stock.
- HomeIntro ticker (NFL names) — three genericize attempts rejected; **parked**. Do not retry blur or card-over.
- Signal Issue 03: Webflow splits, teaser email, “new LUCI” as sneak-peek / **beta framing**, not a launch blast.
- LinkedIn strategy summary approved (v3). Copy pass still with Mike.
- **Case-study visual template locked to Sam’s Town** (photo-band, inline photo, mint wash, scope-story title colors). Narrative spine: consolidation, denominator first, “Consolidation you can see,” one interface, named subtraction.
- Yaamava, Ameristar, Tachi rebuilt to that spine. Yaamava becomes featured install on the website index and capabilities p08 (Ameristar no longer the default featured proof).
- Website case-study routes live on the working branch. PDFs: Ameristar and Tachi in `public/downloads/`; Sam’s Town PDF noted forthcoming in data.
- Sales: retrofit/upgrade/LED proposal work; budgetary clip fixes; Yaamava layout variant still waiting on Jane.
- Launch campaign: three streams (existing-customer beta / demand gen / warm AC tracks). Feature list waiting on Mike. **Do not call it an August launch.**
- COS calendar snapshot 27 Aug. Design repo HEAD 27 Aug. Website last **committed** bulk 20 Aug; 28 Aug uncommitted Tachi image + Sam’s Town preview HTML.

---

## 5. Surfaces and what “done” looks like

### Website (`luci-website`)
Built on the working branch: home, platform, who-we-serve (6 personas), industries (5 verticals live; corporate/campus was in early IA as a sixth — **not a live slug**), resources, FAG, blog (one post: variable reduction), four case studies, Signal 01–03, legal pages, AskLuciChat (mock/curated — not a generic sales widget at launch).

Casino is the industry template. Persona copy draws from the Field Activation Guide.

**Still open (COS):** fall launch; messaging/feature audit; e-mesh CTA/footer; ticker genericize parked; README phases stale.

### Sales and portal
Templates: brochure, capabilities, FAG, sales deck, SOW, proposal, proposal-luci-retrofit, proposal-upgrade, budgetary-estimate, MPSA (Word pipeline). Customization Studio + `_brand/SKILL.md` + per-template SKILL. Fit-check is mandatory for HTML letter docs.

### Case studies
| Property | Notes |
|---|---|
| Yaamava' | Featured on site index; first draft / review asks in portal assets |
| Ameristar Council Bluffs | Approved; PDF; “three days” story — dek must still be consolidation, not duration-only |
| Tachi Palace | Approved; copy-spine reference; website image WIP 28 Aug |
| Sam’s Town | Visual template; due for review v2 in queue |

### The Signal
Issues 01–03 exist. Cadence: start ~1st, send 15th. Next: Sep 1 / Sep 15.

### Social
LinkedIn company page, 2–3 posts/week. Friday prep. Caption closes on the abstraction (one interface / one map / one team). LED/racks are the hook, not the headline. No progress photos.

### Customer journey
Emails 1a–10 exist. Clearwater sequence is the live calendar. Tachi 60-day sent. Stay out of Mark/Mike live deals.

---

## 6. Current status

See [`shared/CURRENT-WORK-BOARD.md`](shared/CURRENT-WORK-BOARD.md) for the dated board. Do not operate from this section if the board is newer.

**Nearest customer action at snapshot:** Clearwater “LUCI is Live” (28 Aug).  
**Nearest marketing production:** September Signal start 1 Sep.  
**Largest strategic block:** Mike’s feature list + Jane’s launch bucket confirmation → then What’s New one-pager.  
**Largest build surface:** website on `persona-hero-subhead-gold`, reviewed on `.37`, GitHub not updated.

---

## 7. Inferences (do not treat as Jane locks)

- Fall 2026 is the public Astro cutover window (COS + campaign plan). Early `_project-context` “August 2026 platform release” is **overruled** by later “do not date as an August launch.”
- A machine loss without Jane’s disk / LAN VMs would lose most 2026 work; GitHub is not a backup of current main.
- Budgetary “hold until Jane confirms” on the COS parked list may be leftover after a Jul 9 trim — **ask**, don’t assume open or closed.

---

## 8. What “good” looks like for this team

- Strategy and design **settle** before Maker touches files.
- GLM does the production. ChatGPT/Claude only when the protocol gate is met.
- Review sounds like Jane at 11pm: specific issue + specific fix. No silent redesign.
- Nothing customer-facing invents claims, percentages, or Q-SYS replacement.
- Jane sees work on **`.37` / `.17`**, not as a Grok screenshot of a cloud-computer mock.
