---
tags:
  - paios/knowledge
  - paios/software-development
  - paios/accessibility
related:
  - "Project-Phases.md"
  - "Testing-Lifecycle.md"
  - "../Product-Design/UI-Design-System.md"
  - "../Product-Design/02-Product.md"
  - "09-Documentation.md"
---

# Accessibility (a11y)

## Standards
WCAG 2.1 AA is the minimum target. Four principles: Perceivable, Operable, Understandable, Robust.

## Design Phase
- Color contrast: minimum 4.5:1 for text, 3:1 for large text (use contrast checkers)
- Don't rely on color alone to convey information (add icons, patterns, text)
- Touch targets: minimum 44x44px for mobile
- Readable font sizes: 16px minimum for body text
- Focus indicators: 2px+ outline, high contrast
- Keyboard navigation order matches visual order

## Development Phase
- Semantic HTML: `<nav>`, `<main>`, `<aside>`, `<header>`, `<footer>`, `<button>`, `<label>`
- Form inputs must have associated `<label>` (for/id or aria-label)
- Images: meaningful alt text (or `alt=""` for decorative)
- ARIA: use native HTML first, ARIA only when no HTML equivalent exists
  - aria-label, aria-labelledby, aria-describedby
  - role="alert" for dynamic content updates
  - aria-live="polite/assertive" for live regions
- Headings: hierarchical (h1 → h6), no skipping levels
- Links: descriptive text (not "click here")
- Focus management: skip-to-content link, trap focus in modals

## Testing Phase
- Keyboard-only: navigate the entire app with Tab/Shift+Tab/Enter/Escape
- Screen reader: test with NVDA (Windows) or VoiceOver (Mac)
- Zoom: 200% zoom without horizontal scroll or lost content
- Reduced motion: respect prefers-reduced-motion media query
- Color contrast: automated checks (axe, WAVE, Lighthouse) + manual check
- Automated: axe-core, Lighthouse a11y audit, eslint-plugin-jsx-a11y

## Common Failures to Avoid
- Missing form labels
- Low contrast text
- Keyboard traps (can't Tab out of a widget)
- Non-text content without text alternatives
- Empty buttons/links
- Auto-playing video/audio without pause control
