# LUCI document customization (Cursor workflow)



Template masters on the Internal Marketing Portal. **Mike's workflow: copy URL → paste in Cursor chat.** No folder setup required.



**Portal:** `http://10.10.1.17:8081/internal-portal/customization/`  

**Manifest:** `http://10.10.1.17:8081/internal-portal/customization/cursor-manifest.json`



## Workflow



1. Open a template preview (or use **Copy doc URL** on the portal).

2. Paste the URL into Cursor chat with client name and demo notes.

3. Cursor reads `SKILL.md`, `_brand/SKILL.md`, and `CURSOR.md` from the OneDrive "Cursor Branding Files" folder.

4. Create a client workspace at `~/Desktop/LUCI Docs/<client-name>/` using `scripts/create-client-workspace.sh` — symlinks to OneDrive for CSS/assets, client HTML in `clients/`.

5. **Fine-tune in Cursor's HTML preview** — click editable text (Client Summary, cover, close page) and type directly. No extra prompt needed.

6. Export PDF when ready (via the dev server's `POST /__pdf` or `scripts/render-pdf.sh`).



Each preview HTML embeds a `luci-cursor-context` JSON block so the agent knows which skills to load from the URL alone.



## Templates



| Document | Preview URL | Status |

|----------|-------------|--------|

| Capabilities | `…/capabilities-document/capabilities-document.html` | Ready |
| Sales deck | `…/sales-deck/sales-deck.html` | Ready |

| Scope of work | `…/scope-of-work/scope-of-work.html` | Ready |

| Budgetary estimate | `…/budgetary-estimate/budgetary-estimate.html` | Ready (4-page trim) |



## Agent files (HTTP + local)



| File | Role |

|------|------|

| `cursor-manifest.json` | URL → template routing |

| `CURSOR.md` | Agent checklist |

| `<template>/SKILL.md` | Editable vs locked map |

| `_brand/SKILL.md` | Brand guardrails |



## Updating masters



Jane updates in luci-design → `npm run deploy:portal`. Portal previews and embedded context refresh automatically.

