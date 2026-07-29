# Content Pipeline (YouTube Automation)

> The flow that turns any intake (files / text / docs / new learnings) into a published, monetized YouTube video. **One QA gate** prevents bad content from going public.

```
Knowledge Base (Obsidian vault + intake drop-zone)
        │
        ▼
Claude / Gemini — Content Planning
        │
        ▼
Script Generation
        │
        ▼
NotebookLM — Research / Voice (grounding + free audio)
        │
        ▼
Storyboard Generation
        │
        ▼
Higgsfield / ComfyUI — Animation & visuals
        │
        ▼
Voice Generation (ElevenLabs free; NotebookLM audio fallback)
        │
        ▼
Video Editing (FFmpeg assembly)
        │
        ▼
Thumbnail Generation (ComfyUI / SDXL)
        │
        ▼
Metadata Generation (title, description, tags)
        │
        ▼
SEO Optimization
        │
        ▼
╔══════════════════════════╗
║   QA Review (GATE)       ║   ◀── gates upload; bad content never ships
╚══════════════════════════╝
        │
        ▼
YouTube Upload (Data API v3)
        │
        ▼
Analytics Collection (views, retention, CTR, subs)
        │
        ▼
Feedback into Knowledge Base  ── loops back to Content Planning
```

---

## Stage → tool → script mapping

| # | Stage | Primary tool | Free fallback | Script |
|---|---|---|---|---|
| 0 | Intake | File watcher + parser | — | `scripts\00-intake.py` |
| 1 | Content Planning | Claude (judgment) | Gemini (free) | `scripts\01-content-planning.py` |
| 2 | Script Generation | Gemini (volume) | Claude free | `scripts\02-script-generation.py` |
| 3 | Research / Voice | NotebookLM | Perplexity free | `scripts\03-research-voice.py` |
| 4 | Storyboard | Gemini | Claude free | `scripts\04-storyboard.py` |
| 5 | Animation / Visuals | Higgsfield (free credits) | ComfyUI local ($0) | `scripts\05-animation.py` |
| 6 | Voice Generation | ElevenLabs free tier | NotebookLM audio | `scripts\06-voice-generation.py` |
| 7 | Video Editing | FFmpeg (local, $0) | — | `scripts\07-video-editing.py` |
| 8 | Thumbnail | ComfyUI / SDXL local ($0) | Higgsfield free | `scripts\08-thumbnail.py` |
| 9 | Metadata | Gemini | Claude free | `scripts\09-metadata.py` |
| 10 | SEO | Gemini + Perplexity | — | `scripts\10-seo.py` |
| 11 | **QA Review (GATE)** | Claude (high judgment) | — | `scripts\11-qa-review.py` |
| 12 | Upload | YouTube Data API v3 | — | `scripts\12-upload.py` |
| 13 | Analytics → KB | YouTube Analytics API | — | `scripts\13-analytics-feedback.py` |

---

## The QA gate (stage 11)

Before upload, the QA script runs the **QA Criticism Framework** adapted for content:

- **Accuracy** — claims grounded in NotebookLM/Perplexity sources?
- **Clarity & pacing** — script reads naturally at target WPM?
- **Brand fit** — matches channel mission (build/automate/secure/document)?
- **Metadata quality** — title hooks, description has value, tags on-niche?
- **SEO** — keyword in title + first 60s of script; timestamp chapters present?
- **Thumbnail** — high contrast, ≤5 words, readable at phone size?
- **Accessibility** — captions accurate, no flashing >3Hz, narration clear?
- **Compliance** — copyright clear (music/B-roll), no misleading metadata?

Approval threshold: all categories PASS, score avg ≥ 9.0, Risk = LOW. Fails are held for revision; upload does **not** proceed.

---

## Inputs (the intake drop-zone)

```
Pipeline\intake\
├── INSTRUCTIONS.md      # what to drop here
├── raw\                 # files, images, PDFs, docs — untouched originals
├── text\                # .md / .txt notes, Obsidian exports, learnings
└── processed\           # normalized JSON produced by script 00
```

Anything placed in `raw\` or `text\` triggers ingestion → `00-intake.py` normalizes it into `processed\intake.json`, which feeds stage 1.

---

## Feedback loop (the cycle, not the line)

Stage 13 writes analytics back into the Knowledge Base:
- Top-performing topics → prioritized for new content.
- Audience-retention drop-offs → editing pattern notes.
- High-CTR title/thumbnail patterns → template library.
- Subscriber conversion sources → marketing focus.

This closes the loop: every published video improves the next plan.
