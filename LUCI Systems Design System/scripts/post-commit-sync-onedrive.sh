#!/usr/bin/env bash
# Post-commit hook: automatically sync customization studio files to the
# OneDrive "Cursor Branding Files" folder when master templates, CSS,
# assets, or SKILL.md files change.
#
# Install: copy this file to .git/hooks/post-commit and make it executable.
#   cp scripts/post-commit-sync-onedrive.sh .git/hooks/post-commit
#   chmod +x .git/hooks/post-commit

# Only run if the OneDrive folder exists.
ONEDRIVE="$HOME/Library/CloudStorage/OneDrive-LUCISystems/Sales - Sales/Cursor Branding Files"
if [ ! -d "$ONEDRIVE" ]; then
  exit 0
fi

# Check if any customization studio files changed in this commit.
CHANGED=$(git diff --name-only HEAD~1 HEAD 2>/dev/null | grep -E \
  '^LUCI Systems Design System/(ui_kits/sales/[^/]+\.html|ui_kits/sales/[^/]+\.css|ui_kits/internal-portal/customization/|assets/|scripts/(render-pdf|prepare-client-doc|patch-sales-pdf|prepare-sales-pdf))' \
  | head -1)

if [ -z "$CHANGED" ]; then
  exit 0
fi

echo "Customization Studio files changed — syncing to OneDrive..."

# Find the design system root.
ROOT="$(git rev-parse --show-toplevel)/LUCI Systems Design System"
if [ ! -d "$ROOT" ]; then
  ROOT="$(git rev-parse --show-toplevel)"
fi

# Run the sync script.
if [ -f "$ROOT/scripts/sync-to-onedrive.sh" ]; then
  bash "$ROOT/scripts/sync-to-onedrive.sh" > /dev/null 2>&1 && \
    echo "  Synced to OneDrive." || \
    echo "  Sync failed — run scripts/sync-to-onedrive.sh manually."
else
  echo "  sync-to-onedrive.sh not found — skipping."
fi
