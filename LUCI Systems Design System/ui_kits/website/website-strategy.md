# LUCI Website Strategy (Outline)

> **Design hub preview:** Open `website-strategy.html` (styled review doc). **Visual IA walkthrough:** `website-ia-wireframe.html` (nav + section order + draft copy where available). Regenerate strategy HTML after edits: `python3 md-to-strategy-html.py` in this folder.

**Status:** Draft for planning — copy details TBD  
**Last updated:** June 2026  
**Audience:** Internal (marketing, leadership, Webflow build)

This document defines information architecture, page topics, and homepage messaging for **lucisystems.com**.

### Source documents (how they relate)

| Document | Role on the website |
|----------|---------------------|
| **Messaging Guide** (canonical) | Tagline, four message pillars, key features, voice, “who hears what” — **primary copy source for the site** |
| **Persona Guide** (internal + public page) | Sales depth; informs **Who we serve** combined with orchestration story |
| **Nick · Messaging Framework V6** (`LUCI_Messaging_Framework_V6-reference.html`) | Brain dump — two pillars, services model, variable reduction, proof rules. **Incorporate selectively; does not override Jane’s approved lockup** |
| **Two-pillar diagram** (`assets/diagrams/luci-two-pillars.png`) | **Homepage visual only** — one offering (platform + embedded partnership); not split into top-level nav |

---

## Approved messaging (website — trumps V6 drafts)

Use on the site. V6 appendix/homepage drafts are **reference only** until leadership aligns the Messaging Guide.

| Element | Copy |
|--------|------|
| **Tagline** | The Orchestration Engine for Enterprise Multimedia |
| **Sub-tagline** | One interface to control, automate, and execute the entire guest experience. |
| **Value prop / boilerplate** | LUCI Systems orchestrates every layer of technology running your property — AV, signage, building, and operational infrastructure — from a single interface your team controls from anywhere. Rather than adding layers to your stack, LUCI reduces the variables, hardware, and interfaces your team has to manage. When onsite experience and operational continuity are non-negotiable, LUCI delivers coordinated, real-time execution, end to end. |

**Synced with Messaging Guide — Jun 9, 2026.**

---

## Strategic frame: one product (platform + partnership)

LUCI Systems is **one product**: orchestration software **with** embedded partnership built in. Nick’s V6 “two pillars” (software + embedded org) remain **true in the story** but must **not** drive top-level navigation — that reads as two products (“LUCI” vs “The Systems”).

| Part of the offering | What it is | How the site treats it |
|----------------------|------------|-------------------------|
| **Platform** | Orchestration software — one interface across property layers | **Platform** page + homepage teaser |
| **Partnership** | Embedded team — design, deploy, support, refine; built in, not bolted on | **Same Platform page** (section: “How we work with you”) — not a separate nav pillar |

**Website must make clear:** Software never arrives alone; partnership is part of the offering — discussed **in tandem** on Platform, not as a second nav destination.

**Diagram:** Use two-pillar visual on **homepage** (and optionally on Platform) framed as **“one offering”** — platform + partnership unified — not two site sections to choose between.

---

## Language rules (website — Jane decisions)

These override conflicting lines in V6 where noted.

| Topic | Use on public site | Avoid |
|-------|-------------------|--------|
| **Fragmented property tech** | **Layers** of technology/endpoints (slightly negative connotation is intentional — “digging through layers”) | Calling the client environment “systems” |
| **LUCI’s role** | **Orchestrates** those layers through **one interface** | Nick’s “LUCI is the layer above…” positioning |
| **“Systems” (capital S)** | Body copy on **Platform** when explaining embedded org — **not** a top-level nav label | Nav items “LUCI” / “The Systems”; client AV/IT as “systems” |
| **Two-pillar framing** | Homepage **visual + copy** only | Splitting site IA into two product pillars |
| **Client endpoints** | AV, signage, building, operational tech, endpoints, infrastructure, property environment | Client tech as “systems” |
| **Internal terms** | Plain language on site | Leading with FDE, infrastructure jargon tables, naming-convention appendices |
| **Philosophy principles** | Light touch only (see below) | Dedicated “principles” section mirroring V6 philosophy chapter |
| **V6 capability↔principle table** | **Blog / long-form content**, not core web UX | Full table on Platform page |

**Voice:** Still follow Messaging Guide — institutions not adjectives, subtraction framing where it helps, declarative tone.

---

## Variable reduction (important — how to use on the site)

**Idea (from V6):** LUCI’s value is not “simple UI.” Each variable removed from the environment eliminates a tree of downstream questions. Complexity shrinks because there is **less to manage**.

**Where it belongs on the website:**

| Placement | Treatment |
|-----------|-----------|
| **Homepage** | One band: headline + 2–3 sentences + optional 3–4 bullets (not the full V6 table) |
| **Platform** | Core narrative: accumulation → variable reduction → vs alternatives; tie to key features as *examples* of variables removed |
| **Why LUCI (standalone page)** | **Not in nav at launch** — optional later for SEO/long-form |
| **Blog** | Full “variable reduction” article with V6-style table for CIO/COO readers |

**Signature line (usable):** *Complexity isn’t solved by a better interface. It’s solved by a shorter list of things to manage.*

**Do not** bury this only in About/philosophy — it is a primary **why buy** story for technical and operational buyers.

---

## Philosophy & principles (light touch only)

V6 principles (subtraction as design discipline, standardization, software+ops unity, discretion) stay **mostly internal**.

| Principle | Website treatment |
|-----------|-------------------|
| Subtraction / variable reduction | **Yes** — via variable-reduction band (above), not labeled “philosophy” |
| Standardization | **Yes** — woven into Platform copy |
| Software + operations unity | **Yes** — homepage “one offering” band + Platform (tandem) |
| Discretion / no client names in hero | **Yes** — proof rules below |
| Full “LUCI View” dark-panel poetry | **About page only** (optional shortened), not homepage |

---

## How we work with you (six services — on Platform)

Six **named services** (any customer, any time — not a one-time project menu). V6 list; public names may simplify on site.

| # | Service (V6 name) | Public site one-liner |
|---|-------------------|------------------------|
| 01 | LUCI FDE | Engineers embedded from scoping through year five — same team, no handoff *(describe role; “FDE” optional in subcopy)* |
| 02 | Design & Deployment | In-person scoping, architecture, stand-up — phased so value lands early |
| 03 | Owner's-Rep Partnership | Standing extension of your enterprise — roadmap, vendors, capital, technical decisions |
| 04 | Training & Enablement | Role-based curriculum; knowledge survives turnover |
| 05 | Support & Operations | One accountable team, not tiered vendor queue — including off-hours |
| 06 | Continuous Refinement | Platform appreciates on the same line item; field learning feeds releases |

**Placement (decided):** **Platform page** §6 — “How we work with you” (six services + “available anytime”). Homepage **teaser** + link to Platform anchor. **No** `/the-systems` or separate Services nav item.

**Copy rule:** Never “professional services” or “support package.” Prefer **“How we work with you”** / **“built into every deployment”** — avoid **“The Systems”** as a nav label.

**Engagement cycle** (Plan → Deploy → Operate → Refine): **sales deck + blog**, not primary site IA.

---

## Message pillars on the website

**Use Messaging Guide four pillars** for site structure (not V6’s five alternate pillars) until Jane completes a deliberate merge with Nick.

| MG pillar | Typical site placement |
|-----------|------------------------|
| 01 Complete visibility & control | Platform (capabilities) |
| 02 Align teams by default | Who we serve + Platform |
| 03 Activate guest experience | Industries + CMO angle on Who we serve |
| 04 Invest / appreciates over time | CFO angle + Platform (partnership / refinement) |

V6 pillar 05 (“one platform, one embedded team, one outcome”) is a strong **one-offering summary line** for homepage diagram band — compatible with MG, not a replacement.

---

## Proof, logos, and client names (from V6 §08)

| Context | Named clients? |
|---------|----------------|
| Homepage body / hero / pillar copy | **No** — portfolio scale language only |
| Logo wall | **Yes** — trusted partners, no rhetorical “X saved Y%” |
| Case studies | **Yes** — with permission; full story |
| Message pillars / value prop | **No** |
| Sales deck opening | **No** (logo wall later) |

**Brand-level portfolio line (OK on site):**  
*LUCI runs at some of the largest, most operationally complex properties in gaming and hospitality — where guest experience and operational uptime are not optional.*

**Never in brand copy:** % reduction headlines, “learnings from Client A to Client B,” stat+logo combo claims.

---

## Primary navigation (simplified — one product)

**Removed from nav:** `LUCI` ▾, `The Systems` ▾, `Solutions` ▾. Case studies live **only** under Resources.

```
Logo → Home

Platform            →  Single page: software + capabilities + how we work with you (tandem)
                       [Optional later: anchor links #capabilities #partnership]

Industries ▾        →  Casinos & gaming · Hotels & resorts · Sports & venues
                       · Airports & transportation · Conference & convention centers
                       · Corporate & campus properties

Who we serve        →  One page: orchestration by function + what each team can do in LUCI
                       (merge Persona Guide + V6 entry points; internal workshop on “can do”)

Resources ▾         →  Hub · Blog · Case studies · Support portal
                       (no The Signal — customer-only; see below)

Company ▾           →  About · Contact · Careers [TBD]

[Primary CTA]       →  Request a conversation / See LUCI in action
```

**Nav label note:** Use **Platform** (not “LUCI” next to logo “LUCI Systems”). “Product” is acceptable alternate; avoid redundant naming.

**Utility footer:** Customer login · Privacy · Terms · Accessibility · Sitemap

---

## Customer access: The Signal

**The Signal** (newsletter hub) is for **existing customers**, not public marketing navigation.

| Rule | Treatment |
|------|-----------|
| Primary nav / Resources ▾ | **Do not list** The Signal |
| Homepage | **No** Signal promo card — use Resources teaser (hub, blog, case studies) |
| Access | **Customer login** (footer utility) and/or authenticated experience; onboarding email (e.g. Signal welcome) links customers in |
| Public copy | May mention “monthly updates for customers” without a nav path to `/newsletter` |
| Production | `/newsletter` route should be **customer-gated** on live site |

Design system hub keeps Signal assets under **Newsletter** for internal/Webflow build — separate from public IA.

---

## Industries (launch — six pages)

| Vertical | Page focus |
|----------|------------|
| **Casinos & gaming** | Gaming floors, guest experience, uptime |
| **Hotels & resorts** | Property-wide AV, signage, ops continuity |
| **Sports & venues** | Arenas, event spaces, game-day orchestration |
| **Airports & transportation** | Airports, rail/intermodal stations, transit hubs — one story (fragmented endpoints, high-stakes uptime) |
| **Conference & convention centers** | Meeting spaces, digital signage, event turnover |
| **Corporate & campus properties** | Headquarters, multi-building campuses, enterprise facilities — AV, signage, and building tech as one coordinated layer |

**Removed:** Integrated resorts (overlaps casinos + hotels + sports; ambiguous label).

### Phase 2 industry candidates (not in launch nav)

| Vertical | Fit with LUCI |
|----------|----------------|
| Museums & cultural venues | AV-heavy visitor journeys, multi-zone control |
| Higher education campuses | Stadiums, unions, lecture halls, distributed endpoints |
| Entertainment districts / mixed-use | Retail + hospitality + signage at scale |
| Healthcare campuses | Wayfinding, operational AV (often longer sales cycle) |
| Cruise & maritime | Hospitality-like complexity; niche proof path |

---

## Homepage messaging map (revised)

**Division of labor:** Home = **why care + who it’s for + proof**; [Platform page](#platform-page-scroll-order) = **how it works + what you get + how we show up**.

| # | Section | Job | Source |
|---|---------|-----|--------|
| 1 | **Hero** | Tagline + sub-tagline + CTA | Approved lockup |
| 2 | **Value band** | Boilerplate | Approved value prop |
| 3 | **One offering** | Diagram: platform + partnership unified — **not** two nav destinations | V6 diagram + one-product framing |
| 4 | **Variable reduction** | Teaser — structurally different | V6 principle (simplified) |
| 5 | **Four pillars** | Outcomes | Messaging Guide 01–04 |
| 6 | **Platform teaser** | Key features headline + link to Platform | Messaging Guide (not full feature list) |
| 7 | **Partnership teaser** | Six services headline + link to Platform §6 | V6 §04 — anchor on Platform |
| 8 | **Industries** | Vertical relevance | Industry pages |
| 9 | **Who we serve** | By function, one orchestration story | Persona Guide + V6 §07 |
| 10 | **Proof** | Logo wall + Ameristar case study | Proof rules §08 |
| 11 | **Resources** | Blog, case studies, hub — no Signal (customer-only) | Resources hub |
| 12 | **Closing CTA** | Convert | — |

**Removed from homepage:** Full engagement cycle, philosophy principles list, V6 alternate tagline, duplicate “why buy” page content.

---

## Platform page (scroll order)

Single deep dive at `/platform` (label TBD: **Platform** vs **The Platform**). Software and partnership on **one scroll** — not split pages.

| # | Section | Job | Source |
|---|---------|-----|--------|
| 1 | **Hero** | Orchestration engine + one interface | Approved lockup territory |
| 2 | **The problem** | Layers of property tech | Language rules |
| 3 | **How it works** | Product UI / map control visual | Product marketing |
| 4 | **Capabilities** | Messaging Guide key features (de-boxed) | Messaging Guide |
| 5 | **Why it’s structurally different** | Variable reduction + vs control panel / dashboard / point solution | V6 (absorbs old “Why LUCI” nav page) |
| 6 | **How we work with you** | Six services + “available anytime”; embedded team | V6 §04 |
| 7 | **CTA** | Request conversation / See LUCI in action | — |

**Retired as separate IA destinations:** `/the-systems`, `/capabilities`, `/why-luci` — content lives here unless spun out as blog posts later.

---

## Who we serve (single page)

**Not** six persona microsites.

**Structure:**

1. Opening: multimedia orchestration — one platform, every function connected  
2. **By function** (cards or rows): Leadership · Operations · Technology · Finance · Marketing/Guest experience · Technical/Facilities  
3. For each: V6 “message that lands” + Persona Guide pain/outcome + **TBD: what this team can do in LUCI** (internal workshop)  
4. CTA: Platform + Contact  

**Later:** Blog/resources filter by function tag.

---

## Page inventory (summary)

| Page | Topics |
|------|--------|
| **Home** | [Homepage map](#homepage-messaging-map-revised) — teasers to Platform |
| **Platform** | [Platform scroll order](#platform-page-scroll-order) — unified product + partnership |
| **Industries** | Template per vertical (×6) — see [Industries (launch — six pages)](#industries-launch-six-pages) |
| **Who we serve** | Combined persona/orchestration page |
| **Resources** | Hub · Blog · **Case studies** · Support — no public Signal |
| **The Signal** | Customer-only via login — not in page inventory nav |
| **Case study detail** | Named proof; Ameristar first (linked from Resources) |
| **About** | Optional short worldview; founders/integrator DNA — not V6 full philosophy page |
| **Contact** | Conversion form |

---

## Content → channel matrix (V6 ideas routed correctly)

| V6 content | Website | Sales deck | Blog / resources |
|------------|---------|------------|------------------|
| Two pillars + diagram | **Home** (one offering); optional on Platform | Yes | — |
| Six services | **Platform** §6 | Yes | Service deep-dives optional |
| Variable reduction table | Home teaser + **Platform** §5 | Optional slide | **Full article** |
| Capability ↔ principle table | — | Appendix | **Yes** |
| Engagement cycle | — | **Yes** | Optional series |
| “What this model produces” | Fold into MG pillars | Yes | — |
| Persona cards | Who we serve | Tailored opens | — |
| Proof / client rules | **All public pages** | Decks | Case studies |
| V6 tagline “layer above” | **Do not use** | — | — |

---

## Standard site requirements

Unchanged from prior draft: conversion paths, legal, support portal link, SEO, accessibility, analytics, security summary [TBD], press/partners optional.

---

## Open questions

1. ~~Dedicated Systems/Services page at launch?~~ **Resolved:** folded into **Platform**; no separate nav.  
2. ~~Sub-tagline final wording.~~ **Resolved:** One interface to control, automate, and execute the entire guest experience.  
3. Primary CTA label.  
4. Launch industries vs proof-gated.  
5. **Internal workshop:** What can each function *do in LUCI* on Who we serve?  
6. When to reconcile Messaging Guide pillars with V6 pillar set (Jane-owned).  
7. Nav/page label: **Platform** vs **The Platform** vs **Product**.  
8. Platform §6 headline: **“How we work with you”** vs **“Partnership”** vs **“Delivery”**.  
9. Simplify public service names (e.g. “Support & operations” vs internal FDE naming).

---

## Suggested build phases

| Phase | Scope |
|-------|--------|
| **1 — Foundation** | Home (one offering + variable reduction + approved lockup), **Platform** page, Contact, legal |
| **2 — Audience & proof** | Who we serve, industries (3 launch verticals), case studies under Resources, logo wall rules |
| **3 — Resources** | Hub, blog template (public); customer-gated Signal route |
| **4 — Depth** | Remaining industry pages (6 total), variable-reduction long read (blog), engagement-cycle content |

---

## Next steps

1. Jane + Nick align: one-product public language (“layers” vs V6 “layer above”; partnership in tandem).  
2. Wireframe **Platform** page + simplified nav in `website-ia-wireframe.html`.  
3. Schedule “what each team can do in LUCI” workshop for Who we serve.  
4. Label pass: Platform nav + §6 partnership headline.  
5. Update Messaging Guide when pillar/tagline merge is ready — **website follows MG, not V6 lockup**.
