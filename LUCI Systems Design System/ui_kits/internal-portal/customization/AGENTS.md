# Customize documents — agent instructions

**Paste a portal preview URL into Cursor chat, or just name the document type and client.** No specific folder needs to be open. The agent reads master templates, CSS, assets, and skills from the shared OneDrive "Cursor Branding Files" folder.

## When a portal URL is pasted

1. Read **`cursor-manifest.json`** from the OneDrive "Cursor Branding Files" folder (or `http://10.10.1.17:8081/internal-portal/customization/cursor-manifest.json` as a fallback).
2. Read the template **`SKILL.md`** and **`_brand/SKILL.md`** from the OneDrive folder.
3. Read **`CURSOR.md`** in this folder for the full checklist (includes **automatically opening the rendered client HTML in Cursor's in-editor browser** after customizing — not the HTML source).
4. **Create a client workspace** using `scripts/create-client-workspace.sh "<Client Name>" <template-name> <doc-type>` — creates `~/Desktop/LUCI Docs/<client-name>/` with symlinks to OneDrive.

Each preview HTML also embeds `#luci-cursor-context` JSON with the same skill URLs.

## If working in luci-design locally

Same files under `ui_kits/internal-portal/customization/` — read locally instead of fetching HTTP. Use `scripts/prepare-client-doc.sh` to create client files in the top-level `clients/` folder.
