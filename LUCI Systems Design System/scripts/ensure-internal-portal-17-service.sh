#!/usr/bin/env bash
# One-time + ongoing: ensure nginx Docker service on .17 serves the rsync'd portal on :8081.
# Called automatically at the end of deploy-internal-portal-17.sh (rsync mode).

set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
HOST="${LUCI_DEPLOY_HOST:-user-007@10.10.1.17}"
PORTAL_DIR="${LUCI_DEPLOY_DIR:-/home/user-007/internal-marketing-portal}"
SERVICE_DIR="${LUCI_PORTAL_SERVICE_DIR:-/home/user-007/internal-marketing-portal-service}"
COMMENTS_DIR="${LUCI_PORTAL_COMMENTS_DIR:-/home/user-007/internal-marketing-portal-comments}"
SSH_OPTS=(-o StrictHostKeyChecking=accept-new -o ConnectTimeout=15)
if [ -n "${LUCI_DEPLOY_KEY:-}" ]; then
  SSH_OPTS+=(-i "${LUCI_DEPLOY_KEY/#\~/$HOME}")
fi

echo "Ensuring portal service on ${HOST} (:8081)…"

ssh "${SSH_OPTS[@]}" "$HOST" "mkdir -p '${PORTAL_DIR}' '${SERVICE_DIR}' '${COMMENTS_DIR}'"

scp "${SSH_OPTS[@]}" \
  "$ROOT/ui_kits/internal-portal/deploy/nginx.conf" \
  "$ROOT/ui_kits/internal-portal/deploy/docker-compose.host.yml" \
  "$ROOT/ui_kits/internal-portal/deploy/comments-api.py" \
  "${HOST}:${SERVICE_DIR}/"

ssh "${SSH_OPTS[@]}" "$HOST" bash -s <<REMOTE
set -euo pipefail
cd '${SERVICE_DIR}'
export PORTAL_CONTENT_DIR='${PORTAL_DIR}'
export PORTAL_COMMENTS_DIR='${COMMENTS_DIR}'
docker compose -f docker-compose.host.yml up -d --remove-orphans
# nginx.conf is a bind mount; compose won't recreate the running container when only the
# mounted file changed, so reload nginx to pick up any proxy/server edits.
docker exec internal_marketing_portal nginx -t
docker exec internal_marketing_portal nginx -s reload || true
docker compose -f docker-compose.host.yml ps
REMOTE

HOST_IP="${HOST#*@}"
echo ""
echo "Portal service: http://${HOST_IP}:8081/internal-portal/index.html"
