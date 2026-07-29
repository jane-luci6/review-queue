# LUCI internal team wallpapers

Desktop wallpapers for the LUCI team. Three directions — pick one and the other two get deleted.

| File | Direction |
|---|---|
| `wallpaper-a-quiet-1920x1080.png` / `-2560x1440.png` | **A — Quiet executive.** Vast negative space, faint mint-mark watermark upper-right, logo + tagline bottom-left. Calm, confident. |
| `wallpaper-b-architectural-1920x1080.png` / `-2560x1440.png` | **B — Architectural.** The isometric mint mark motif bleeds off the right edge (one plane in gold), tagline anchored left. More designed. |
| `wallpaper-c-diagram-1920x1080.png` / `-2560x1440.png` | **C — System orbit.** Abstract concentric orbit rings + nodes (one gold) with a soft central glow, tagline left, logo bottom-right. Evokes "the orchestrated system." |

## Specs
- Canvas `--navy-deep` `#0A161C`; mint `#68E3BE` primary, gold `#EDD086` secondary.
- Tagline: "The Orchestration Engine for Enterprise Multimedia" (Space Grotesk; "Orchestration Engine" in mint).
- Sub-tagline: "One interface to control, automate, and execute the entire guest experience." (Inter).
- Two resolutions: 1920×1080 (FHD) and 2560×1440 (QHD).

## Regenerate
```bash
cd "LUCI Systems Design System"
scripts/render-internal-team-assets.sh
```
Sources are the `.html` files + `_wallpaper-base.css`; they reference `../fonts/luci-brand-fonts.css` and `../logos/`. Edit the HTML, re-run the script. See `scripts/render-internal-team-assets.sh`.

Companion Teams/Zoom backgrounds live in `../teams-backgrounds/`; the LinkedIn personal-profile team banner is in `../social/linkedin-team-banner.html`.
