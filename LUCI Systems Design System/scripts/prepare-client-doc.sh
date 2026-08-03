#!/usr/bin/env bash
# Copy a sales document template (or existing client file) to the top-level
# clients/ folder and adjust all relative paths so CSS, fonts, textures, logos,
# and diagrams resolve correctly from the new location.
#
# Usage:
#   scripts/prepare-client-doc.sh <template-or-source.html> <client-file-name.html>
#
# Example:
#   scripts/prepare-client-doc.sh ui_kits/sales/proposal-luci-retrofit.html clients/ameristar-blackhawk-proposal-luci-retrofit.html
#
# Path adjustments (ui_kits/sales/ → clients/):
#   ../../assets/...        → ../assets/...          (root assets: fonts, textures)
#   ../../index.html        → ../index.html          (hub link)
#   href="X.css"            → href="../ui_kits/sales/X.css"  (same-folder CSS)
#   src="assets/...         → src="../ui_kits/sales/assets/...  (sales-specific assets)
#   url('../../assets/...') → url('../assets/...')   (inline CSS url() to root assets)
#
set -e

if [ "$#" -lt 2 ]; then
  echo "Usage: $0 <source.html> <output.html>" >&2
  exit 64
fi

src="$1"
out="$2"

ROOT="$(cd "$(dirname "$0")/.." && pwd)"

# Resolve source relative to ROOT.
src_abs="$ROOT/$src"
if [ ! -f "$src_abs" ]; then
  echo "Source not found: $src_abs" >&2
  exit 1
fi

out_abs="$ROOT/$out"
mkdir -p "$(dirname "$out_abs")"

# Copy and adjust paths in one pass.
# Order matters: do the specific CSS replacements before the generic ones.
sed \
  -e 's|href="sales-document\.css|href="../ui_kits/sales/sales-document.css|g' \
  -e 's|href="capabilities-document\.css|href="../ui_kits/sales/capabilities-document.css|g' \
  -e 's|href="brochure\.css|href="../ui_kits/sales/brochure.css|g' \
  -e 's|href="budgetary-estimate\.css|href="../ui_kits/sales/budgetary-estimate.css|g' \
  -e 's|href="proposal\.css|href="../ui_kits/sales/proposal.css|g' \
  -e 's|href="scope-of-work\.css|href="../ui_kits/sales/scope-of-work.css|g' \
  -e 's|href="led-upgrade\.css|href="../ui_kits/sales/led-upgrade.css|g' \
  -e 's|src="assets/|src="../ui_kits/sales/assets/|g' \
  -e "s|url('../../assets/|url('../assets/|g" \
  -e 's|../../assets/|../assets/|g' \
  -e 's|../../index\.html|../index.html|g' \
  "$src_abs" > "$out_abs"

echo "Created: $out"
echo "  Source:  $src"
echo "  Output:  $out"
