# LUCI document customization

**Mike's workflow: copy URL → paste in Cursor chat with client name.** No folder setup required.

**Portal:** `http://10.10.1.17:8081/internal-portal/customization/`

## Templates

| Document | Preview URL | Status |
|----------|-------------|--------|
| Capabilities | `…/capabilities-document/capabilities-document.html` | Ready |
| Sales deck | `…/sales-deck/sales-deck.html` | Ready |
| Scope of work | `…/scope-of-work/scope-of-work.html` | Ready |
| Budgetary estimate | `…/budgetary-estimate/budgetary-estimate.html` | Ready |
| Proposal - LED | `…/proposal/proposal.html` | Ready |
| Proposal - LUCI Retrofit | `…/proposal-luci-retrofit/proposal-luci-retrofit.html` | Ready |
| Proposal - Upgrade | `…/proposal-upgrade/proposal-upgrade.html` | Ready |

## How it works

1. Open a template preview (or use **Copy prompt** on the portal).
2. Paste the prompt into Cursor chat with client name and notes.
3. Cursor reads `_brand/SKILL.md` + the template `SKILL.md` from the OneDrive folder, creates a workspace at `~/Desktop/LUCI Docs/<client-name>/`, and customizes.
4. Fine-tune in Cursor's preview — click editable text and type. Save writes back automatically.
5. Export PDF when ready.

## Updating masters

Jane updates in luci-design → `npm run deploy:portal`. Portal previews and embedded context refresh automatically.
