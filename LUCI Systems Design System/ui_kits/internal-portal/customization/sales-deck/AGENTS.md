# Sales deck — Cursor agent entry

**Portal preview:** `http://10.10.1.17:8081/internal-portal/customization/sales-deck/sales-deck.html`

When this URL (or a request to customize the sales deck) appears in chat:

1. Read **`SKILL.md`** (this folder) — editable vs locked slides, selectors, photo rules.
2. Read **`../_brand/SKILL.md`** — typography, accent, voice, file hygiene.
3. Read **`../CURSOR.md`** if the URL alone was pasted — confirms source paths.

## Edit in luci-design (not on the VM)

| Role | Path |
|------|------|
| Master (copy from, do not use as client deliverable) | `LUCI Systems Design System/ui_kits/sales/sales-deck.html` |
| Client deliverable | `LUCI Systems Design System/clients/<client>-sales-deck.html` |

Copy the master to a client file, then customize **slides 1–2** (copy, logo, photos).

## Default workflow

Ask for (or use provided): property name, client logo path, optional property photos, and any cover/environment copy tweaks. Apply edits per `SKILL.md`. **Preserve** `deck-edit`, `contenteditable`, and `data-studio` on editable nodes. **Automatically open the rendered client HTML in Cursor's in-editor browser for click-to-edit fine-tuning** (see `../CURSOR.md` → "Open the rendered preview in the editor"); do not open a `file://` URI (that shows the source). Use Download HTML when done.
