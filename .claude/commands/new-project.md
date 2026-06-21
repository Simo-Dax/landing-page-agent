---
description: Orchestratore end-to-end — guida passo-passo dall'onboarding (tool, chiavi, MCP, contesto) fino al deploy
argument-hint: [nome progetto / tipo: landing | mini-site | web app]
---

# /new-project — Orchestratore workflow completo (guida step-by-step)

Avvia e guida l'**intero** processo, dall'onboarding al deploy, seguendo `FRAMEWORK.md`.
Non esegue tutto in un colpo: procede **una fase alla volta**, in ordine, fermandosi ai
gate. Dopo ogni step: riepiloga cosa è stato fatto, mostra l'artefatto, e annuncia il
comando successivo. **Nessun passaggio va saltato in silenzio.**

Input: **$ARGUMENTS** (nome progetto + tipo, se noto).

## Carica sempre prima
`CLAUDE.md`, `FRAMEWORK.md`, `directives/orchestrator_index.md`, e — se già compilati —
`PRODUCT.md`, `DESIGN.md`, `context/brand/*`.

---

## FASE 0 — Onboarding: tool, chiavi & MCP (guida step-by-step)

Questa è la parte di setup. Guida l'utente **un servizio alla volta**, spiegando a cosa
serve e cosa procurare. Non assumere che conosca i tool. Riferimento: `CONNECTORS.md`.

**Step 0.1 — Tipo di progetto.** Chiedi cosa vuole costruire e fissa il branch:
- **Landing / pagina statica** → niente login/dati. Servono: design + copy + hosting.
- **Mini-site** → più pagine statiche.
- **Web app** → landing + area riservata con login + dati. Servono in più: auth + database + email tool + webhook.

**Step 0.2 — Ambiente.** Verifica: Node ≥ 20, `gh` CLI, Claude Code attivo nella cartella.

**Step 0.3 — File chiavi.** Se manca `.env`, copia da `.env.example`. Spiega: mai committare `.env`.

**Step 0.4 — Connettori & MCP (uno alla volta).** Per ogni servizio che serve al branch
scelto, di' a cosa serve, dove prendere la chiave (`CONNECTORS.md`), e fattela incollare
in `.env`. Poi spunta "disponibile ora / dopo". Ordine consigliato:
1. **Firecrawl** (`FIRECRAWL_API_KEY`) — ricerca/scrape/design-clone. ⚠️ consuma crediti: conferma prima di ricerche grosse.
2. **Vercel** — hosting/deploy (OAuth al primo collegamento, o `VERCEL_TOKEN`).
3. *(solo web app)* **Auth** — Clerk (pk + sk + webhook secret) **o** Firebase Auth.
4. *(solo web app)* **Database** — Supabase (URL + service_role + access token MCP) **o** Firestore.
5. *(solo web app)* **Email tool** — ⚠️ **chiedi quale usa** (Mailchimp / ConvertKit / Brevo / Klaviyo / Sendfox / altro): API token + ID lista.
6. *(opzionale)* **Cloudflare/Turnstile**, **Dominio**.

**Step 0.5 — Verifica MCP.** Controlla `.mcp.json` (supabase, firecrawl, vercel) e che i
server siano abilitati. Clerk = connettore claude.ai (snippet SDK), non MCP.

**Step 0.6 — Skill/plugin.** Verifica che le skill pesanti referenziate siano installate
(`ui-ux-pro-max`, `impeccable`, `firecrawl`, `the-ai-ad-lab`). Se mancano, indica come installarle.

> **Gate 0:** non proseguire finché le chiavi "disponibili ora" non sono in `.env` e i
> connettori che servono **subito** (almeno Firecrawl se farai ricerca) rispondono. Le
> chiavi "dopo" (auth/db/deploy) si affrontano alla loro fase, senza bloccare l'inizio.

---

## FASE 0.5 — Contesto & brand layer (ricorda e ripopola)

Prima di qualsiasi output creativo, il **brand layer** deve essere pieno. Nel template è vuoto.

**Step 0.5.1 — Controlla.** Apri `PRODUCT.md`, `context/brand/business_strategy.md`,
`context/brand/tone_of_voice.md`, `context/brand/Brand Guidelines.md`. Se contengono ancora
i placeholder `[…]`, **sono da compilare**.

**Step 0.5.2 — Ripopola.** Raccogli dall'utente (o da un brand/URL esistente) e scrivi:
- `PRODUCT.md` — chi/cosa/perché, personas, anti-references, design principles.
- `context/brand/business_strategy.md` — business, offerta, audience, differenziazione.
- `context/brand/tone_of_voice.md` — voce, do/don't, espressioni tipiche.
- `context/brand/anti-ai-writing-style.md` — regole anti-AI (di solito già valide, conferma).

> **Gate 0.5:** non passare al brief finché tono e posizionamento sono definiti (regola #1 di `CLAUDE.md`).

---

## FASE 1→ — Pipeline di costruzione (un command per step)

| # | Step | Command | Gate | Solo web app |
|---|---|---|---|---|
| 1 | Brief CRO (obiettivo, audience, traffico, offerta, KPI) | `/setup` | ⟦GATE⟧ brief | |
| 2 | Brand DNA + design system → `DESIGN.md` | `/brand-dna` | ⟦GATE⟧ direzione | |
| 3 | Architettura / wireframe | `/wireframe` | ⟦GATE⟧ | |
| 4 | Copy di conversione (anti-AI) | `/copy` | | |
| 5 | Build (design + HTML/app) | `/build` | | |
| 6 | Auth / login | `/auth-setup` | | ✅ |
| 7 | Database + webhook + email tool | `/db-setup` | | ✅ |
| 8 | QA (anti-slop + a11y + CRO) | `/qa` | | |
| 9 | Deploy (GitHub + Vercel/Firebase) | `/deploy` | ⟦GATE⟧ prod | |
| 10 | Retro → `LEARNINGS.md` | `/retro` | | |

Landing statica = salta 6-7. Dopo ogni step: riepilogo + artefatto + comando successivo.
Non superare un gate senza ok esplicito. Ogni step lascia un artefatto ispezionabile in `output/`.

**Step opzionali da PROPORRE** (non saltarli in silenzio): ricerca firecrawl approfondita
(fase 2, costa crediti), Cloudflare hardening (fase 9, col dominio), A/B + analytics (post-lancio).

## Output
Tutto in `output/<slug>_<YYYY-MM-DD>/` (brief / copy / build). Per le web app, lo scaffold
dell'app vive nello stesso progetto (landing statica a `/`).

## Regole
Valgono tutte le regole di `CLAUDE.md`: contesto prima dell'output, gate obbligatori, mai
inventare dati, mai usare crediti a pagamento senza conferma, mai pubblicare senza conferma.
