#!/usr/bin/env node
/**
 * Pull live comments/approvals from the review API into review-comments.json
 * (local Cursor archive) so feedback is captured outside the portal.
 *
 * Usage:
 *   node scripts/pull-review-comments.mjs
 *   COMMENTS_API_URL=http://10.10.1.17:8081/api/comments node scripts/pull-review-comments.mjs
 *
 * If COMMENTS_API_URL is not set, falls back to `commentsApiUrl` in review-queue.json.
 */
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const root = path.join(__dirname, '..');
const reviewDir = path.join(root, 'ui_kits', 'review');
const queue = JSON.parse(fs.readFileSync(path.join(reviewDir, 'review-queue.json'), 'utf8'));
const apiUrl = (process.env.COMMENTS_API_URL || queue.commentsApiUrl || '').trim();

if (!apiUrl) {
  console.error('Set COMMENTS_API_URL or commentsApiUrl in review-queue.json');
  process.exit(1);
}

const res = await fetch(apiUrl);
if (!res.ok) {
  console.error('Fetch failed', res.status, await res.text());
  process.exit(1);
}
const data = await res.json();
const out = {
  updated: new Date().toISOString().slice(0, 10),
  note: 'Synced from live review API',
  comments: data.comments || [],
  approvals: data.approvals || {},
};
fs.writeFileSync(path.join(reviewDir, 'review-comments.json'), JSON.stringify(out, null, 2) + '\n');
console.log('Saved', out.comments.length, 'comments +', Object.keys(out.approvals).length, 'approvals to review-comments.json');
