# Shared TipTap Editor Strategy

**For:** Developers building applications that need rich-text editing
**Status:** Proposed — 2026-07-07 (Will v2 + agreed decisions)
**Authors:** William Morse (wiki), Jane (marketing)

> **If you're reading this in Cursor:** this document is written so that
> both human developers AND AI agents can understand the architecture and
> take action. The "Current state" section tells you what exists today
> and what to do right now. The rest describes the target architecture.

---

## Agreed decisions (2026-07-07)

Will's v2 names Jane as owner; the items below are additional decisions from the
marketing side that override naming/boundaries in Will's base doc.

1. **One name:** The server application on `.17` is the **Internal Marketing Portal** — the same product as the portal being built in this repo (not a separate "Marketing Portal").
2. **Wiki API reads:** **Document Studio does not** read wiki content. The **Internal Marketing Portal** does (search, article lookup, references).
3. **Ownership:** Jane owns Document Studio + Internal Marketing Portal (API, review UI, deployment on `.17`). Confirmed in Will v2 contact section.

---

## Current state (read this first)

### What exists today

- **Wiki TipTap editor** — deployed at `http://10.10.1.17:8080`, built from
  the `tiptap-poc/` directory. Standalone SPA wrapping TipTap for wiki
  article editing. Uses Next.js + TypeScript + Tailwind.
- **Wiki API** — FastAPI at `http://10.10.1.17:8000`, serving 4,250 articles
  with a full proposal/review workflow (Pillar C).
- **Wiki Browse UI** — Flask at `http://10.10.1.17:5001`.
- **Document Studio** — being iterated on by Jane. Runs **locally on the
  editor's laptop** (not on .17). Not yet deployed.
- **Internal Marketing Portal** — **production** on `.17:8081` (see `docs/deploy-17.md`).
  Server-side API + review UI not built yet.
  Will follow the same proposal/review workflow as the wiki.

### What does NOT exist yet

- **The shared `@luci/editor` package** — proposed extraction from
  `tiptap-poc/`. Needs to be created before all three apps share the
  editor core.
- **The Internal Marketing Portal server** — API, database, and TipTap
  review UI on `.17` that receives document submissions from Document
  Studio and manages the human review/approval workflow.

### What to do RIGHT NOW

**Start with a standalone TipTap project.** The shared `@luci/editor`
package doesn't exist yet. Structure your code so the eventual refactor
is a one-file swap:

```typescript
// document-studio/src/editor.ts
// Put ALL your TipTap setup in ONE file so it's easy to swap later.

import { Editor } from '@tiptap/core';
import StarterKit from '@tiptap/starter-kit';
import Image from '@tiptap/extension-image';
import Link from '@tiptap/extension-link';

export function createEditor(element: HTMLElement, config: {
  onSave: (html: string, markdown: string) => Promise<void>;
  onLoad: () => Promise<{ html: string; markdown: string }>;
}) {
  return new Editor({
    element,
    extensions: [StarterKit, Image, Link],
    content: '',
  });
}
```

When the shared package is ready, swap this file for:
```typescript
import { createLuciEditor } from '@luci/editor';
```

### NPM packages you'll need

```bash
npm install @tiptap/core @tiptap/starter-kit @tiptap/extension-link \
  @tiptap/extension-image @tiptap/extension-table @tiptap/extension-placeholder
```

Check [tiptap.dev](https://tiptap.dev) for the latest versions.

### Where to find the existing TipTap code

The wiki's TipTap editor is in the `tiptap-poc/` directory. Look at:
- `tiptap-poc/src/` — the editor component setup
- `tiptap-poc/package.json` — which TipTap packages and versions are used
- `tiptap-poc/Dockerfile` — how the editor is containerized

This is the code that will be extracted into the shared `@luci/editor`
package.

---

## The problem

Three applications need TipTap, each in a different deployment context:

1. **Wiki Editor** (.17, existing) — article authoring with markdown-backed
   storage, proposal-based review workflow, Confluence migration support.
2. **Document Studio** (editor's laptop, new) — marketing document
   authoring tool that runs locally. Editors create documents on their
   laptop, then submit them to the Internal Marketing Portal for review.
   Does **not** read wiki content.
3. **Internal Marketing Portal** (.17, new) — server-side application that
   receives document submissions from Document Studio, manages the human
   review/approval workflow, and reads wiki content via the Wiki API.
   Same Pillar C pattern as the wiki: authors submit, humans review,
   approved content goes live.

The **motivation for sharing TipTap** across all three:
- All three need the same editor engine (ProseMirror, extensions,
  serialization, event handling)
- The Internal Marketing Portal follows the **same workflow pattern** as
  the wiki (author → submit → review → approve) — so the review UI needs
  the same TipTap capabilities (diff view, comments, approve/reject buttons)
- The Internal Marketing Portal reads wiki articles for reference and
  linking — so it uses wiki-aware extensions (link resolution, attachment
  handling, markdown serialization)
- Avoiding three separate TipTap codebases that drift apart

## The solution: shared editor core + per-app configuration

TipTap is a **headless editor** — no CSS, no UI components. The editor's
appearance is entirely controlled by the host application. We share the
editor *engine* while each app owns its own *design*, *toolbar*, *save
logic*, and *extensions*.

```
┌─────────────────────────────────────────────────────────────────┐
│  Shared: @luci/editor                                            │
│                                                                  │
│  THE ENGINE (shared, one codebase):                              │
│  • TipTap / ProseMirror setup                                    │
│  • Shared extensions (StarterKit, Link, Image, Table)           │
│  • Wiki-aware extensions (used by Internal Marketing Portal):   │
│    - WikiLinkResolver (/article/slug → display title)           │
│    - WikiAttachmentHandler (attachments/filename.png)           │
│    - MarkdownSerializer (HTML ↔ wiki markdown format)           │
│  • Content serialization (HTML ↔ Markdown)                      │
│  • Event handling (onChange, onSave, onAutosave)                │
│                                                                  │
│  NOT INCLUDED (each app provides its own):                       │
│  • CSS / visual design                                           │
│  • Toolbar layout and styling                                    │
│  • Save/load handlers (API endpoints)                           │
│  • App-specific extensions                                       │
│  • Routing, auth, state management                               │
└──────┬──────────────────┬──────────────────┬────────────────────┘
       │                  │                  │
  imports           imports           imports
       │                  │                  │
       ▼                  ▼                  ▼
┌──────────────┐  ┌──────────────┐  ┌──────────────────────────┐
│  Wiki Editor │  │  Document    │  │  Internal Marketing       │
│  (.17 :8080) │  │  Studio      │  │  Portal (.17 :8081, new)  │
│              │  │  (LOCAL)     │  │                           │
│  Authors     │  │              │  │  Receives submissions     │
│  wiki        │  │  Authors     │  │  from Document Studio     │
│  articles    │  │  marketing   │  │  Review UI with TipTap    │
│              │  │  documents   │  │  (diff, comments,         │
│  Submits to  │  │              │  │   approve/reject)         │
│  wiki API    │  │  Submits to  │  │  Reads wiki via Wiki API  │
│  (proposals) │  │  Internal    │  │                           │
│              │  │  Marketing   │  │  Same Pillar C flow:      │
│  OWN DESIGN: │  │  Portal API  │  │  draft → in_review →      │
│  wiki CSS    │  │              │  │  approved → merged        │
│  wiki toolbar│  │  OWN DESIGN: │  │                           │
│              │  │  studio CSS  │  │  OWN DESIGN:              │
│              │  │  studio      │  │  portal CSS               │
│              │  │  toolbar     │  │  portal toolbar           │
│              │  │              │  │  (review-focused)         │
└──────────────┘  └──────────────┘  └──────────────────────────┘
```

**Key insight:** TipTap renders content as standard HTML elements
(`<h1>`, `<p>`, `<ul>`, etc.). Each app styles them with its own CSS.
The editor *behavior* is shared; the editor *appearance* is not. Three
apps can share the same editor and look completely different.

---

## The workflow (same pattern as the wiki)

Both the wiki and the Internal Marketing Portal follow the **Pillar C
proposal workflow**: authors create content, submit it as a proposal, a
human reviewer approves/modifies/rejects it, approved content goes live.

```
WIKI FLOW (existing):
  Author → TipTap editor (.17:8080) → submit proposal → Wiki API →
  Reviewer → review queue → approve → article goes live

MARKETING FLOW (new):
  Editor → Document Studio (local laptop) → submit to Internal Marketing Portal →
  Reviewer → Internal Marketing Portal review UI (.17) → approve →
  marketing document goes live
```

The **state machine is the same** in both:

```
draft → in_review → approved → merged
                ├──→ rejected
                ├──→ withdrawn
                └──→ request_changes → draft (back to author)
```

The shared `@luci/editor` package supports this workflow by providing:
- **Authoring mode** — the editor for creating/editing content (used by
  wiki editor + Document Studio)
- **Review mode** — the editor in read-only/diff mode for reviewing
  submissions (used by wiki review screen + Internal Marketing Portal review UI)
- **Comment threading** — comments on proposals (shared by both review
  surfaces)

---

## How "dueling designs" work

TipTap's headless design means the shared package doesn't dictate any
visual style. Each app controls its own look:

| Aspect | Shared package | Wiki Editor | Document Studio | Internal Marketing Portal |
|--------|----------------|-------------|-----------------|---------------------------|
| Content rendering | Provides `<h1>`, `<p>`, etc. | Wiki CSS theme | Studio CSS theme | Portal CSS theme |
| Toolbar | Exports primitives (buttons) | Wiki-style toolbar | Studio-style toolbar | Review-focused toolbar |
| Layout | None (headless) | Sidebar + editor + rail | [Studio's own layout] | Review layout (diff + comments) |
| Extensions | Shared set + wiki-aware | Adds wiki-specific | Adds marketing-specific | Adds review-specific + wiki-aware |
| Wiki API | — | Via wiki API (native) | Does not use | Reads wiki for search/reference |

Think of it like a car engine — the same engine can go in a sedan, a
truck, or a sports car. The engine is shared; the body design is not.

---

## The configuration interface

```typescript
import { createLuciEditor } from '@luci/editor';

const editor = createLuciEditor({
  extensions: [...],           // shared + app-specific TipTap extensions
  toolbar: [...],              // each app picks which buttons to show
  mode: 'author' | 'review',   // authoring mode or review (read-only/diff) mode
  onSave: async (html, md) => {/* your save logic */},
  onLoad: async () => {/* your load logic */},
  onAutosave?: async (html, md) => {/* autosave */},
  onUpload?: async (file) => {/* attachment upload */},
  // Review-mode options (used by wiki review screen + Internal Marketing Portal):
  diffBase?: string,           // base content for diff comparison
  onApprove?: () => Promise<void>,
  onRequestChanges?: (comment: string) => Promise<void>,
  onReject?: (comment: string) => Promise<void>,
});
```

---

## Deployment architecture

```
┌──────────────────────────────────────────────────────────────┐
│  Editor's Laptop (LOCAL)                                      │
│                                                               │
│  ┌─────────────────────────────────────────────────┐         │
│  │  Document Studio                                 │         │
│  │  - TipTap authoring (via @luci/editor)           │         │
│  │  - Authors marketing documents locally           │         │
│  │  - Submits to Internal Marketing Portal API      │         │
│  │    (on .17)                                      │         │
│  │  - Does NOT read wiki content                    │         │
│  │  - Own design, own toolbar, own extensions       │         │
│  └─────────────────────────────────────────────────┘         │
└──────────────────────────────────────────────────────────────┘
                    │
                    │ submits documents via HTTP
                    │
┌──────────────────────────────────────────────────────────────┐
│  .17 (VM)                                                     │
│                                                               │
│  ┌──────────────┐  ┌──────────────────────────┐  ┌────────┐ │
│  │  Wiki API    │  │  Internal Marketing       │  │ Wiki   │ │
│  │  :8000       │  │  Portal :8081 (new)       │  │ TipTap │ │
│  │              │  │                           │  │ :8080  │ │
│  │  - articles  │  │  - receives submissions   │  │        │ │
│  │  - search    │  │  - review workflow        │  │ - wiki │ │
│  │  - proposals │  │    (Pillar C pattern)     │  │   auth │ │
│  │  (Pillar C)  │  │  - TipTap review UI       │  │        │ │
│  │              │  │  - reads wiki via API ────┼──┘        │ │
│  └──────┬───────┘  │  - approve/reject/        │             │ │
│         │          │    request changes         │             │ │
│  ┌──────┴───────┐  │  - own database           │             │ │
│  │  Postgres    │  └──────────────────────────┘             │ │
│  │  - wiki DB   │                                              │ │
│  │  - internal_ │                                              │ │
│  │    marketing │                                              │ │
│  │    _portal   │                                              │ │
│  │    DB (new)  │                                              │ │
│  └──────────────┘                                              │ │
└──────────────────────────────────────────────────────────────┘
```

**Three deployment contexts:**

| App | Where | Port | Container | Notes |
|-----|-------|------|-----------|-------|
| Wiki Editor | .17 | :8080 | kb_editor (existing) | Authors wiki articles |
| Document Studio | Editor's laptop | N/A (local) | N/A (local app) | Authors marketing docs locally |
| Internal Marketing Portal | .17 | :8081 | internal_marketing_portal (new) | API, review UI, wiki reads |

Document Studio is **not** a Docker container on .17. It runs locally
on the editor's laptop as a standalone web app (or Electron/PWA). It
communicates with .17 via HTTP (submitting to the Internal Marketing
Portal API only).

---

## Code example: Document Studio (local authoring)

```typescript
// document-studio/src/main.ts
import { createLuciEditor } from '@luci/editor';
import { StarterKit, Image, Table, Link } from '@luci/editor/extensions';
import { BrandKit, TemplateLibrary } from './studio-extensions';

const editor = createLuciEditor({
  mode: 'author',
  extensions: [StarterKit, Image, Table, Link, BrandKit, TemplateLibrary],
  toolbar: ['bold', 'italic', 'h1', 'h2', 'link', 'image',
            'brand-color', 'template', 'save'],

  // Submit to the Internal Marketing Portal API
  onSave: async (html, markdown) => {
    await fetch('http://10.10.1.17:8081/api/documents', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ content: html, content_markdown: markdown }),
    });
  },

  // Load a document for editing
  onLoad: async () => {
    const resp = await fetch(`http://10.10.1.17:8081/api/documents/${docId}`);
    const data = await resp.json();
    return { html: data.content, markdown: data.content_markdown || '' };
  },

  // Upload attachments to the Internal Marketing Portal
  onUpload: async (file: File) => {
    const formData = new FormData();
    formData.append('file', file);
    const resp = await fetch('http://10.10.1.17:8081/api/assets', {
      method: 'POST',
      body: formData,
    });
    return (await resp.json()).url;
  },
});

document.getElementById('editor-container').appendChild(editor);
```

## Code example: Internal Marketing Portal review UI (server-side)

```typescript
// internal-marketing-portal/src/review.ts
import { createLuciEditor } from '@luci/editor';
import { StarterKit, Image, Table } from '@luci/editor/extensions';

const reviewEditor = createLuciEditor({
  mode: 'review',              // read-only with diff view
  extensions: [StarterKit, Image, Table],
  toolbar: ['approve', 'request-changes', 'reject'],

  // Load the submitted document
  onLoad: async () => {
    const resp = await fetch(`/api/proposals/${proposalId}`);
    const data = await resp.json();
    return { html: data.proposed_content, markdown: '' };
  },

  // Base content for diff comparison
  diffBase: baseContent,  // the current version, if editing an existing doc

  // Review actions — call the Internal Marketing Portal API
  onApprove: async () => {
    await fetch(`/api/proposals/${proposalId}/approve`, { method: 'POST' });
  },
  onRequestChanges: async (comment) => {
    await fetch(`/api/proposals/${proposalId}/request-changes`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ comment }),
    });
  },
  onReject: async (comment) => {
    await fetch(`/api/proposals/${proposalId}/reject`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ comment }),
    });
  },
});
```

---

## Repository structure

Recommended: **monorepo** with three apps sharing one editor package.

```
luci-frontend/
├── packages/
│   └── editor/              ← SHARED: @luci/editor
│       ├── src/
│       │   ├── index.ts     ← exports createLuciEditor(config)
│       │   ├── extensions/  ← shared + wiki-aware extensions
│       │   ├── toolbar/     ← shared toolbar primitives
│       │   └── types.ts     ← EditorConfig interface
│       ├── package.json
│       └── tsconfig.json
│
├── apps/
│   ├── wiki-editor/         ← William's territory (.17 :8080)
│   │   ├── src/
│   │   │   ├── main.ts      ← wiki authoring config
│   │   │   └── review.ts    ← wiki review screen config
│   │   ├── Dockerfile
│   │   └── package.json
│   │
│   ├── document-studio/     ← Jane's territory (LOCAL)
│   │   ├── src/
│   │   │   ├── main.ts      ← local authoring config
│   │   │   ├── studio-extensions.ts
│   │   │   └── save-handler.ts
│   │   ├── package.json     ← no Dockerfile (runs locally)
│   │   └── README.md
│   │
│   └── internal-marketing-portal/  ← Jane's territory (.17 :8081)
│       ├── src/
│       │   ├── review.ts    ← review UI config
│       │   ├── api/         ← Internal Marketing Portal API
│       │   ├── wiki-client.ts  ← Wiki API reads (search, articles)
│       │   └── review-handler.ts
│       ├── Dockerfile
│       └── package.json
│
├── skills/                  ← shared development guidelines
├── package.json             ← workspace root
└── docker-compose.yml       ← .17 deployment config
```

**Ownership:**

| Directory | Who owns it |
|-----------|-------------|
| `packages/editor/` | Both (PR review required) |
| `apps/wiki-editor/` | William only |
| `apps/document-studio/` | Jane only |
| `apps/internal-marketing-portal/` | Jane only |
| `skills/` | Shared (general guidelines) |

---

## Wiki API integration

The **Internal Marketing Portal** reads wiki content for search, reference,
and linking. **Document Studio does not** call the Wiki API.

### Authentication

Agent key minted for Jane (read-only). Store in `.env` (gitignored):

```bash
# ui_kits/internal-portal/.env
WIKI_API_URL=http://10.10.1.17:8000
WIKI_AGENT_KEY=luci_agent_<your-key>
```

See `docs/wiki-agent-key.md` for permissions and usage. To mint a replacement:

```bash
python tools/agent_keys.py mint \
  --display-name internal-marketing-portal \
  --spaces KB,SD,LS,JIRA-CLIENT-SAFE \
  --actions read \
  --max-audience staff
```

### Key endpoints

Full interactive docs: `http://10.10.1.17:8000/docs`

| Endpoint | Method | What it does |
|----------|--------|-------------|
| `/api/v1/search` | POST | Search wiki content |
| `/api/v1/articles/{slug}` | GET | Get article by slug |
| `/api/v1/articles` | GET | List articles with filters |
| `/api/v1/spaces` | GET | List spaces |

```typescript
// internal-marketing-portal/src/wiki-client.ts
const resp = await fetch('http://10.10.1.17:8000/api/v1/search', {
  method: 'POST',
  headers: {
    'Authorization': `Bearer ${AGENT_KEY}`,
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({ query: 'product features', top_k: 10 }),
});
```

---

## FAQ

### "Can I use a completely different CSS framework?"

Yes. TipTap is headless. Use Tailwind, Bootstrap, plain CSS, or anything
else. The editor renders standard HTML — you style it.

### "Can I add my own TipTap extensions?"

Yes. Pass them in the `extensions` array. App-specific extensions
(BrandKit, TemplateLibrary, PDFExport) live in your app directory, not
in the shared package.

### "Can Document Studio work offline?"

Yes — it runs locally on the editor's laptop. The TipTap editor works
entirely client-side. Save/load handlers can cache locally and sync with
the Internal Marketing Portal when the laptop is online. The shared
`@luci/editor` package doesn't depend on any server — it's a client-side
library.

### "How does submitting to the Internal Marketing Portal work?"

Document Studio makes an HTTP POST to the Internal Marketing Portal API on `.17`:
```
POST http://10.10.1.17:8081/api/documents
```
This creates a "proposal" (same state machine as the wiki's Pillar C):
`draft → in_review → approved → merged`. A human reviewer opens the
Internal Marketing Portal's review UI on `.17`, reviews the document with
TipTap (in `mode: 'review'`), and approves/rejects/requests changes.

### "Does the Internal Marketing Portal need its own database?"

Yes. The Internal Marketing Portal should have its own database (e.g.,
`internal_marketing_portal` in the same Postgres instance on `.17`). It
manages its own proposals, documents, and review state. It does not write
to the wiki's `knowledgebase` database.

### "Can the Internal Marketing Portal push content to the wiki?"

Yes, via the wiki's proposal API (`POST /api/v1/proposals`). But this
follows the wiki's safety invariant: agents/users propose, humans merge.
The portal cannot bypass review.

### "What if the wiki editor changes break my app?"

They can't — unless the `EditorConfig` interface changes. Internal
changes to the shared package are transparent. Interface changes require
a PR that both developers review.

### "Can I deploy independently?"

Yes. Document Studio runs locally (no deployment to .17 needed). The
Internal Marketing Portal deploys as its own Docker container on
`.17:8081`, independent of the wiki containers. The only shared
dependency is `packages/editor/`, compiled into each app at build time.

---

## Getting started checklist

For Jane (Document Studio + Internal Marketing Portal):

- [x] **Get the `skills/` folder** — in `ui_kits/internal-portal/skills/`
- [x] **Agree architecture** — naming, wiki-read boundary, ownership (2026-07-07)
- [ ] **Review the Wiki API** — open `http://10.10.1.17:8000/docs` (Swagger UI)
- [x] **Get an agent key** — minted 2026-07-07; stored in `ui_kits/internal-portal/.env` (gitignored). See `docs/wiki-agent-key.md`.
- [x] **Deploy Phase 1 to .17** — `npm run deploy:portal` → `http://10.10.1.17:8081`. See `docs/deploy-17.md`.
- [ ] **Build Internal Marketing Portal server** — API + wiki-client (Phase 2; after static parity)

---

## Contact

- **Wiki editor owner:** William Morse (wmorse@lucisystems.com)
- **Document Studio + Internal Marketing Portal owner:** Jane
- **Shared package:** PR review by both developers required for changes

---

## Shared development guidelines

The `skills/` folder is in this project at `ui_kits/internal-portal/skills/`:

- `api-design.md` — REST API conventions
- `testing-patterns.md` — testing strategies
- `docker-workflows.md` — container patterns
- `deployment.md` — deployment procedures

Also from Will:

1. **An agent key** for the Wiki API — minted; see `docs/wiki-agent-key.md` and `.env.example`
2. **The Wiki API OpenAPI spec** — at `http://10.10.1.17:8000/docs` or
   `http://10.10.1.17:8000/openapi.json`
