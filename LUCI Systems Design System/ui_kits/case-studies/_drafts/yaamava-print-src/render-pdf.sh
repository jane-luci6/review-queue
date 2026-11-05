#!/bin/bash
# Anti-blink PDF pipeline: Chrome export → Ghostscript passthrough → qpdf linearize
# Bakes CSS gradients into photos (in print.css) to avoid PDF Shading objects
# that repaint lazily (blink) in Preview/Acrobat.
set -e
D="$(cd "$(dirname "$0")/.." && pwd)"
CH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
"$CH" --headless=new --disable-gpu --no-pdf-header-footer --virtual-time-budget=10000 \
  --print-to-pdf="$D/yaamava-partnership-print-raw.pdf" "file://$D/yaamava-partnership-print.html"
gs -o "$D/yaamava-partnership-print-gs.pdf" -sDEVICE=pdfwrite \
  -dSubsetFonts=false -dEmbedAllFonts=true -dCompressFonts=false \
  -dAutoFilterColorImages=false -dColorImageFilter=/DCTEncode \
  -dAutoFilterGrayImages=false -dGrayImageFilter=/DCTEncode \
  "$D/yaamava-partnership-print-raw.pdf" 2>/dev/null
qpdf --stream-data=compress --recompress-flate --linearize \
  "$D/yaamava-partnership-print-gs.pdf" "$D/yaamava-partnership-print.pdf"
rm -f "$D/yaamava-partnership-print-raw.pdf" "$D/yaamava-partnership-print-gs.pdf"
echo "Done: $D/yaamava-partnership-print.pdf ($(du -h "$D/yaamava-partnership-print.pdf" | cut -f1))"
