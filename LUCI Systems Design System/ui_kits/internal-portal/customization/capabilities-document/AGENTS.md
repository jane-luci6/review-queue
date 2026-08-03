# Capabilities document — Cursor agent entry

**Portal preview:** `http://10.10.1.17:8081/internal-portal/customization/capabilities-document/capabilities-document.html`

**Source:** OneDrive "Cursor Branding Files" folder — read master templates, CSS, and skills from here.

When this URL (or a request to customize the capabilities doc) appears in chat:

1. Read **`SKILL.md`** (this folder) — editable vs locked pages, selectors, do-not list.
2. Read **`../_brand/SKILL.md`** — typography, accent, voice, file hygiene.
3. Read **`../CURSOR.md`** if the URL alone was pasted — confirms source paths.

## Source + working folder

| Role | Path |
|------|------|
| Master (OneDrive) | `ui_kits/sales/capabilities-document.html` (in the "Cursor Branding Files" folder) |
| Client working file | `~/Desktop/LUCI Docs/<client-name>/clients/<client-name>-capabilities.html` |

Create a client workspace with `scripts/create-client-workspace.sh "<Client Name>" capabilities-document capabilities`, then customize **cover (page 1)** and **close (page 9)** only.

## Default workflow

Ask for (or use provided): property name, client summary, client logo path, rep contact on close page. Apply edits per `SKILL.md`. **Automatically open the rendered client HTML in Cursor's in-editor browser for click-to-edit fine-tuning** (see `../CURSOR.md` → "Open the rendered preview in the editor"); do not open a `file://` URI (that shows the source). PDF export on request.
