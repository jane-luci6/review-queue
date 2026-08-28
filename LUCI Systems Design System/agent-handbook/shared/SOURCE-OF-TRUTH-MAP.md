# Source of truth map

**Snapshot:** 28 August 2026  
**When sources disagree, use this order.** Do not “blend” a stale file with a current rule.

## Precedence (highest wins)

1. **Jane, this week** — spoken lock, or COS board / this handbook’s work board if newer.
2. **Always-on Cursor rules** in `luci-design/.cursor/rules/` — especially messaging voice, modern design guidelines, mint/gold, case studies, phrasebook, rule-scope gate.
3. **Messaging Guide / Philosophy / Personas** — OneDrive Word is canonical; HTML in `ui_kits/review/messaging/` is the synced working copy (last sync noted **27 Aug 2026**).
4. **Stakeholder queue** `ui_kits/review/review-queue.json` — what Mike/Nick have approved vs due.
5. **COS-task-calendar.json** — operating board.
6. **Channel rules** — `luci-case-studies.mdc`, `luci-sales-document-system.mdc`, `luci-social-media.mdc`, `luci-website-pattern-standard.mdc`, portal `SKILL.md` files.
7. **This handbook** — snapshot of the above. If a rule file is newer than the handbook snapshot date, **the rule file wins**. Update the handbook.

## Repos and machines

| What | Where | Notes |
|---|---|---|
| Design system, sales, portal, Signal, campaigns, rules | `~/Documents/Cursor Projects/luci-design` | Local `main` far ahead of GitHub |
| Public site rebuild | `~/Documents/Cursor Projects/luci-website` | Work on `persona-hero-subhead-gold`, not GitHub `main` |
| Website review VM | `http://10.10.1.37` | `./deploy.sh` — Jane’s deliverable, not localhost:4321 |
| Internal Marketing Portal | `http://10.10.1.17:8081` | `npm run deploy:portal` |
| Old hub | `http://10.10.1.37:8080` | **Stale.** Parked cleanup. |
| Messaging Word | OneDrive `Marketing - Documents/Strategy & Messaging/` | Paths in `messaging-sources.json` |
| Client photography reference | OneDrive `Marketing - Documents/Content/Project Media` | Environments only; never publish those files as site images |
| Grok shared files | `/workspace/LUCI-Agent-Handbook` | Copy of this pack. Not the master. |

**GitHub is not the day-to-day source of truth.** A Bot that clones `jane-luci6/luci-website` or `review-queue` will miss most of 2026.

## Design / visual canon (read these, don’t invent)

| File | Role |
|---|---|
| `.cursor/rules/luci-modern-design-guidelines.mdc` | **New assets** — tracks A/B/C, spacing, three-tier type, contrast |
| `.cursor/rules/luci-visual-design.mdc` | De-boxed, sharp corners, Inter body |
| `.cursor/rules/luci-dual-accent-system.mdc` | Mint vs gold, light vs dark |
| `.cursor/rules/luci-mint-primary-gold-secondary.mdc` | Mint primary, gold secondary |
| `.cursor/rules/luci-canonical-assets.mdc` | Diagram masters never resized |
| `.cursor/rules/luci-image-prompt-rules.mdc` | Custom photography, not AI stock |
| `.cursor/rules/luci-website-pattern-standard.mdc` | Circuit pattern on webpages only |
| `assets/fonts/luci-brand-fonts.css` | Embedded Syncopate / Space Grotesk / Inter |
| `assets/diagrams/*.svg` | Canonical diagram masters |

Handbook snapshot: [`../canon/brand-visual-system.md`](../canon/brand-visual-system.md)

## Voice / copy canon

| File | Role |
|---|---|
| `.cursor/rules/luci-messaging-voice.mdc` | Always-on voice contract |
| `ui_kits/review/messaging/messaging-guide.html` | Full guide (synced) |
| `ui_kits/review/messaging/philosophy.html` | Philosophy |
| `ui_kits/review/messaging/personas.html` | Personas |
| `ui_kits/internal-portal/customization/_brand/SKILL.md` | Portal-shipped voice + doc workflow |

Handbook snapshot: [`../canon/messaging-voice.md`](../canon/messaging-voice.md)

## Production / workflow canon

| File | Role |
|---|---|
| `luci-website-review-deploy.mdc` | Website → `.37` |
| `luci-internal-portal-deploy.mdc` | Portal → `.17` |
| `luci-propagation-workflow.mdc` | “Propagate” diagrams |
| `luci-visual-options-workflow.mdc` | 2–3 variants on branches |
| `luci-commit-cadence.mdc` | Small commits (Cursor agents; Grok does not commit from Grok) |
| `luci-doc-customization.mdc` | Portal URL → Cursor customize |
| `luci-stakeholder-review.mdc` | Mike/Nick queue |
| `luci-phrasebook.mdc` | Jane’s plain English |
| `luci-parked-followups.mdc` | Parked items that survive sessions |
| `luci-rule-scope-gate.mdc` | Ask before house-wide rules |

Handbook snapshot: [`../canon/asset-and-production-workflows.md`](../canon/asset-and-production-workflows.md)

## Channel playbooks

See [`../canon/channel-playbooks.md`](../canon/channel-playbooks.md) and:

- Case studies: `luci-case-studies.mdc` + `ui_kits/case-studies/sams-town.html` (visual template) + `tachi-palace.html` (copy spine)
- Sales docs: `luci-sales-document-system.mdc` + `ui_kits/sales/`
- Social: `luci-social-media.mdc` + `ui_kits/content-marketing/social-production.html`
- Campaigns: `ui_kits/content-marketing/campaigns/luci-campaign-plan.md`
- Website IA (historical structure): `ui_kits/website/website-ia-wireframe.html` — live site is `luci-website`

## Do not use as current instruction

| Source | Why |
|---|---|
| `LUCI Systems Design System/README.md` (Figma-era) | ALL CAPS headers, Space Grotesk as body, old stats — conflicts with Inter + modern guidelines |
| `_project-context.md` | 16 Jun 2026. Value prop still says “orchestrates every layer” (retired). IA history only. |
| `CURSOR-MORNING-BRIEF.md` | 8 Jul — useful portal workflow history, not the board |
| `WIP-notes.md` | June dates |
| `luci-website/README.md` “next phases” | Stale vs branch |
| Root `luci-campaign-plan.md` | Shorter duplicate; prefer `content-marketing/campaigns/luci-campaign-plan.md` |
| `ui_kits/website/LUCI_Messaging_Framework_V6-reference.html` | Pre-brand V6 |
| `colors_and_type.css` `--font-body: Space Grotesk` | Conflicts with Inter body |
| `ui_kits/review/internal-portal/` | **Built mirror** — edit `ui_kits/internal-portal/` then build |
| `.tmp-webflow/` | Scratch |
| Case study `assets/sams-town/_*.jpg` | Debug crops |
| `#176B54`, Jackpot Red as accent, “orchestration layer,” “AV,” “absurdly simple,” dark gold text on light | Retired |
| Seamless circuit texture tiles | Retired; webpages use one mint/gold tile, cover, no-repeat |
| Hub `index.html` PRIORITY_QUEUE | Can lag COS calendar |

## Generated output

Never hand-edit `ui_kits/review/` mirrors as if they were sources. Rebuild with `npm run build:review` after editing sources.
