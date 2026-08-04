# LUCI document customization — Cursor entry

**Paste a portal preview URL into Cursor chat, or just name the document type and client.** The agent reads skills from the shared OneDrive "Cursor Branding Files" folder, then creates a working copy at `~/Desktop/LUCI Docs/<client-name>/`.

## URL → template routing

| URL path segment | Document | Template folder |
|------------------|----------|-----------------|
| `sales-deck` | Sales deck | `sales-deck` |
| `capabilities-document` | Capabilities | `capabilities-document` |
| `scope-of-work` | Scope of work | `scope-of-work` |
| `proposal` | **Proposal - LED** | `proposal` |
| `proposal-luci-retrofit` | Proposal - LUCI Retrofit | `proposal-luci-retrofit` |
| `proposal-upgrade` | Proposal - Upgrade | `proposal-upgrade` |
| `budgetary-estimate` | Budgetary estimate | `budgetary-estimate` |

Portal base: `http://10.10.1.17:8081/internal-portal/customization/`

## What to read (only these 2 files)

1. `ui_kits/internal-portal/customization/_brand/SKILL.md` — workflow, voice, fit check, PDF, all house rules
2. `ui_kits/internal-portal/customization/<template>/SKILL.md` — page map, editable vs locked regions for this template

**Do not read other files** (AGENTS.md, README.md, other templates, other SKILL.md files). Everything you need is in those 2 files. **Do not download every template or all design files** — `create-client-workspace.sh` copies the one template you need and symlinks all CSS/fonts/textures/assets. Everything is already in the template.

## Stable tooling (call these — do not re-derive)

| Task | Script | When |
|------|-------|------|
| Fit check | `python3 scripts/fit-check.py <html> --url <dev-url>` | After any content edit (mandatory) |
| Pack SOW | `python3 scripts/pack-content.py <html> --mode sow --start-page N --end-page M --url <dev-url> --write` | When SOW sections overflow or are underfilled |
| Pack line items | `python3 scripts/pack-content.py <html> --mode lineitems --start-page N --end-page M --url <dev-url> --write` | When line-item groups overflow or are underfilled |
| Ingest spreadsheet | `python3 scripts/ingest-budgetary-lineitems.py <xlsx>` | To convert a line-item spreadsheet to HTML rows |
| Render PDF | `POST /__pdf` on the dev server, or `bash scripts/render-pdf.sh <html> <out.pdf>` | To generate the final PDF |

**Do not write your own fit-check, packing, or measurement scripts.** These are committed and handle the edge cases (scrollHeight-returns-fixed-height, iframe same-origin, Chrome headless polling, greedy packing with totals exception, footer renumbering). Just call them.

## Full preview URLs

| Document | URL |
|----------|-----|
| Sales deck | `http://10.10.1.17:8081/internal-portal/customization/sales-deck/sales-deck.html` |
| Capabilities | `http://10.10.1.17:8081/internal-portal/customization/capabilities-document/capabilities-document.html` |
| Scope of work | `http://10.10.1.17:8081/internal-portal/customization/scope-of-work/scope-of-work.html` |
| Proposal - LED | `http://10.10.1.17:8081/internal-portal/customization/proposal/proposal.html` |
| Proposal - LUCI Retrofit | `http://10.10.1.17:8081/internal-portal/customization/proposal-luci-retrofit/proposal-luci-retrofit.html` |
| Proposal - Upgrade | `http://10.10.1.17:8081/internal-portal/customization/proposal-upgrade/proposal-upgrade.html` |
| Budgetary estimate | `http://10.10.1.17:8081/internal-portal/customization/budgetary-estimate/budgetary-estimate.html` |
