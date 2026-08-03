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

**Do not read other files** (AGENTS.md, README.md, other templates, other SKILL.md files). Everything you need is in those 2 files.

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
