# Prompt for Cornelius — New LUCI Upgrade Landing Page

**Model: Use GLM for this task only.** Select GLM before starting. Do not switch models mid-task.

---

You're building the **New LUCI Upgrade Landing Page** — a detailed, web-first page at `lucisystems.com/luci-upgrade-guide` that expands the New LUCI two-pager promotional brochure into a full landing page with layered detail.

**Start here:** Read `CURSOR-BRIEF-new-luci-upgrade-landing-page.md` in the `luci-design` repo root. It has the full blueprint: section structure, interaction pattern, content inventory, source-of-truth file map, design/voice rules, and locked decisions. This prompt is just a pointer — the brief is the spec.

**The job in one sentence:** Take the two-pager's design language and 3-pillar structure, expand it into a 9-section web page with progressive disclosure (scan → explore → deep-dive), and build it as an Astro page in the `luci-website` repo at `src/pages/luci-upgrade-guide.astro`.

**Read these files first (in this order):**

1. `CURSOR-BRIEF-new-luci-upgrade-landing-page.md` (luci-design root) — the blueprint you're building from
2. `LUCI Systems Design System/ui_kits/internal-portal/new-luci-feature-list.json` (luci-design) — **the source of truth** for all pillars, features, bullets, and technical detail. Read this before writing any feature copy.
3. `LUCI Systems Design System/ui_kits/sales/new-luci-whats-new-onepager-flow-c.html` (luci-design) — the two-pager. Final tuned copy for all 10 features, pillar names, hero, design language. Model the page's visual style on this.
4. `LUCI Systems Design System/ui_kits/sales/new-luci-whats-new-pillar-benefit-framing.md` (luci-design) — the "power of programming" theme, partnership promise, and voice guardrails
5. `luci-website/src/pages/platform.astro` — the existing product page pattern. Reuse `PlatformChapterNav` (sticky section nav with scroll-spy), `SectionBlock` (the section lockup component), and the `<details>` FAQ accordion pattern.
6. `luci-website/src/pages/resources/field-activation-guide/customer.astro` + `luci-website/src/assets/fag-customer/fag-customer.css` — the FAG accordion CSS (`.fag-acc__btn`, `.fag-acc__panel` with `aria-expanded`) and sticky nav scroll-spy JS. Adapt these for the feature deep-dive accordions.

**Locked decisions (from Jane):**

- **Release date:** January 19 as placeholder. It will likely change — build it as a single variable so it's a one-line update later.
- **Screenshots and videos:** Leave placeholders. Build fixed aspect-ratio containers with placeholder states (a muted LUCI-tinted background + a small "screenshot placeholder" label) so swapping in real captures later is trivial. Jane supplies the real assets at a later date.
- **Accordion behavior:** Multi-open (a reader can open multiple features at once within a pillar).
- **Page navigation:** Sticky section nav (like `platform.astro`'s `PlatformChapterNav`) + back-to-top button. This handles the long-page concern — a reader is always one click from any section or the top. Add an optional "Expand all / Collapse all" toggle per pillar.
- **Design:** Model on the two-pager — dark masthead with mesh background, mint/gold accent hierarchy, 3-pillar structure, mint-tinted cards (`linear-gradient(155deg,#EBF9F4 0%,#F4FCF9 100%)`, `border-left:3px solid var(--accent-light)`, `border-radius:10px`).

**Follow the LUCI design system rules** (in `luci-design/.cursor/rules/`):

- `luci-modern-design-guidelines.mdc` — Track A (interactive web); three-tier fonts (Syncopate display ≤3 words, Space Grotesk structure, Inter body — copy text is never Space Grotesk); mint primary / gold secondary; `#2b9e80` light accent on light canvases; 8px spacing scale; soft-icon tiles for grouped points; one display moment per page.
- `luci-visual-design.mdc` — De-boxed: whitespace and hairlines carry structure; sharp corners are a brand trait; 4px mint accent bar for true callouts only.
- `luci-messaging-voice.mdc` — "orchestration engine" not "layer"; "A/V" not "AV"; institutions not adjectives; subtraction over addition; declarative over promotional; no named clients; no percentage claims.
- `luci-mint-primary-gold-secondary.mdc` — Mint primary accent; gold secondary. Eyebrows/lockup rules stay mint. Gold for watermark numbers, secondary labels, duotone icon details, highlight phrases.

**Voice guardrails (from the pillar-benefit-framing memo):**

Do not promise: less need for the LUCI team · fewer reasons to call LUCI · self-service as replacement for support · a property left to operate alone.

Do promise: more direct control over day-to-day decisions · a shorter path from decision to execution · better context when the team involves LUCI · continuing support from a team that stays.

**What still needs writing (you draft, Jane reviews):**

- Fuller paragraph for each of the 10 features (Layer 2) — pull from `new-luci-feature-list.json` bullets
- Technical detail section content (Layer 3) — adapt from the JSON `technical` and `technical.additional` blocks
- Upgrade path content (timeline, process, what's involved)
- FAQ questions + answers (6-8 entries)
- The "scales and improves over time" thesis paragraph (Section 2)

**Still open (flag these to Jane, don't block on them):**

- Whether to include a past-improvements timeline visual in Section 2 (leaning skip unless Jane asks)
- Whether "Live screen view" needs a JSON entry (it's in the two-pager but not in the feature-list JSON)
- Technical detail section format: tabs vs. accordions (propose one)
- Access model: public vs. unlisted vs. customer-only

**Build location:** `luci-website/src/pages/luci-upgrade-guide.astro` (new page). Data file at `luci-website/src/data/upgradeGuide.ts` if you want to separate content from layout (recommended — matches the case-study pattern). Reuse `BaseLayout`, `SectionBlock`, `PlatformChapterNav` from the existing site.

**Deploy:** When ready, run `./deploy.sh` from the `luci-website` repo root. It builds and rsyncs to `http://10.10.1.37`. Tell Jane to hard-refresh (Cmd+Shift+R). Commit your work in small logical chunks as you go.
