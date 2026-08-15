---
tags:
  - paios/knowledge
  - paios/product-design
  - paios/ui
related:
  - "02-Product.md"
  - "UX-Research.md"
  - "../Software-Development/Accessibility.md"
  - "../Software-Development/Frontend.md"
---

# UI Design System

## Core Principles
- Consistency: same components behave the same everywhere
- Reusability: build once, use many times
- Scalability: new features don't require new components
- Accessibility: all components meet WCAG 2.1 AA

## Design Token Hierarchy
- **Global tokens**: colors, typography, spacing, breakpoints, shadows (raw values)
- **Alias tokens**: semantic meanings (color.primary, color.danger)
- **Component tokens**: scoped to specific components (button.bg, card.shadow)

### Example Token Structure (YAML)
```
colors:
  primary: "#2563EB"
  danger: "#DC2626"
  neutral-100: "#F3F4F6"
  neutral-900: "#111827"
typography:
  font-family: "Inter, system-ui, sans-serif"
  scale:
    body: 16px
    h1: 32px
    h2: 24px
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
breakpoints:
  mobile: 640px
  tablet: 1024px
  desktop: 1280px
```

## Component Library (standard set)
- Button (primary, secondary, ghost, danger, icon) — with loading, disabled states
- Input (text, password, search, textarea, select) — with error, helper text, label
- Card — with header, body, footer slots
- Modal/Dialog — focus trap, escape to close, backdrop click to close
- Table — responsive, sortable, selectable rows, pagination
- Tabs — horizontal, vertical, scrollable overflow
- Form — validation states, error summary, async submit
- Navigation — sidebar, top nav, breadcrumb, mobile drawer
- Spinner/Skeleton — loading states for every data-driven component

## Responsive Design
- Mobile-first CSS (base styles for mobile, media queries for larger)
- Breakpoints: sm (640px), md (768px), lg (1024px), xl (1280px)
- Use CSS Grid or Flexbox — never float-based layouts
- Test on: iPhone SE, iPhone 14, Pixel 7, iPad, 13" laptop, 27" monitor

## Accessibility in the Design System
- Every component has a keyboard interaction spec
- Focus styles: 2px outline + offset, high contrast ring
- Color pairs checked for 4.5:1 contrast
- Form components include error state linked via aria-describedby
- Modals trap focus and manage aria-hidden on background

## Tooling
- Figma for component design + prototyping
- Storybook for component development + documentation
- Chromatic for visual regression testing
- Style Dictionary for token export to multiple platforms

## Process
1. Audit: identify recurring UI patterns
2. Tokenize: extract colors, spacing, typography into tokens
3. Build: implement components from bottom up (atoms → molecules → organisms)
4. Document: usage guidelines, code examples, accessibility notes
5. Version: major/minor/patch for breaking/addition/fix changes
