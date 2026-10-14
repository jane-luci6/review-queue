CURSOR BRIEF
Repo: luci-website (primary) + luci-design only if ui_kits mirror needed
Branch: existing working branch for luci-website (persona-hero-subhead-gold or current local — do NOT use GitHub as source of truth)
Model: GLM
Why not GLM: n/a — GLM (shell + layout only; no unlocked spine)
Mode: execute

Outcome Jane will see:
A scaffolded Osage / Sand Springs case-study page on the review site under `/resources/case-studies/osage-sand-springs/` (or closest slug that matches Aliante-family pattern), clearly marked details TBD, with real safe project photos. Preview URL for IMP In Progress.

Where she looks: http://10.10.1.37/resources/case-studies/osage-sand-springs/ (hard-refresh). Also Resources case-studies index if you add a card.

Locked (do not invent):
- Naming: **Osage / Sand Springs** (consistent with Signal Issue 05 In the Field). Property/display naming should read Osage / Sand Springs — not invent other brands.
- This is a **shell only**. Jane will supply written details later. Do **not** write a GPT spine. Do **not** invent challenge/solution/results metrics, quotes, or claims.
- Placeholders required for: challenge, solution/approach, results, quote — with clear **“details TBD”** markers Jane can spot.
- Photos source (OneDrive Project Media):
  - `…/Marketing - Documents/Content/Project Media/Osage Ponca LED 1/` (Osage_1.jpeg … Osage_7.jpeg)
  - `…/Marketing - Documents/Content/Project Media/Osage Ponca LED 2/` (named osage-*.jpeg/jpg + IMG_* stills)
  - No separate Sand Springs folder found — do not invent Sand Springs-only media.
- **Do not publish the customer floor plan as-is.** If any CAD/plan/PDF floor plan appears, exclude it. Gaming-floor photography is OK; documents named plan/floorplan are not.
- Do **not** mine `Brian Osage Write ups.docx` for public copy in this pass — leave for Jane’s later details / GPT spine later.
- Visual/template: same family as Aliante Astro case study (`CaseStudyAliante.astro` + `caseStudyAliante.ts` + page + `public/images/case-studies/…`). Prefer cloning that structure over inventing a new layout thesis. Sam’s Town visual system rules already in Cursor — do not recap brand.
- No video/reel required for this shell.
- No Webflow / public lucisystems.com cutover work. Local Astro → deploy `.37` only.
- Always A/V (Cursor rules already enforce — do not lecture).

Open (GLM owns):
- Scaffold page + component + data module with placeholders.
- Copy a small set of **safe** photos into `public/images/case-studies/osage-sand-springs/` (web-sized as other studies). Prefer clearly photographic install/property shots; skip anything that looks like a customer floor plan drawing.
- Wire into case-studies index / resources listing in the same pattern as Aliante (card can say In Progress / details TBD if the pattern allows; otherwise still list it so IMP can link).
- Deploy to review `http://10.10.1.37`.
- Update Active jobs row `osage-cs-shell` on `luci-design/.../agent-handbook/shared/CURRENT-WORK-BOARD.md`: Stage = Jane review / waiting details; Artifact = preview URL + key paths; Waiting on Jane = written details; Next = Consuelo tells Cornelius URL for Weatherby/IMP; GPT spine only after Jane sends details.

Files / paths (start here):
- Pattern: `src/pages/resources/case-studies/aliante.astro`, `src/components/CaseStudyAliante.astro`, `src/data/caseStudyAliante.ts`, site.ts card entry, index listings
- Media: OneDrive paths above
- Board: agent-handbook `shared/CURRENT-WORK-BOARD.md` row `osage-cs-shell`

Definition of done:
1. Preview URL live on `.37` for Osage / Sand Springs shell
2. Placeholders + details TBD visible; no invented metrics/quotes
3. Safe photos in place; no floor plan as-is
4. Board row updated with URL
5. Return to Consuelo: URL, changed paths, commit, what was TBD, any visual gaps

Handoff when done: Consuelo (Case Studies). Consuelo notifies Cornelius for Weatherby/IMP In Progress. Do not start GPT spine. Do not ping Jane for copy.
