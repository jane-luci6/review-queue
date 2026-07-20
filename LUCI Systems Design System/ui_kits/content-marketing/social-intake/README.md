# Social intake — Friday drop folder

Raw progress photos and videos for the **next** week's LinkedIn batch land here. Jane drops files (or pastes them into chat); Cursor inventories them, proposes cuts/treatments, edits exports, and drafts the week's posts.

This is **not** a finished-asset library. Approved posts still live in `social-this-week.html` (and eventually LinkedIn). Edited exports for a given week stay under that week's folder until the week ships.

## Folder layout

```
social-intake/
  README.md
  YYYY-MM-DD/           ← Monday of the posting week (preferred), or Friday of prep
    raw/                ← Jane's originals (photos, .mov/.mp4, screen grabs)
    exports/            ← Cursor cuts / crops / stills / simple reels (ready for the post)
    NOTES.md            ← optional: client sensitivities, "don't show X", reveal-post plan
```

Example: posts going live the week of **2026-07-27** → `social-intake/2026-07-27/`.

## How to start a Friday

1. Create (or ask Cursor to create) `social-intake/<posting-week-Monday>/raw/`.
2. Drop photos/videos into `raw/`, or attach them in chat and say **"Friday social prep"** / **"prep next week's posts"**.
3. Cursor proposes treatments → edits into `exports/` → drafts the 3-slot batch into Social Studio / `social-this-week.html`.

## If there are no new photos

Say so in chat. Cursor searches Content Lab sources, mined insights, case studies, canonical diagrams, and prior approved visuals, then proposes a strategic bench for Jane to pick from.

## Media rules (hard)

- No client names on in-the-field posts; crop/blur identifiable signage, uniforms, landmarks.
- State work-in-progress; keep a placeholder for the reveal post.
- Large binaries (`.mov`, `.mp4`, raw dumps) are gitignored — keep them local; only commit small exports Jane wants versioned, or leave media out of git entirely.

## Phrasebook

| You say | Agent does |
|---|---|
| "Friday social prep" / "prep next week's posts" | Run the Friday workflow in `.cursor/rules/luci-social-media.mdc` |
| "cut this for LinkedIn" / "make a 15s reel" | ffmpeg (or HyperFrames if branded motion is needed) → `exports/` |
| "no new photos this week" | Search existing content; propose Slot A/B/C options |
