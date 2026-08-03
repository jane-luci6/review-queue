# Capabilities document — Cursor agent entry

**Portal preview:** `http://10.10.1.17:8081/internal-portal/customization/capabilities-document/capabilities-document.html`

When this URL (or a request to customize the capabilities doc) appears in chat:

1. Read **`SKILL.md`** (this folder) — editable vs locked pages, selectors, do-not list.
2. Read **`../_brand/SKILL.md`** — typography, accent, voice, file hygiene.
3. Read **`../CURSOR.md`** if the URL alone was pasted — confirms source paths.

## Edit in luci-design (not on the VM)

| Role | Path |
|------|------|
| Master (copy from, do not use as client deliverable) | `LUCI Systems Design System/ui_kits/sales/capabilities-document.html` |
| Client deliverable | `LUCI Systems Design System/clients/<client>-capabilities.html` |

Copy the master to a client file, then customize **cover (page 1)** and **close (page 9)** only.

## Default workflow

Ask for (or use provided): property name, client summary, client logo path, rep contact on close page. Apply edits per `SKILL.md`. **Automatically open the rendered client HTML in Cursor's in-editor browser for click-to-edit fine-tuning** (see `../CURSOR.md` → "Open the rendered preview in the editor"); do not open a `file://` URI (that shows the source). PDF export on request.
