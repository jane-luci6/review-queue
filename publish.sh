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
if [[ -f .env ]]; then
  set -a
  # shellcheck disable=SC1091
  source .env
  set +a
fi
echo "→ Building review site (sync + inline queue + Teams due-date notify)…"
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
echo "  • Netlify uses the GitHub App (not repo Webhooks tab): https://github.com/settings/installations"
echo "    → Netlify → Configure → review-queue listed once; no duplicate Netlify apps."
echo "  • Netlify → Site → Build & deploy → only ONE site linked to review-queue."
echo "  • Optional: turn off Deploy Previews if you only need production (main)."
echo "  • Manual fix: Deploys → Trigger deploy → Deploy project (main)."
