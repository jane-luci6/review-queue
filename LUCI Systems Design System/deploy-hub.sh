#!/usr/bin/env bash
# Deploy the Internal Marketing Portal to production (.17).
#
# Canonical pipeline — same as:  npm run deploy:portal
#
# Production:  http://10.10.1.17:8081/internal-portal/index.html
#
# See: ui_kits/internal-portal/docs/deploy-17.md

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
exec "$SCRIPT_DIR/scripts/deploy-internal-portal-17.sh" "$@"
