# Wiki API agent key (Jane)

**Minted by:** William Morse  
**For:** Internal Marketing Portal server (wiki search + article reads)  
**Not for:** Document Studio (does not call the Wiki API)

## What this key can do

- Search the wiki — `POST /api/v1/search`
- Read articles in **KB**, **SD**, **LS**, **JIRA-CLIENT-SAFE**
- Get article details, breadcrumbs, and related articles

## What this key cannot do

- Write to the wiki (no `propose` action)
- Access **JIRA-INTERNAL** (internal-only tickets)
- Merge proposals (Pillar C safety — agents never merge)

## Where the key lives

| File | Purpose |
|------|---------|
| `.env` | Local secret (gitignored) — `WIKI_API_URL`, `WIKI_AGENT_KEY` |
| `.env.example` | Template for other devs / CI — no real key |

## Usage (server-side)

```typescript
// internal-marketing-portal/src/wiki-client.ts
const WIKI_API = process.env.WIKI_API_URL;
const AGENT_KEY = process.env.WIKI_AGENT_KEY;

const resp = await fetch(`${WIKI_API}/api/v1/search`, {
  method: 'POST',
  headers: {
    Authorization: `Bearer ${AGENT_KEY}`,
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({ query: 'product features', top_k: 10 }),
});
```

## Key endpoints

Interactive docs: `http://10.10.1.17:8000/docs`

| Endpoint | Method | What it does |
|----------|--------|-------------|
| `/api/v1/search` | POST | Search wiki content |
| `/api/v1/articles/{slug}` | GET | Get article by slug |
| `/api/v1/articles` | GET | List articles with filters |
| `/api/v1/spaces` | GET | List spaces |

## Security

- Do not commit the key to git or paste in public chat
- Key is shown once at mint time — if lost, ask Will to revoke and re-mint
- Scoped read-only key limits risk if compromised
