#!/usr/bin/env bash
# Render a local HTML document to a smooth, brand-correct PDF via headless Chrome.
#
# Usage:
#   scripts/render-pdf.sh <input.html> <output.pdf>
#
# Why these flags:
#   --virtual-time-budget=8000   Lets the self-contained base64 brand fonts
#                                (assets/fonts/luci-brand-fonts.css) decode
#                                BEFORE print fires. Without it, Chrome snapshots
#                                the page before the web fonts are ready and
#                                falls back to Trebuchet MS, then embeds a
#                                separate font subset per page (preview-choppy).
#
# Font rule for the source HTML (already applied to the sales docs):
#   The Google Fonts <link> MUST be absent (or commented out). Google serves
#   Inter as a *variable* font, which headless Chrome renders in print as Type3
#   vector outlines -- one drawing procedure per glyph. macOS Preview executes
#   those slowly, so the PDF "blinks in and out" and scrolls choppy. The static
#   base64 brand fonts embed as real Type0 fonts and render smoothly. The base64
#   CSS is self-contained and covers every weight the docs use, so the Google
#   fallback is not needed.
#
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"

if [ "$#" -lt 2 ]; then
  echo "Usage: $0 <input.html> <output.pdf>" >&2
  exit 64
fi

in="$1"
out="$2"

# Print-sized rasters + HTML font discipline (static Inter, no oversized embeds).
python3 "$ROOT/scripts/prepare-sales-pdf-assets.py" >/dev/null

# Resolve an absolute file:// URL (accepts relative or absolute input paths).
case "$in" in
  /*) abspath="$in" ;;
  *)  abspath="$(cd "$(dirname "$in")" && pwd)/$(basename "$in")" ;;
esac

patched="${abspath%.html}.pdf-export.html"
trap 'rm -f "$patched"' EXIT
python3 "$ROOT/scripts/patch-sales-pdf-html.py" --input "$abspath" --output "$patched" >/dev/null
print_src="file://$patched"

CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
if [ ! -x "$CHROME" ]; then
  echo "Google Chrome not found at: $CHROME" >&2
  exit 1
fi

"$CHROME" --headless=new --disable-gpu --no-pdf-header-footer \
  --virtual-time-budget=8000 \
  --print-to-pdf="$out" \
  "$print_src"

# Post-process for Acrobat: baseline JPEG passthrough, linearize for first-page paint.
# Do NOT downsample or re-subset fonts — that fuzzes diagram rasters and body text.
if command -v gs >/dev/null 2>&1; then
  gs_out="${out%.pdf}.gs.pdf"
  if gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.6 -dPrinted=true \
    -dDownsampleColorImages=false -dDownsampleGrayImages=false \
    -dDownsampleMonoImages=false \
    -dPassThroughJPEGImages=true \
    -dAutoFilterColorImages=false -dColorImageFilter=/DCTEncode \
    -dCompressFonts=false -dSubsetFonts=false \
    -dDetectDuplicateImages=true \
    -dNOPAUSE -dBATCH -dQUIET -sOutputFile="$gs_out" "$out" 2>/dev/null; then
    mv "$gs_out" "$out"
  else
    rm -f "$gs_out"
    echo "Warning: Ghostscript flatten failed; keeping Chrome PDF." >&2
  fi
fi

if command -v qpdf >/dev/null 2>&1; then
  optimized="${out%.pdf}.qpdf.pdf"
  if qpdf --object-streams=generate --stream-data=compress --recompress-flate --compression-level=9 "$out" "$optimized" \
    && qpdf --warning-exit-0 --check "$optimized" >/dev/null 2>&1; then
    mv "$optimized" "$out"
  else
    rm -f "$optimized"
    echo "Warning: qpdf optimization failed; keeping Chrome PDF." >&2
  fi
  linear="${out%.pdf}.linear.pdf"
  if qpdf --linearize "$out" "$linear" 2>/dev/null; then
    mv "$linear" "$out"
  else
    rm -f "$linear"
  fi
fi

bytes=$(stat -f%z "$out" 2>/dev/null || stat -c%s "$out")
echo "Wrote $out (${bytes} bytes)"
if command -v qpdf >/dev/null 2>&1; then
  if ! qpdf --warning-exit-0 --check "$out" >/dev/null 2>&1; then
    echo "Warning: qpdf reported structure issues in $out" >&2
  fi
fi
if [ "$bytes" -gt 1200000 ]; then
  echo "Warning: PDF is over 1.2 MB — re-run prepare:pdf or check for unstaged SVG/img refs." >&2
fi
