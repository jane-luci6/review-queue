/**
 * Resolves library-manifest.json against review-queue.json for stakeholder review site.
 */
import fs from 'fs';
import path from 'path';

function publishPreviewPath(item) {
  const hub = (item.hubPreviewPath || '').trim();
  if (hub) return hub.replace(/^ui_kits\//, '');
  const prev = (item.previewUrl || '').trim();
  if (!prev || /^https?:\/\//i.test(prev)) return '';
  return prev.replace(/^\.\.\//, '').replace(/^ui_kits\//, '');
}

function queueMap(queue) {
  const map = new Map();
  for (const list of [queue.approvedAssets, queue.dueForReview, queue.inProgress]) {
    for (const item of list || []) {
      if (item?.id) map.set(item.id, item);
    }
  }
  return map;
}

function approvedIds(queue) {
  return new Set((queue.approvedAssets || []).map((item) => item.id).filter(Boolean));
}

/**
 * @param {string} manifestPath
 * @param {object} queue
 * @returns {{ updated: string, groups: object[], byId: Record<string, object> }}
 */
export function buildLibrary(manifestPath, queue) {
  const manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf8'));
  const qMap = queueMap(queue);
  const approved = approvedIds(queue);
  const byId = {};
  const groups = [];

  for (const group of manifest.groups || []) {
    const items = [];
    for (const raw of group.items || []) {
      if (raw.comingSoon) {
        const entry = {
          id: raw.id,
          label: raw.label,
          note: raw.note || 'Coming soon',
          comingSoon: true,
        };
        items.push(entry);
        byId[raw.id] = entry;
        continue;
      }

      let entry = null;
      if (raw.queueId) {
        if (raw.whenApproved && !approved.has(raw.queueId)) continue;
        const qItem = qMap.get(raw.queueId);
        if (!qItem) continue;
        const preview = publishPreviewPath(qItem) || raw.path || '';
        entry = {
          id: raw.id,
          label: raw.label || qItem.title,
          path: preview.replace(/^\//, ''),
          liveUrl: (qItem.liveUrl || '').trim(),
          approved: qItem.approved || '',
          summary: qItem.summary || '',
          queueId: raw.queueId,
          downloads: raw.downloads || [],
        };
      } else if (raw.path) {
        entry = {
          id: raw.id,
          label: raw.label,
          path: raw.path.replace(/^\//, ''),
          liveUrl: (raw.liveUrl || '').trim(),
          downloads: raw.downloads || [],
          note: raw.note || '',
        };
      }

      if (entry) {
        items.push(entry);
        byId[raw.id] = entry;
      }
    }

    if (items.length) {
      groups.push({
        id: group.id,
        label: group.label,
        defaultOpen: group.defaultOpen !== false,
        items,
      });
    }
  }

  return {
    updated: manifest.updated || '',
    groups,
    byId,
  };
}

/**
 * Copy static library HTML paths into review dir when not already present.
 */
export function syncLibraryAssets(library, reviewDir, root, copyFns) {
  const { copyFile, copyLinkedAssets, rewritePreviewHtmlPaths, copied } = copyFns;
  let count = 0;

  for (const item of Object.values(library.byId)) {
    if (item.comingSoon || !item.path || item.liveUrl) continue;
    const rel = item.path.replace(/^\//, '');
    if (rel.startsWith('http')) continue;

    let srcHtml = path.join(reviewDir, rel);
    if (!fs.existsSync(srcHtml)) {
      const alt = path.join(root, 'ui_kits', 'review', rel);
      if (fs.existsSync(alt)) srcHtml = alt;
      else continue;
    }

    const destHtml = path.join(reviewDir, rel);
    if (!fs.existsSync(destHtml) || srcHtml !== destHtml) {
      copyFile(srcHtml, destHtml, copied);
    }
    copyLinkedAssets(srcHtml, destHtml, copied);
    rewritePreviewHtmlPaths(destHtml);
    count += 1;
  }

  for (const item of Object.values(library.byId)) {
    for (const dl of item.downloads || []) {
      const rel = (dl.path || '').replace(/^\//, '');
      if (!rel) continue;
      const src = fs.existsSync(path.join(reviewDir, rel))
        ? path.join(reviewDir, rel)
        : path.join(root, rel.replace(/^assets\//, 'assets/').replace(/^messaging\//, 'ui_kits/review/messaging/'));
      const candidates = [
        path.join(reviewDir, rel),
        path.join(root, rel),
        path.join(root, 'LUCI Systems Design System', rel),
      ];
      for (const c of candidates) {
        if (fs.existsSync(c)) {
          copyFile(c, path.join(reviewDir, rel), copied);
          break;
        }
      }
    }
  }

  return count;
}
