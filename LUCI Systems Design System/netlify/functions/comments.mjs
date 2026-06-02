import { getStore } from '@netlify/blobs';

const HEADERS = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
  'Access-Control-Allow-Headers': 'Content-Type',
  'Content-Type': 'application/json',
};

function store() {
  return getStore({ name: 'luci-review-comments', consistency: 'strong' });
}

const KEY = 'comments';

export default async (req) => {
  if (req.method === 'OPTIONS') {
    return new Response(null, { status: 204, headers: HEADERS });
  }

  try {
    if (req.method === 'GET') {
      const data = await store().get(KEY, { type: 'json' });
      return new Response(JSON.stringify(data || { comments: [] }), { status: 200, headers: HEADERS });
    }

    if (req.method === 'POST') {
      const body = await req.json();
      const assetId = (body.assetId || '').trim();
      const author = (body.author || '').trim();
      const text = (body.text || '').trim();
      if (!assetId || !author || !text) {
        return new Response(JSON.stringify({ error: 'assetId, author, and text required' }), {
          status: 400,
          headers: HEADERS,
        });
      }

      const data = (await store().get(KEY, { type: 'json' })) || { comments: [] };
      const entry = {
        assetId,
        author,
        text,
        at: new Date().toISOString(),
      };
      data.comments.push(entry);
      await store().setJSON(KEY, data);
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
