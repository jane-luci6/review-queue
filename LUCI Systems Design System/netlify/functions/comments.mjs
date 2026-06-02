import { getStore } from '@netlify/blobs';
import {
  assetReviewLink,
  buildMessageCard,
  ownerWebhookUrl,
  postTeamsWebhook,
} from '../../lib/teams-webhook.mjs';

const HEADERS = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
  'Access-Control-Allow-Headers': 'Content-Type',
  'Content-Type': 'application/json',
};

const REVIEWERS = ['Mike', 'Nick'];

function store() {
  return getStore({ name: 'luci-review-comments', consistency: 'strong' });
}

const COMMENTS_KEY = 'comments';
const APPROVALS_KEY = 'approvals';

async function readComments() {
  return (await store().get(COMMENTS_KEY, { type: 'json' })) || { comments: [] };
}

async function readApprovals() {
  return (await store().get(APPROVALS_KEY, { type: 'json' })) || { byAsset: {} };
}

function normalizeReviewer(name) {
  const n = (name || '').trim();
  return REVIEWERS.includes(n) ? n : '';
}

async function notifyOwner(card) {
  const url = ownerWebhookUrl();
  if (!url) return;
  const result = await postTeamsWebhook(url, card);
  if (!result.ok && !result.skipped) {
    console.error('Teams (owner) failed:', result.status || result.error || result.body);
  }
}

async function notifyOwnerComment(entry, body) {
  const assetTitle = (body.assetTitle || '').trim();
  const title = assetTitle || entry.assetId || 'Review asset';
  const excerpt = entry.text.length > 500 ? `${entry.text.slice(0, 497)}…` : entry.text;
  const link = assetReviewLink(entry.assetId, body.reviewUrl);
  await notifyOwner(
    buildMessageCard({
      summary: `${entry.author} commented on ${title}`,
      activityTitle: 'New review comment',
      activitySubtitle: title,
      facts: [
        { name: 'Asset', value: title },
        { name: 'From', value: entry.author },
      ],
      text: excerpt,
      link,
    })
  );
}

async function notifyOwnerApproval({ assetId, reviewer, assetTitle, reviewUrl }) {
  const title = (assetTitle || '').trim() || assetId;
  const link = assetReviewLink(assetId, reviewUrl);
  await notifyOwner(
    buildMessageCard({
      summary: `${reviewer} approved ${title}`,
      activityTitle: 'Stakeholder approval',
      activitySubtitle: title,
      facts: [
        { name: 'Asset', value: title },
        { name: 'Approved by', value: reviewer },
      ],
      link,
      themeColor: '2b9e80',
    })
  );
}

export default async (req) => {
  if (req.method === 'OPTIONS') {
    return new Response(null, { status: 204, headers: HEADERS });
  }

  try {
    if (req.method === 'GET') {
      const comments = await readComments();
      const approvals = await readApprovals();
      return new Response(
        JSON.stringify({
          comments: comments.comments || [],
          approvals: approvals.byAsset || {},
        }),
        { status: 200, headers: HEADERS }
      );
    }

    if (req.method === 'POST') {
      const body = await req.json();

      if (body.action === 'approval') {
        const assetId = (body.assetId || '').trim();
        const reviewer = normalizeReviewer(body.reviewer);
        if (!assetId || !reviewer) {
          return new Response(JSON.stringify({ error: 'assetId and reviewer (Mike or Nick) required' }), {
            status: 400,
            headers: HEADERS,
          });
        }

        const data = await readApprovals();
        const byAsset = data.byAsset || {};
        const asset = { ...(byAsset[assetId] || {}) };
        const wasApproved = !!asset[reviewer];
        if (wasApproved) {
          delete asset[reviewer];
        } else {
          asset[reviewer] = new Date().toISOString();
        }
        if (Object.keys(asset).length) {
          byAsset[assetId] = asset;
        } else {
          delete byAsset[assetId];
        }
        await store().setJSON(APPROVALS_KEY, { byAsset });
        const nowApproved = !!asset[reviewer];
        if (nowApproved) {
          await notifyOwnerApproval({
            assetId,
            reviewer,
            assetTitle: body.assetTitle,
            reviewUrl: body.reviewUrl,
          });
        }
        return new Response(
          JSON.stringify({ ok: true, approvals: byAsset, assetId, reviewer, approved: nowApproved }),
          { status: 200, headers: HEADERS }
        );
      }

      const assetId = (body.assetId || '').trim();
      const author = (body.author || '').trim();
      const text = (body.text || '').trim();
      if (!assetId || !author || !text) {
        return new Response(JSON.stringify({ error: 'assetId, author, and text required' }), {
          status: 400,
          headers: HEADERS,
        });
      }

      const data = await readComments();
      const entry = {
        assetId,
        author,
        text,
        at: new Date().toISOString(),
      };
      data.comments.push(entry);
      await store().setJSON(COMMENTS_KEY, data);
      await notifyOwnerComment(entry, body);
      return new Response(JSON.stringify({ ok: true, comment: entry }), { status: 200, headers: HEADERS });
    }

    return new Response(JSON.stringify({ error: 'Method not allowed' }), { status: 405, headers: HEADERS });
  } catch (err) {
    return new Response(JSON.stringify({ error: String(err.message || err) }), {
      status: 500,
      headers: HEADERS,
    });
  }
};
