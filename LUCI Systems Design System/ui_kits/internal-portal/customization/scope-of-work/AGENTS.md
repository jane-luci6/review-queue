# Scope of work — Cursor agent entry

**Portal preview:** `http://10.10.1.17:8081/internal-portal/customization/scope-of-work/scope-of-work.html`

When this URL (or a request to customize the scope of work) appears in chat:

1. Read **`SKILL.md`** (this folder) — section map, typography table, editable scope.
2. Read **`../_brand/SKILL.md`** — typography, accent, voice, file hygiene.
3. Read **`../CURSOR.md`** if the URL alone was pasted — confirms source paths.

## Edit in luci-design (not on the VM)

| Role | Path |
|------|------|
| Master | `LUCI Systems Design System/ui_kits/sales/scope-of-work.html` |
| Client deliverable | `LUCI Systems Design System/ui_kits/sales/<client>-scope-of-work.html` |

Copy the master to a client file, then customize cover and scope sections per `SKILL.md`. Preserve CSS classes — never inline `font-family`.

## Default workflow

Ask for property context, phased scope notes, and open items. Apply edits per `SKILL.md`. **Automatically open the rendered client HTML in Cursor's in-editor browser for click-to-edit fine-tuning** (see `../CURSOR.md` → "Open the rendered preview in the editor"); do not open a `file://` URI (that shows the source). PDF export on request.
