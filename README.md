# StevenSpeak

Real-time AI avatar platform combining voice conversation, sentiment analysis, and lip-synced video generation.

## Features

- Voice conversation via OpenAI Realtime API
- Sentiment-driven mood dynamics with happy/sad/thinking video states
- Lip-synced avatar video generation via SadTalker on RunPod
- Multi-agent system with web search and computer use capabilities
- Persona system with distinct voices and personalities

## Tech Stack

- **Backend**: FastAPI, Python 3.12+
- **Frontend**: Next.js 15, React 19, Tailwind CSS 4
- **AI**: OpenAI Realtime API, GPT for sentiment classification
- **Video**: SadTalker on RunPod for lip-sync generation
- **Database**: Supabase (PostgreSQL + pgvector)

## Architecture

```
server/          # FastAPI backend
├── app/
│   ├── ai_agents/   # Multi-agent orchestration
│   ├── services/    # Voice, sentiment, video services
│   └── main.py      # WebSocket entrypoint

web/             # Next.js frontend
├── src/
│   ├── app/         # App Router pages
│   ├── components/  # React components
│   └── hooks/       # WebSocket client hooks
```

## Open Source Lip Sync Model

For lip-sync generation, I evaluated several open source models and chose **SadTalker** over Wav2Lip.

**Why SadTalker:**
- Wav2Lip produces good lip synchronization but the rest of the face remains static—only the mouth moves
- SadTalker adds realistic head movements, expressions, and gestures, creating a more lifelike result
