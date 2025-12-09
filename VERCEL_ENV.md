How to configure Gemini API credentials and endpoint for Vercel

1) Log into your Vercel dashboard: https://vercel.com
2) Open the project: `A-Simple---Professional-Chatbot` (import it if you haven't yet)
3) Go to Settings → Environment Variables
4) Add two environment variables:

   - Key: `GEMINI_ENDPOINT`
     Value: the full Gemini/Generative API endpoint URL you want to use.
     Example: `https://generativeai.googleapis.com/v1/models/text-bison-001:generate`

   - Key: `GEMINI_API_KEY`
     Value: your API key (keep this secret)

5) Select the environment (Preview/Production) and save.
6) Trigger a new deployment by pushing to `main` or clicking "Redeploy" in the Vercel dashboard.

Notes
- Do NOT commit your real API key to the repository. Use Vercel environment variables or GitHub secrets.
- The included `api/gemini.js` function will read `GEMINI_ENDPOINT` and `GEMINI_API_KEY` and forward POST requests from the frontend.
- Frontend usage: POST to `/api/gemini` with JSON body `{ "prompt": "your prompt here", "model": "optional-model-name" }`.
