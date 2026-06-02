/**
 * Microsoft Teams Incoming Webhook — Office 365 MessageCard format.
 */
import fs from 'fs';

export function siteUrl() {
  return (process.env.REVIEW_SITE_URL || 'https://startling-fudge-f9965f.netlify.app').trim().replace(/\/$/, '');
}

export function assetReviewLink(assetId, reviewUrl) {
  const fromBody = (reviewUrl || '').trim();
  if (fromBody) return fromBody;
  if (!assetId) return siteUrl();
  return `${siteUrl()}/#/review/${encodeURIComponent(assetId)}`;
}

export function buildMessageCard({
  summary,
  activityTitle,
  activitySubtitle = '',
  facts = [],
  text = '',
  link = '',
  themeColor = '68E3BE',
}) {
  const card = {
    '@type': 'MessageCard',
    '@context': 'https://schema.org/extensions',
    themeColor,
    summary: summary || activityTitle,
    sections: [
      {
        activityTitle,
        ...(activitySubtitle ? { activitySubtitle } : {}),
        ...(facts.length ? { facts } : {}),
        ...(text ? { text, markdown: true } : {}),
      },
    ],
  };
  if (link) {
    card.potentialAction = [
      {
        '@type': 'OpenUri',
        name: 'Open in review queue',
        targets: [{ os: 'default', uri: link }],
      },
    ];
  }
  return card;
}

export async function postTeamsWebhook(webhookUrl, body) {
  const url = (webhookUrl || '').trim();
  if (!url) return { ok: false, skipped: true };
  try {
    const res = await fetch(url, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(body),
    });
    const text = await res.text().catch(() => '');
    return { ok: res.ok, status: res.status, body: text };
  } catch (err) {
    return { ok: false, error: String(err.message || err) };
  }
}

/** Power Automate / Logic Apps HTTP trigger — not a Teams channel. */
export function isPowerAutomateWebhook(url) {
  return /logic\.azure\.com|powerautomate|powerplatform|flow\.microsoft|azure-apihub/i.test(url || '');
}

/**
 * auto = MessageCard for channel webhooks, plain JSON for Power Automate (DM you only).
 * Set REVIEW_TEAMS_OWNER_FORMAT=powerautomate to force when auto-detection fails.
 */
export function ownerWebhookFormat(url) {
  const mode = (process.env.REVIEW_TEAMS_OWNER_FORMAT || 'auto').trim().toLowerCase();
  if (mode === 'powerautomate' || mode === 'flow') return 'powerautomate';
  if (mode === 'messagecard' || mode === 'channel') return 'messagecard';
  return isPowerAutomateWebhook(url) ? 'powerautomate' : 'messagecard';
}

/** Flat JSON for Power Automate → Post message in a chat (recipient = you only). */
export function buildOwnerAlertPayload({
  alertType,
  summary,
  assetTitle,
  assetId,
  author = '',
  reviewer = '',
  text = '',
  link = '',
}) {
  const lines = [summary];
  if (text) lines.push('', text);
  if (link) lines.push('', `Open: ${link}`);
  return {
    alertType,
    summary,
    message: lines.join('\n'),
    assetTitle,
    assetId,
    author,
    reviewer,
    text,
    link,
  };
}

export async function postOwnerWebhook(url, { messageCard, ownerPayload }) {
  const format = ownerWebhookFormat(url);
  const body = format === 'powerautomate' ? ownerPayload : messageCard;
  return postTeamsWebhook(url, body);
}

export function loadDotEnv(envPath) {
  if (!envPath || !fs.existsSync(envPath)) return;
  const text = fs.readFileSync(envPath, 'utf8');
  for (const line of text.split('\n')) {
    const t = line.trim();
    if (!t || t.startsWith('#')) continue;
    const i = t.indexOf('=');
    if (i < 0) continue;
    const key = t.slice(0, i).trim();
    let val = t.slice(i + 1).trim();
    if (
      (val.startsWith('"') && val.endsWith('"')) ||
      (val.startsWith("'") && val.endsWith("'"))
    ) {
      val = val.slice(1, -1);
    }
    if (!process.env[key]) process.env[key] = val;
  }
}

export function ownerWebhookUrl() {
  return (
    process.env.REVIEW_TEAMS_WEBHOOK_OWNER ||
    process.env.REVIEW_TEAMS_WEBHOOK_URL ||
    ''
  ).trim();
}

export function stakeholdersWebhookUrl() {
  return (process.env.REVIEW_TEAMS_WEBHOOK_STAKEHOLDERS || '').trim();
}
