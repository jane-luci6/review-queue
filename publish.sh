#!/usr/bin/env bash
# Push LUCI review site → GitHub → Vercel auto-deploys.
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
echo "→ Building review site (sync + inline queue)…"
node scripts/build-stakeholder-review.mjs

cd "$ROOT"
# vercel.json + built site both live under the design-system dir; this covers them.
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
echo "Done. One push to main triggers ONE Vercel production deploy."
echo "Site: ${REVIEW_SITE_URL:-https://<your-project>.vercel.app/}"
echo ""
echo "Vercel project must be configured (one-time, in the dashboard):"
echo "  • Root Directory   = LUCI Systems Design System"
echo "  • Build Command    = npm run build:review   (or leave blank — vercel.json sets it)"
echo "  • Output Directory = ui_kits/review         (vercel.json sets it)"
echo "  • Storage          = Upstash Redis (Marketplace) connected → injects KV/UPSTASH env vars"
echo "  • Env var          = REVIEW_TEAMS_WEBHOOK_OWNER (Teams notifications)"
echo "  • Env var          = REVIEW_SITE_URL (your live Vercel URL, used in Teams links)"
echo ""
echo "If a deploy fails or is skipped:"
echo "  • Vercel → Project → Deployments → check the build log."
echo "  • Ensure only ONE Vercel project is linked to the review-queue repo."
echo "  • Comments/approvals need the Redis store connected to this project (Storage tab)."
