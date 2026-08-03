#!/usr/bin/env bash
# Sync the Customization Studio files from the luci-design repo to the
# shared OneDrive "Cursor Branding Files" folder.
#
# Run this after updating master templates, CSS, SKILL.md files, or assets
# in the luci-design repo. It copies only the files the Customization Studio
# needs — not the entire repo.
#
# Usage:
#   scripts/sync-to-onedrive.sh
#
# OneDrive destination:
#   ~/Library/CloudStorage/OneDrive-LUCISystems/Sales - Sales/Cursor Branding Files
#
set -e

SRC="$(cd "$(dirname "$0")/.." && pwd)"
DEST="${HOME}/Library/CloudStorage/OneDrive-LUCISystems/Sales - Sales/Cursor Branding Files"

if [ ! -d "$DEST" ]; then
  echo "OneDrive folder not found: $DEST" >&2
  echo "Make sure OneDrive is running and the 'Cursor Branding Files' folder exists." >&2
  exit 1
fi

echo "Syncing from: $SRC"
echo "Syncing to:   $DEST"
echo ""

# 1. Master templates + CSS (ui_kits/sales/)
echo "Copying master templates + CSS..."
for f in proposal.html proposal-luci-retrofit.html proposal-upgrade.html \
         budgetary-estimate.html capabilities-document.html scope-of-work.html \
         sales-deck.html _template-sales-document.html \
         sales-document.css capabilities-document.css brochure.css \
         budgetary-estimate.css proposal.css scope-of-work.css \
         sales-deck.css field-activation-guide-print.css; do
  cp "$SRC/ui_kits/sales/$f" "$DEST/ui_kits/sales/" 2>/dev/null && echo "  $f"
done

# 2. Sales-specific assets (ui_kits/sales/assets/)
echo ""
echo "Copying sales-specific assets..."
mkdir -p "$DEST/ui_kits/sales/assets"
cp -R "$SRC/ui_kits/sales/assets/"* "$DEST/ui_kits/sales/assets/" 2>/dev/null && echo "  assets/" || echo "  (no sales assets)"

# 3. Customization folder (ui_kits/internal-portal/customization/)
echo ""
echo "Copying customization instructions + dev server..."
cp -R "$SRC/ui_kits/internal-portal/customization/"* "$DEST/ui_kits/internal-portal/customization/" 2>/dev/null
rm -f "$DEST/ui_kits/internal-portal/customization/luci-dev-server.py.bak"
echo "  customization/"

# 3a. Portal index page (ui_kits/internal-portal/index.html)
echo ""
echo "Copying portal index page..."
mkdir -p "$DEST/ui_kits/internal-portal"
cp "$SRC/ui_kits/internal-portal/index.html" "$DEST/ui_kits/internal-portal/" 2>/dev/null && echo "  index.html"

# 4. Root assets (fonts, textures, logos, diagrams)
echo ""
echo "Copying root assets..."
mkdir -p "$DEST/assets/fonts" "$DEST/assets/textures" "$DEST/assets/logos" "$DEST/assets/diagrams"
cp -R "$SRC/assets/fonts/"* "$DEST/assets/fonts/" 2>/dev/null && echo "  fonts/"
cp -R "$SRC/assets/textures/"* "$DEST/assets/textures/" 2>/dev/null && echo "  textures/"
cp -R "$SRC/assets/logos/"* "$DEST/assets/logos/" 2>/dev/null && echo "  logos/"
cp -R "$SRC/assets/diagrams/"* "$DEST/assets/diagrams/" 2>/dev/null && echo "  diagrams/"

# 5. Scripts
echo ""
echo "Copying scripts..."
for f in render-pdf.sh prepare-client-doc.sh patch-sales-pdf-html.py prepare-sales-pdf-assets.py \
         create-client-workspace.sh post-commit-sync-onedrive.sh sync-to-onedrive.sh; do
  cp "$SRC/scripts/$f" "$DEST/scripts/" 2>/dev/null && echo "  $f"
done

# 5a. Python dependencies (requirements.txt)
cp "$SRC/requirements.txt" "$DEST/" 2>/dev/null && echo "  requirements.txt"

# NOTE: Client files (clients/) are NOT synced — they are working files
# managed separately in each environment.

# Clean up stale files that were deleted from the source repo but would
# otherwise linger in OneDrive from a previous sync.
rm -f "$DEST/ui_kits/internal-portal/customization/AGENTS.md"
find "$DEST/ui_kits/internal-portal/customization" -name "AGENTS.md" -delete 2>/dev/null

echo ""
echo "Sync complete."
echo "  OneDrive will sync to Mike's machine automatically."
du -sh "$DEST" | awk '{print "  Total size: " $1}'
