---
name: youtube-shorts-pipeline
description: |
  Verticals v3 — automated YouTube Shorts pipeline: news → script → AI visuals →
  voiceover → captions → upload. Any niche, ~$0.11 per video, ~3 min wall time.
version: 1.0.0
author: Rushindra Sinha (rushindrasinha)
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [youtube, shorts, pipeline, ai-content, verticals, niche-intelligence]
    source: https://github.com/rushindrasinha/youtube-shorts-pipeline
    category: media
---

# YouTube Shorts Pipeline (Verticals v3)

## What it does

One command produces a published YouTube Short from any topic and niche:

```bash
python -m verticals run --topic "Sam Altman just mass-fired 200 safety researchers" --niche tech
```

Pipeline stages: Research → Script → Visuals → Voice → Captions → Assemble → Upload

## Niche Intelligence

15 built-in niches shape every stage — script tone, visual style, caption aesthetics, music mood, thumbnail strategy. Build your own in 5 minutes.

Built-in niches: tech, gaming, finance, fitness, cooking, travel, true_crime, science, politics, entertainment, sports, fashion, education, motivation, comedy, general.

## Stage details

| Stage | Tool | Details |
|-------|------|---------|
| Research | DuckDuckGo + web scraping | Anti-hallucination gate — facts only from research |
| Script | LLM (Claude/Gemini/GPT/Ollama/MiniMax) | Niche-toned, hook-driven, 150-170 words |
| Visuals | Gemini Imagen | 3 b-roll frames, 9:16 crop, Ken Burns motion |
| Voice | Edge TTS (free) / ElevenLabs / MiniMax | 300+ voices, niche-suggested voice characteristics |
| Captions | Whisper + ASS/SRT | Word-level timestamps, niche-configurable fonts |
| Assemble | ffmpeg | Voice ducking, background music, animated b-roll |
| Upload | YouTube API | Private by default, SRT captions, AI thumbnail |

## LLM Providers

| Provider | Cost | Setup |
|----------|------|-------|
| Claude (Anthropic) | ~$0.02/script | `ANTHROPIC_API_KEY` |
| Gemini (Google) | Free tier | `GEMINI_API_KEY` |
| GPT (OpenAI) | ~$0.01/script | `OPENAI_API_KEY` |
| Ollama (local) | Free | Install Ollama + model |
| Claude CLI | Free w/ Max | Claude Code subscription |
| MiniMax | Pay-as-you-go | `MINIMAX_API_KEY` |

## TTS Providers

| Provider | Cost | Setup |
|----------|------|-------|
| Edge TTS | Free | None (recommended default) |
| ElevenLabs | ~$0.05/video | `ELEVENLABS_API_KEY` |
| MiniMax | Pay-as-you-go | `MINIMAX_API_KEY` |

## CLI Commands

```bash
# Full pipeline
python -m verticals run --topic "headline" --niche tech

# Individual stages
python -m verticals draft --topic "headline" --niche tech
python -m verticals produce --draft <path> --lang en
python -m verticals upload --draft <path> --lang en
python -m verticals topics --niche tech --limit 20

# Flags
--niche NAME       Niche profile (default: general)
--provider NAME    LLM provider (default: claude)
--voice NAME       TTS provider (default: edge)
--platform NAME    Draft target: shorts, reels, tiktok, all
--lang CODE        Language (default: en)
--dry-run          Draft only, skip produce and upload
--force            Redo all stages
--verbose          Debug logging
```

## Security

- Credential storage: 0600 permissions via atomic os.open()
- API keys: sent via headers, never URL parameters
- Upload privacy: YouTube uploads default to private
- Prompt injection: research snippets truncated to 300 chars
- Niche profiles: YAML parsed with safe_load (no code execution)
- Dependency pinning: compatible release bounds

## Integration with PAIOS agents

- **composio**: YouTube upload tools, API key management
- **skill-ecosystem**: Content pipeline skill management
- **integration-orchestrator**: Coordinate multi-stage pipeline
- **web-content**: Research stage (DuckDuckGo scraping)
- **evelyn-brain**: Log content performance to memory

## Setup

```bash
git clone https://github.com/rushindrasinha/youtube-shorts-pipeline.git
cd youtube-shorts-pipeline
pip install -r requirements.txt
```

Set API keys in `.env`:
```
ANTHROPIC_API_KEY=***
GEMINI_API_KEY=***
OPENAI_API_KEY=***
```

## Error handling

- Research failed → retry with different search query
- LLM error → switch provider via --provider flag
- TTS error → fallback to Edge TTS
- Upload failed → check YouTube OAuth, retry private upload
- Image generation failed → uses fallback frames