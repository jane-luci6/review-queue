# New LUCI Upgrade Landing Page — brief for Cornelius

**From:** Jane, via Cursor (GLM)
**Date:** 22 September 2026
**Status:** Blueprint ready for build; some content still to be written

---

## The job

Build a **detailed, web-first landing page** at `lucisystems.com/luci-upgrade-guide` that introduces the **New LUCI platform release** to two audiences:

1. **Existing LUCI customers** who need to understand what's new, what changes for them, and how to upgrade
2. **Prospects** evaluating LUCI who need deeper technical detail than a promotional brochure can carry

This page is the **detail destination** the two-pager points to. The two-pager (`new-luci-whats-new-onepager-flow-c.html`) is the shortest complete argument; this landing page is where the detail lives. The format strategy memo (`new-luci-whats-new-format-strategy.md`) already defined this role: *"The customer goes to the New LUCI Upgrade Guide + FAQ at one stable URL."*

**What's new in this brief:** Jane wants the page to be **more promotional than the format strategy originally described** — modeled on the two-pager's design language, not a dry reference doc. It should feel like an extension of the brochure, with layered detail that lets readers go as deep as they need. The format strategy said "customer reference, not a long public marketing release page"; Jane's direction is to make it both: a promotional landing page that also carries the reference detail, in layers.

---

## Design direction

**Modeled on the two-pager.** Same dark masthead, same mint/gold accent hierarchy, same 3-pillar structure, same mint-tinted card treatment. The page should feel like the brochure expanded onto the web — not a separate design language.

**Layered detail (progressive disclosure).** Three layers of depth, so a reader can scan, explore, or deep-dive depending on their role and interest:

| Layer | What you see | Who it's for | Interaction |
|---|---|---|---|
| **1 — Scan** | Pillar names + feature names + 1-sentence descriptions | Everyone (the glance) | Just scroll — no interaction |
| **2 — Explore** | Screenshot + fuller paragraph + benefit checklist | Evaluators (the verify) | Click a feature → sticky detail panel updates |
| **3 — Deep dive** | Specs, integrations, APIs, security/compliance, upgrade mechanics | IT/A/V leads (the technical verify) | Tabbed or accordion section |

**Critical rule** (from the research): Layer 1 must be persuasive on its own. Someone who never clicks anything must still understand what's new and why it matters. The two-pager already proves that works — this page adds the depth beneath it.

---

## Section structure (9 sections)

### 1. Hero *(dark masthead, mesh background — same as two-pager Page 1)*

- **Eyebrow:** "A new version of LUCI is coming"
- **Headline:** "The power of programming is in your hands" (mint accent on "power of programming")
- **Release date:** January 19 (gold) — *date may still be placeholder; confirm with Jane*
- **Two CTAs:** "Book a demo" (prospects) + "Talk to your account team" (existing customers)
- **Visual:** the live map (not a static screenshot — this is the web, it can move)

### 2. The thesis *(light section — expands the two-pager callout)*

- **H2:** "The only A/V that scales and improves just got better"
- A short paragraph explaining what "more capable over time" means — this validates the promise LUCI has been making to customers (Messaging Pillar 4: "Invest in the only A/V that scales and improves — Traditional A/V depreciates and expires. LUCI doesn't. Year Five is more capable than Year One on the same line item.")
- **Optional:** a small timeline visual of past improvements (v1 → 1.5 → 2.0) to make the "improves over time" point concrete. *Jane to decide if this visual is wanted.*

### 3. Three pillars overview *(light section — the scannable grid)*

- The 01/02/03 columns with feature pills, same as Page 1 of the two-pager
- This is **Layer 1** — the glance. Each pill is a **click target** that scrolls to / opens the corresponding feature in the deep-dive section below.
- **Pillar names (locked in the two-pager):**
  - 01: Greater **control** of the room
  - 02: Flexible **control** of your view
  - 03: Deeper **control** over security
  - ("control" in gold, matching the two-pager treatment)

### 4. Feature deep-dive *(the main event — accordion + sticky panel)*

Three sub-sections (one per pillar), each with an accordion of its features. **Left column:** accordion list — click a feature to expand. **Right column (sticky):** updates in sync — screenshot/diagram + 2-3 sentence paragraph + benefit checklist.

This is **Layer 2**. The two-pager's one-sentence descriptions become the accordion headers; the sticky panel adds the depth.

**Pillar 01 — Greater control of the room (3 features):**

| Feature | Two-pager description (accordion header) | Layer 2 source |
|---|---|---|
| **Venue panels** | In-venue tablets show only the approved controls for that space. Operators adjust what they need without full access. | JSON → Operate → Venue panels (6 bullets) |
| **Staging** | Prepare screens, sources, and audio levels behind the scenes. Apply the change on cue, or save it as a preset for next time. | JSON → Operate → Staging (5 bullets) |
| **Audio group control** | Move several audio zones together: apply the same incremental change to keep their balance, or set them all to one volume. | JSON → Technical → Audio group control (moved into Pillar 01 in the two-pager) |

**Pillar 02 — Flexible control of your view (3 features):**

| Feature | Two-pager description (accordion header) | Layer 2 source |
|---|---|---|
| **Customizable interface** | Make LUCI your own with brand colors, light and dark modes, backsplashes, and more. | JSON → Make it yours → Customizable interface (5 bullets) |
| **Live map flexibility** | Upload your own floor plan maps, rotate them to match your view, and see every device's status update live. | JSON → Make it yours → Live map flexibility (4 bullets) |
| **Live screen view** | See what's playing on any TV or LED wall from your iPad, shown exactly as it appears live. | *Not in JSON — Jane added during two-pager tuning. Confirm whether it needs a JSON entry.* |

**Pillar 03 — Deeper control over security (3 features):**

| Feature | Two-pager description (accordion header) | Layer 2 source |
|---|---|---|
| **Audit trails** | Trace each action to a person, preset, or schedule and export the record when needed. | JSON → See and secure → Audit trails (3 bullets) |
| **Live monitoring** | See device, display, and audio status live, including when a device stops responding. | JSON → See and secure → Live monitoring (4 bullets) |
| **Sign-in & session control** | Use email, PIN, or Microsoft for sign-in, end sessions on command, or message everyone in the platform. | JSON → See and secure → Sign-in and session control (4 bullets) |

### 5. In-product support *(its own section — same emphasis as the two-pager spotlight)*

- Full-width mint-tinted card, gold star icon, same treatment as Page 2
- Expanded paragraph + screenshot of the support request flow
- Framed as the cross-cutting feature that applies to all three pillars
- **Two-pager description:** "Raise a request from a device, incident, or error with the relevant context and logs already attached."
- **Layer 2 source:** JSON → Operate → In-product support (2 bullets)
- *Note: In the JSON, In-product support sits under Operate. In the two-pager, it was promoted to a standalone spotlight. Follow the two-pager treatment — it's a cross-cutting feature, not just an Operate item.*

### 6. Technical detail *(Layer 3 — new content, not in two-pager)*

Tabbed or accordion section for the technical evaluator. This is where the "more technical information" lives — the depth that doesn't fit in a promotional brochure.

**Suggested tabs/accordions:**

1. **Integrations** — what LUCI connects to (link to `/integrations` page)
2. **Security & compliance** — audit trails, session control, SSO (Microsoft Entra ID), data handling, private tunnel
3. **API access** — open APIs, documentation links
4. **Infrastructure** — standard network, minimal head-end, what the upgrade touches on property

**Source content:** `new-luci-feature-list.json` → `technical` block (4 items: Audio group control, Add any endpoint, Video wall layout sync, Central display model catalog) + `additional` block (IT-facing detail for pillar features: Venue panels, Staging/presets/schedules, Audit trails/incidents/support, Endpoint management, Identity and sessions, Private tunnel, Scoped diagnostic capture).

*Note: The JSON has rich technical detail that has not been used in any customer-facing asset yet. This section is where it finally surfaces. Read the JSON `technical.additional` block carefully — it has the deeper IT/A/V paragraphs an evaluator will want.*

### 7. Upgrade path *(for existing customers — what the URL promises)*

- "How to get the upgrade" — timeline, what's involved, who to contact
- This is the section that justifies the `/luci-upgrade-guide` URL
- **Content to write:** What changes on your property, how long it takes, whether it's a software update or hardware, who to talk to
- **Source context:** The format strategy memo notes the upgrade guide should cover "readiness, prerequisites, permissions, compatibility, rollout, and upgrade steps." The COS task calendar notes: "merge upgrade guide+IT companion" and "free client upgrades" and "rollout is ordered rather than simultaneous."

### 8. FAQ *(accordions — same `<details>` pattern as `platform.astro`)*

Questions existing customers and prospects will have. Use native `<details>` elements (already shipped on `platform.astro`).

**Suggested questions (content to write):**

- Is this a software update or a hardware upgrade?
- How long does the upgrade take?
- What happens to my current presets and configurations?
- Is there a cost for existing customers?
- Can I see it before it ships?
- What if I just installed LUCI recently?
- How does the rollout work across multiple properties?
- What does my IT team need to prepare?

### 9. Closing CTA + contact *(dark section)*

- Mike's contact info (from the two-pager footer): Michael Epstein, CEO, mepstein@lucisystems.com, 833.333.5868
- Two CTAs: "Book a demo" (prospects) + "Talk to your account team" (existing customers)

---

## Interaction pattern — accordion + sticky panel (Section 4)

The feature deep-dive uses a two-column layout:

- **Left column:** accordion list of features within each pillar. Click a feature to expand. Only one feature open at a time per pillar (or allow multiple — Jane to decide).
- **Right column (sticky):** updates in sync when a feature opens — screenshot/diagram on top, 2-3 sentence paragraph below, benefit checklist beneath that.

**Reference pattern:** [shadcn feature-accordion block](https://www.shadcn-ui-blocks.com/blocks/marketing/feature-sections/feature-accordion) — two-column with stacked accordion on the left and a synchronized sticky detail panel on the right.

**Existing LUCI patterns to build on:**

- `platform.astro` already uses native `<details>` accordions for its FAQ — same accessibility pattern (keyboard, `aria-expanded`)
- FAG customer page has accordion CSS defined (`.fag-acc__btn`, `.fag-acc__panel`) with `aria-expanded` and keyboard support, plus a sticky nav with scroll-spy — though the accordions aren't populated in the current FAG body. This CSS can be adapted.
- The two-pager's mint-tinted card style (`linear-gradient(155deg,#EBF9F4 0%,#F4FCF9 100%)`, `border-left:3px solid var(--accent-light)`, `border-radius:10px`) should carry through to the landing page cards.

**Accessibility:** All progressive disclosure must be keyboard accessible and screen-reader compatible (WCAG 2.2). Hidden content that is inaccessible to assistive technology is a compliance issue, not just a UX preference.

---

## Content inventory — what we have vs. what needs writing

### Already have (from the two-pager + JSON)

- All 10 feature names + 1-sentence descriptions (two-pager HTML)
- The 3 pillar names and structure (two-pager)
- The hero headline, eyebrow, release date (two-pager)
- The thesis callout: "The only A/V that scales and improves just got better" (two-pager)
- In-product support copy (two-pager)
- Contact info: Michael Epstein, CEO, mepstein@lucisystems.com, 833.333.5868 (two-pager)
- Deep feature bullets for all 8 JSON features + 4 technical items + 7 IT-detail blocks (`new-luci-feature-list.json`)
- Messaging Pillar 4 text: "Invest in the only A/V that scales and improves…" (`_project-context.md`)
- The "power of programming" theme and partnership promise ("more control does not mean less LUCI support") (`new-luci-whats-new-pillar-benefit-framing.md`)

### Need to write (new for the landing page)

- Fuller paragraph for each of the 10 features (Layer 2 — 10 paragraphs)
- Screenshots/diagrams for each feature (10 visuals) — *real New LUCI captures only, cropped to the action, anonymized*
- Technical detail section content (Layer 3 — adapt from JSON `technical` block)
- Upgrade path content (timeline, process, what's involved)
- FAQ questions + answers (6-8 entries)
- The "scales and improves over time" thesis paragraph (Section 2)
- Past-improvements timeline visual (if Jane wants it)
- Pillar overview pill click-through behavior (scroll-to-accordion interaction)

---

## Source of truth files

| File | What it contains |
|---|---|
| `ui_kits/internal-portal/new-luci-feature-list.json` | **THE source of truth** for pillars, features, bullets, technical detail. Read this first. |
| `ui_kits/sales/new-luci-whats-new-pillar-benefit-framing.md` | The messaging strategy, pillar framing, "power of programming" theme, partnership promise |
| `ui_kits/sales/new-luci-whats-new-format-strategy.md` | The campaign stack (one-pager + upgrade guide + webinar + email), what detail lives where |
| `ui_kits/sales/new-luci-whats-new-onepager-approach.md` | What stays on the one-pager vs. what moves to the upgrade guide |
| `ui_kits/sales/new-luci-whats-new-onepager-flow-c.html` | The two-pager (final tuned copy for all 10 features, pillar names, hero, design language) |
| `_project-context.md` | The four messaging pillars, including Pillar 4: "Invest in the only A/V that scales and improves" |
| `luci-website/src/pages/platform.astro` | Existing website pattern for product pages + FAQ accordions (`<details>`) |
| `luci-website/src/pages/resources/field-activation-guide/customer.astro` | FAG customer page — accordion + sticky nav pattern (CSS defined, scroll-spy JS) |
| `luci-website/src/data/features.ts` | Existing platform features data (6 features — the current platform, not the new release) |

---

## Design and voice rules

**Follow the LUCI design system rules** (in `.cursor/rules/`):

- `luci-modern-design-guidelines.mdc` — Track A (interactive web) for the page; three-tier fonts (Syncopate display only, Space Grotesk structure, Inter body); mint primary / gold secondary accent hierarchy; `#2b9e80` light accent on light canvases; 8px spacing scale; soft-icon tiles for grouped points
- `luci-visual-design.mdc` — De-boxed: whitespace and hairlines carry structure, not stacked containers; sharp corners (`border-radius:0`) is a brand trait; 4px mint accent bar reserved for true callouts
- `luci-messaging-voice.mdc` — "orchestration engine" not "layer"; "A/V" not "AV"; institutions not adjectives; subtraction over addition; declarative over promotional; no named clients in public materials; no percentage claims
- `luci-mint-primary-gold-secondary.mdc` — Mint is always the primary accent; gold is secondary. Eyebrows/lockup roles/mint rules stay mint. Gold for watermark numbers, secondary labels, duotone icon details, highlight phrases.
- `luci-canonical-assets.mdc` — If any canonical diagrams are used, follow the master→copy propagation rules

**Voice guardrails from the pillar-benefit-framing memo:**

Do not promise: less need for the LUCI team · fewer reasons to call LUCI · self-service as a replacement for support · a property left to operate or troubleshoot alone.

Do promise: more direct control over day-to-day decisions · a shorter path from decision to execution · better context when the team does involve LUCI · continuing support from a team that stays.

**Partnership bridge line (from the memo, near the pillar sequence):**
> More control in your hands, with the LUCI team still there when you need us.

That line is a framing recommendation, not locked final copy. The final wording should preserve both halves: customer agency and continuing LUCI partnership.

---

## Open decisions (Jane still owns)

1. **Release date** — January 19 is in the two-pager but may be placeholder. Confirm before building.
2. **Past-improvements timeline visual** (Section 2) — does Jane want it, or just a paragraph?
3. **Accordion behavior** — one feature open at a time per pillar, or allow multiple?
4. **Live screen view** — this feature is in the two-pager but not in the feature-list JSON. Does it need a JSON entry, or stays page-only?
5. **Technical detail section format** — tabs or accordions? (Tabs are cleaner for 4 categories; accordions are more consistent with the rest of the page.)
6. **Screenshots** — 10 feature visuals needed. Real New LUCI captures only, cropped to the action, anonymized. Who supplies these?
7. **Access model** — is the upgrade guide public, unlisted, or customer-only? (The format strategy flagged this as a decision; Jane hasn't locked it yet.)
8. **Deep-link anchors** — the format strategy says emails should deep-link to relevant sections. Confirm the anchor scheme before building.

---

## TLDR for Cornelius

- Build a promotional landing page at `/luci-upgrade-guide` that expands the two-pager into a detailed web page
- Model the design on the two-pager (dark masthead, mint/gold, 3 pillars, mint-tinted cards)
- Use progressive disclosure: Layer 1 (scan the pillars) → Layer 2 (accordion + sticky panel for feature depth) → Layer 3 (technical detail tabs/accordions)
- 9 sections: hero → thesis → pillars overview → feature deep-dive → in-product support → technical detail → upgrade path → FAQ → CTA
- **Read `new-luci-feature-list.json` first** — it's the source of truth for all feature content
- **Read the two-pager HTML** for the final tuned copy and design language
- Follow LUCI design system rules (Track A, three-tier fonts, mint primary/gold secondary, de-boxed)
- 10 feature screenshots still needed (real captures, anonymized)
- Upgrade path, FAQ, and thesis paragraph content still to be written
- Jane still owns: release date, timeline visual, accordion behavior, access model, screenshot supply

