# LUCI design — morning brief for Cursor

**Updated:** July 8, 2026  
**Workspace:** `luci-design` (open this repo in Cursor)

Jane: start a new chat and `@CURSOR-MORNING-BRIEF.md` (or just open this file first) to restore context from yesterday's session.

---

## What we finished yesterday

### 1. Paragon Capabilities document (client copy)

- **File:** `LUCI Systems Design System/ui_kits/sales/paragon-capabilities.html`
- **Cover:** Paragon Casino Resort client summary (editable)
- **Close page (page 10):** **Michael Epstein** / `mepstein@lucisystems.com` (replaced Mark Filler)
- **Locked:** Pages 2–9 (LUCI story) — do not edit unless Jane asks
- **Master (unchanged):** `ui_kits/sales/capabilities-document.html` still has Mark as default contact

**Local preview:**

```bash
cd "LUCI Systems Design System"
npm run serve
# → http://localhost:8765/ui_kits/sales/paragon-capabilities.html
```

**PDF export:**

```bash
cd "LUCI Systems Design System"
npm run prepare:pdf
npm run pdf -- ui_kits/sales/paragon-capabilities.html ~/Downloads/LUCI-Capabilities-Paragon.pdf
```

### 2. Mike's Cursor customization workflow (portal → client doc)

Nick's vision: Mike pastes a portal URL into Cursor chat. Cursor knows what to do. **No specific folder needs to be open.**

| Step | What Mike does |
|------|----------------|
| 1 | Portal → **Customize** tab → **Copy doc URL** (or click the URL box below it) |
| 2 | Paste URL + client notes into a **new** Cursor chat |
| 3 | Cursor customizes → saves client copy under `ui_kits/sales/<client>-<doc>.html` |
| 4 | **Click editable text in Cursor's HTML preview** to fine-tune (Client Summary, cover, close) |
| 5 | Save file; export PDF when ready |

**Portal (production):** http://10.10.1.17:8081/internal-portal/index.html#customize  
Hard-refresh (Cmd+Shift+R) after deploys.

**Capabilities URL:**

```
http://10.10.1.17:8081/internal-portal/customization/capabilities-document/capabilities-document.html
```

### 3. URL only — starter prompt is optional

**Just the URL is enough** for Cursor to find skills, master file, and save location. Three mechanisms:

1. Always-on rule: `.cursor/rules/luci-doc-customization.mdc`
2. Embedded JSON on each preview page: `#luci-cursor-context`
3. Manifest: `ui_kits/internal-portal/customization/cursor-manifest.json`

Mike **must still add client notes** in the same message (property name, pain points, contact, logo). Example:

```
http://10.10.1.17:8081/internal-portal/customization/capabilities-document/capabilities-document.html

Customize for [Client Name]. [demo notes, contact, logo path]
```

**Copy starter prompt** on the portal is a fill-in-the-blanks convenience — not required.

### 4. Click-to-edit: Cursor preview, not a canvas

Mike edits directly in **Cursor's HTML preview** of the client file. Editable regions use `contenteditable="true"` on `.doc-edit` and `[data-studio]` elements.

**Do not** push him toward a separate canvas — that workflow was removed.

### 5. Portal clipboard fix

Copy buttons failed on HTTP (`10.10.1.17`). Fixed with `document.execCommand('copy')` fallback. **Copy doc URL** and the URL box below it both work after hard-refresh.

---

## Key paths

| Purpose | Path |
|---------|------|
| Paragon client doc | `LUCI Systems Design System/ui_kits/sales/paragon-capabilities.html` |
| Capabilities master | `LUCI Systems Design System/ui_kits/sales/capabilities-document.html` |
| Portal customization hub | `LUCI Systems Design System/ui_kits/internal-portal/customization/` |
| Cursor routing | `…/customization/CURSOR.md` |
| Per-template skills | `…/customization/<template>/SKILL.md` |
| Brand guardrails | `…/customization/_brand/SKILL.md` |
| Cursor rule (always on) | `.cursor/rules/luci-doc-customization.mdc` |
| PDF asset prep | `LUCI Systems Design System/scripts/prepare-sales-pdf-assets.py` |
| PDF render | `LUCI Systems Design System/scripts/render-pdf.sh` |

---

## Deploy commands

**Internal Marketing Portal** (Mike's customize tab lives here):

```bash
cd "LUCI Systems Design System"
npm run deploy:portal
# Live at http://10.10.1.17:8081
```

**LUCI website** (separate project — review at `.37`, not `.17`):

```bash
cd luci-website
./deploy.sh
# Live at http://10.10.1.37
```

---

## Capabilities doc — editable vs locked

| Page | Status |
|------|--------|
| 1 — Cover | **Editable** (client name, summary, kicker, subhead, logo) |
| 2–9 — LUCI story | **Locked** |
| 10 — Close | **Editable** (kicker, headline, body, contact name/email) |

Full map: `ui_kits/internal-portal/customization/capabilities-document/SKILL.md`

---

## Testing as Mike (5-minute smoke test)

1. Open http://10.10.1.17:8081/internal-portal/index.html#customize
2. **Copy doc URL** on Capabilities → paste in a **new** Cursor chat with one line of client notes
3. Confirm agent writes/updates `ui_kits/sales/<client>-capabilities.html`
4. Open that file in Cursor preview → click Client Summary → change a word → save
5. Optional: run PDF pipeline and spot-check page 10 contact

---

## Not in scope / removed

- **LUCI Doc Preview canvas** — deleted; not part of Mike's workflow
- **`sync-doc-preview-canvas.mjs`** — deleted
- Mike does **not** need Remote-SSH to `.17` for customization

---

## Open items (if you pick up tomorrow)

- **Client document library** — planned workflow in `LUCI Systems Design System/ui_kits/internal-portal/docs/client-document-library-plan.md` (deferred; Mike saves locally under `ui_kits/sales/` for now)
- Paragon PDF: re-export if cover/close copy changed since last PDF run
- Budgetary estimate template: portal status is **pending trim** — hold new client work until Jane confirms
- Website work lives in `luci-website` repo; deploy to `10.10.1.37`

---

## Quick agent reminders

- Client work saves to `ui_kits/sales/<client>-<doc>.html` — never the VM deploy folder
- Preserve `contenteditable` and `data-studio` when customizing
- Canonical diagram changes → ask Jane: master or local copy only (see `.cursor/rules/luci-canonical-assets.mdc`)
- Body copy = Inter; headlines/labels = Space Grotesk; display moments = Syncopate (≤3 words)
