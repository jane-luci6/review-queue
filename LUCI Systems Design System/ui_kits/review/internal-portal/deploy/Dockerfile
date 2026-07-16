# Internal Marketing Portal — Phase 1 static deploy (.17 :8081)
#
# Build from LUCI Systems Design System root (after npm run build:review):
#   docker build -f ui_kits/internal-portal/deploy/Dockerfile -t internal-marketing-portal .
#   docker run --rm -p 8081:8081 internal-marketing-portal

FROM nginx:1.27-alpine

COPY ui_kits/internal-portal/deploy/nginx.conf /etc/nginx/conf.d/default.conf
COPY ui_kits/review/ /usr/share/nginx/html/

EXPOSE 8081

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD wget -q -O /dev/null http://127.0.0.1:8081/internal-portal/index.html || exit 1
