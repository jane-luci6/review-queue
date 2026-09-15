# Canon — channel playbooks

**Snapshot:** 28 August 2026  
Apply voice + visual canon first. This file is **where** work lives and what “good” means per channel.

---

## Website (luci-website)

- IA: Home · Platform · Who We Serve · Industries · Resources · About · Contact. Persistent CTA: Request a conversation / See LUCI in action.
- Hero should **show the platform** (UI, map, in-action), not copy alone.
- Platform + partnership in tandem.
- No popups / generic sales chat at launch. AskLuci is curated/mock until Phase B.
- `llms.txt` + schema for AISEO.
- Circuit pattern: webpage rule only (`luci-website-pattern-standard.mdc`).
- Case studies under `/resources/case-studies/`. Index order at snapshot: Yaamava → Ameristar → Tachi → Sam’s Town.
- Industries live: casinos-gaming, hotels-resorts, sports-venues, airports-transportation, conference-convention-centers. Casino is the template vertical.
- Six personas: operations, marketing, finance, technology, facilities, leadership.
- Fall launch. Review: `http://10.10.1.37`.
- Working git branch: `persona-hero-subhead-gold`.

**In flight:** messaging/feature audit; Tachi bingo image; Sam’s Town section variants preview; e-mesh footer; parked ticker names.

---

## Sales documents

PDF-first, Track C, US Letter. Brochure = 5-page overview. Capabilities = personalized deep-dive (locked story pages vs editable cover/close). FAG = prospect vs customer versions.

Never full-bleed dark mid-doc for emphasis. Proof = impact, not persona icon rows that duplicate the brochure. Two outcome stats max on the proof page, sourced.

Client copies: `ui_kits/sales/<client>-<doc>.html` — never the VM folder.

**In flight:** Yaamava layout pick on capabilities/retrofit.

---

## Case studies

Web-first. PDF later. Spine in `luci-case-studies.mdc`. Visual = Sam’s Town. Copy spine target = Tachi.

Public discretion still applies **outside** the approved named study.

**In flight:** Sam’s Town review v2; Yaamava featured; Tachi photo; no New LUCI launch case study.

---

## The Signal (newsletter)

Flagship Issue 01 for editorial rhythm. Issues 02–04 exist in `ui_kits/newsletter/`. Webflow head/body splits for live site. Hub on website `/the-signal/`.

Cadence: start ~day 1, send day 15.

New LUCI in Signal = **beta framing only**, never “we launched.”

**Traffic checklist (Grok observes; Cursor fixes):**

- 5–6 articles
- A theme that actually connects them
- Welcome/intro is a welcome, not a second feature
- Length fits the slot (field story longer; panels shorter)
- Visuals where the channel usually has them
- Jane picks ideas before GPT writes the issue
- Jane approves the packet, then Webflow, then AC from the last teaser/issue template
- Queue the list; do not Send unless Jane says so

**Cursor routing:** GLM adapts a case study into the template and lays out locked copy. GPT proposes the rest + features, then writes after Jane picks. Photos from real project media, not invented.

**Publish to Webflow:** see `shared/SIGNAL-WEBFLOW-PUBLISH-PLAYBOOK.md`. Webflow publishing is a Cursor task — Cursor hosts media, wires URLs, pushes custom code via the Webflow API, and verifies the live page. Bots hand the publish to Cursor with a brief; they do not paste HTML into the Designer or call the Webflow API themselves.

---

## LinkedIn / social

Company page only (Phase 1). 2–3 posts/week. Tue series / Wed proof or diagram / Thu thought or news (conditional).

Season 1 video series: **Control the Whole Property**. Jane generates video in Claude; agent assembles. All series visuals AI-generated — no client B-roll, no stock.

News: commentary, not reshare. No competitor promo. Partner news only if already public.

Strategy summary HTML is the **approved** external-alignment doc. Full `social-media-strategy.html` is internal/superseded for Mike alignment.

**Waiting:** Mike copy pass. Jane can still produce in production mode.

---

## Customer journey email

Templates `ui_kits/email/email-1a` through `email-10`. Calendar in COS JSON. Do not use journey copy in live Mark/Mike deal threads.

**Near-term:** Clearwater go-live 28 Aug 2026.

---

## New LUCI launch (three streams)

Canonical plan: `ui_kits/content-marketing/campaigns/luci-campaign-plan.md`

1. **Existing customers** — What’s New one-pager → upgrade FAQ → IT companion → announcement email → LinkedIn + screenshots → talking points → Signal follow-up as beta. Order waits on Mike’s list + Jane’s bucket confirm.
2. **Demand gen** — website (fall) + LinkedIn after copy pass. Launch is **not** the public splash.
3. **Warm leads** — two short ActiveCampaign tracks (quiet 10 days / 30 days, four emails). Suppress live deals. Not built until Jane says go.

---

## Webflow vs Astro

- **New marketing site:** Astro. Do not rebuild it in Webflow.
- **Still Webflow:** some live Signal/FAG/case-study embeds and landing-page handoff files under `ui_kits/`. `.tmp-webflow/` is scratch — ignore.

---

## Field Activation Guide

Prospect + customer HTML; live on lucisystems.com; website routes + PDF in `public/resources/`. Persona pages borrow FAG copy. “Pick your team” lead-in is **FAG-specific** — do not promote to a global subhead pattern (rule-scope lesson).
