# Customize documents — agent instructions

**Paste a portal preview URL into Cursor chat.** No specific folder needs to be open.

## When a portal URL is pasted

1. Fetch or read **`cursor-manifest.json`** — `http://10.10.1.17:8081/internal-portal/customization/cursor-manifest.json`
2. Fetch the template **`SKILL.md`** and **`_brand/SKILL.md`** (URLs in manifest or derived from pasted URL).
3. Read **`CURSOR.md`** in this folder for the full checklist (includes **automatically opening the rendered client HTML in Cursor's in-editor browser** after customizing — not the HTML source).

Each preview HTML also embeds `#luci-cursor-context` JSON with the same skill URLs.

## If working in luci-design locally

Same files under `ui_kits/internal-portal/customization/` — read locally instead of fetching HTTP.
