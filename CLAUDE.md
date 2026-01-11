# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

StevenSpeak is a real-time AI avatar platform combining voice conversation, sentiment analysis, and video generation. It uses OpenAI's Realtime API, sentiment-driven mood dynamics, and lip-synced video generation (via D-ID) to create lifelike digital personas.

## Repository Structure

- **server/** - FastAPI backend (Python 3.12+, managed with `uv`)
- **web/** - Next.js 15 frontend (TypeScript, React 19, Tailwind CSS 4)
- **docs/** - Planning notes and architecture documentation

## Development Commands

### Server (FastAPI Backend)
```bash
cd server

# Install dependencies
uv sync

# Run development server
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Lint and format
uv run ruff check app tests
uv run ruff check app tests --fix
uv run ruff format app tests

# Run tests
uv run pytest

# Run a single test
uv run pytest tests/test_<module>.py -k "test_name"
```

### Web (Next.js Frontend)
```bash
cd web

# Install dependencies
npm install

# Run development server
npm run dev

# Build
npm run build

# Lint
npm run lint

# Run E2E tests
npx playwright test
npx playwright test --ui  # Interactive mode
```

### Database (Supabase)
```bash
cd web
supabase db reset --db-url "$SUPABASE_DB_URL"
```

## Architecture

### Multi-Agent AI System
The backend orchestrates multiple AI agents:
- **Realtime Conversation Agent** - Main voice interaction via OpenAI Realtime API
- **Web Search Agent** - Information retrieval with handoff pattern
- **Sentiment Classifier** - GPT-5-mini for mood analysis
- **Computer Use Agent** - Playwright browser automation

Agents are defined in `server/app/ai_agents/` and services in `server/app/services/`.

### WebSocket Communication
The main entrypoint is `server/app/main.py` which manages WebSocket sessions at:
```
ws://localhost:8000/realtime/ws?persona={persona_name}
```

Audio streams as base64-encoded PCM at 24kHz.

### Persona System
Two personas with distinct voices and mood videos:
- **Joi** (default) - `en-US-AriaNeural`
- **Officer K** - `en-US-GuyNeural`

Each persona has happy/sad/thinking mood videos that switch based on sentiment analysis.

### Frontend Structure
- `web/src/app/` - Next.js App Router pages and API routes
- `web/src/components/` - React components
- `web/src/hooks/` - Custom hooks (including WebSocket client)
- `web/src/lib/supabase/` - Database helpers and typed queries

### Database Schema
Migrations in `web/supabase/migrations/`. Key tables: profiles, media_assets, processing_jobs, conversations, messages, memories (with pgvector embeddings), session_events.

## Code Style

### Python (server/)
- Python 3.12+, 4-space indentation
- Type hints on public interfaces
- Use explicit module paths: `from app.services.voice import VoiceService`
- Run Ruff before committing

### TypeScript (web/)
- ES modules with named exports
- PascalCase for React components
- Tailwind utility classes preferred over custom CSS
- 2-space indentation

## Testing Requirements

- Mirror module names in tests: `tests/test_<module>.py`
- Use fixture doubles for external API mocking in `tests/conftest.py`
- Always run tests after completing a task

## PR Guidelines

- Imperative mood commit messages ("Add onboarding upload step")
- Include summary, screenshots for UI changes, confirmation that lint passes
- Note any new environment variables or Supabase migrations
- Update CHANGELOG.md with changes
