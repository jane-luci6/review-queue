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
import {
  transformMessagingBody,
  buildResourcePage,
  extractStoredBody,
} from './transform-messaging-html.mjs';

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

function libraryFromConfig(config, manifest = { docs: [] }) {
  return (config.docs || []).map((d) => {
    const m = (manifest.docs || []).find((x) => x.id === d.id);
    return {
      id: d.id,
      title: d.title,
      url: `messaging/${d.id}.html`,
      note: m?.sourceModified
        ? 'Updated ' +
          new Date(m.sourceModified).toLocaleDateString('en-US', {
            month: 'short',
            day: 'numeric',
            year: 'numeric',
          })
        : '',
    };
  });
}

function publishDoc({ docId, rawBody, libraryDocs, updatedIso, fallbackTitle }) {
  const { title, deck, bodyHtml, tocHtml } = transformMessagingBody(rawBody);
  return buildResourcePage({
    docId,
    title: title || fallbackTitle,
    deck,
    bodyHtml,
    tocHtml,
    libraryDocs,
    updatedIso,
  });
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

  let priorManifest = { updated: new Date().toISOString().slice(0, 10), docs: [] };
  if (fs.existsSync(manifestPath)) {
    priorManifest = JSON.parse(fs.readFileSync(manifestPath, 'utf8'));
  }

  const manifest = { updated: new Date().toISOString().slice(0, 10), docs: [] };
  let synced = 0;
  let skipped = 0;
  let reprocessed = 0;

  for (const doc of config.docs || []) {
    const publishPath = `/messaging/${doc.id}.html`;
    const destHtml = path.join(messagingDir, `${doc.id}.html`);
    const sourceDocx = path.join(docsRoot, doc.file);
    let rawBody = null;
    let updatedIso = new Date().toISOString();
    let sourceModified = null;

    if (fs.existsSync(sourceDocx)) {
      const tmpHtml = path.join(messagingDir, `.tmp-${doc.id}.html`);
      try {
        convertDocx(sourceDocx, tmpHtml);
        const raw = fs.readFileSync(tmpHtml, 'utf8');
        rawBody = extractBody(raw);
        sourceModified = fs.statSync(sourceDocx).mtime;
        updatedIso = sourceModified.toISOString();
        fs.unlinkSync(tmpHtml);
        synced += 1;
        if (!quiet) console.log('Messaging doc:', publishPath);
      } catch (err) {
        if (fs.existsSync(tmpHtml)) fs.unlinkSync(tmpHtml);
        console.error('Failed to convert', doc.file, err.message || err);
        process.exit(1);
      }
    } else if (fs.existsSync(destHtml)) {
      const stored = extractStoredBody(fs.readFileSync(destHtml, 'utf8'));
      if (/<p class="p2">/i.test(stored)) {
        rawBody = stored;
        const stat = fs.statSync(destHtml);
        updatedIso = stat.mtime.toISOString();
        const prior = priorManifest.docs?.find((x) => x.id === doc.id);
        sourceModified = prior?.sourceModified || null;
        reprocessed += 1;
        if (!quiet) console.log('Reprocessed committed HTML:', publishPath);
      } else {
        const stat = fs.statSync(destHtml);
        manifest.docs.push({
          id: doc.id,
          title: doc.title,
          url: publishPath,
          sourceModified: priorManifest.docs?.find((x) => x.id === doc.id)?.sourceModified || null,
          htmlModified: stat.mtime.toISOString(),
        });
        skipped += 1;
        continue;
      }
    } else {
      if (!quiet) console.warn('Source missing (no HTML):', sourceDocx);
      skipped += 1;
      continue;
    }

    const libraryDocs = libraryFromConfig(config, priorManifest);
    const wrapped = publishDoc({
      docId: doc.id,
      rawBody,
      libraryDocs,
      updatedIso,
      fallbackTitle: doc.title,
    });
    fs.writeFileSync(destHtml, wrapped);

    manifest.docs.push({
      id: doc.id,
      title: doc.title,
      url: publishPath,
      sourceModified: sourceModified ? sourceModified.toISOString() : null,
      htmlModified: new Date().toISOString(),
    });
  }

  const libraryDocs = libraryFromConfig(config, manifest);
  fs.writeFileSync(manifestPath, JSON.stringify(manifest, null, 2) + '\n');

  return { synced, skipped, reprocessed, manifest };
}

export function applyMessagingDocsToQueue(queue) {
  if (!fs.existsSync(manifestPath)) return queue;
  const manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf8'));
  queue.messagingDocs = (manifest.docs || []).map((d) => ({
    title: d.title,
    url: (d.url || '').replace(/^\//, ''),
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
  console.log(
    'Synced',
    result.synced,
    'doc(s); reprocessed',
    result.reprocessed,
    ';',
    result.skipped,
    'skipped.'
  );
  console.log('Wrote', manifestPath);
}
