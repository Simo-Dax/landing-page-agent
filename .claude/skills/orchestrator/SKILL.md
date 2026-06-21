---
name: orchestrator
description: Playbook di orchestrazione del workflow per costruire landing, web page, mini-site e web app. Mappa ogni fase del FRAMEWORK a subagent + skill + MCP + gate. Usa quando guidi un progetto end-to-end o devi sapere quale subagent/skill richiamare per una fase.
---

# Orchestrator — playbook del workflow

Fonte di verità del processo: `FRAMEWORK.md`. Questo skill è la **tabella di routing** che l'agente principale usa per dispatchare ogni fase al subagent giusto, con i suoi skill/MCP, fermandosi ai gate.

## Routing: fase → subagent → cosa richiama → output → gate

| Fase | Subagent | Skill / MCP che il subagent richiama | Output | Gate |
|---|---|---|---|---|
| 1 Brief & Discovery | (main, inline) | `directives/01_landing_brief`, `directives/08_grill_me` | brief CRO | ⟦GATE⟧ |
| 2-4 Brand DNA + References + Design System | `design-system-agent` | `brand`, `firecrawl-website-design-clone`, `firecrawl-competitive-intel`, `ui-ux-pro-max`, `design-system` | bozza in `brief/design_system.md` → poi `DESIGN.md` | ⟦GATE⟧ approva in brief, poi promuovi |
| 5 Architettura/Wireframe | `wireframe-agent` | `directives/05_frontend_design`, `directives/09_marketing_psychology` | wireframe testuale | ⟦GATE⟧ |
| 6 Copy | `copy-agent` | `copywriting`, `copy-editing`, `marketing-psychology`, `anti-ai-writing-style` | copy per blocco | — |
| 7 Build | `design-build-agent` | `directives/05_frontend_design`, `directives/06_web_artifacts`, `ui-styling`, `impeccable`, `directives/11_framer_motion` | HTML/CSS o app Next.js | — |
| 8 Auth | `backend-agent` | Clerk MCP | sign-up/login + middleware | — |
| 9 Database | `backend-agent` | Supabase MCP | schema + webhook + tracking | — |
| 10 QA & anti-slop | `qa-agent` | `impeccable`, `directives/07_vercel_guidelines`, `directives/03_editing_selfcheck` | report QA + fix | — |
| 11 Deploy | `deploy-agent` | Vercel MCP | sito live | ⟦GATE⟧ |
| 12 Retro | (main, inline) | `/retro` → `LEARNINGS.md` | lezioni + edit propagati | — |

## Regole di orchestrazione
0. **Lezioni prima.** Leggi `LEARNINGS.md` a inizio progetto e applica le lezioni accumulate dai feedback passati.
1. **Contesto prima.** Ogni dispatch passa al subagent: brief, `PRODUCT.md`, `DESIGN.md`, `context/brand/*` rilevanti. I subagent partono "freddi": dai loro il contesto necessario.
2. **Gate.** Non superare ⟦GATE⟧ senza ok esplicito dell'utente (brief, wireframe, deploy).
3. **Branch.** Pagina statica → salta 8-9. Web app con login → tutte le fasi.
4. **Crediti a pagamento.** firecrawl e simili consumano crediti: conferma prima di lanciare ricerche estese (regola 7 CLAUDE.md).
5. **Mai pubblicare** senza conferma. Preview prima di production.
6. Dopo ogni fase: riepiloga cosa è stato fatto e qual è la fase successiva.
7. **Retro.** Dopo il deploy lancia `/retro` per chiudere il loop e aggiornare `LEARNINGS.md`.
8. **Step opzionali che migliorano l'output: proponili, non saltarli in silenzio.** Alcune cose non sono obbligatorie ma alzano la qualità/sicurezza: **chiedi sempre all'utente** se attivarle, spiegando il beneficio. Casi noti: **Cloudflare hardening** in deploy (WAF/bot/rate-limit/Turnstile, protegge IP e lead); **ricerca firecrawl approfondita** in brand DNA (benchmark reali → design migliore, ma costa crediti); **A/B test** / analytics post-lancio. Tienili a mente e mettili sul tavolo al momento giusto.

## Come dispatchare
L'agente principale (o `orchestrator-agent`) spawna il subagent della fase con il Task/Agent tool, passando: obiettivo della fase, file di contesto da leggere, output atteso e percorso dove salvarlo (`output/<slug>_<data>/`).
