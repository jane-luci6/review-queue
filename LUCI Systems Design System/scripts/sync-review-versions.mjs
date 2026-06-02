#!/usr/bin/env node
/**
 * Keep reviewVersion + versionHistory in sync on dueForReview assets.
 * Jane bumps reviewVersion and optional versionNote; build appends history rows.
 */
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(path.join(__dirname, '..'));
const reviewDir = path.join(root, 'ui_kits', 'review');
const queuePath = path.join(reviewDir, 'review-queue.json');

export function currentReviewVersion(item) {
  const n = Number(item?.reviewVersion);
  return Number.isFinite(n) && n >= 1 ? Math.floor(n) : 1;
}

/**
 * @param {object} queue
 * @param {string} [filePath]
 * @returns {boolean} whether review-queue.json was written
 */
export function syncReviewVersions(queue, filePath = queuePath) {
  const today = new Date().toISOString().slice(0, 10);
  let changed = false;

  for (const item of queue.dueForReview || []) {
    const v = currentReviewVersion(item);
    if (item.reviewVersion !== v) {
      item.reviewVersion = v;
      changed = true;
    }

    const note = (item.versionNote || '').trim();
    const hist = Array.isArray(item.versionHistory) ? item.versionHistory.map((e) => ({ ...e })) : [];
    let entry = hist.find((e) => e.version === v);

    if (!entry) {
      entry = { version: v, published: today, note };
      hist.push(entry);
      hist.sort((a, b) => a.version - b.version);
      item.versionHistory = hist;
      changed = true;
    } else if (note && entry.note !== note) {
      entry.note = note;
      changed = true;
    }
  }

  if (changed && filePath) {
    queue.updated = today;
    fs.writeFileSync(filePath, JSON.stringify(queue, null, 2) + '\n');
  }

  return changed;
}

if (process.argv[1] && fileURLToPath(import.meta.url) === path.resolve(process.argv[1])) {
  const queue = JSON.parse(fs.readFileSync(queuePath, 'utf8'));
  const changed = syncReviewVersions(queue);
  console.log(changed ? 'Updated review-queue.json version history.' : 'Version history already in sync.');
}
