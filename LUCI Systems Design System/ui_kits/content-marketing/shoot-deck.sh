#!/usr/bin/env bash
# Screenshot every slide of a deck at 1280x720 into /tmp/<name>-sNN.png.
#
#   ./shoot-deck.sh new-luci-launch-marketing-plan.html [slides] [port]
#
# Geometry comes from sales-deck.css: body has padding-top 40px and gap 32px,
# and .slide is a fixed 720 tall — so slide N starts at 40 + N*752. Don't try
# to infer the pitch from pixels; the slide drop-shadow bleeds into the gap
# and throws the measurement off by ~6px per slide, which silently clips the
# last slide. The viewport must also be tall enough for the whole deck or
# Chrome returns a short image and the final crop comes back black.

set -euo pipefail

PAGE="${1:?usage: shoot-deck.sh <page.html> [slides] [port]}"
N="${2:-8}"
PORT="${3:-8767}"

TOP=40
PITCH=752
H=720

NAME="$(basename "$PAGE" .html)"
URL="http://127.0.0.1:${PORT}/ui_kits/content-marketing/${PAGE}"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
SHOT="/tmp/${NAME}-full.png"
VIEW=$(( TOP + N * PITCH + 200 ))

curl -sfo /dev/null "$URL" || { echo "No server at $URL — serve ui_kits/ first"; exit 1; }

"$CHROME" --headless --disable-gpu --hide-scrollbars \
  --screenshot="$SHOT" --window-size=1280,"$VIEW" "$URL" 2>/dev/null

python3 - "$SHOT" "$NAME" "$N" "$TOP" "$PITCH" "$H" <<'PY'
import sys
from PIL import Image

shot, name, n, top, pitch, h = sys.argv[1], sys.argv[2], *map(int, sys.argv[3:6+1][:4])
img = Image.open(shot)

need = top + (n - 1) * pitch + h
if img.height < need:
    sys.exit(f'Viewport too short: {img.height}px, need {need}px')

for i in range(n):
    t = top + i * pitch
    img.crop((0, t, 1280, t + h)).save(f'/tmp/{name}-s{i+1:02d}.png')

print(f'{n} slides -> /tmp/{name}-s01..s{n:02d}.png')
PY
