# LUCI Website Rebuild — Project Context

**Last updated:** 2026-06-16  
**Purpose:** Running source of truth for the lucisystems.com rebuild. Update this file as decisions are made. Paste into any new conversation for a quick briefing.

---

## Project overview

Full rebuild of **lucisystems.com** from scratch — replacing the current single scrolling page (no global nav) with a minimal multi-page site built for self-serve evaluation, qualified pipeline, and AI/LLM discoverability.

**Strategic foundation:** Minimal canonical site + intelligent discovery layer + AISEO infrastructure + interactive proof.

**Why now:** Major platform release ships August 2026; industry expansion follows. Site must establish category leadership before buyers arrive via search, AI tools, or sales.

**Source documents in this repo:**
- `LUCI Systems Design System/ui_kits/website/website-strategy-brief.html` — leadership brief (purpose, positioning, experience principles)
- `LUCI Systems Design System/ui_kits/website/website-ia-wireframe.html` — IA + approved draft copy + page-by-page section structure
- `LUCI Systems Design System/ui_kits/website/website-strategy.html` — extended strategy outline (reference)

**Design guides for the build** (how to use each):

| Source | Role in rebuild |
|---|---|
| **IA wireframe** | Structure, nav, section order, approved copy — structural authority |
| **Sales brochure** (`ui_kits/sales/brochure.html`) | Visual language, condensed product story, two-forces diagram treatment |
| **Current lucisystems.com** | What worked (hero rhythm, proof placement, logo wall); what to retire (stat grids, buried case studies, monolith scroll) |
| **Capabilities doc** | Platform depth, services list, orbit diagram — reference for `/platform` |
| **Case study** (`ameristar-council-bluffs.html`) | Proof page template + live content to migrate |

---

## Stack & workflow

| Layer | Decision |
|---|---|
| **Framework** | Astro |
| **Deployment** | Netlify (existing account) |
| **Version control** | GitHub |
| **Blog** | Markdown files (`.md`) within the Astro project |
| **Editor** | Cursor |
| **CMS** | None |
| **Legacy platforms** | No Webflow, no Squarespace |

**Content editing model:**
- Blog posts: written in Markdown, editable without touching layout code
- Site copy (headlines, callouts, pillars): edited directly in code via Cursor global search (`Cmd+Shift+F`)
- No headless CMS at launch

### Accounts & setup (what you actually need)

**Astro does not require an account.** [astro.build](https://astro.build) is the framework docs site — not a hosting platform. There is nothing to sign up for there.

| What | Required? | Notes |
|---|---|---|
| **Node.js** (local) | Yes | Install from [nodejs.org](https://nodejs.org) — LTS version. Runs `npm create astro@latest` locally. |
| **GitHub** | Yes | Repo for the Astro project + version control |
| **Netlify** | Yes | Existing account — connect to GitHub repo for deploys |
| **Cursor** | Yes | Editor (already in use) |
| **astro.build account** | No | Not a thing — Astro is open-source, free |
| **Navless** | No | Discovery layer built in-house (see below) |

**Local project creation** (when ready — no Astro signup):
```bash
npm create astro@latest
```
Then connect the repo to Netlify; Netlify auto-detects Astro builds.

**Optional later:** LLM API key (OpenAI, Anthropic, etc.) for Phase B grounded search — only when that layer ships.

---

## Brand

### Colors

| Token | Hex | Use |
|---|---|---|
| Navy deep | `#0A161C` | Dark sections, footer |
| Navy | `#10232D` | Nav, dark panels |
| Navy mid | `#314955` | Secondary text on light |
| Mint | `#68E3BE` | Accent on dark only |
| Sand | `#E5E3DF` | Warm light panels |
| Off-white | `#F5F8FA` | Reading canvas (not pure white) |
| Body ink | `#354F5C` | Body text on light |
| Light accent | `#2b9e80` | Light-surface accent — kickers, labels, links, bars, icons (canonized) |

**Accent note:** Light-surface accents use `#2b9e80` (canonized brand light accent) — used every time on white/off-white/light. `#176B54` is retired. Bright mint/gold stay dark-only.

#### Atmosphere colors (scroll-zone dimension)

Mint stays the **primary accent** (dark surfaces only). Three complementary tones add depth on scroll — like Railway’s secondary glows — without competing with mint in the hero.

| Token | Hex | Character | Typical use |
|---|---|---|---|
| **Harbor** | `#4A7285` | Cool blue-teal | Platform / product sections; tech credibility |
| **Clay** | `#B8926A` | Warm sandstone | Proof, case studies, industries; hospitality warmth |
| **Dusk** | `#8A7FA6` | Muted lilac | Partnership, team, editorial breaks |

**Rules:** Use as section tints (`--atmosphere-*-tint` at ~9–10% opacity), soft gradients, or illustration fills — **one per section**, not on the same viewport as a full mint hero. Never for small body text on light. CSS vars: `--atmosphere-harbor`, `--atmosphere-clay`, `--atmosphere-dusk` (+ `-rgb`, `-tint`).

### Homepage hero (locked)

- **Headline:** Control the whole floor.
- **Lead:** Map-based control for every display, source, and zone — with a team that stays.
- Tagline remains for SEO, footer, and sales collateral — not the homepage lead.

### Typography

| Role | Font |
|---|---|
| Display / headers | **Syncopate** (700) — short, high-impact only |
| Body / real headlines | **Space Grotesk** (400–700) |

**Rule:** Syncopate for masthead-scale moments and tracked uppercase labels only. Article headlines, section titles, and running copy = Space Grotesk bold/semibold.

### Design principles (from design system)

- De-boxed layout — whitespace and hairlines, not stacked containers
- Sharp corners (`border-radius: 0`) — defining brand trait
- Mint accent bar (4px) reserved for true callouts and pull quotes
- One display-scale moment per page max
- Proof via visuals and case studies — not spreadsheet-style stat grids

---

## Site structure & navigation

### Primary nav (launch)

**Home · Platform · Who We Serve · Industries · Resources · About · Contact**

Persistent CTA in header: **Request a conversation** / **See LUCI in action**

### Dropdowns

**Industries** (6 verticals — proof-gated at launch):
1. Casinos & gaming
2. Hotels & resorts
3. Sports & venues
4. Airports & transportation
5. Conference & convention centers
6. Corporate & campus properties

**Resources:**
- Blog
- Case studies
- Support portal
- Hub (resources index)

**Note:** Strategy brief originally used "By function" and "Company" as nav labels. Build uses **Who We Serve** (persona/function page) and top-level **About** + **Contact** instead.

### Utility footer (all pages)

Customer login · Privacy · Terms · Accessibility · Sitemap

**The Signal** (newsletter) — customer login/utility only; **not** in public nav.

### URL map (draft)

| Page | Path |
|---|---|
| Home | `/` |
| Platform | `/platform` |
| Who we serve | `/who-we-serve` |
| Industry (template × 6) | `/industries/{vertical}` |
| Resources hub | `/resources` |
| Case studies index | `/resources/case-studies` |
| Case study detail | `/resources/case-studies/ameristar-council-bluffs` (live content exists) |
| Blog index | `/blog` |
| Blog post | `/blog/{slug}` |
| About | `/about` |
| Contact | `/contact` |

---

## Approved copy (canonical)

### Lockup

**Tagline:** The Orchestration Engine for Enterprise Multimedia

**Sub-tagline:** One interface to control, automate, and execute the entire guest experience.

**Primary CTA:** Request a conversation  
**Secondary CTA:** See LUCI in action

### Value proposition (boilerplate)

LUCI Systems orchestrates every layer of technology running your property — AV, signage, building, and operational infrastructure — from a single interface your team controls from anywhere. Rather than adding layers to your stack, LUCI reduces the variables, hardware, and interfaces your team has to manage. When onsite experience and operational continuity are non-negotiable, LUCI delivers coordinated, real-time execution, end to end.

### One offering

**Summary line:** One platform, one embedded team, one outcome.

**Platform:** The multimedia orchestration engine your team runs day to day.

**Partnership:** The team that designs, deploys, supports, refines, and partners with your property — built in, not bolted on.

**Offering statement:** LUCI is a fully managed A/V operating platform — software, hardware, operating model, and an embedded engineering team — deployed as a complete system your team takes over from day one.

### Variable reduction

**Headline:** Complexity isn't solved by a better interface. It's solved by a shorter list of things to manage.

**Accumulation:** Complex environments don't fail because of what they lack. They fail because of what they accumulate. Every property runs on a stack of vendors, processors, interfaces, and workarounds that each made sense at the time, but create downstream challenges.

**Subtraction:** LUCI doesn't address this with an additional tool; it addresses this with the principle of subtraction. By removing variables. Its success is evidenced by the number of things our clients no longer have to think about.

### Four message pillars

1. **Complete visibility and control** — One interface surfaces every endpoint, zone, and system across your property. Every team sees the same picture and acts from the same place.
2. **Align your teams by default** — LUCI connects every team to the same system, so your organization can stop negotiating internally and start executing towards a shared vision.
3. **Fully activate the guest experience** — Turn passive screens into purposeful moments by planning, programming, and responding to guest signals in real time.
4. **Invest in the only A/V that scales and improves** — Traditional A/V depreciates and expires. LUCI doesn't. When you expand into sister properties, each one benefits from what came before — and Year Five is more capable than Year One on the same line item.

### Platform features (6)

- Map-based dashboard — Live visual map of every display, audio zone, and system endpoint across the property
- Open API integration — Connects to any A/V, signage, building, or content system
- PIN-delegated control — Every user controls only their designated zones
- Predictive monitoring & alerts — Surfaces and resolves common issues automatically, before the guest notices
- Mobile control from any device — Full property control from any authorized device, on or off property
- Scalable by architecture — Add venues, floors, or sister properties without replacing the core

### Six services (embedded partnership)

Intro: Six capabilities — available anytime, built into every deployment.

1. **LUCI FDE** — Engineers embedded from scoping through year five — same team, no handoff
2. **Design & Deployment** — In-person scoping, architecture, stand-up — phased so value lands early
3. **Owner's-Rep Partnership** — Standing extension of your enterprise — roadmap, vendors, capital, technical decisions
4. **Training & Enablement** — Role-based curriculum; knowledge survives turnover
5. **Support & Operations** — One accountable team, not tiered vendor queue — including off-hours
6. **Continuous Refinement** — Platform appreciates on the same line item; field learning feeds releases

### LUCI is / is not

**LUCI is:**
- An operating system that connects infrastructure
- Software, hardware, operating model, and embedded engineering — delivered as one system
- A platform that appreciates over time
- A team of seasoned engineers accountable from design through ongoing refinement

**LUCI is not:**
- A control panel (runs one system at a time)
- A dashboard (reports on a property, doesn't operate one)
- A point solution that creates an integration problem
- A vendor that hands off after deployment

### Who we serve — persona lines

Opening: Multimedia orchestration — one platform, every function connected.

| Function | Line |
|---|---|
| **Leadership** (CEO / GM) | Your floor is already influencing guest behavior. LUCI makes that influence more targeted and activating. |
| **Operations** (COO / Gaming Director) | Run a tighter operation. Automate the routine. Respond instantly to the unexpected. One team accountable for the whole outcome. |
| **Technology** (CIO / IT Director) | One interface for every system on the property — on standard network infrastructure, without proprietary hardware or specialist programming. |
| **Finance** (CFO) | Infrastructure that appreciates. One subscription replaces compounding capital costs — and year five is more capable than year one on the same line item. |
| **Marketing / Guest experience** (CMO) | Deliver the right experience, in the right zone, at exactly the right moment — every time, across the whole property. |
| **Technical / Facilities** (AV Manager) | See everything. Control anything. From any device. Without leaving the floor. |

### Proof copy

**Portfolio line:** LUCI runs at some of the largest, most operationally complex properties in gaming and hospitality — where guest experience and operational uptime are not optional.

**Featured case study — Ameristar Council Bluffs:**
- Title: Three days to a future-ready platform
- Dek: LUCI completed a full retrofit of Ameristar Council Bluffs' AV infrastructure in under three days, modernizing a system that had run since 2012 and centralizing control on land to prepare the property for its next phase of growth.
- Live page exists: `/case-studies/ameristar-council-bluffs` (will migrate to `/resources/case-studies/...`)

---

## Page structure (section order)

### Home (`/`) — 12 sections

1. **Hero** — Tagline + sub-tagline + CTA · *must show platform in action (UI, zone map, or in-action visual — not copy alone)*
2. **Value band** — Approved value prop boilerplate
3. **One offering** — Two-pillar diagram + platform/partnership summary → link to Platform
4. **Variable reduction** — Teaser headline + subtraction body
5. **Four message pillars** — Outcome blocks
6. **Platform teaser** — Top 3 features → link to `/platform#capabilities`
7. **Partnership teaser** — Six services intro + list → link to `/platform#partnership`
8. **Industries** — Six vertical entry cards
9. **Who we serve** — Persona teaser rows → link to `/who-we-serve`
10. **Proof** — Logo wall + Ameristar case study callout
11. **Resources** — Hub teaser (Blog · Case studies · Support)
12. **Closing CTA** — Request a conversation / See LUCI in action

**Homepage role-path rule:** Most executives land on Home and never open nav dropdowns. Section 9 (Who we serve) is the primary routing moment for function-specific proof — not the nav alone.

### Platform (`/platform`) — 7 sections

1. Hero — Tagline lockup
2. The problem — Accumulation / layers of property tech
3. How it works — Product visual (map-based control UI)
4. Capabilities — All 6 features (`#capabilities`)
5. Why it's structurally different — Variable reduction + LUCI is / is not
6. How we work with you — Six services + offering statement (`#partnership`)
7. CTA

### Who we serve (`/who-we-serve`) — 3 sections

1. Opening — Orchestration by function
2. By function — Full persona rows + LUCI capabilities by role *(workshop pending)*
3. CTA — Links to Platform + Contact

### Industry page (template × 6) — 5 sections

1. Hero — Vertical-specific headline *(TBD per vertical)*
2. Vertical challenges — Context *(TBD)*
3. How LUCI fits — Pillar 03 (guest experience activation)
4. Proof — Case study + vertical logo subset
5. CTA

### Resources hub (`/resources`) — 3 sections

1. Hero — "Resources" + deck
2. Featured — Ameristar case study card
3. Browse — Case studies · Blog · Support portal · Hub

### Case studies (`/resources/case-studies`) — 3 sections

1. Index hero — Portfolio line
2. Study list — Featured Ameristar + future studies
3. Detail template — Challenge · approach · outcomes · quotes · CTA  
   *(Reference: `ui_kits/case-studies/ameristar-council-bluffs.html`)*

### Blog (`/blog`) — template

- Index: post list
- Article: title · deck · body · related posts · CTA
- Planned topics: variable reduction table, capability ↔ principle deep dive, engagement cycle (Plan → Deploy → Operate → Refine)

### About (`/about`) — 4 sections

1. Hero — Offering statement
2. Worldview — Accumulation + subtraction (light touch)
3. One offering — Summary + two-pillar diagram
4. CTA

### Contact (`/contact`) — 3 sections

1. Hero — "Start a conversation"
2. Form — Name · Organization · Role · Message · Submit
3. Supporting — What happens after you reach out *(TBD)*

---

## Strategic principles (non-negotiable at launch)

1. **Hero shows the platform** — Real UI, property context, or compelling in-action visual. LUCI is easy to misread (signage vendor, AV integrator, content production). Copy alone cannot fix that at executive speed.
2. **Minimal canonical site** — Stable IA humans and search engines can rely on; escalating depth Home → Platform → Resources.
3. **Intelligent discovery layer** — Plain-language intent entry built **in-house** (not Navless). Sits on top of the static site; not a replacement for it. See **Discovery & personalization** section below.
4. **AISEO infrastructure** — `llms.txt`, semantic HTML, structured schema so LUCI is citable in ChatGPT, Perplexity, etc.
5. **Interactive proof** — Platform demos, walkthroughs, structural visuals (disk model, rack before/after, zone diagrams).
6. **No popups or exit-intent modals** at launch.
7. **No generic floating sales-chat widget** at launch — discovery layer is intent-driven, not interrupt-driven.
8. **Authority through proof** — not proclaimed in hero copy. Logos and case studies used strategically.
9. **Platform + partnership in tandem** — never split into competing nav destinations. Two-pillar diagram = one offering visual.

---

## Audiences — what each must leave believing

| Function | Belief |
|---|---|
| **Leadership** | The floor shapes guest behavior — LUCI makes that influence deliberate and property-wide. |
| **Technology** | Enterprise AV runs as standard network infrastructure — one interface, no proprietary sprawl. |
| **Operations** | The property runs tighter with one accountable team — routine automated, unexpected handled fast. |
| **Finance** | Multimedia infrastructure appreciates — one subscription replaces the 5–7 year refresh cycle. |
| **Marketing** | Campaigns aren't limited to marketing's screens — schedule and coordinate across the whole property. |
| **Facilities / AV** | Property AV doesn't mean server-room runs — proactive command of one coherent system. |

---

## Conversion model

- **Primary CTA:** Talk to us / Demo — consistent placement; single action optimized toward
- **Self-serve path:** Platform depth, industries, Who we serve, Resources — scannable, escalating clarity
- **Intent discovery path:** Plain-language Q&A surfaces curated answers → hands off to CTA / form / scheduler
- **Anti-clutter:** No popups, no generic chat at launch; behavior-based CTA emphasis on long pages only (e.g. Platform scroll) may follow later

---

## Discovery & personalization (build in-house)

**Decision:** Build custom discovery + persona layers in Astro — do **not** embed Navless or a generic chat widget. Navless was evaluated as a buy option; custom fits better because content is already structured in this repo, brand control matters, and Astro + tagged Markdown gives a native content model.

### Persona personalization (no LLM required)

Content blocks tagged in frontmatter:

```yaml
personas: [finance, leadership]
industries: [casinos]
topics: [tco, subscription]
```

**Behaviors:**
- Homepage role picker: "Which best describes your role?" → reorder/highlight Who we serve rows, swap proof callout, persist in `sessionStorage`
- Deep links for sales: `/who-we-serve?role=finance`, `/platform?role=it`
- Components show/hide or emphasize tagged content per selected persona

**Persona keys:** `leadership` · `operations` · `technology` · `finance` · `marketing` · `facilities`

### AI search / ask bar (phased)

| Phase | What | When |
|---|---|---|
| **A — Curated intent** | ~20–30 mapped questions → styled answer cards + page links. No LLM. Zero hallucination risk. | Launch or shortly after core site |
| **B — Grounded AI** | Site content indexed; Netlify Function + LLM with retrieved chunks; answers cite pages | After content corpus stable |
| **C — Playlists + handoff** | Shareable proof bundles per persona/industry; CTA wired to contact | Sales-driven, post-launch |

Phase B uses selected persona as context when available.

### AISEO (ships with core site)

- `llms.txt` at site root
- JSON-LD structured data
- Semantic HTML throughout
- Content tagged for both human nav and LLM citation

### Build sequence

1. Core Astro site — wireframe pages, brochure-informed visual system, current-site proof patterns
2. Persona self-selection + tagged content
3. AISEO baseline (`llms.txt`, schema)
4. Curated intent ask bar (Phase A)
5. Grounded AI search (Phase B)
6. Playlists / advanced handoff (Phase C)

---

## Assets & references in design system

| Asset | Path |
|---|---|
| Two-pillar diagram | `assets/diagrams/luci-two-pillars.png` |
| System diagram (disks) | `assets/diagrams/luci-system-diagram-v3.svg` |
| System architecture | `assets/diagrams/luci-system-architecture.svg` |
| Platform screenshot | `ui_kits/sales/assets/interface-floor-view.png` |
| Ameristar case study (source) | `ui_kits/case-studies/ameristar-council-bluffs.html` |
| Capabilities doc (sales reference) | `ui_kits/sales/capabilities-document.html` |
| Field Activation Guide | `ui_kits/sales/field-activation-guide.html` |
| Persona guide | `ui_kits/review/messaging/personas.html` |
| Sales brochure (visual guide) | `ui_kits/sales/brochure.html` |
| Messaging guide | `ui_kits/review/messaging/messaging-guide.html` |

---

## Phases (updated for Astro build)

| Phase | Status | Scope |
|---|---|---|
| **Phase 1** | Complete | Strategy brief — align on foundation, structure, content priorities |
| **Phase 2** | Complete | IA + wireframe — nav, page templates, approved draft copy |
| **Phase 3** | **In progress** | **Astro build on Netlify** — pages, content, proof assets, discovery layer pilot |
| ~~Phase 3 (original)~~ | ~~Superseded~~ | ~~Webflow build~~ — replaced by Astro + GitHub + Netlify |

---

## Open questions / TBD

- [ ] **Interactive demo / platform walkthrough** — format (video, clickable tour, explorable visual); Ramp-style benchmark
- [ ] **Homepage hero visual** — which proof asset ships at launch (floor-view screenshot, disk model, zone map, video)
- [ ] **Industry page copy** — vertical-specific headlines and pain points for all 6 verticals
- [ ] **Who we serve** — "LUCI capabilities by role" section *(workshop pending)*
- [ ] **Contact page** — post-submit flow copy
- [ ] **Careers** — in Company nav as TBD; defer at launch
- [ ] **Success measure baselines** — traffic, pipeline, discoverability metrics post-launch
- [ ] **Case study URL migration** — current live path `/case-studies/ameristar-council-bluffs` → new `/resources/case-studies/...` (redirect strategy)
- [ ] **Blog launch content** — which posts ship with site vs. post-launch
- [ ] **LLM provider** — OpenAI vs Anthropic vs other for Phase B search *(when Phase B starts)*
- [ ] **Astro project location** — new repo vs folder in this monorepo

---

## Decisions log

| Date | Decision |
|---|---|
| 2026-06-16 | Full rebuild from scratch — **Astro + Netlify + GitHub**, no CMS, no Webflow |
| 2026-06-16 | Blog as Markdown files in Astro project; site copy edited in code via Cursor |
| 2026-06-16 | Nav: Home · Platform · Who We Serve · Industries · Resources · About · Contact |
| 2026-06-16 | Phase 3 updated from Webflow build to Astro/Netlify build |
| 2026-06-16 | **Design guides:** IA wireframe (structure) + sales brochure (visual/story) + current site (proof patterns) |
| 2026-06-16 | **Discovery layer:** build in-house — persona personalization + phased AI ask bar; Navless not used |
| 2026-06-16 | **No Astro account needed** — open-source framework; GitHub + Netlify + Node.js locally |

---

*Update the **Decisions log** and **Open questions** sections whenever scope, copy, or architecture changes.*
