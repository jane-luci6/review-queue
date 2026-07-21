# Social intake — episode prompts

Home of the **Control the Whole Property** weekly-series Claude video prompts (`control-the-whole-property/epNN-*.md`). Jane pastes a prompt into Claude to generate each Tuesday's 30-second AI video.

> **Progress / on-site field photos are retired (Jul 2026).** Grand-reveal leakage + OSHA risk made them not worth it. This folder is **no longer a field-photo drop** — do not stage in-progress installation media here. See `.cursor/rules/luci-social-media.mdc` ("No progress photos").

## Folder layout

```
social-intake/
  README.md
  control-the-whole-property/
    ep01-series-intro-claude-prompt.md
    ep02-casino-floor-claude-prompt.md
    …
```

## Where the work happens now

The production workspace is **`../social-production.html`** (idea bench → 3-week calendar → per-post production). Friday prep farms ideas from the transcript miner, recent case studies, and the newsletter — not from field photos.

## Media rules (hard)

- **No progress / on-site field photos.** Retired — do not stage them here.
- **Named case study only with the client's OK**; unnamed is the default.
- **Always A/V** — never "AV" or "A-V."
- Large binaries (`.mov`, `.mp4`, images) are gitignored — keep them local.

## Phrasebook

| You say | Agent does |
|---|---|
| "Friday social prep" / "prep next week's posts" | Run the Friday workflow in `.cursor/rules/luci-social-media.mdc` — farm ideas, fill the calendar |
| "generate the Ep0N video" | Hand Jane the per-episode Claude prompt from `control-the-whole-property/` |
