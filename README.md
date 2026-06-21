# Landing Page & CRO Agent — engine

Engine riusabile per progettare e costruire landing page, mini-site e web-app ad alta conversione: dalla strategia al copy, dal design system al build, fino a deploy e analytics. Gira dentro **Claude Code**.

## Com'è fatto (template a due livelli)
- **Engine riusabile** (non cambia tra progetti): `CLAUDE.md`, `directives/`, `.claude/` (agents, commands, skills), `.mcp.json`, `FRAMEWORK.md`, `execution/`, `CONNECTORS.md`.
- **Brand layer per-cliente** (vuoto nel template, da riempire): `PRODUCT.md`, `DESIGN.md`, `context/` (identità, tone of voice, reference).
- **Output per-cliente**: `output/<progetto>/` (brief, copy, build). Gitignored.

## Prerequisiti
- Claude Code attivo in questa cartella.
- Node ≥ 20 (per build/app). `gh` CLI per GitHub. Account + chiavi dei servizi quando servono (Vercel, Supabase, Clerk, …).
- Copia `.env.example` → `.env` e riempi le chiavi man mano (vedi `CONNECTORS.md`). **Mai committare `.env`.**
- Installa via marketplace le skill/plugin pesanti referenziate (impeccable, ui-ux-pro-max, firecrawl, the-ai-ad-lab).

## Partire da zero (i "bottoni")
Ogni step è un command. In ordine:

| # | Command | Cosa fa | Serve da te |
|---|---|---|---|
| 1 | `/setup` | Brief + cosa vuoi costruire + lista credenziali (ora/dopo) + scaffold cartelle | obiettivo, audience, traffico, stack, chiavi |
| 2 | `/brand-dna` | Brand DNA + design system → `DESIGN.md` | direzione look / sito reference |
| 3 | `/wireframe` | Architettura + wireframe ⟦gate⟧ | approvazione |
| 4 | `/copy` | Copy di conversione (anti-AI) | testi sorgente / dati |
| 5 | `/build` | Build pagina/app nel design system | — |
| 6 | `/auth-setup` + `/db-setup` | (web-app) auth + DB + webhook | chiavi auth/DB + email tool |
| 7 | `/qa` | QA anti-slop + a11y + self-check CRO | — |
| 8 | `/deploy` | GitHub + Vercel (o Firebase), env, preview → prod ⟦gate⟧ | repo + token |
| — | `/new-project` | Orchestratore: lancia la sequenza 1→8 | — |
| — | `/retro` | Aggiorna `LEARNINGS.md` a fine progetto | feedback |

## Dove guardare
- **`FRAMEWORK.md`** — le 12 fasi, l'ordine dei sub-agent per tipo di progetto, e i comandi.
- **`.claude/agents/`** — i sub-agent (descrizione + quando usarli nel frontmatter di ognuno).
- **`CONNECTORS.md`** — ogni servizio: chiavi + cosa fare dentro.
- **`directives/orchestrator_index.md`** — catalogo delle directives (procedure per fase).
- **`LEARNINGS.md`** — lezioni dai feedback (lette a inizio progetto).
- **`ROADMAP.md`** — stato + prossimi step del progetto corrente.

## Riusare per un nuovo brand
Il template parte **pulito** (brand layer vuoto, nessuna chiave). Per un nuovo progetto: copia `.env.example` → `.env`, lancia `/setup`, e l'engine riempie `PRODUCT.md`, `DESIGN.md` e `context/` per quel brand. I segreti non si committano mai; `output/` non si condivide.
