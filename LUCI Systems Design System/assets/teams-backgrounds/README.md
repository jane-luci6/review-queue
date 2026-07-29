# LUCI Teams / Zoom virtual backgrounds

1920×1080 backgrounds for Microsoft Teams and Zoom video calls. The center is kept clean navy so the person on camera reads clearly; branding sits in the corners/edges where the apps don't crop the subject. Three directions — pick one and the other two get deleted.

| File | Direction |
|---|---|
| `teams-bg-a-quiet.png` | **A — Quiet executive.** Logo + tagline bottom-right, faint mint-mark watermark upper-left. |
| `teams-bg-b-architectural.png` | **B — Architectural.** Isometric mint-mark motif bleeds off the far-right edge, logo + tagline bottom-left. |
| `teams-bg-c-diagram.png` | **C — System orbit.** Abstract orbit rings + nodes centered behind the subject (the subject appears inside the orbit), logo + tagline bottom-right. |

## Specs
- Canvas `--navy-deep` `#0A161C`; mint `#68E3BE` primary, gold `#EDD086` secondary.
- Tagline: "The Orchestration Engine for Enterprise Multimedia" (Space Grotesk; "Orchestration Engine" in mint).
- 1920×1080, PNG.

## To use
- **Teams:** Meetings → Effects and avatars → Add background → select the PNG.
- **Zoom:** Settings → Virtual Background → add the PNG.

## Regenerate
```bash
cd "LUCI Systems Design System"
scripts/render-internal-team-assets.sh
```
Sources are the `.html` files + `_teams-base.css`; they reference `../fonts/luci-brand-fonts.css` and `../logos/`. Edit the HTML, re-run the script.

Companion desktop wallpapers live in `../wallpapers/`; the LinkedIn personal-profile team banner is in `../social/linkedin-team-banner.html`.
