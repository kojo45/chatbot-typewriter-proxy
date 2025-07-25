# Chatbot Typewriter Proxy

A simple chatbot web app with a typewriter effect, powered by a Python Flask backend and a `corpus.json` knowledge base.

## Features

- **Typewriter effect** for chatbot answers in the browser.
- **Corpus-based responses** using fuzzy matching.
- **Flask backend** serves answers via REST API.
- **Front-end** in plain HTML/JS.
- **Auto-deployment** to [Vercel](https://vercel.com/) via GitHub Actions.

## Files

- `index.html` – Chatbot frontend with JavaScript.
- `app.py` – Flask backend for answer lookup.
- `corpus.json` – Question/answer pairs for the chatbot.
- `requirements.txt` – Python dependencies.
- `Procfile` – For Heroku compatibility (optional).
- `.github/workflows/vercel.yml` – GitHub Actions for Vercel deploy.

## Local Development

1. **Clone the repository**
    ```sh
    git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
    cd YOUR_REPO
    ```

2. **Install Python dependencies**
    ```sh
    pip install -r requirements.txt
    ```

3. **Run the Flask server**
    ```sh
    python app.py
    ```

4. **Open frontend**
    - Visit [http://localhost:5000](http://localhost:5000) in your browser.

## Deployment

### Frontend

You can deploy the frontend (`index.html`) using GitHub Pages or Vercel.

### Backend

Vercel now supports Python serverless functions (see [Vercel Python Docs](https://vercel.com/docs/functions/serverless-functions/python)), so you can deploy `app.py` as an API function.

**Note:** For Vercel Python API, place `app.py` in the `api/` directory. See [Vercel Python Example](https://vercel.com/docs/functions/serverless-functions/python#example).

## Auto-Deploy to Vercel

This repository uses [GitHub Actions](https://github.com/features/actions) for automatic deployment to Vercel on every push to `main`.

### Setup

1. [Create a Vercel project](https://vercel.com/new).
2. Get your Vercel [token](https://vercel.com/account/tokens).
3. Add `VERCEL_TOKEN`, `VERCEL_ORG_ID`, and `VERCEL_PROJECT_ID` as [GitHub repository secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets).

### Required GitHub Secrets

- `VERCEL_TOKEN` — Your Vercel personal token.
- `VERCEL_ORG_ID` — Your Vercel organization ID.
- `VERCEL_PROJECT_ID` — Your Vercel project ID.

## Example corpus.json

```json
{
  "questions": [
    {"q": "What is your name?", "a": "I'm your friendly chatbot."},
    {"q": "How are you?", "a": "I'm doing great, thank you!"},
    {"q": "What can you do?", "a": "I can answer questions from my corpus."}
  ]
}
```

## License

MIT