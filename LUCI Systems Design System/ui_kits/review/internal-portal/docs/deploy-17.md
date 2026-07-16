# Internal Marketing Portal — deployment pipeline

**Production:** [http://10.10.1.17:8081/internal-portal/index.html](http://10.10.1.17:8081/internal-portal/index.html)

This is the canonical deploy path for the Internal Marketing Portal.

---

## Quick deploy

From `LUCI Systems Design System/` on your Mac:

```bash
npm run deploy:portal
```

Hard-refresh after deploy: **Cmd+Shift+R**.

### SSH note

Deploy uses `user-007@10.10.1.17` with `~/.ssh/id_ed25519` (passphrase-protected). Run from **Terminal.app**. One-time, to avoid repeated passphrase prompts:

```bash
ssh-add --apple-use-keychain ~/.ssh/id_ed25519
```

---

## Test locally before deploying

There is no staging server. Preview on your Mac, then deploy to `.17` when ready:

```bash
npm run build:review
cd ui_kits/review && python3 -m http.server 8766
```

Open **http://localhost:8766/internal-portal/index.html**

Or edit `ui_kits/internal-portal/index.html` and use `npm run serve` (design-system root on `:8765`) if you're working on source files before a full review build.

---

## What the pipeline does

```
npm run deploy:portal
  └─ scripts/deploy-internal-portal-17.sh
       1. npm run build:review          → ui_kits/review/
       2. ssh mkdir remote content dir
       3. rsync ui_kits/review/         → .17:/home/user-007/internal-marketing-portal/
       4. normalize file permissions
       5. scripts/ensure-internal-portal-17-service.sh
            → Docker nginx on :8081 (container: internal_marketing_portal)
```

### Build output (`ui_kits/review/`)

- `internal-portal/index.html` — portal shell
- Review queue + library manifests
- Customization Studio preview HTML (capabilities, budget estimate, scope of work, LG guide)
- Sales docs, messaging docs, shared assets/PDFs

Secrets (`.env`) are **not** deployed — dotfiles are skipped when copying into the review bundle.

---

## Infrastructure on .17

| Item | Value |
|------|--------|
| Host | `10.10.1.17` |
| SSH user | `user-007` |
| Port | `8081` (wiki editor uses `:8080`) |
| Content path | `/home/user-007/internal-marketing-portal/` |
| Service path | `/home/user-007/internal-marketing-portal-service/` |
| Comments data | `/home/user-007/internal-marketing-portal-comments/` (survives `rsync --delete`) |
| Container | `internal_marketing_portal` (nginx:1.27-alpine) |
| Comments container | `internal_marketing_portal_comments` (python:3.12-alpine, `:8090` internal) |
| Compose file | `ui_kits/internal-portal/deploy/docker-compose.host.yml` |

`.17` has no `/var/www`. Content lives in `user-007`'s home directory; nginx runs in Docker.

## Comment/approval sync

Comments and approvals are stored server-side so Jane sees Mike/Mark's feedback from any browser:

- Portal JS calls same-origin `/api/comments` (GET / POST); nginx proxies to the `comments_api` container (`python:3.12-alpine`, `comments-api.py`, JSON-file store at `/data/comments.json`).
- `addComment` / `toggleApproval` POST to the API (optimistic local update + localStorage cache); `loadState` pulls server state and merges with the `SEED_*` baseline; a 30s poll + hashchange refresh keeps the list/detail live.
- If the API is unreachable (e.g. local `file://` preview), the portal falls back to `SEED_*` + localStorage as before.
- Archive live feedback to `ui_kits/review/review-comments.json`: `node scripts/pull-review-comments.mjs` (reads `commentsApiUrl` from `review-queue.json`).
- After editing `nginx.conf`, nginx must reload: `docker exec internal_marketing_portal nginx -s reload` (the deploy script scp's the config but does not force-recreate the running container).

---

## npm scripts

| Script | Target |
|--------|--------|
| `npm run deploy:portal` | Production — `.17:8081` |
| `npm run deploy:portal:17` | Same as `deploy:portal` (alias) |
| `npm run deploy:portal:17:docker` | Build Docker image locally (dev/test only) |

### Environment overrides

```bash
LUCI_DEPLOY_HOST=user-007@10.10.1.17 \
LUCI_DEPLOY_DIR=/home/user-007/internal-marketing-portal \
LUCI_DEPLOY_KEY=~/.ssh/id_ed25519 \
./scripts/deploy-internal-portal-17.sh
```

---

## Smoke test after deploy

- [ ] Home — quick actions, status strip
- [ ] Download materials — PDFs and links resolve
- [ ] Review Queue — assets open, comments work (localStorage)
- [ ] Customization Studio — capabilities, budget estimate, scope of work
- [ ] Messaging & Philosophy — doc links open

---

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| `Permission denied (publickey)` | Run from Terminal; `ssh-add --apple-use-keychain ~/.ssh/id_ed25519` |
| Stale content in browser | Hard-refresh (Cmd+Shift+R) |
| `Connection refused` on :8081 | Re-run deploy (restarts Docker service) or on .17: `docker ps` check `internal_marketing_portal` |
| Build OK, deploy fails mid-rsync | Check SSH; re-run `npm run deploy:portal` |

---

## Phase 2 (not in this pipeline yet)

- Server-backed review queue
- Wiki API search (`wiki-client.ts` — key in gitignored `.env`)
- Proposal API for Document Studio submissions

---

## Related files

- `scripts/deploy-internal-portal-17.sh` — main deploy script
- `scripts/ensure-internal-portal-17-service.sh` — Docker nginx service
- `scripts/build-stakeholder-review.mjs` — build step
- `ui_kits/internal-portal/deploy/nginx.conf` — container nginx config
