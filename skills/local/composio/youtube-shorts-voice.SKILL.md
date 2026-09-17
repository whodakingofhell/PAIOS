---
name: youtube-shorts-voice
description: Voiceover: Edge TTS (free), ElevenLabs, MiniMax, macOS say
version: 1.0.0
author: Coach (auto-generated from rushindrasinha/youtube-shorts-pipeline)
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [auto-generated, coach, youtube-shorts, media-content]
    source: https://github.com/rushindrasinha/youtube-shorts-pipeline
---

# Youtube Shorts Voice

## When to use

Voiceover: Edge TTS (free), ElevenLabs, MiniMax, macOS say

## Tools

- `voice-tts`
- `voice-edge`
- `voice-elevenlabs`

## Workflow

1. Initialize the pipeline component
2. Execute the relevant tool
3. Handle response or error
4. Log result

## Error handling

- Stage failed → retry with --force flag
- Provider error → switch via --provider flag
- Upload failed → check YouTube OAuth, retry private upload
