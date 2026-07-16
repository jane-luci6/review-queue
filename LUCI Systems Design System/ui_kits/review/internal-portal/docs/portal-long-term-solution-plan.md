# Internal Marketing Portal — long-term solution plan

**Status:** Draft for review — 2026-07-13 (rev. 3 — added CTXHUB write-schema/read-contract model; rev. 2 added multi-source line-item ingest, sales-deck environment photos, Scope-of-Work text-dump)
**Owner:** Jane
**Audience:** Jane, Mike (sales authoring), Mark (VPN review), William Morse (shared editor), Cursor agents
**Builds on:** `shared-tiptap-strategy.md`, `client-document-library-plan.md`, `deploy-17.md`, `wiki-agent-key.md`, `skills/agent-readiness-testing.md`, `skills/cover-page-customization.md`

---

## 1. TL;DR

Pivot the Internal Marketing Portal from static HTML + `rsync --delete` to a **FastAPI + Postgres + TipTap** application where templates and client files are stored as **JSONB structured-block trees**, all functionality is exposed through an API, and humans edit via a TipTap block editor. Execute in **six phases over ~7–12 weeks** for one full-stack developer, starting with an **agent-readiness test of the API** before any real building.

The plan covers three document-specific customization flows: (a) **multi-source line-item quotes** (Excel **or** Smartsheet) → budgetary estimate; (b) **prospect-environment photos** → sales-deck slide 2; (c) **Scope of Work from a large text dump** → paginated, on-brand SOW. It also defines a **two-tier storage model**: marketing owns a private JSONB write schema, and on publish converts JSONB → **markdown + envelope** into the shared **CTXHUB pool** — the uniform read contract for agents and other domains.

This plan **extends** `shared-tiptap-strategy.md` (which already agreed TipTap + FastAPI + Postgres + the Pillar C review workflow) and **evolves** `client-document-library-plan.md` (client files move from git-folder HTML to DB-stored JSONB). It retires the static Customization Studio stopgap in favor of **Document Studio** (local authoring) + the **Portal review UI** (.17).

---

## 2. Background — what exists today

- **Static portal on `.17:8081`** — nginx in Docker, built by `scripts/build-stakeholder-review.mjs`, deployed via `scripts/deploy-internal-portal-17.sh` (`rsync -avz --delete`). The build is reference-driven and ships a fixed list of master templates (`budgetary-estimate.html`, `capabilities-document.html`, `sales-deck.html`, `scope-of-work.html`).
- **Customization Studio** — a client-side form that injects field values into a preview iframe via DOM manipulation. **Ephemeral**: the portal reloads the preview on field activity, wiping injections. The cover-page simulation (`skills/cover-page-customization.md`) found concrete gaps: the goals field has no `inject` target, there is no LUCI-voice rewrite step, uploaded logos are not persisted, and the preview shows the **master** template, not the client file.
- **Master templates** — rich HTML sales docs (budgetary, capabilities, sales-deck, scope-of-work) plus the brochure, with `contenteditable` regions, embedded base64 fonts, print CSS, and canonical diagrams.
- **Client files today** — copies of masters saved as `ui_kits/sales/<client>-<doc>.html` (per `.cursor/rules/luci-doc-customization.mdc`); one-off artifacts not in the build ship-list, so they don't reach `.17` unless explicitly added.
- **Agent integration today** — browser-DOM hacking (the simulation). No API.
- **Wiki API available** — FastAPI on `.17:8000`, 4,250 articles, with a read-only agent key already minted for the portal (`docs/wiki-agent-key.md`).
- **Agreed architecture (2026-07-07)** — `shared-tiptap-strategy.md` already decided: shared `@luci/editor` (TipTap/ProseMirror) across Wiki Editor, Document Studio, and the Internal Marketing Portal; FastAPI portal server; Postgres on `.17`; monorepo (`luci-frontend/`); Pillar C workflow (`draft → in_review → approved → merged`); Document Studio runs locally on the editor's laptop, Portal on `.17:8081`; Jane owns Document Studio + Portal.

The portal server ("Phase 2" in `deploy-17.md`) is **not yet built**. This document is the detailed execution plan for it, refined by today's JSONB-block decision and the customization findings.

---

## 3. Goals & non-goals

### Goals
- **Durable, API-driven customization** — cover, goals→LUCI-voice rewrite, logo placement, tier highlight + editable pricing all persist. No more ephemeral DOM injection.
- **Multi-source line-item ingestion** — upload an Excel spreadsheet **or** connect a Smartsheet sheet (via the Smartsheet API) to generate a customized, line-item quote document that fits the budgetary estimate's current format.
- **Prospect-environment photos for the sales deck** — upload photos of the prospect's environment and place them into slide 2 of the sales deck.
- **Scope of Work from a text dump** — paste a large body of text and have it structured and paginated into the SOW document's design across several pages.
- **JSONB block model (write schema)** — templates and client files stored as typed block trees in Postgres, rendered to the existing branded HTML for screen + print/PDF.
- **CTXHUB read contract** — on publish, the marketing JSONB is converted to **markdown + envelope** and written to the shared CTXHUB pool, the uniform read contract for agents and other domains (which never touch the JSONB).
- **TipTap block editor** — Document Studio (authoring) and Portal review UI share `@luci/editor`; custom blocks render as branded, interactive NodeViews (tier chips, price rows, environment galleries, etc.).
- **Print/PDF parity** — a block→branded-HTML renderer + a headless-Chrome PDF API reproduce the current sales-doc output.
- **Agent-ready API** — the production agent calls the API directly (no TipTap, no browser). Shaped by an agent-readiness test before building.
- **Server-backed review queue** — Pillar C proposals for client docs, same state machine as the wiki.
- **Client document library** — list, resume, preview, export, and review saved client work, backed by the DB.
- **Wiki reads** — the Portal proxies the Wiki API (search, article lookup) using the existing agent key.

### Non-goals
- Do not refactor the existing static portal — it runs in parallel until cutover (zero disruption during the build).
- Not a general-purpose CMS.
- Not wiki authoring — the wiki keeps its own stack; the Portal only reads it.
- Not changing the brand design system or visual output — the renderer must **reproduce** the current print design, not redesign it.

---

## 4. Decisions (locked)

| Area | Decision | Source |
|---|---|---|
| Editor | TipTap via shared `@luci/editor` | `shared-tiptap-strategy.md` |
| Backend | FastAPI (Python) — matches Wiki API; reuses existing Python PDF/headless-Chrome scripts | `shared-tiptap-strategy.md` |
| Database | Postgres on `.17`, dedicated `internal_marketing_portal` DB | `shared-tiptap-strategy.md` |
| Doc model | **JSONB structured blocks** for marketing docs; markdown only inside prose fields | This plan (2026-07-13) — refines the markdown-serializer approach for wiki content |
| Storage model | Two-tier: marketing **JSONB write schema** (private) + **CTXHUB pool read contract** (markdown + envelope) | This plan (2026-07-13) |
| Frontend | React + TipTap (TypeScript) for Document Studio + Portal review UI | `shared-tiptap-strategy.md` |
| Hosting | `.17` Docker Compose (app + postgres + nginx), Portal on `:8081`; Document Studio local on Mike's laptop | `shared-tiptap-strategy.md` |
| Review workflow | Pillar C (`draft → in_review → approved → merged`, with `rejected` / `request_changes`) | `shared-tiptap-strategy.md` |
| Naming / ownership | "Internal Marketing Portal" (one name); Jane-owned; wiki reads by Portal only | `shared-tiptap-strategy.md` §Agreed decisions |

**One refinement to call out:** `shared-tiptap-strategy.md`'s code examples store marketing docs as `content` (HTML) + `content_markdown`. This plan replaces that with a **JSONB block tree** as the stored format for marketing docs (HTML/markdown become render targets, not the source of truth). Wiki articles keep their markdown storage — the editor *engine* is shared, the *storage format* differs per doc type. The JSONB stays **private to the marketing domain**; what other domains and agents consume is the CTXHUB pool's markdown + envelope (§5.1).

---

## 5. Target architecture

```
┌──────────────────────────────────────────────────────────────────────┐
│  Mike's laptop (LOCAL) — Document Studio                              │
│  • React + TipTap block editor (via @luci/editor)                     │
│  • Authors client docs from templates; custom blocks as NodeViews     │
│  • Ingests xlsx / Smartsheet → line items; uploads env photos;        │
│    pastes SOW text dumps                                               │
│  • Saves/loads via Portal API; submits proposals for review           │
│  • Does NOT read wiki content                                         │
└───────────────────────────┬──────────────────────────────────────────┘
                            │ HTTPS (Portal API)
                            ▼
┌──────────────────────────────────────────────────────────────────────┐
│  .17 (VM) — Docker Compose                                            │
│                                                                       │
│  nginx :8081 ──► FastAPI Portal API                                   │
│                   ├─ /templates, /client-documents, /customize        │
│                   ├─ /rewrite (LLM: goals → LUCI voice)               │
│                   ├─ /ingest/line-items (xlsx OR Smartsheet → blocks) │
│                   ├─ /ingest/sow-text (text dump → SOW blocks, LLM)   │
│                   ├─ /render (blocks → HTML), /render/pdf (Chrome)    │
│                   ├─ /assets (logos + env photos), /proposals (Pillar)│
│                   ├─ /publish (→ .17 live + CTXHUB pool), /wiki/search│
│                   └─ /auth                                             │
│                                                                       │
│  Postgres: internal_marketing_portal                                  │
│    templates · client_documents(JSONB) · clients · users ·            │
│    line_items · assets · proposals · versions                         │
│    ctxhub_pool (markdown + envelope — read contract)                  │
│                                                                       │
│  Headless-Chrome render service (PDF/print)                           │
│  Wiki API :8000 (existing, read-only via agent key)                   │
└──────────────────────────────────────────────────────────────────────┘
                            ▲
                            │ API (no UI, no browser)
                            ▼
┌──────────────────────────────────────────────────────────────────────┐
│  Production agent (Cursor / other) — calls Portal API directly        │
│  (authors on JSONB; consumes the CTXHUB pool as markdown + envelope)  │
└──────────────────────────────────────────────────────────────────────┘
```

> **Publish also writes the markdown + envelope rendering to the shared CTXHUB pool (the read contract for agents and other domains) — see §5.1.**

**Data model (core tables):** `templates` (block tree + meta), `client_documents` (block tree JSONB + client_id + template_id + status + version), `clients`, `users` (auth + RBAC), `assets` (logos/images, binary or object store), `proposals` (review state + diffs + comments), `versions` (audit history). Line items live inside `priceGroup` blocks in the doc tree, not a separate table. The **CTXHUB pool** (markdown + envelope; see §5.1) is a separate read table — `kb_articles_v2` (shared with the wiki) or a marketing-domain table — written only at publish time.

**Agent path vs human path:** Document Studio is the *human* editor (TipTap). The production *agent* does **not** use TipTap — it sends block-tree patches to the API to author, and reads published docs from the CTXHUB pool (markdown + envelope) to consume. This decoupling is a feature: the agent is never coupled to a UI framework, and consumers never touch the private JSONB.

### API surface (agent-ready)

| Endpoint | Method | Purpose |
|---|---|---|
| `/api/v1/templates` · `/{id}` | GET | List/read master templates |
| `/api/v1/client-documents` | POST/GET | Create from template / list library |
| `/api/v1/client-documents/{id}` | GET/PATCH | Read / update block tree |
| `/api/v1/client-documents/{id}/customize` | POST | Apply field edits (client name, logo, tier selection, env photos, etc.) |
| `/api/v1/rewrite` | POST | Goals text → LUCI-voice overview (LLM) |
| `/api/v1/ingest/line-items` | POST | **xlsx file OR Smartsheet sheet** → `priceGroup` blocks (column mapping; auto-paginate). Replaces `scripts/ingest-budgetary-lineitems.py`; adds a Smartsheet adapter |
| `/api/v1/ingest/sow-text` | POST | Large text dump → SOW block tree (LLM-structured) for the Scope of Work template |
| `/api/v1/assets` · `/{id}` | POST/GET | Upload/serve logos, prospect-environment photos & images |
| `/api/v1/render` · `/render/pdf` | POST | Block tree → HTML / PDF (headless Chrome) |
| `/api/v1/proposals` · `/{id}/{approve,reject,request-changes}` | POST/GET | Pillar C review workflow |
| `/api/v1/publish` | POST | Approved doc → live on `.17` **and convert JSONB → markdown + envelope into the CTXHUB pool** |
| `/api/v1/ctxhub` · `/ctxhub/{id}` | GET | Read published docs from the CTXHUB pool (markdown + envelope) — the agent / other-domain read contract |
| `/api/v1/wiki/search` · `/wiki/articles/{slug}` | GET | Proxy to Wiki API (agent key, server-side) |
| `/api/v1/auth` | POST | Token auth |

### 5.1 Write schema vs read contract (CTXHUB pool)

The marketing domain keeps a **private JSONB write schema**; the rest of the system consumes a **uniform read contract** from the shared CTXHUB pool. The two are separated by a single conversion boundary at publish time:

```
MARKETING DOMAIN (owns its write schema)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  JSONB storage
  - Rich formatting, nested structures, brand kits
  - Design loops: create, iterate, fragment, recombine
  - TipTap renders the JSONB for visual editing
  - This is the domain's private business — CTXHUB doesn't
    care about the JSONB structure
      │
      │ "Publish to pool" (the conversion boundary)
      │ JSONB → markdown + envelope
      │
      ▼
CTXHUB POOL (the read contract)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Markdown + envelope frontmatter
  - 9 required + 2 optional envelope fields (routing/filtering/gating)
  - Markdown body (a rendering of the JSONB, not the JSONB itself)
  - Stored in Postgres (kb_articles_v2 or a domain-specific table)
  - This is what agents and other domains consume
```

**In words:**

- **Marketing domain (owns its write schema).** JSONB storage — rich formatting, nested structures, brand kits. Design loops (create, iterate, fragment, recombine) happen here. TipTap renders the JSONB for visual editing. This is the domain's private business; CTXHUB doesn't care about the JSONB structure.
- **Publish to pool (the conversion boundary).** On publish, the approved JSONB block tree is converted to **markdown + envelope**. The markdown body is *a rendering of the JSONB, not the JSONB itself*.
- **CTXHUB pool (the read contract).** Markdown + envelope frontmatter — 9 required + 2 optional envelope fields for routing/filtering/gating. Stored in Postgres (`kb_articles_v2` or a domain-specific table). This is what agents and other domains consume.

This keeps the JSONB block model private to marketing while giving agents and other domains a stable, uniform read surface. The production agent that *authors* uses the Portal API (JSONB); agents that *consume/reference* read the CTXHUB pool (markdown + envelope). The conversion is one-way at publish — the pool is a read contract, not an edit surface.

---

## 6. The block model (core design)

### Why JSONB blocks, not markdown
These docs are print-designed and layout-rich. Plain markdown cannot express navy `doc-page-band` headers with a gold accent word, soft-icon tile grids, pricing tables with editable cells, highlightable tier chips, circuit textures, base64-embedded fonts, or controlled page breaks. Storing a typed block tree lets the renderer map blocks → the **existing** CSS/components, achieving print parity *by construction* rather than re-deriving layout from prose. Markdown is used **only inside prose fields** (intro/summary, SOW body) and as the **publish rendering** into the CTXHUB pool (§6.1), via `tiptap-markdown`.

### Storage format
A **thin domain JSONB schema** that maps 1:1 to TipTap node types, so the API speaks domain block types (not ProseMirror internals) and the agent contract stays clean. `@luci/editor` serializes TipTap doc ↔ domain block JSON. This JSONB is the marketing domain's **private write schema** — it never leaves the domain; external consumers read the CTXHUB pool instead (§5.1).

**Example — a `cover` block:**
```json
{
  "type": "cover",
  "attrs": {
    "clientName": "Paragon Casino Resort",
    "summaryText": "Paragon Casino Resort is bringing its full property …",
    "logoAssetId": "ast_01H8…",
    "logoMismatchConfirmed": true
  }
}
```

**Example — a `tierGrid` block:**
```json
{
  "type": "tierGrid",
  "attrs": {
    "tiers": [
      { "qty": 50,  "discount": "0%",   "price": "$419.00", "selected": false },
      { "qty": 100, "discount": "5%",   "price": "$399.00", "selected": true  },
      { "qty": 250, "discount": "10%",  "price": "$379.00", "selected": false }
    ]
  }
}
```

### Per-template blocks (sales deck + Scope of Work)

The budgetary estimate is the parity pilot, but the same renderer serves the other sales templates. Two templates need additional block types for their customization features:

**Sales deck — `environmentGallery` (slide 2):** holds prospect-environment photos uploaded via `/assets`.
```json
{
  "type": "environmentGallery",
  "attrs": {
    "slideNo": 2,
    "media": [
      { "assetId": "ast_01H9…", "caption": "Sportsbook floor — existing TV wall" },
      { "assetId": "ast_01HA…", "caption": "Back-of-house rack" }
    ],
    "layout": "two-up"
  }
}
```

**Scope of Work — `sowSection` / `sowBody` / `sowList` / `sowTable` / `sowDeliverable`:** produced by `/ingest/sow-text` from a large text dump (LLM-structured), then paginated by the renderer.
```json
{
  "type": "sowSection",
  "attrs": { "title": "Project Overview", "number": "1.0" },
  "content": [
    { "type": "sowBody", "attrs": { "text": "LUCI will furnish …" } },
    { "type": "sowList", "attrs": { "items": ["Deliverable A", "Deliverable B"] } },
    { "type": "sowDeliverable", "attrs": { "name": "Core hardware", "detail": "…" } }
  ]
}
```

Full per-template taxonomies are in **Appendix A**.

### Renderer + PDF
A server-side renderer walks the block tree and emits the branded HTML (reusing the current `sales-document.css` / per-doc CSS) with print rules. PDF is produced by a headless-Chrome render service (evolved from the existing `scripts/prepare-sales-pdf-assets.py` + `render-pdf.sh`). The renderer handles **pagination** — critical for the SOW text-dump flow, which spans several pages. The renderer and PDF service are the print-parity surface — the highest-risk area, now **Med** because they reuse the same components the current docs use.

### 6.1 Publish conversion (JSONB → markdown + envelope)
At publish time (§5.1), the same renderer that produces branded HTML/PDF also produces a **markdown rendering** of the block tree, paired with an **envelope** (frontmatter with 9 required + 2 optional fields for routing/filtering/gating). This `{ envelope, markdown }` pair is written to the CTXHUB pool — the read contract for agents and other domains. The JSONB remains marketing's private write schema; consumers never see it. The conversion is one-way at publish (the pool is a read contract, not an edit surface), so the JSONB stays the single source of truth and the pool is a derived, consumable projection.

---

## 7. Phased execution plan (in order)

Each phase lists goal, scope, deliverables, exit criteria, effort, risk, and dependencies. **Order is mandatory:** each phase's exit criteria feed the next.

### Phase 0 — Design + agent-readiness test  ·  *BLOCKER*
**Goal:** Lock the block taxonomy, JSONB schema, API contract, and CTXHUB envelope empirically before building.
**Scope:**
- Draft block taxonomy (Appendix A) + JSONB schema for the budgetary estimate, sales deck, and Scope of Work.
- Draft FastAPI OpenAPI sketch (§5 surface), including both ingest paths (xlsx/Smartsheet, SOW text-dump), the env-photo placement flow, **and the CTXHUB envelope (9 required + 2 optional fields) + publish-conversion contract**.
- Run an **agent-readiness test** (`skills/agent-readiness-testing.md`): stand up a stub of the API and have an LLM role-play the production agent against it — cover customization, goals rewrite, **line-item ingest (xlsx + Smartsheet)**, **sales-deck environment photos**, **SOW text-dump structuring**, render, **and the publish → CTXHUB (JSONB → markdown + envelope) conversion**. Discover missing endpoints/fields.
- Close open decisions (§9).
**Deliverables:** `block-taxonomy.md`, OpenAPI sketch (incl. envelope), agent-readiness test report, go/no-go for Phase 1.
**Exit criteria:** An agent can complete the full cover-customize → ingest → env-photos → sow-text → render → publish-to-pool flow against the stub with no undocumented endpoints; block schemas for all three templates and the envelope schema are stable.
**Effort:** 5–7 days · **Risk:** Low · **Dep:** none.
*Why first:* the block schema and envelope are the contracts the renderer, editor, agent API, DB, and CTXHUB pool all depend on. Getting them right while it's cheap de-risks everything else.

### Phase 1 — Foundation  ·  FastAPI + Postgres + auth + CRUD
**Goal:** A running app + DB on `.17` with skeleton CRUD.
**Scope:**
- Docker Compose (FastAPI + Postgres + nginx) on `.17:8081`; the static portal keeps running in parallel.
- Postgres schema + migrations (Alembic) for all core tables, including the CTXHUB pool table.
- Auth + RBAC (Mike/Mark/Jane/agents).
- CRUD for templates, client documents, clients, assets.
- CI (lint, test, migrate).
- Scaffold React app for Document Studio + Portal review UI, talking to the API.
**Deliverables:** Deployable v0 app; auth; CRUD endpoints; empty React shell.
**Exit criteria:** Authenticated CRUD round-trips a client document (create → read → update → list) via the API and the React shell.
**Effort:** 1–2 weeks · **Risk:** Low–Med (ops) · **Dep:** Phase 0.

### Phase 2 — Block model + renderer + PDF API  ·  *the print-parity surface*
**Goal:** Render a JSONB block tree to branded HTML + PDF that matches the current budgetary estimate; prove pagination works for multi-page docs.
**Scope:**
- Implement the renderer (blocks → existing CSS/components → print HTML), including **pagination across pages** (navy page bands, page breaks, headers/footers, page numbers).
- Headless-Chrome PDF render service (port the existing Python PDF prep).
- Convert the **budgetary estimate** master to the block tree (pilot); verify print/PDF parity against the current `LUCI-Budgetary-Estimate.pdf`.
- `/render` + `/render/pdf` endpoints.
**Deliverables:** Renderer, PDF service, budgetary master as blocks, parity report.
**Exit criteria:** Rendered budgetary PDF is visually/electronically indistinguishable from the current budgetary PDF (sign-off by Jane); pagination primitives proven.
**Effort:** 2–3 weeks · **Risk:** Med (print parity) · **Dep:** Phase 1.
*Note:* This is where the design-fidelity risk lives — mitigated by reusing the existing components rather than re-deriving layout. The sales-deck and SOW master conversions happen at the start of Phase 3 (renderer is reusable).

### Phase 3 — Document Studio (TipTap block editor) + customization features
**Goal:** Mike can author/customize client docs across all three templates in a real editor, with all features durable.
**Scope:**
- TipTap block editor (React NodeViews) via `@luci/editor`; per-app chrome (toolbar, "/" insert menu, drag handles).
- Custom NodeViews: `tierGrid` (click to select offered tier, editable discounts), `priceGroup` (editable cells), `deliversGrid`, `cover`, `environmentGallery` (sales deck), SOW blocks.
- Convert the **sales-deck** and **Scope-of-Work** masters to block trees (renderer is reusable from Phase 2; this is mechanical decomposition).
- **Budgetary — multi-source line-item ingestion:** `/ingest/line-items` accepts an uploaded **xlsx** **or** a **Smartsheet** sheet (Smartsheet API adapter + column mapping via header synonyms), producing `priceGroup` blocks with auto-pagination when the stack exceeds a page.
- **Budgetary — cover + tiers:** `/customize`, `/rewrite` (LLM goals→LUCI voice, with the confirm-on-mismatch logo policy enforced server-side), tier highlight + editable pricing, logo upload via `/assets`.
- **Sales deck — prospect-environment photos:** upload photos via `/assets` and place them into the slide-2 `environmentGallery` block (constrained `layout` modes: `single` / `two-up` / `grid`).
- **Scope of Work — text-dump ingestion:** `/ingest/sow-text` takes a large text dump, LLM-structures it into SOW blocks (`sowSection`, `sowBody`, `sowList`, `sowTable`, `sowDeliverable`), and the renderer paginates it into the SOW design across several pages. A human review step in Document Studio catches structuring errors before submit.
- Live preview renders the **actual client file** from the API (not the master).
**Deliverables:** Document Studio app; customization + ingest endpoints; end-to-end flows for budgetary (xlsx/Smartsheet), sales deck (env photos), and SOW (text dump).
**Exit criteria:** Mike can (a) build a budgetary quote from an Excel file **and** from a Smartsheet sheet, (b) upload prospect photos into sales-deck slide 2, and (c) paste an SOW text dump and get a paginated, on-brand SOW — all persisted, no ephemeral injection.
**Effort:** 3–4.5 weeks · **Risk:** Med (NodeView complexity; LLM structuring quality for SOW; Smartsheet column-mapping variability) · **Dep:** Phase 2.
*TipTap impact:* the editor core is handled; remaining work is chrome + NodeViews + serializers + the three ingest adapters.

### Phase 4 — Portal review UI + server-backed review queue + library + wiki reads + publish-to-pool
**Goal:** Reviewers (Jane/Mark) review proposals; the client library is DB-backed; wiki reads work; approved docs publish to the CTXHUB pool.
**Scope:**
- Portal review UI: TipTap in `review` mode (read-only/diff + comments + approve/reject/request-changes).
- `/proposals` Pillar C workflow; server-backed review queue replacing `review-queue.json`.
- Client document library UI (list/resume/preview/export).
- `/wiki/search` + `/wiki/articles` proxy (reuse agent key).
- `/publish` (approved → live on `.17`) **+ publish-to-pool**: convert the approved JSONB block tree → markdown + envelope (9 required + 2 optional fields) and write to the CTXHUB pool (Postgres) — the read contract for agents and other domains (§5.1).
- `/ctxhub` read endpoint for consumers.
**Deliverables:** Review UI; review queue; library; wiki integration; **publish-to-pool converter (JSONB → markdown + envelope)**.
**Exit criteria:** A doc moves draft → in_review → approved → published **to `.17` and to the CTXHUB pool**; reviewer can diff and comment; wiki search returns results; an agent can read the published doc from the pool as markdown + envelope.
**Effort:** ~1.5 weeks · **Risk:** Low–Med (conversion fidelity) · **Dep:** Phase 3.

### Phase 5 — Migration + QA + cut-over + training
**Goal:** Move live, train the team, retire the stopgap.
**Scope:**
- Migrate existing client files (e.g., `paragon-casino-budgetary-estimate.html`) into the DB block model.
- Print-parity QA across budgetary, sales deck, and SOW; accessibility + contrast checks per the design system.
- Train Mike (Document Studio) and Mark (VPN review).
- Cut over `.17:8081` to the app; archive the static portal.
**Deliverables:** Migrated docs; QA report; trained users; live app.
**Exit criteria:** Mike and Mark complete a real end-to-end doc per template without the old tooling; static portal retired.
**Effort:** ~1 week · **Risk:** Med (migration/conversion) · **Dep:** Phase 4.

### Phase 6 — Ongoing / hardening (post-launch)
- Convert remaining templates (capabilities, brochure) to block models.
- Optional real-time collaboration (Yjs + Hocuspocus, self-hosted).
- CI auto-deploy on push; managed Postgres / backups; monitoring.
- Export client docs to git for archival if the "repo as source of truth" preference is retained (see §9).

---

## 8. Effort & risk summary

| Phase | Effort | Risk | Notes |
|---|---|---|---|
| 0. Design + agent-readiness test | 5–7 days | Low | Highest-leverage; de-risks all; covers 3 templates + envelope |
| 1. Foundation | 1–2 weeks | Low–Med | Ops: stateful DB + app on .17 |
| 2. Block model + renderer + PDF | 2–3 weeks | **Med** | Print parity + pagination primitives (mitigated by reusing components) |
| 3. Document Studio + customization (3 templates) | 3–4.5 weeks | Med | NodeViews; LLM SOW structuring; Smartsheet mapping; env-photo layout |
| 4. Review UI + queue + library + wiki + publish-to-pool | ~1.5 weeks | Low–Med | JSONB → markdown conversion fidelity |
| 5. Migration + QA + cut-over | ~1 week | Med | Conversion of existing client files |

**Total: ~7–12 weeks** for one full-stack developer (rough order of magnitude, not a quote). The increase over the budgetary-only baseline (~5–9 weeks) reflects pulling the **sales-deck** and **Scope-of-Work** templates forward (their customization features need them as blocks), the **Smartsheet** and **SOW text-dump** ingest paths, and the **publish-to-pool** converter. The dominant residual risk is print parity in Phase 2, now **Med** (down from High on the markdown path) because the renderer reuses the existing branded components. Reusing the existing design-system CSS/components is the biggest accelerator — the renderer wires, it does not redesign.

**Risk register:** (1) print/PDF parity — Phase 2 sign-off gate; (2) ops burden of a stateful Postgres + app on `.17` — backups, updates; (3) `.17` becomes a real server (LAN exposure is low but it is now stateful); (4) migration/conversion of existing one-off client files; (5) **LLM structuring quality for SOW text-dumps** — large messy text may mis-parse (mitigation: human review step in Document Studio before submit, plus `/rewrite`-style prompt versioning); (6) **Smartsheet column-mapping variability** — each prospect's sheet may name columns differently (mitigation: synonym mapping + a confirm-mapping step, as the existing `ingest-budgetary-lineitems.py` does); (7) **sales-deck slide-2 image layout** — variable photo counts/orientations need fit/crop rules (mitigation: constrained `layout` modes like `two-up`/`single`, with the renderer handling fit); (8) **JSONB → markdown conversion fidelity** — the pool's markdown is a lossy rendering of the branded layout by design (a read contract, not a reprint); mitigation: document the envelope + markdown contract clearly, and keep the JSONB as the single source of truth so the pool is always re-derivable. Mitigation overall: the static portal runs in parallel throughout, so there is zero disruption during the build.

---

## 9. Open decisions (close in Phase 0)

- **Git's role.** `client-document-library-plan.md` held "repo is the source of truth." With a DB, the DB becomes the source of truth for client docs (editable, versioned). Decide: DB-only with optional git **export** for archival, or keep templates (masters) in git + DB and client docs DB-only. Recommendation: DB source of truth + git export for archival/audit.
- **Render service language.** FastAPI confirmed for the app. The existing PDF prep scripts are Python — keep a Python headless-Chrome sidecar (Playwright/Pyppeteer) vs port to a Node sidecar. Recommendation: keep Python (reuse existing scripts).
- **Auth method.** Local accounts, SSO, or shared with the wiki. Recommendation: start with local accounts + API tokens for agents; SSO later.
- **Collaboration timing.** Yjs real-time co-editing day-1 or deferred. Recommendation: defer to Phase 6.
- **Logo/asset storage.** Postgres `bytea`, filesystem on `.17`, or object storage. Recommendation: filesystem + metadata in `assets` (simplest for serving via nginx).
- **Hosting.** `.17` (stateful) vs a dedicated host / managed Postgres. Recommendation: `.17` for now; revisit if backups/uptime become a burden.
- **Logo-mismatch policy enforcement.** The confirm-on-mismatch rule (`skills/cover-page-customization.md`) becomes a server behavior: `/customize` or `/rewrite` flags a logo/company mismatch and requires `logoMismatchConfirmed: true` to place (see the `cover` block example in §6).
- **Smartsheet credentials & column maps.** Per-user API token stored server-side (encrypted) vs a shared workspace token; how column maps are saved/reused across prospects. Recommendation: server-stored per-workspace token + reusable saved column maps.
- **LLM provider/model** for `/rewrite` (goals→LUCI voice) and `/ingest/sow-text` (text-dump structuring) — model choice, credentials, prompt versioning, and a human review gate before paginating/submitting SOW.
- **Sales-deck slide-2 image rules.** How many photos, aspect-ratio/crop policy, fallback layout when fewer photos. Recommendation: 1–4 photos, `single`/`two-up`/`grid` layouts, renderer fits/crops to the slide-2 frame.
- **CTXHUB envelope schema.** Define the 9 required + 2 optional envelope fields (routing/filtering/gating); align with the wiki's existing envelope if it has one, so marketing and wiki publish into the same pool shape.
- **CTXHUB pool table.** Share `kb_articles_v2` with the wiki vs a marketing-domain table (`ctxhub_marketing`). Recommendation: shared `kb_articles_v2` (one pool, domain-tagged) unless the wiki's schema can't accommodate marketing's envelope — then a sibling table with the same envelope contract.
- **Conversion ownership.** Marketing owns the JSONB → markdown + envelope converter (it's the only domain that understands the block model); the envelope *schema* is cross-domain. Decide where the converter runs (Portal API at publish time). Recommendation: converter runs in the Portal API at `/publish`.

---

## 10. Gains vs risks

**Gained:** durable customization (no ephemeral injection); the preview shows the actual client file; multi-source line-item quotes (Excel + Smartsheet); prospect-environment photos in the sales deck; SOW-from-a-text-dump; an agent-ready API (production agent stops browser-hacking); server-backed review with version history; a DB-backed client library; wiki reads in-portal; retirement of the `rsync --delete` footgun; multi-user + RBAC; **a uniform CTXHUB read contract (markdown + envelope) so agents and other domains consume marketing docs without touching the private JSONB**.

**Risked:** print/design fidelity during the renderer rebuild (Phase 2 gate); new ops burden (stateful DB + app, backups); `.17` becomes a real stateful server; one-time migration of existing client files; LLM-structuring quality for SOW dumps; JSONB→markdown conversion fidelity for the pool (lossy by design). All mitigated by parallel-running the static portal during the build and keeping the JSONB as the single source of truth.

---

## 11. Relationship to existing plans

- **`shared-tiptap-strategy.md`** — this plan is the detailed build-out of its "Internal Marketing Portal server (Phase 2)". Refines one point: marketing docs store a JSONB block tree (not raw HTML/markdown); the `@luci/editor` engine is still shared with the wiki, which keeps markdown storage. The JSONB is marketing's private write schema; the CTXHUB pool is the cross-domain read contract (§5.1).
- **`client-document-library-plan.md`** — evolved: client files move from git-folder HTML to DB-stored JSONB, edited via Document Studio and reviewed via the Portal. Git remains available as an export/archive format (open decision §9). The library UI + Mike/Mark/Jane flows described there are realized in Phases 3–5.
- **`deploy-17.md`** — the current static deploy pipeline stays for the static portal during the build; the app introduces a Docker-Compose deploy target alongside it, eventually replacing it at cut-over (Phase 5).
- **`skills/agent-readiness-testing.md`** — the Phase-0 method.
- **`skills/cover-page-customization.md`** — the cover-feature spec (inputs, placement areas, rewrite contract, logo-mismatch policy) is realized durably by `/customize` + `/rewrite` in Phase 3.
- **`scripts/ingest-budgetary-lineitems.py`** — becomes `/api/v1/ingest/line-items` in Phase 3 (xlsx path); the Smartsheet adapter is a new sibling source.
- **CTXHUB pool** — the shared read contract the wiki already publishes into (`kb_articles_v2`); marketing joins it at publish time (§5.1), converting JSONB → markdown + envelope. This is the cross-domain seam: marketing's private JSONB write schema stays private; the pool is what agents and other domains read.

---

## 12. Immediate next step

Begin **Phase 0**:
1. Draft the block taxonomy + JSONB schema for **all three templates** (budgetary, sales deck, Scope of Work) — `block-taxonomy.md`.
2. Draft the FastAPI OpenAPI sketch (§5 surface), including both ingest paths, the env-photo placement flow, **and the CTXHUB envelope (9 required + 2 optional fields) + publish-conversion contract**.
3. Run the agent-readiness test against a stub per `skills/agent-readiness-testing.md`, covering cover-customize → rewrite → **ingest (xlsx + Smartsheet)** → **sales-deck environment photos** → **SOW text-dump** → render → **publish-to-pool (JSONB → markdown + envelope)**.
4. Close the §9 open decisions; produce a go/no-go for Phase 1.

On approval, I can produce the Phase-0 artifacts (block taxonomy doc, OpenAPI sketch with envelope, and the agent-readiness test plan) next.

---

## Appendix A — Block taxonomy

### Budgetary estimate (parity pilot)

| Block type | Existing component / CSS | Editable fields | Notes |
|---|---|---|---|
| `cover` | `.doc-page--cover` / `.doc-cover` | `clientName`, `summaryText` (prose), `logoAssetId`, `logoMismatchConfirmed` | One per doc; display headline + summary + logo |
| `pageBand` | `.doc-page-band` | `kicker`, `title`, `accentWord` (gold), `deck`, `pageNo` | Navy header per interior page |
| `intro` | `.be-intro` | `preparedFor` (prose), `body` (markdown) | Page-2 prepared-for text |
| `whatLuciIs` | identity diagram + feature cards (brochure p2 scaled) | `diagramAssetId`, `features[] {icon, head, body}` | Scaled "What LUCI is" |
| `scopeList` | `.be-scope` | `groups[] {label, endpoints[] {name, qty}}`, `bridgeLine` (prose), `tally {}` | Customer-facing bridge line |
| `priceGroup` | `.be-price-group` / `.be-price-row` | `groupName`, `rows[] {mfg, item, desc, qty, unitPrice, subtotal}`, `groupSubtotal` | Populated via `/ingest/line-items` (xlsx or Smartsheet) |
| `investmentSummary` | totals block | `capex`, `opex`, `total`, breakdown | Computed from price groups |
| `deliversGrid` | `.be-delivers` (soft-icon 2×3) | `items[] {icon, verb, text}` | Verb-led outcomes |
| `tierGrid` | `.be-tier-grid` / `.be-tier-chip` | `tiers[] {qty, discount, price, selected}` | `selected` = offered tier highlight |
| `close` | contact panel | `contactName` (Michael Epstein), `role`, `email`, `nextSteps[]` | Anchored to page bottom |

### Sales deck (slide-2 environment-photo feature)

| Block type | Existing component / CSS | Editable fields | Notes |
|---|---|---|---|
| `deckCover` | sales-deck cover slide | `clientName`, `logoAssetId`, `subtitle` | Slide 1 |
| `environmentGallery` | slide-2 image region | `media[] {assetId, caption}`, `layout` (`single`/`two-up`/`grid`) | Prospect-environment photos via `/assets` |
| `deckNarrative` | slide body / bullet block | `heading`, `points[]`, `body` (markdown) | Standard slide content |
| `deckClosing` | closing slide | `contactName`, `cta`, `logoAssetId` | Last slide |

### Scope of Work (text-dump feature)

| Block type | Existing component / CSS | Editable fields | Notes |
|---|---|---|---|
| `sowCover` | SOW cover | `clientName`, `projectName`, `date`, `logoAssetId` | Page 1 |
| `sowSection` | `.doc-page-band` + section body | `title`, `number`, `content[]` | Renderer paginates across pages |
| `sowBody` | SOW body paragraph | `text` (markdown) | Prose |
| `sowList` | SOW bulleted/numbered list | `items[]`, `ordered` | |
| `sowTable` | SOW table | `headers[]`, `rows[][]` | e.g. deliverables, schedule |
| `sowDeliverable` | deliverable callout | `name`, `detail`, `owner?`, `due?` | |
| `sowFooter` | SOW page footer | `pageNo`, `clientName` | Auto per page |

## Appendix B — Current-state references

- `scripts/build-stakeholder-review.mjs` — reference-driven asset copy; fixed master ship-list (`syncStudioPreviews`).
- `scripts/deploy-internal-portal-17.sh` — `rsync -avz --delete` to `.17` (the footgun this plan retires).
- `.cursor/rules/luci-doc-customization.mdc` — current client-file save path (`ui_kits/sales/<client>-<doc>.html`).
- `ui_kits/review/review-queue.json` — current static review queue (→ server-backed in Phase 4).
- `skills/cover-page-customization.md` — cover feature spec + gaps (→ `/customize` + `/rewrite` in Phase 3).
- `scripts/ingest-budgetary-lineitems.py` — Excel line-item ingestion (→ `/api/v1/ingest/line-items` xlsx path in Phase 3; Smartsheet adapter is new).
- `docs/shared-tiptap-strategy.md`, `docs/wiki-agent-key.md`, `docs/deploy-17.md` — prior architecture, wiki key, deploy pipeline.
