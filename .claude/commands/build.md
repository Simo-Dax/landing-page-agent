---
description: Lancia il design-build-agent — build del design + HTML/CSS (o app Next.js) nel design system
argument-hint: [progetto o superficie]
---

# /build

Avvia il `design-build-agent` (Fase 7). Step indipendente (a valle di wireframe + copy approvati).

Input: $ARGUMENTS

## Cosa fare
1. Leggi wireframe approvato, copy (`output/<slug>/copy/`), `DESIGN.md`, `PRODUCT.md`.
2. Traduci in pagina rispettando token e regole nominate di `DESIGN.md`. `directives/05_frontend_design`, `ui-styling`, `06_web_artifacts` se React; motion `11_framer_motion`; craft con `impeccable`.
3. Default: HTML statico self-contained. Web app: scaffold Next.js, landing a `/`, route app per il resto (stesso dominio). Build React → parti dallo **stack front-end consigliato** (React+TS, shadcn/ui, Tailwind mobile-first, Lucide React, React Hook Form, calendari React Big Calendar/FullCalendar), da adattare al caso — vedi `design-build-agent`.
4. Output: `output/<slug>/build/`. Mai design basico; mobile-first; WCAG AA; zero em dash. Non pubblicare (è del `deploy-agent`).
