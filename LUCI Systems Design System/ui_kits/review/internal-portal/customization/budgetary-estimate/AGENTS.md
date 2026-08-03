# Budgetary estimate — Cursor agent entry

**Portal preview:** `http://10.10.1.17:8081/internal-portal/customization/budgetary-estimate/budgetary-estimate.html`

**Status:** Ready — 4-page trim (post-capabilities follow-on).

When this URL (or a request to customize the budgetary estimate) appears in chat:

1. Read **`SKILL.md`** (this folder) — editable pages, pricing selectors, no-auto-math rule.
2. Read **`../_brand/SKILL.md`** — typography, accent, voice, file hygiene.
3. Read **`../CURSOR.md`** if the URL alone was pasted — confirms source paths.

## Edit in luci-design (not on the VM)

| Role | Path |
|------|------|
| Master | `LUCI Systems Design System/ui_kits/sales/budgetary-estimate.html` |
| Client deliverable | `LUCI Systems Design System/clients/<client>-budgetary-estimate.html` |

Copy the master to a client file. Editable: cover, context + scope (p2), proposal (p3), investment/tiers/close contact (p4). Marketing delivers grid on p4 stays locked per `SKILL.md`.

## Default workflow

Use after the client has the Capabilities document. Ask for scope counts, line items, and tier values — type numbers manually (no auto-math). **Automatically open the rendered client HTML in Cursor's in-editor browser for click-to-edit fine-tuning** (see `../CURSOR.md` → "Open the rendered preview in the editor"); do not open a `file://` URI (that shows the source). PDF export on request.
