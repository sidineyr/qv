const ALLOWED_ORIGINS = new Set([
  'https://sidineyr.github.io',
  'http://localhost:8000',
  'http://127.0.0.1:8000'
]);

function headers(origin) {
  return {
    'Access-Control-Allow-Origin': origin,
    'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type, Accept',
    'Cache-Control': 'no-store',
    'Content-Type': 'application/json; charset=utf-8',
    'Vary': 'Origin',
    'X-Robots-Tag': 'noindex, nofollow'
  };
}
function json(body, status, origin) { return new Response(JSON.stringify(body), {status, headers: headers(origin)}); }

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const origin = request.headers.get('Origin') || '';
    if (!ALLOWED_ORIGINS.has(origin)) return new Response(null, {status: 403});
    if (request.method === 'OPTIONS') return new Response(null, {status: 204, headers: headers(origin)});
    if (url.pathname !== '/completions') return json({error: 'Not found'}, 404, origin);
    await env.DB.prepare('CREATE TABLE IF NOT EXISTS completion_counter (id INTEGER PRIMARY KEY CHECK (id = 1), total INTEGER NOT NULL DEFAULT 0 CHECK (total >= 0))').run();
    if (request.method === 'GET') {
      const row = await env.DB.prepare('SELECT total FROM completion_counter WHERE id = 1').first();
      return json({total: row?.total ?? 0}, 200, origin);
    }
    if (request.method !== 'POST') return json({error: 'Method not allowed'}, 405, origin);
    if (request.headers.get('Content-Type') !== 'application/json') return json({error: 'Unsupported media type'}, 415, origin);
    if (request.headers.get('Content-Length') && Number(request.headers.get('Content-Length')) > 64) return json({error: 'Payload too large'}, 413, origin);
    if (await request.text() !== '{"completed":true}') return json({error: 'Invalid request'}, 400, origin);
    const row = await env.DB.prepare('INSERT INTO completion_counter (id,total) VALUES (1,1) ON CONFLICT(id) DO UPDATE SET total = total + 1 RETURNING total').first();
    return json({total: row.total}, 200, origin);
  }
};
