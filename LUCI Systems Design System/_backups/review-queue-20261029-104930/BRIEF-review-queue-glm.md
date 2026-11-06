# Brief (GLM, --execute): simplify the IMP Review Queue view

File to edit (ONLY this file): `LUCI Systems Design System/ui_kits/internal-portal/index.html`.
Do not touch any other file (review-queue.json and library-manifest.json are already updated by Grok). Commit locally when done (luci-cursor default is fine); never push. No deploy.

## What Jane wants
Mike should see at a glance what he needs to review and click straight in.

1. In `#view-review`, REMOVE the whole "Viewing badges as" control block (`<div class="review-viewer" id="review-viewer">` with the select, Reset unread button and hint). Make the JS null-safe so nothing breaks without it (`bindReviewViewerSelect`, `resetUnreadForViewer`, `getViewerAuthor` callers, etc. must not throw; the comment form's author select elsewhere must keep working). Do not remove the unread/comment logic used by other views; just remove this control from the UI.
2. Shorten the page-head intro to one short line (e.g. "What Mike needs to review."), or drop it.
3. Rewrite `renderReviewList()` so each item in `allReviewItems()` renders as a clean card/row with ONLY: the title, a one-line what-it-is, and ONE clear "Review" button (styled as the portal's primary/mint button) that links straight to the item, opening in a new tab: use `item.liveUrl` if present, else `previewUrl(item)` (existing helper). No status pills, no due dates, no approver line, no unread counters, no long descriptions. The one-liner: add a short field `oneLiner` support (use `item.oneLiner || item.summary`), and truncate visually to one line with CSS ellipsis.
   Use these one-liners by setting a small map in the JS keyed by id (so data files stay untouched):
   - `new-luci-upgrade-guide`: "Customer walkthrough for moving to New LUCI (on the review site)."
   - `case-study-yaamava-review`: "Yaamava' case study: five systems on one LUCI platform."
   - `events-overview-2026-10`: "2027 events: at-a-glance table, docs and membership options."
   Titles: "Upgrade Guide", "Yaamava' case study", "Events overview" (map by id too; fall back to item.title).
4. Remove counters about the review queue on this page if any are shown inside `#view-review` (sidebar nav badges elsewhere may stay but must not break).
5. Keep `#review/<id>` detail routing working (don't delete renderReviewDetail); it's just no longer the primary click.
6. Look: use existing portal tokens/classes/fonts already in the file. NO new external font loads, no new external assets. Three calm cards with whitespace, title + one-liner left, Review button right; stacks on narrow screens.

## Self-check
Open the file logic mentally/grep: no `review-viewer` markup remains in `#view-review`; `renderReviewList` emits exactly one link per item; page JS has no references that would throw on missing `#review-viewer-select` / `#review-reset-unread`. Print a short summary.
