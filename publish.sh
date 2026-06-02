#!/usr/bin/env bash
# Push LUCI review site → GitHub → Netlify auto-deploys.
# Usage:
#   ./publish.sh
#   ./publish.sh "Your commit message"
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
DS="$ROOT/LUCI Systems Design System"
MSG="${1:-Update review site and messaging docs}"

cd "$DS"
echo "→ Building review site (sync + inline queue)…"
node scripts/build-stakeholder-review.mjs

cd "$ROOT"
git add "LUCI Systems Design System/"

if git diff --staged --quiet; then
  echo "→ No file changes to commit."
else
  git commit -m "$MSG"
  echo "→ Committed."
fi

echo "→ Pushing to GitHub (origin main)…"
git push origin main

echo ""
echo "Done. Netlify builds from main automatically."
echo "Site: https://startling-fudge-f9965f.netlify.app/"
