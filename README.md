# Resume Chatbot

A chatbot that answers questions about my background, grounded in my resume and a short knowledge base. It powers the chat on my site.

**Live:** https://oluwashina.ca

## How it works

```
Visitor -> Site (GitHub Pages, docs/)
        -> FastAPI /chat/stream (Google Cloud Run)
        -> OpenAI embeddings + Pinecone (top 5 chunks)
        -> gpt-4o-mini, grounded prompt
        -> answer streamed back to the page
```

If the answer is not in my documents, the bot says "I don't have that information" instead of guessing.

## Features

- Grounded answers (RAG) from my resume PDF and `data/knowledge.md`
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
├── src/resume_chatbot/   # RAG code (loading, splitting, embedding, retrieval)
├── api.py                # FastAPI app
├── docs/                 # Website (GitHub Pages): index.html, style.css, chat.js
├── data/                 # Resume PDF and knowledge.md
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
   Open http://localhost:5500

## Deploy

- **API:** `gcloud run deploy resume-chatbot --source . --region us-central1 --max-instances 2`
- **Site:** GitHub Pages, served from `/docs`
- **Domain:** Cloudflare DNS records set to "DNS only", HTTPS enforced on GitHub Pages

## Design decisions

- **Chunks of 500 characters with 50 overlap:** small enough to be specific, overlap keeps sentences from being cut off.
- **Temperature 0:** factual answers, no creativity about my career.
- **Grounded prompt:** the model may only use retrieved text.
- **Keys at runtime:** passed as environment variables, never baked into the Docker image.
- **Streaming:** the visitor sees the answer start right away.

## Known limitations

- Sessions and rate limits are stored in memory, so they reset on restart or when Cloud Run scales to a new instance.
- Cold starts: the first message after idle time can be slow.
- No source citations in answers yet.
- No retrieval evaluation set yet.

## Next steps

- Source tags on answers
- Suggested question buttons
- Retrieval evaluation set
- Prompt injection test suite
- CI for this repo

## Author

Oluwashina Moluw. GitHub: [Mosh1132](https://github.com/Mosh1132)
