# Scope of work — LED · Cursor agent entry

**Portal preview:** `http://10.10.1.17:8081/internal-portal/customization/scope-of-work-led/scope-of-work-led.html`

When this URL (or a request to customize the LED scope of work) appears in chat:

1. Read **`SKILL.md`** (this folder) — page map, editable vs locked regions, typography table.
2. Read **`../_brand/SKILL.md`** — typography, accent, voice, file hygiene.
3. Read **`../CURSOR.md`** if the URL alone was pasted — confirms source paths.

## Edit in luci-design (not on the VM)

| Role | Path |
|------|------|
| Master | `LUCI Systems Design System/ui_kits/sales/scope-of-work-led.html` |
| Client deliverable | `LUCI Systems Design System/ui_kits/sales/<client>-scope-of-work-led.html` |

Copy the master to a client file, then customize cover, scope, specs, fee, estimates, terms, and signature per `SKILL.md`. Preserve CSS classes — never inline `font-family`.

## What's editable vs locked (summary)

- **Editable:** cover (except LUCI logo + "Prepared by LUCI Systems, LLC"), project intent narrative, COB stat values, gallery photos + captions, scope lists, client obligations, spec values + pitch in title, fee milestones + tariff note, all estimate line items + totals, warranty duration, client org name on signature.
- **Locked:** COB advantage + NovaStar architecture boilerplate (page 3), spec schema labels, warranty 4-column grid, gallery layout, document CSS/structure, page footers, band big numerals, LUCI contact line.

## Default workflow

Ask for property context, pixel pitch(s), per-installation line items, fee terms, and warranty duration. Apply edits per `SKILL.md`. **Automatically open the rendered client HTML in Cursor's in-editor browser for click-to-edit fine-tuning** (see `../CURSOR.md` → "Open the rendered preview in the editor"); do not open a `file://` URI (that shows the source). PDF export on request.

## Variable page counts

- **Spec pages:** one per pixel pitch — add/remove `.doc-page--led-specs` sections.
- **Estimate pages:** one per LED installation — clone `.doc-page--led-estimate` sections and renumber trailing page footers + band numerals.
