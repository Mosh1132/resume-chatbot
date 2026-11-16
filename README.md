# Resume Chatbot

A chatbot that answers questions about my background, grounded in a knowledge base about my resume and projects. It powers the chat on my site.

**Live:** https://oluwashina.ca

## How it works

```
Visitor -> Site (GitHub Pages, docs/)
        -> FastAPI /chat/stream (Google Cloud Run)
        -> Intent classifier: "future" or "now"
             future -> fixed "Anticipate" reply (no search, no sources)
             now    -> OpenAI embeddings + Pinecone (top 3 chunks)
                    -> gpt-4o-mini, grounded prompt
        -> answer streamed back, with the source sections in an X-Sources header
        -> page shows the answer and the source tags
```

If the answer is not in my documents, the bot says "I don't have that information" instead of guessing.

## Features

- Grounded answers (RAG) from `data/knowledge.md`
- Source tags on every answer, showing which section of the knowledge base it came from
- Intent classifier that routes questions about upcoming projects to a fixed reply
- Streaming replies (token by token)
- Per-visitor conversation memory
- Input length limit (500 characters)
- Rate limiting per IP (HTTP 429)
- CORS allow list (only my site and local dev can call the API)
- API keys live on the server, never in the browser
- Cloud Run instance cap and spend caps on Google Cloud and OpenAI
- Responsive site with dark mode, plain HTML/CSS/JS

## Project layout

```
resume-chatbot/
├── src/resume_chatbot/   # RAG code (loading, splitting, embedding, retrieval, classifier)
├── api.py                # FastAPI app
├── docs/                 # Website (GitHub Pages): index.html, style.css, chat.js
├── data/                 # knowledge.md
├── evals/                # classifier evaluation and results log
├── tests/
├── Dockerfile
└── requirements.txt
```

## Run locally

1. Create a `.env` file:
   ```
   LLM_API_KEY=your-openai-key
   PINECONE_API_KEY=your-pinecone-key
   ```
2. Build and run the API:
   ```
   docker build -t resume-chatbot .
   docker run --rm -p 8080:8080 --env-file .env resume-chatbot
   ```
3. Test it at http://127.0.0.1:8080/docs
4. Serve the site:
   ```
   cd docs
   python -m http.server 5500
   ```
   Open http://localhost:5500. The API URL in `docs/chat.js` must use the same port the API is running on.

If you change `data/knowledge.md`, delete the Pinecone index and start the API once so it re-ingests the file.

## Evaluation

The intent classifier (future vs now) is tested in `evals/classifier_eval.py`:

| Set | Questions | Accuracy |
|---|---|---|
| Labelled set | 20 | 100% |
| Held-out set (different wording) | 20 | 100% |

Real misses are added to the test set, and results are logged in `evals/eval_log.md`. Run it with:

```
python evals/classifier_eval.py
```

Small sets can look perfect, so the next step is a harder set (typos, mixed questions, very short questions, attack attempts).

## Deploy

- **API:** `gcloud run deploy resume-chatbot --source . --region us-central1`
- **Site:** GitHub Pages, served from `/docs`. A push to `docs/` updates it.
- **Domain:** Cloudflare DNS records set to "DNS only", HTTPS enforced on GitHub Pages

Pushing to GitHub does not update the API. Only `gcloud run deploy` does.

## Design decisions

- **Split by heading, then by size:** chunks of 500 characters with 50 overlap, and each chunk keeps its section name for the source tags. The heading is also added to the chunk text so search can match on it.
- **Temperature 0:** factual answers, no creativity about my career.
- **Grounded prompt:** the model may only use retrieved text.
- **Classifier in code, not in the prompt:** a prompt rule for upcoming-project questions was ignored by the model, so a separate classifier step decides before the answer model runs.
- **Sources in a response header:** they are known before the answer starts, so they are sent in `X-Sources` and read by the page, which keeps the streamed text clean.
- **Keys at runtime:** passed as environment variables, never baked into the Docker image.
- **Streaming:** the visitor sees the answer start right away.

## Known limitations

- Sessions and rate limits are stored in memory, so they reset on restart or when Cloud Run scales to a new instance.
- Cold starts: the first message after idle time can be slow.
- Each question makes an extra model call for the classifier, which adds a little latency and cost.
- No retrieval evaluation set yet.

## Author

Oluwashina Moluw. GitHub: [Mosh1132](https://github.com/Mosh1132)
