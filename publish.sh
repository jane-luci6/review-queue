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
echo "Done. One push should trigger ONE Netlify production deploy."
echo "Site: https://startling-fudge-f9965f.netlify.app/"
echo ""
echo "If deploys show as Canceled:"
echo "  • Wait for the latest deploy to finish — do not push again right away."
echo "  • GitHub → jane-luci6/review-queue → Settings → Webhooks → only ONE hook to api.netlify.com"
echo "  • Netlify → Site → check you do not have two sites linked to this same repo."
echo "  • Use Deploys → Trigger deploy → Deploy project (main) on the newest commit."
