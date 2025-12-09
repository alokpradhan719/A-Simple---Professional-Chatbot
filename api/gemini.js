export default async function handler(req, res) {
  if (req.method !== 'POST') return res.status(405).json({ error: 'Method not allowed' });
  const { prompt, model, options } = req.body || {};
  if (!prompt) return res.status(400).json({ error: 'Missing prompt in request body' });

  const endpoint = process.env.GEMINI_ENDPOINT;
  const apiKey = process.env.GEMINI_API_KEY;

  if (!endpoint || !apiKey) return res.status(500).json({ error: 'GEMINI_ENDPOINT or GEMINI_API_KEY not configured' });

  try {
    const response = await fetch(endpoint, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${apiKey}`
      },
      body: JSON.stringify({ prompt, model, options })
    });

    const text = await response.text();
    try {
      const json = JSON.parse(text);
      return res.status(response.status).json(json);
    } catch (e) {
      // Not JSON - return raw text
      return res.status(response.status).send(text);
    }
  } catch (err) {
    console.error('Error forwarding to Gemini endpoint:', err);
    return res.status(500).json({ error: err.message || 'Unknown error' });
  }
}
