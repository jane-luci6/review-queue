#!/bin/bash
# Render LUCI internal-team assets (desktop wallpapers, Teams/Zoom backgrounds, and the
# LinkedIn personal-profile team banner) from their HTML sources to PNG via headless Chrome.
#
# Outputs:
#   assets/wallpapers/wallpaper-{a,b,c}-*.png        @ 1920x1080 and 2560x1440
#   assets/teams-backgrounds/teams-bg-{a,b,c}-*.png   @ 1920x1080
#   assets/social/linkedin-team-banner.png            @ 1584x396 (@1x) and @2x
#
# Usage: scripts/render-internal-team-assets.sh
set -eu

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
if [ ! -x "$CHROME" ]; then
  echo "Google Chrome not found at: $CHROME" >&2
  exit 1
fi

render() {
  # $1 = src html (relative to ROOT), $2 = out png, $3 = width, $4 = height, $5 = scale
  local src="$1" out="$2" w="$3" h="$4" scale="${5:-1}"
  "$CHROME" --headless=new --disable-gpu --hide-scrollbars \
    --default-background-color=0A161CFF \
    --force-device-scale-factor="$scale" \
    --virtual-time-budget=8000 \
    --window-size="$w,$h" \
    --screenshot="$ROOT/$out" \
    "file://$ROOT/$src"
  echo "Wrote $out"
  sips -g pixelWidth -g pixelHeight "$ROOT/$out" 2>/dev/null | sed "s|^|$out: |" || true
}

# ---- Wallpapers (1920x1080 @1x and 2560x1440 @1x) ----
for v in a-quiet b-architectural c-diagram; do
  render "assets/wallpapers/wallpaper-${v}.html" "assets/wallpapers/wallpaper-${v}-1920x1080.png" 1920 1080
  # 2560x1440 — render the same source at a 2560x1440 window
  render "assets/wallpapers/wallpaper-${v}.html" "assets/wallpapers/wallpaper-${v}-2560x1440.png" 2560 1440
done

# ---- Teams / Zoom backgrounds (1920x1080 @1x) ----
for v in a-quiet b-architectural c-diagram; do
  render "assets/teams-backgrounds/teams-bg-${v}.html" "assets/teams-backgrounds/teams-bg-${v}.png" 1920 1080
done

# ---- LinkedIn personal-profile team banner (1584x396 @1x and @2x) ----
render "assets/social/linkedin-team-banner.html" "assets/social/linkedin-team-banner.png" 1584 396
"$CHROME" --headless=new --disable-gpu --hide-scrollbars \
  --default-background-color=0A161CFF \
  --force-device-scale-factor=2 \
  --virtual-time-budget=8000 \
  --window-size=1584,396 \
  --screenshot="$ROOT/assets/social/linkedin-team-banner@2x.png" \
  "file://$ROOT/assets/social/linkedin-team-banner.html"
echo "Wrote assets/social/linkedin-team-banner@2x.png"
sips -g pixelWidth -g pixelHeight "$ROOT/assets/social/linkedin-team-banner@2x.png" 2>/dev/null | sed 's|^|@2x: |' || true

echo
echo "Done. Review the wallpapers and Teams backgrounds side by side (A/B/C) and pick a direction."
