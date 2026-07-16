# Client document library — planned workflow

**Status:** Deferred (logged 2026-07-09) · **Budgetary estimate trim:** Done 2026-07-09 (4-page master)  
**Owner:** Jane  
**Audience:** Mike (sales), Mark (VPN access), Cursor agents

---

## Current workflow (sufficient for now)

Mike can:

1. **Clone `luci-design` once** and open it in Cursor each session
2. **`git pull`** at session start for latest masters/skills (optional but recommended)
3. **Copy a template URL** from the portal Customize tab → paste into Cursor chat with client notes
4. **Customize** via agent (cover + close editable; story pages locked per template `SKILL.md`)
5. **Fine-tune** by clicking editable text in Cursor’s HTML preview
6. **Save locally** to `LUCI Systems Design System/ui_kits/sales/<client>-<doc>.html`

No portal library, no push script, no Client documents UI yet.

**Portal:** http://10.10.1.17:8081/internal-portal/index.html#customize  
**Agent rule:** `.cursor/rules/luci-doc-customization.mdc`  
**Morning brief:** `CURSOR-MORNING-BRIEF.md` (repo root)

---

## Problem we’re solving later

- Mike works in his own clone; saves must land in a **predictable place** everyone can find
- Mark (VPN) needs to **grab finished or in-progress docs** without hunting
- Mike should **resume unfinished work** without starting from the master template
- Jane needs a clear **handoff** (pull + deploy) without manual file shuffling
- Prefer **one “push when ready” action** — not re-cloning, not emailing HTML

---

## Agreed direction (not built yet)

### Repo is the source of truth

Client deliverables live in git — not a separate VM-only library that diverges from the design system.

### Proposed folder layout

```
LUCI Systems Design System/ui_kits/internal-portal/customization/clients/
  <client-slug>/
    capabilities.html
    capabilities.pdf          # optional, after PDF export
    meta.json                 # clientName, templateId, status, updated, author
  README.md
```

- **Masters** stay in `ui_kits/sales/` (e.g. `capabilities-document.html`)
- **Client work** moves out of flat `ui_kits/sales/<client>-capabilities.html` into `clients/<slug>/`
- Example migration: `paragon-capabilities.html` → `clients/paragon-casino-resort/capabilities.html`

### Portal Customize tab (two sections)

| Section | Purpose |
|---------|---------|
| **Start from template** | Existing — Copy doc URL, starter prompt |
| **Client documents** | List saved work from `clients-manifest.json` — preview, copy URL for Cursor, repo path, download PDF |

Manifest generated at `npm run build:review` by scanning `clients/`.

### Mike — target daily flow

1. Open `luci-design` in Cursor · `git pull`
2. New doc: template URL + client notes → agent saves under `clients/<slug>/`
3. Edit in preview · save
4. When ready: **`npm run clients:push`** (script TBD) — stages only `clients/`, commit, push

Portal **cannot** run git on Mike’s Mac. “Push” button on portal = **copy command** or **copy agent phrase** (“Push my client documents to git”).

Optional: Cursor task in `.vscode/tasks.json` — Run Task → Push client documents.

### Jane — target handoff

```bash
git pull
cd "LUCI Systems Design System"
npm run deploy:portal
```

Optional later: GitHub/GitLab Action on push to `main` (paths under `clients/`) → SSH `deploy:portal` to `.17` so Jane is out of the loop.

### Mark — target access

VPN → portal Client documents on `.17` (after deploy), or `git pull` + same repo paths.

---

## Build checklist (when resuming)

- [ ] Create `customization/clients/` + `README.md`
- [ ] Add `clients-manifest.json` generation to `scripts/build-stakeholder-review.mjs`
- [ ] Portal UI: **Client documents** section on Customize tab
- [ ] Include `clients/` in review/deploy bundle (`.17` preview)
- [ ] `scripts/push-client-docs.sh` + `npm run clients:push`
- [ ] Portal: **Copy push command** on Customize tab
- [ ] Update `.cursor/rules/luci-doc-customization.mdc` + template `SKILL.md` save paths
- [ ] Migrate `paragon-capabilities.html` into `clients/paragon-casino-resort/`
- [ ] Optional: `luci-mike.code-workspace`, auto `git pull` in agent rule
- [ ] Optional: CI deploy on push

---

## Decisions still open

- Does Mike run `git push` himself, or only commit locally and Jane pushes?
- Shared git remote (GitHub/GitLab) — confirm Mike has access
- Auto-deploy to `.17` vs manual `deploy:portal` after pull
- PDF storage in `clients/` per doc vs export on demand only

---

## Related docs

- `customization/README.md` — current Cursor URL workflow
- `customization/CURSOR.md` — agent routing
- `docs/deploy-17.md` — portal deploy pipeline
- `docs/shared-tiptap-strategy.md` — long-term Will API / review workflow
