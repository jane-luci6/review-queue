# Canon — asset and production workflows

**Snapshot:** 28 August 2026  
**Sources:** deploy rules, `luci-canonical-assets.mdc`, `luci-propagation-workflow.mdc`, `luci-visual-options-workflow.mdc`, `luci-doc-customization.mdc`, `luci-sales-document-system.mdc`, `luci-stakeholder-review.mdc`, portal `SKILL.md` files  
**Execution:** Cursor + **GLM** unless a model gate is met. Grok writes the brief.

---

## Repos

- `luci-design` — almost all marketing ops  
- `luci-website` — Astro site; **current branch `persona-hero-subhead-gold`**

Do not clone GitHub as source of truth.

---

## Website deploy

From `luci-website`: `./deploy.sh` → `luci@10.10.1.37:/var/www/luci`  
Jane looks at **`http://10.10.1.37`**. Hard-refresh Cmd+Shift+R.  
Bump `?v=N` on changed images. Localhost:4321 is not the deliverable.

## Portal deploy

From `LUCI Systems Design System/`: `npm run deploy:portal` → `http://10.10.1.17:8081`  
SSH as `user-007@10.10.1.17`. Jane hard-refreshes.

Edit **source** `ui_kits/internal-portal/`, then build. Do not hand-edit `ui_kits/review/internal-portal/` as master.

## Diagram propagate

When Jane says propagate / ship / lock in / update everywhere:

```
cd "LUCI Systems Design System"
node scripts/propagate-diagram.mjs <basename> --dry-run
node scripts/propagate-diagram.mjs <basename>
```

Then deploy consumers (`.37` / `.17`) as needed. Raster PNG re-export is a flagged follow-up, not silent skip.

Ask first if a diagram change is **canonical master** vs **local to this asset**.

---

## Visual variants

Open-ended look: 2–3 branches, genuine axes, preview, Jane picks, merge, delete losers.  
Tiny tweak / locked mock: **do not** spawn variants.

Commit current work before branching (Cursor agent). Grok does not run git from Grok unless Jane’s Cursor session is doing it.

---

## Sales PDF / letter pages

- Template: `ui_kits/sales/_template-sales-document.html` + `sales-document.css` (`doc-` prefix). Brochure uses `brochure.css` (`cap-`).
- **Page-count invariant:** sheet is 8.5×11, `overflow: hidden`. Overflow is **silent**. If it doesn’t fit, **add a page**. Never silently trim Jane’s copy. Run `python3 scripts/fit-check.py`.
- PDF: `npm run prepare:pdf` then `bash scripts/render-pdf.sh`. No Ghostscript `/ebook`. No Google Fonts `<link>` — brand font CSS only.
- Body copy is Inter.

## Portal customization (Mike / Maker)

1. Read `_brand/SKILL.md` + `<template>/SKILL.md` only (for instructions).  
2. `scripts/create-client-workspace.sh`  
3. Edit **listed editable regions only**. Locked page = no CSS, no copy, no “small tweak” without Jane override (local vs canonical).  
4. Preserve `contenteditable` / `data-studio`.  
5. Preview at the LUCI docs server, not `file://`.

URL path → template id: sales-deck, capabilities-document, scope-of-work, proposal, proposal-luci-retrofit, proposal-upgrade, budgetary-estimate, mpsa.

---

## Stakeholder review (Mike/Nick)

Source: `review-queue.json`. Jane says push to review with due date → edit queue → `build-stakeholder-review.mjs` → deploy. Email Mike/Nick **manually** when adding an asset (`notify-email-templates.txt`). Do not email on each comment.

---

## Messaging Word sync

After OneDrive philosophy/guide/personas edit: `sync-messaging-docs.mjs` then rebuild review. Drift analysis is manual until automated.

---

## Social production

Workspace: `ui_kits/content-marketing/social-production.html`. Friday: farm ideas → Jane picks → produce (GLM for most; Jane still generates season video in Claude Design). No field-progress photos.

---

## Maker self-check (mechanical, before Review)

- Tokens only; no new colors/type  
- A/V spelling; no LUCI “layer”  
- Fit-check if letter HTML  
- Deploy + curl 200 if the brief said ship  
- Cache-buster if assets changed  
- Locked SKILL regions untouched  
- Contrast: mint not on light as body/accent fill  

Maker does **not** self-certify brand taste. That is Review.
