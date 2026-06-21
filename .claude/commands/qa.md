---
description: Lancia il qa-agent — QA qualità + anti-AI-slop + a11y + self-check CRO sulla pagina costruita
argument-hint: [progetto]
---

# /qa

Avvia il `qa-agent` (Fase 10). Step indipendente, prima del deploy.

Input: $ARGUMENTS

## Cosa fare
1. Leggi il build in `output/<slug>/build/`, `DESIGN.md`, `PRODUCT.md`, brief.
2. Anti-slop con i detector `impeccable` (gradienti viola, bounce, grigio-su-colore, em dash...). Audit `directives/07_vercel_guidelines` (WCAG AA, focus, keyboard, mobile). Coerenza copy con `anti-ai-writing-style`. Self-check `directives/03_editing_selfcheck`.
3. Web app: verifica flusso end-to-end (signup → email → login → area → tracking).
4. Output: `output/<slug>/build/qa_report.md` + fix applicati. Prioritizza per impatto conversione.
