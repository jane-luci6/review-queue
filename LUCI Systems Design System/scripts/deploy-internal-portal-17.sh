#!/usr/bin/env bash
# Build and deploy the Internal Marketing Portal to .17 (production).
#
# Production: http://10.10.1.17:8081/internal-portal/index.html
#
# Usage:
#   ./scripts/deploy-internal-portal-17.sh              # rsync (default)
#   ./scripts/deploy-internal-portal-17.sh --docker     # build image locally
#   ./scripts/deploy-internal-portal-17.sh --docker-push  # build + save tarball for .17
#
# SSH: user-007@10.10.1.17 with ~/.ssh/id_ed25519 (passphrase-protected).
# Run once so deploys don't prompt every time:
#   ssh-add --apple-use-keychain ~/.ssh/id_ed25519
# Or run deploy from your Mac Terminal after a successful `ssh user-007@10.10.1.17`.
#
# Rsync overrides:
#   LUCI_DEPLOY_HOST=user-007@10.10.1.17
#   LUCI_DEPLOY_PORT=8081
#   LUCI_DEPLOY_DIR=/home/user-007/internal-marketing-portal
#   LUCI_DEPLOY_KEY=~/.ssh/id_ed25519   # optional; omit to use ssh-agent/default keys
#
# Requires: npm, rsync, ssh (rsync mode); docker (docker modes)

set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
MODE="${1:-rsync}"

HOST="${LUCI_DEPLOY_HOST:-user-007@10.10.1.17}"
PORT="${LUCI_DEPLOY_PORT:-8081}"
REMOTE_DIR="${LUCI_DEPLOY_DIR:-/home/user-007/internal-marketing-portal}"
IMAGE="${LUCI_PORTAL_IMAGE:-internal-marketing-portal:latest}"

# No BatchMode — allows macOS keychain / ssh-agent with passphrase-backed keys.
SSH_OPTS=(-o StrictHostKeyChecking=accept-new -o ConnectTimeout=15)
if [ -n "${LUCI_DEPLOY_KEY:-}" ]; then
  SSH_OPTS+=(-i "${LUCI_DEPLOY_KEY/#\~/$HOME}")
fi

cd "$ROOT"
echo "Building portal (ui_kits/review/)…"
npm run build:review

case "$MODE" in
  rsync)
    REMOTE_PATH="${REMOTE_DIR%/}/"
    echo "Ensuring remote content directory exists…"
    ssh "${SSH_OPTS[@]}" "$HOST" "mkdir -p '${REMOTE_PATH}'"

    echo "Syncing ui_kits/review/ → ${HOST}:${REMOTE_PATH}"
    rsync -avz --delete -e "ssh ${SSH_OPTS[*]}" "$ROOT/ui_kits/review/" "${HOST}:${REMOTE_PATH}"

    echo "Normalizing permissions…"
    ssh "${SSH_OPTS[@]}" "$HOST" "find '${REMOTE_PATH}' -type f ! -perm -004 -exec chmod a+r {} +" \
      || echo "  warning: permission normalization could not run — check ssh access."

    bash "$ROOT/scripts/ensure-internal-portal-17-service.sh"

    HOST_IP="${HOST#*@}"
    echo ""
    echo "Deploy complete (rsync)."
    echo "  Portal:  http://${HOST_IP}:${PORT}/"
    echo "  Direct:  http://${HOST_IP}:${PORT}/internal-portal/index.html"

    echo ""
    echo "Verifying portal is live…"
    PORTAL_URL="http://${HOST_IP}:${PORT}/internal-portal/index.html"
    sleep 1
    HTTP_CODE="$(curl -s -o /dev/null -w "%{http_code}" --max-time 10 "$PORTAL_URL" || true)"
    if [[ "$HTTP_CODE" == "200" ]]; then
      echo "[LIVE + VERIFIED] HTTP 200 at $PORTAL_URL"
      echo "  Hard-refresh in your browser: Cmd+Shift+R"
    else
      echo "[WARNING] Deploy finished but portal URL returned HTTP ${HTTP_CODE:-(no response)}."
      echo "  Re-run this script and hard-refresh (Cmd+Shift+R) before debugging."
    fi
    ;;

  --docker)
    echo "Building Docker image ${IMAGE}…"
    docker build -f ui_kits/internal-portal/deploy/Dockerfile -t "$IMAGE" .
    echo ""
    echo "Image ready. Run locally:"
    echo "  docker run --rm -p 8081:8081 ${IMAGE}"
    echo "  open http://localhost:8081/internal-portal/index.html"
    ;;

  --docker-push)
    echo "Building Docker image ${IMAGE}…"
    docker build -f ui_kits/internal-portal/deploy/Dockerfile -t "$IMAGE" .
    TARBALL="${ROOT}/.texcheck/internal-marketing-portal-image.tar"
    mkdir -p "$(dirname "$TARBALL")"
    docker save -o "$TARBALL" "$IMAGE"
    echo ""
    echo "Saved image to ${TARBALL}"
    echo "On .17: docker load -i internal-marketing-portal-image.tar"
    echo "        docker compose -f ui_kits/internal-portal/deploy/docker-compose.yml up -d"
    ;;

  *)
    echo "Unknown mode: $MODE" >&2
    echo "Usage: $0 [rsync|--docker|--docker-push]" >&2
    exit 1
    ;;
esac
