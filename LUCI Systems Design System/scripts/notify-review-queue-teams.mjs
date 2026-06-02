#!/usr/bin/env node
/**
 * Notify Mike/Nick in Teams when review due dates or asset versions change.
 * Run from build-stakeholder-review.mjs; requires REVIEW_TEAMS_WEBHOOK_STAKEHOLDERS.
 */
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import {
  assetReviewLink,
  buildMessageCard,
  loadDotEnv,
  postTeamsWebhook,
  stakeholdersWebhookUrl,
} from '../lib/teams-webhook.mjs';
import { currentReviewVersion } from './sync-review-versions.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(path.join(__dirname, '..'));
const reviewDir = path.join(root, 'ui_kits', 'review');
const statePath = path.join(reviewDir, 'review-queue-notify-state.json');

loadDotEnv(path.join(root, '.env'));

function formatDue(iso) {
  if (!iso) return '';
  return new Date(iso + 'T12:00:00').toLocaleDateString('en-US', {
    weekday: 'short',
    month: 'short',
    day: 'numeric',
    year: 'numeric',
  });
}

function readState() {
  if (!fs.existsSync(statePath)) return { version: 2, byId: {} };
  const state = JSON.parse(fs.readFileSync(statePath, 'utf8'));
  if (!state.byId) state.byId = {};
  return state;
}

function writeState(state) {
  fs.writeFileSync(statePath, JSON.stringify(state, null, 2) + '\n');
}

function assetState(state, id) {
  return state.byId[id] || {};
}

/**
 * @returns {Array<{ item, dueJob?, versionJob? }>}
 */
function pendingNotifications(queue, state) {
  const jobs = [];

  for (const item of queue.dueForReview || []) {
    const id = item.id;
    const prev = assetState(state, id);
    const due = (item.due || '').trim();
    const version = currentReviewVersion(item);
    const prevDue = prev.stakeholdersNotifiedDue || '';
    const prevVersion = Number(prev.stakeholdersNotifiedVersion) || 0;

    let dueJob = null;
    let versionJob = null;

    if (due && prevDue !== due) {
      dueJob = {
        due,
        kind: prevDue ? 'due-changed' : 'new',
        prevDue,
      };
    }

    if (version > prevVersion) {
      if (prevVersion > 0) {
        versionJob = {
          version,
          prevVersion,
          note: (item.versionNote || '').trim(),
          kind: 'version-bump',
        };
      } else if (!dueJob) {
        versionJob = {
          version,
          prevVersion: 0,
          note: (item.versionNote || '').trim(),
          kind: 'version-first',
        };
      }
    }

    if (dueJob || versionJob) {
      jobs.push({ item, dueJob, versionJob });
    }
  }

  return jobs;
}

function buildStakeholderCard(job) {
  const { item, dueJob, versionJob } = job;
  const title = item.title || item.id;
  const link = assetReviewLink(item.id);
  const version = currentReviewVersion(item);
  const summaryText = (item.summary || item.context || '').trim();
  const versionNote = (item.versionNote || '').trim();

  let activityTitle = 'Ready for review';
  if (versionJob?.kind === 'version-bump' && !dueJob) {
    activityTitle = 'New version ready for review';
  } else if (dueJob?.kind === 'new' && !versionJob) {
    activityTitle = 'New asset ready for review';
  } else if (dueJob?.kind === 'due-changed' && !versionJob) {
    activityTitle = 'Review due date updated';
  } else if (dueJob && versionJob) {
    activityTitle = 'Updated asset ready for review';
  } else if (versionJob && dueJob) {
    activityTitle = 'New version ready for review';
  }

  const facts = [{ name: 'Asset', value: title }];
  facts.push({ name: 'Version', value: `v${version}` });

  if (dueJob) {
    facts.push({ name: 'Due', value: formatDue(dueJob.due) });
    if (dueJob.kind === 'due-changed' && dueJob.prevDue) {
      facts.push({ name: 'Previous due', value: formatDue(dueJob.prevDue) });
    }
  }

  if (versionJob?.kind === 'version-bump' && versionJob.prevVersion) {
    facts.push({ name: 'Previous version', value: `v${versionJob.prevVersion}` });
  }

  const textParts = [];
  if (summaryText) textParts.push(`**Context:** ${summaryText}`);
  if (versionNote && versionJob) {
    textParts.push(`**What changed:** ${versionNote}`);
  }

  const summary =
    versionJob?.kind === 'version-bump'
      ? `${title} — v${version} uploaded`
      : dueJob
        ? `${title} — due ${formatDue(dueJob.due)}`
        : `${title} — v${version}`;

  return buildMessageCard({
    summary,
    activityTitle,
    activitySubtitle: title,
    facts,
    text: textParts.join('\n\n'),
    link,
  });
}

function applyStateAfterNotify(state, job) {
  const id = job.item.id;
  const version = currentReviewVersion(job.item);
  const due = (job.item.due || '').trim();
  const prev = assetState(state, id);

  state.byId[id] = {
    stakeholdersNotifiedDue: due || prev.stakeholdersNotifiedDue || '',
    stakeholdersNotifiedVersion: version,
  };
}

/**
 * @param {object} queue — review-queue.json object
 * @returns {{ sent: number, skipped: boolean, pending: number }}
 */
export async function notifyReviewQueueChanges(queue) {
  const webhook = stakeholdersWebhookUrl();
  const state = readState();
  const pending = pendingNotifications(queue, state);

  if (!pending.length) {
    return { sent: 0, skipped: false, pending: 0 };
  }

  if (!webhook) {
    console.warn(
      'Teams (Mike/Nick):',
      pending.length,
      'update(s) need notify but REVIEW_TEAMS_WEBHOOK_STAKEHOLDERS is not set.',
      'Add it to LUCI Systems Design System/.env (see teams-notifications-guide.txt).'
    );
    return { sent: 0, skipped: true, pending: pending.length };
  }

  let sent = 0;
  for (const job of pending) {
    const card = buildStakeholderCard(job);
    const result = await postTeamsWebhook(webhook, card);
    if (!result.ok) {
      console.error(
        'Teams (Mike/Nick) failed for',
        job.item.id,
        result.status || result.error || result.body
      );
      continue;
    }
    applyStateAfterNotify(state, job);
    sent++;
    const v = currentReviewVersion(job.item);
    const label = job.versionJob ? `v${v}` : formatDue(job.dueJob?.due);
    console.log('Teams (Mike/Nick): notified —', job.item.title || job.item.id, label);
  }

  if (sent) writeState(state);
  return { sent, skipped: false, pending: pending.length };
}

if (process.argv[1] && fileURLToPath(import.meta.url) === path.resolve(process.argv[1])) {
  const queuePath = path.join(reviewDir, 'review-queue.json');
  const queue = JSON.parse(fs.readFileSync(queuePath, 'utf8'));
  notifyReviewQueueChanges(queue).then((r) => {
    if (r.sent === 0 && r.pending === 0) console.log('Teams (Mike/Nick): nothing new to notify.');
  });
}
