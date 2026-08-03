#!/usr/bin/env bash
# Render the LinkedIn company cover HTML to PNG at @1x (1584x396) and @2x (3168x792).
#
# Usage: scripts/render-linkedin-cover.sh
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SRC="$ROOT/assets/social/linkedin-cover.html"
OUT1="$ROOT/assets/social/linkedin-cover.png"
OUT2="$ROOT/assets/social/linkedin-cover@2x.png"

CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
if [ ! -x "$CHROME" ]; then
  echo "Google Chrome not found at: $CHROME" >&2
  exit 1
fi

# @1x — 1584x396
"$CHROME" --headless=new --disable-gpu --hide-scrollbars \
  --default-background-color=0A161CFF \
  --force-device-scale-factor=1 \
  --virtual-time-budget=8000 \
  --window-size=1584,396 \
  --screenshot="$OUT1" \
  "file://$SRC"

# @2x — 3168x792
"$CHROME" --headless=new --disable-gpu --hide-scrollbars \
  --default-background-color=0A161CFF \
  --force-device-scale-factor=2 \
  --virtual-time-budget=8000 \
  --window-size=1584,396 \
  --screenshot="$OUT2" \
  "file://$SRC"

echo "Wrote $OUT1"
sips -g pixelWidth -g pixelHeight "$OUT1" >/dev/null 2>&1 && sips -g pixelWidth -g pixelHeight "$OUT1"
echo "Wrote $OUT2"
sips -g pixelWidth -g pixelHeight "$OUT2" >/dev/null 2>&1 && sips -g pixelWidth -g pixelHeight "$OUT2"
