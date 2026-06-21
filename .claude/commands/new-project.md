---
description: Orchestratore end-to-end — lancia l'intero workflow del FRAMEWORK (fasi 1→11)
argument-hint: [nome cliente / tipo: landing | web app]
---

# /new-project — Orchestratore workflow completo

Avvia e guida l'intero processo di costruzione di una landing/web/web-app seguendo `FRAMEWORK.md`. Non esegue tutto in un colpo: orchestra le fasi in sequenza, fermandosi ai gate per l'approvazione dell'utente.

Input: **$ARGUMENTS** (nome cliente + tipo progetto)

## Carica sempre prima
`CLAUDE.md`, `FRAMEWORK.md`, `PRODUCT.md`, `DESIGN.md`, `context/brand/*`, `directives/index.md`.

## Determina il branch
- **Landing / pagina statica** → fasi 1-7, 10-12 (salta auth/db).
- **Web app / mini-site con login** → tutte le fasi 1-12.

## Sequenza (la pipeline — un command per step)

| # | Step | Command | Gate | Solo web app |
|---|---|---|---|---|
| 1 | Brief + cosa costruire + credenziali | `/setup` | ⟦GATE⟧ brief | |
| 2 | Design system | `/brand-dna` | ⟦GATE⟧ direzione | |
| 3 | Architettura / wireframe | `/wireframe` | ⟦GATE⟧ | |
| 4 | Copy di conversione | `/copy` | | |
| 5 | Build (design + HTML/app) | `/build` | | |
| 6 | Auth/login | `/auth-setup` | | ✅ |
| 7 | Database + webhook + email tool | `/db-setup` | | ✅ |
| 8 | QA (anti-slop + a11y + CRO) | `/qa` | | |
| 9 | Deploy (GitHub + Vercel/Firebase) | `/deploy` | ⟦GATE⟧ prod | |
| 10 | Retro → LEARNINGS | `/retro` | | |

Landing statica = salta 6-7. Dopo ogni step: riepiloga + indica il command successivo. Non superare un gate senza ok esplicito. Ogni step lascia un artefatto in `output/`.

## Output
Tutto in `output/<slug>_<YYYY-MM-DD>/` (brief / copy / build). Per le web app, lo scaffold dell'app vive nello stesso progetto (landing statica a `/`).

## Regole
Valgono tutte le regole di `CLAUDE.md`: contesto prima dell'output, gate obbligatori, mai inventare dati, mai pubblicare senza conferma, mappatura skill/MCP canonica.
