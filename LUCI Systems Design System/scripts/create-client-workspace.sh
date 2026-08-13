#!/usr/bin/env bash
# Create a client working folder at ~/Desktop/LUCI Docs/<client-name>/
# with symlinks to the OneDrive "Cursor Branding Files" folder for CSS,
# assets, and scripts — so the dev server runs locally but reads shared
# files from OneDrive. Only clients/ is a real directory (edits happen
# there, never in OneDrive).
#
# Usage:
#   scripts/create-client-workspace.sh <client-name> <template-name> <doc-type>
#
# Example:
#   scripts/create-client-workspace.sh "Ameristar Black Hawk" proposal-luci-retrofit proposal-luci-retrofit
#
# This creates:
#   ~/Desktop/LUCI Docs/ameristar-black-hawk/
#     clients/ameristar-black-hawk-proposal-luci-retrofit.html  ← the working file
#     ui_kits/  → symlink to OneDrive/ui_kits/
#     assets/   → symlink to OneDrive/assets/
#     scripts/  → symlink to OneDrive/scripts/
#
set -e

if [ "$#" -lt 3 ]; then
  echo "Usage: $0 <client-name> <template-name> <doc-type>" >&2
  echo "Example: $0 \"Ameristar Black Hawk\" proposal-luci-retrofit proposal-luci-retrofit" >&2
  exit 64
fi

CLIENT_NAME="$1"
TEMPLATE_NAME="$2"
DOC_TYPE="$3"

# Convert client name to kebab-case for the folder and filename
CLIENT_SLUG=$(echo "$CLIENT_NAME" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9]+/-/g' | sed 's/^-//;s/-$//')
# Handle spaces and special chars more robustly
CLIENT_SLUG=$(echo "$CLIENT_NAME" | tr '[:upper:]' '[:lower:]' | tr ' ' '-' | tr -cd 'a-z0-9-' | sed 's/--*/-/g' | sed 's/^-//;s/-$//')

# Find the OneDrive "Cursor Branding Files" folder
ONEDRIVE=""
for candidate in \
  "$HOME/Library/CloudStorage/OneDrive-LUCISystems/Sales - Sales/Cursor Branding Files" \
  "$HOME/Library/CloudStorage/OneDrive-LUCISystems/Cursor Branding Files" \
  "$HOME/Library/CloudStorage/OneDrive/Cursor Branding Files"; do
  if [ -d "$candidate" ]; then
    ONEDRIVE="$candidate"
    break
  fi
done

if [ -z "$ONEDRIVE" ]; then
  echo "Error: OneDrive 'Cursor Branding Files' folder not found." >&2
  echo "Checked:" >&2
  echo "  ~/Library/CloudStorage/OneDrive-LUCISystems/Sales - Sales/Cursor Branding Files" >&2
  echo "  ~/Library/CloudStorage/OneDrive-LUCISystems/Cursor Branding Files" >&2
  echo "  ~/Library/CloudStorage/OneDrive/Cursor Branding Files" >&2
  exit 1
fi

# Template source in OneDrive. Word (.docx) masters take precedence over .html
# masters of the same name — the MPSA and other legal docs are .docx, while the
# sales/proposal/SOW templates are .html.
TEMPLATE_DIR="$ONEDRIVE/ui_kits/sales"
TEMPLATE=""
TEMPLATE_EXT=""
for ext in docx html; do
  cand="$TEMPLATE_DIR/${TEMPLATE_NAME}.${ext}"
  if [ -f "$cand" ]; then
    TEMPLATE="$cand"
    TEMPLATE_EXT="$ext"
    break
  fi
done
if [ -z "$TEMPLATE" ]; then
  echo "Error: Template not found: $TEMPLATE_DIR/${TEMPLATE_NAME}.<docx|html>" >&2
  echo "Available templates:" >&2
  ls "$TEMPLATE_DIR"/*.html "$TEMPLATE_DIR"/*.docx 2>/dev/null \
    | sed 's|.*/||;s|\.\(html\|docx\)$||' | sort -u | sed 's/^/  /' >&2
  exit 1
fi

# Create the working folder
WORKSPACE="$HOME/Desktop/LUCI Docs/$CLIENT_SLUG"
mkdir -p "$WORKSPACE/clients"

# Create symlinks to OneDrive (overwrite if they already exist)
ln -sfn "$ONEDRIVE/ui_kits" "$WORKSPACE/ui_kits"
ln -sfn "$ONEDRIVE/assets" "$WORKSPACE/assets"
ln -sfn "$ONEDRIVE/scripts" "$WORKSPACE/scripts"

# Copy the master template to the working folder and adjust paths.
# Do this inline (not via prepare-client-doc.sh) because prepare-client-doc.sh
# resolves paths relative to its own location (OneDrive), not the workspace.
# .docx masters are copied verbatim — their asset refs live inside the zip,
# so the HTML path-rewriting sed below does not apply.
CLIENT_FILE="${CLIENT_SLUG}-${DOC_TYPE}.${TEMPLATE_EXT}"
WORKING_FILE="$WORKSPACE/clients/$CLIENT_FILE"

cp "$TEMPLATE" "$WORKING_FILE"

if [ "$TEMPLATE_EXT" = "html" ]; then
  sed -i '' \
    -e 's|href="sales-document\.css|href="../ui_kits/sales/sales-document.css|g' \
    -e 's|href="capabilities-document\.css|href="../ui_kits/sales/capabilities-document.css|g' \
    -e 's|href="brochure\.css|href="../ui_kits/sales/brochure.css|g' \
    -e 's|href="budgetary-estimate\.css|href="../ui_kits/sales/budgetary-estimate.css|g' \
    -e 's|href="proposal\.css|href="../ui_kits/sales/proposal.css|g' \
    -e 's|href="scope-of-work\.css|href="../ui_kits/sales/scope-of-work.css|g' \
    -e 's|href="sales-deck\.css|href="../ui_kits/sales/sales-deck.css|g' \
    -e 's|href="led-upgrade\.css|href="../ui_kits/sales/led-upgrade.css|g' \
    -e 's|href="field-activation-guide-print\.css|href="../ui_kits/sales/field-activation-guide-print.css|g' \
    -e 's|src="assets/|src="../ui_kits/sales/assets/|g' \
    -e "s|url('../../assets/|url('../assets/|g" \
    -e 's|../../assets/|../assets/|g' \
    -e 's|../../index\.html|../index.html|g' \
    "$WORKING_FILE"
fi

echo "Created workspace: $WORKSPACE"
echo "  Client file:  clients/$CLIENT_FILE"
echo "  Full path:    $WORKING_FILE"
echo ""
if [ "$TEMPLATE_EXT" = "docx" ]; then
  echo "To fill the blanks from Mike's proposal:"
  echo "  python3 scripts/fill-mpsa.py --out \"$WORKING_FILE\" --client \"...\" --effective-date \"...\" \\"
  echo "    --client-entity \"...\" --client-address \"...\" --facility \"...\" --notice-address \"...\" \\"
  echo "    --luci-signer \"...\" --luci-title \"...\" --customer-signer \"...\" --customer-title \"...\""
  echo "  (see ui_kits/internal-portal/customization/mpsa/SKILL.md for the blank map)"
  echo ""
fi
echo "To start the dev server:"
echo "  cd \"$WORKSPACE\" && python3 ui_kits/internal-portal/customization/luci-dev-server.py"
echo ""
echo "Preview URL:"
echo "  http://127.0.0.1:8771/clients/$CLIENT_FILE"
if [ "$TEMPLATE_EXT" = "docx" ]; then
  echo "  (.docx is rendered as an HTML preview; add ?download=1 for the raw Word file)"
fi
