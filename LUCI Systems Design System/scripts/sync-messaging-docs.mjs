#!/usr/bin/env node
/**
 * Sync messaging / philosophy / persona Word docs → HTML in ui_kits/review/messaging/
 * Run locally after OneDrive docs change (or from build when sources are available).
 *
 *   node scripts/sync-messaging-docs.mjs
 */
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { execFileSync } from 'child_process';
import os from 'os';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(path.join(__dirname, '..'));
const reviewDir = path.join(root, 'ui_kits', 'review');
const messagingDir = path.join(reviewDir, 'messaging');
const sourcesPath = path.join(reviewDir, 'messaging-sources.json');
const manifestPath = path.join(reviewDir, 'messaging-manifest.json');

function expandHome(p) {
  return p.replace(/^~(?=$|\/)/, os.homedir());
}

function extractBody(html) {
  const m = html.match(/<body[^>]*>([\s\S]*)<\/body>/i);
  return m ? m[1].trim() : html;
}

const SHELL_HEAD = `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="robots" content="noindex, nofollow">
  <title>{{TITLE}} · LUCI</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Syncopate:wght@700&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: 'Space Grotesk', 'Trebuchet MS', sans-serif;
      font-size: 17px;
      line-height: 1.65;
      color: #354F5C;
      background: #F5F8FA;
      -webkit-font-smoothing: antialiased;
    }
    .doc { max-width: 52rem; margin: 0 auto; background: #fff; border-left: 1px solid #D4D9DC; border-right: 1px solid #D4D9DC; min-height: 100vh; }
    .doc__bar {
      background: #10232D;
      padding: 14px clamp(20px, 4vw, 40px);
      border-bottom: 4px solid #68E3BE;
    }
    .doc__back {
      font-family: 'Syncopate', sans-serif;
      font-size: 10px;
      font-weight: 700;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: #68E3BE;
      text-decoration: none;
    }
    .doc__back:hover { text-decoration: underline; }
    .doc__meta {
      font-size: 12px;
      color: rgba(235, 245, 248, 0.75);
      margin-top: 8px;
    }
    .doc__body {
      padding: clamp(24px, 4vw, 40px);
    }
    .doc__body b, .doc__body strong { font-weight: 600; color: #10232D; }
    .doc__body p { margin: 0 0 14px; max-width: 68ch; }
    .doc__body p:empty { display: none; }
    .doc__body ul, .doc__body ol { margin: 0 0 14px 1.25rem; max-width: 68ch; }
    .doc__body li { margin-bottom: 6px; }
    .doc__body table { width: 100%; border-collapse: collapse; margin-bottom: 20px; font-size: 15px; }
    .doc__body td, .doc__body th { border: 1px solid #D4D9DC; padding: 10px 12px; text-align: left; vertical-align: top; }
    .doc__body h1, .doc__body h2, .doc__body h3,
    .doc__body p.p2 b, .doc__body p.p5 b, .doc__body p.p24 b {
      font-family: 'Space Grotesk', sans-serif;
      font-weight: 700;
      color: #10232D;
      margin: 28px 0 12px;
      letter-spacing: -0.02em;
    }
    .doc__body p.p2 b { font-size: clamp(22px, 4vw, 28px); display: block; margin-top: 0; }
    .doc__body p.p3, .doc__body p.p19, .doc__body p.p21 { font-size: 14px; color: #49616E; }
  </style>
</head>
<body>
  <div class="doc">
    <header class="doc__bar">
      <a class="doc__back" href="/">← Review queue</a>
      <p class="doc__meta">Synced {{UPDATED}}</p>
    </header>
    <div class="doc__body">
`;

const SHELL_TAIL = `
    </div>
  </div>
</body>
</html>
`;

function wrapDocument(title, bodyHtml, updatedIso) {
  const updatedLabel = new Date(updatedIso).toLocaleString('en-US', {
    month: 'short',
    day: 'numeric',
    year: 'numeric',
    hour: 'numeric',
    minute: '2-digit',
  });
  return (
    SHELL_HEAD.replace('{{TITLE}}', title).replace('{{UPDATED}}', updatedLabel) +
    bodyHtml +
    SHELL_TAIL
  );
}

function convertDocx(docxPath, tmpHtml) {
  execFileSync('textutil', ['-convert', 'html', '-output', tmpHtml, docxPath], { stdio: 'pipe' });
}

export function syncMessagingDocs(options = {}) {
  const { quiet = false } = options;
  if (!fs.existsSync(sourcesPath)) {
    console.error('Missing', sourcesPath);
    process.exit(1);
  }

  const config = JSON.parse(fs.readFileSync(sourcesPath, 'utf8'));
  const docsRoot = expandHome(config.oneDriveRoot || '');
  fs.mkdirSync(messagingDir, { recursive: true });

  const manifest = { updated: new Date().toISOString().slice(0, 10), docs: [] };
  let synced = 0;
  let skipped = 0;

  for (const doc of config.docs || []) {
    const publishPath = `/messaging/${doc.id}.html`;
    const destHtml = path.join(messagingDir, `${doc.id}.html`);
    const sourceDocx = path.join(docsRoot, doc.file);

    if (!fs.existsSync(sourceDocx)) {
      if (!quiet) console.warn('Source missing (using committed HTML if any):', sourceDocx);
      if (fs.existsSync(destHtml)) {
        const stat = fs.statSync(destHtml);
        manifest.docs.push({
          id: doc.id,
          title: doc.title,
          url: publishPath,
          sourceModified: null,
          htmlModified: stat.mtime.toISOString(),
        });
      }
      skipped += 1;
      continue;
    }

    const tmpHtml = path.join(messagingDir, `.tmp-${doc.id}.html`);
    try {
      convertDocx(sourceDocx, tmpHtml);
      const raw = fs.readFileSync(tmpHtml, 'utf8');
      const body = extractBody(raw);
      const sourceMtime = fs.statSync(sourceDocx).mtime;
      const wrapped = wrapDocument(doc.title, body, sourceMtime.toISOString());
      fs.writeFileSync(destHtml, wrapped);
      fs.unlinkSync(tmpHtml);

      manifest.docs.push({
        id: doc.id,
        title: doc.title,
        url: publishPath,
        sourceModified: sourceMtime.toISOString(),
        htmlModified: new Date().toISOString(),
      });
      synced += 1;
      if (!quiet) console.log('Messaging doc:', publishPath);
    } catch (err) {
      if (fs.existsSync(tmpHtml)) fs.unlinkSync(tmpHtml);
      console.error('Failed to convert', doc.file, err.message || err);
      process.exit(1);
    }
  }

  fs.writeFileSync(manifestPath, JSON.stringify(manifest, null, 2) + '\n');

  return { synced, skipped, manifest };
}

export function applyMessagingDocsToQueue(queue) {
  if (!fs.existsSync(manifestPath)) return queue;
  const manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf8'));
  queue.messagingDocs = (manifest.docs || []).map((d) => ({
    title: d.title,
    url: d.url,
    note: d.sourceModified
      ? 'Updated ' + new Date(d.sourceModified).toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' })
      : '',
  }));
  queue.messagingDocsUpdated = manifest.updated;
  return queue;
}

const isMain =
  process.argv[1] && fileURLToPath(import.meta.url) === path.resolve(process.argv[1]);
if (isMain) {
  const result = syncMessagingDocs();
  console.log('Synced', result.synced, 'doc(s);', result.skipped, 'skipped (missing source).');
  console.log('Wrote', manifestPath);
}
