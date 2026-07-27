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
| `proposal` | **Proposal - LED** | `ui_kits/sales/<client>-proposal-led.html` (legacy: `<client>-proposal.html`) |
| `budgetary-estimate` | Budgetary estimate | `ui_kits/sales/<client>-budgetary-estimate.html` |

Masters: `ui_kits/sales/<master>.html` (under `LUCI Systems Design System/`).

**Coming (Phase 3–4):** `proposal-luci-retrofit` → **Proposal - LUCI Retrofit**; `proposal-upgrade` → **Proposal - Upgrade**. Until those portal cards exist, do **not** convert a Budgetary Estimate into a Proposal by rewriting it from scratch — wait for the dedicated template or ask Jane.

---

## Efficient customization (mandatory)

Read `_brand/SKILL.md` → **Efficient customization** before any edit. Applies to **every** Customization Studio document.

1. **Populate-in-place** — never rebuild the doc; never invent fine-print.
2. **Mike can click-edit any text** — fonts/colors/layout stay on CSS; only LUCI logos stay non-editable. **Save HTML** / **Download PDF** in the edit bar.
3. **One project folder** with `ui_kits/sales/` + `assets/` mirrored so relative paths resolve; serve from the **project root**, not `ui_kits/sales/`.
4. Edit by `[data-studio]` / listed selectors only — do not rewrite whole sections.
5. Same working HTML forever — do not treat `*-edited.html` downloads as the source of truth; write typed preview edits back into that same file.
6. No accessibility snapshots; mandatory page-overflow fit check after content edits.
7. Do not link extra CSS the master does not already use (causes missing circuit texture / stripped header bands).

**Scope gate:** when a change is about document structure/copy (not efficiency/editability), ask Jane whether it should also apply to other studio templates before propagating.

Also read: `.cursor/rules/luci-doc-customization.mdc`

---

## Agent checklist

1. Identify template from pasted URL (or `#luci-cursor-context` on the page).
2. Fetch/read template `SKILL.md` + `_brand/SKILL.md` + this file’s **Efficient customization** section.
3. Never edit the portal deploy copy on the VM — it refreshes on deploy.
4. Copy master → the **one** client working file; customize per skill. Keep `contenteditable` / `data-studio`. Never edit locked pages/regions — including color or CSS — without confirming first.
5. **Automatically open the rendered client HTML** in Cursor’s in-editor browser (not the HTML source).
6. Before any further agent pass after Mike types in preview: write those edits back into the **same** working file.
7. Export PDF on request.

---

## Open the rendered preview in the editor (automatic — every time)

After customizing the client HTML, **automatically open the rendered doc in Cursor's in-editor (Glass) browser — not the HTML source.** Do this as the final step of every customization, without being asked.

1. Start a local static server rooted at the **project root that contains both `ui_kits/` and `assets/`** (in luci-design: `LUCI Systems Design System/`; on Mike’s machine: the per-job folder). Example: `python3 -m http.server 8771 --bind 127.0.0.1`. **Never** root at `ui_kits/sales/` — logos and circuit textures 404.
2. Verify: `curl …/ui_kits/sales/<client-file>.html` → `200`, and `…/assets/textures/texture-circuit-header-mintgold.png` → `200`.
3. Open `http://127.0.0.1:<port>/ui_kits/sales/<client-file>.html` via `cursor-app-control` `open_resource`. Do **not** use a `file://` URI.
4. Tell the user it's live and click-to-edit. Leave the server running while they review.

**Typed edits:** write preview edits back into the same working HTML before any further agent change. Do not treat “Copy / Download HTML” (`*-edited.html`) as the source of truth.

**User fallback:** `Cmd+Shift+P` → "Simple Browser: Show" → paste the localhost URL.

---

## Full preview URLs

| Document | URL |
|----------|-----|
| Sales deck | `http://10.10.1.17:8081/internal-portal/customization/sales-deck/sales-deck.html` |
| Capabilities | `http://10.10.1.17:8081/internal-portal/customization/capabilities-document/capabilities-document.html` |
| Scope of work | `http://10.10.1.17:8081/internal-portal/customization/scope-of-work/scope-of-work.html` |
| Proposal - LED | `http://10.10.1.17:8081/internal-portal/customization/proposal/proposal.html` |
| Budgetary estimate | `http://10.10.1.17:8081/internal-portal/customization/budgetary-estimate/budgetary-estimate.html` |

---

## Project rule (luci-design)

`.cursor/rules/luci-doc-customization.mdc` — always on; triggers when a portal URL appears in chat, regardless of which file is open.
