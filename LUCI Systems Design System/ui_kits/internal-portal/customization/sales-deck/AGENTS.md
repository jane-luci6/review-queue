# Sales deck — Cursor agent entry

**Portal preview:** `http://10.10.1.17:8081/internal-portal/customization/sales-deck/sales-deck.html`

**Source:** OneDrive "Cursor Branding Files" folder — read master templates, CSS, and skills from here.

When this URL (or a request to customize the sales deck) appears in chat:

1. Read **`SKILL.md`** (this folder) — editable vs locked slides, selectors, photo rules.
2. Read **`../_brand/SKILL.md`** — typography, accent, voice, file hygiene.
3. Read **`../CURSOR.md`** if the URL alone was pasted — confirms source paths.

## Source + working folder

| Role | Path |
|------|------|
| Master (OneDrive) | `ui_kits/sales/sales-deck.html` (in the "Cursor Branding Files" folder) |
| Client working file | `~/Desktop/LUCI Docs/<client-name>/clients/<client-name>-sales-deck.html` |

Create a client workspace with `scripts/create-client-workspace.sh "<Client Name>" sales-deck sales-deck`, then customize **slides 1–2** (copy, logo, photos).

## Default workflow

Ask for (or use provided): property name, client logo path, optional property photos, and any cover/environment copy tweaks. Apply edits per `SKILL.md`. **Preserve** `deck-edit`, `contenteditable`, and `data-studio` on editable nodes. **Automatically open the rendered client HTML in Cursor's in-editor browser for click-to-edit fine-tuning** (see `../CURSOR.md` → "Open the rendered preview in the editor"); do not open a `file://` URI (that shows the source). Use Download HTML when done.
