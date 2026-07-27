# LUCI document customization — Cursor entry

**Paste a portal preview URL into Cursor chat.** That's the whole workflow. No specific folder needs to be open.

Each preview page embeds a `#luci-cursor-context` JSON block (and this manifest) so the agent knows which skills to load.

**Portal base:** `http://10.10.1.17:8081/internal-portal/customization/`  
**Manifest:** `http://10.10.1.17:8081/internal-portal/customization/cursor-manifest.json`

---

## What the agent fetches (from the pasted URL)

| Resource | URL pattern |
|----------|-------------|
| This router | `…/customization/CURSOR.md` |
| Brand rules | `…/customization/_brand/SKILL.md` |
| Template skill | `…/customization/<template-id>/SKILL.md` |
| Template agents | `…/customization/<template-id>/AGENTS.md` |
| Manifest | `…/customization/cursor-manifest.json` |

Example — capabilities doc pasted:

`http://10.10.1.17:8081/internal-portal/customization/capabilities-document/capabilities-document.html`

→ fetch `…/capabilities-document/SKILL.md` + `…/_brand/SKILL.md` + this file.

If the workspace is **luci-design**, the same content lives locally under `ui_kits/internal-portal/customization/`.

---

## URL → document routing

| URL path segment | Document | Client copy pattern |
|------------------|----------|---------------------|
| `sales-deck` | Sales deck | `ui_kits/sales/<client>-sales-deck.html` |
| `capabilities-document` | Capabilities | `ui_kits/sales/<client>-capabilities.html` |
| `scope-of-work` | Scope of work | `ui_kits/sales/<client>-scope-of-work.html` |
| `scope-of-work-led` | Scope of work — LED | `ui_kits/sales/<client>-scope-of-work-led.html` |
| `budgetary-estimate` | Budgetary estimate | `ui_kits/sales/<client>-budgetary-estimate.html` |

Masters: `ui_kits/sales/<master>.html` (under `LUCI Systems Design System/`).

---

## Agent checklist

1. Identify template from pasted URL (or `#luci-cursor-context` on the page).
2. Fetch/read template `SKILL.md` + `_brand/SKILL.md`.
3. Never edit the portal deploy copy on the VM — it refreshes on deploy.
4. Copy master → client-named file; customize per skill. **Keep `contenteditable` on editable regions. Never edit locked pages/regions — including color or CSS — without confirming first** (pre-edit gate in `.cursor/rules/luci-doc-customization.mdc`).
5. **Automatically open the rendered client HTML in Cursor's in-editor browser** (not the HTML source) — see "Open the rendered preview in the editor" below. Mike clicks editable text and types in that preview.
6. Export PDF on request.

---

## Open the rendered preview in the editor (automatic — every time)

After customizing the client HTML, **automatically open the rendered doc in Cursor's in-editor (Glass) browser — not the HTML source.** Do this as the final step of every customization, without being asked.

1. From the client file's folder (`LUCI Systems Design System/ui_kits/sales/`), start a local static server in the background: `python3 -m http.server 8771 --bind 127.0.0.1` (if 8771 is busy, increment until free; reuse it if it's already serving the right file).
2. Verify it serves the file: `curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:<port>/<client-file>.html` → `200`.
3. Open the rendered URL in Cursor's in-editor (Glass) browser via the `cursor-app-control` MCP `open_resource` tool, URI `http://127.0.0.1:<port>/<client-file>.html`. This renders the doc with all CSS, fonts, diagrams, and the client logo inside Cursor; the `contenteditable` regions are click-to-edit there.
4. Tell the user it's live in the editor and click-to-edit. Leave the server running while they review; stop it when they're done or before PDF export.

**Do not** open the client HTML with a `file://` URI — `open_resource` opens that as a text file (HTML source), not a rendered preview. The `http://127.0.0.1:<port>/…` URL is what renders in Cursor.

**User fallback** if the in-editor pane doesn't appear: `Cmd+Shift+P` → "Simple Browser: Show" → paste the localhost URL.

---

## Full preview URLs

| Document | URL |
|----------|-----|
| Sales deck | `http://10.10.1.17:8081/internal-portal/customization/sales-deck/sales-deck.html` |
| Capabilities | `http://10.10.1.17:8081/internal-portal/customization/capabilities-document/capabilities-document.html` |
| Scope of work | `http://10.10.1.17:8081/internal-portal/customization/scope-of-work/scope-of-work.html` |
| Scope of work — LED | `http://10.10.1.17:8081/internal-portal/customization/scope-of-work-led/scope-of-work-led.html` |
| Budgetary estimate | `http://10.10.1.17:8081/internal-portal/customization/budgetary-estimate/budgetary-estimate.html` |

---

## Project rule (luci-design)

`.cursor/rules/luci-doc-customization.mdc` — always on; triggers when a portal URL appears in chat, regardless of which file is open.
