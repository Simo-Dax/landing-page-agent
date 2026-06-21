# FRAMEWORK — Workflow templatizzabile per costruire landing, web page, mini-site e web app

Questo è il workflow step-by-step dell'agente. È pensato per essere **riusabile** (clona il template, riempi il brand layer, fai partire le fasi) e **condivisibile** con altri professionisti.

Due livelli:
- **Engine** (riusabile): `CLAUDE.md`, `directives/`, `.claude/` (commands, skills, settings, `.mcp.json`), `execution/`, questo `FRAMEWORK.md`.
- **Brand layer** (per-cliente): `PRODUCT.md`, `DESIGN.md`, `context/brand/` (voce, business, anti-AI), `context/references/` (reference visive) → si riempiono per ogni progetto.

Branch del workflow:
- **Pagina statica** (landing/web page): fasi 1-7, 10-12. Salta auth/db.
- **Web app / mini-site con login**: tutte le fasi 1-12.

---

## Schema del template (repo Git condivisibile)

```
TEMPLATE AGENTE (repo Git condivisibile)
│
├── ENGINE (riusabile, brand-agnostic) ──────── non cambia tra clienti
│   ├── CLAUDE.md            regole + orchestrazione + mappatura skill
│   ├── FRAMEWORK.md         questo doc: workflow 12 fasi
│   ├── directives/          procedure per ogni fase
│   ├── .claude/commands/    i comandi che lanciano le fasi
│   ├── .claude/skills/      skill custom (le pesanti → install via plugin)
│   ├── .mcp.json            connettori MCP (supabase, firecrawl, vercel)
│   ├── .env.example         template chiavi (copia in .env, mai committare)
│   └── execution/           script/template riusabili
│
├── BRAND LAYER (per-cliente) ───────────────── si riempie ogni progetto
│   ├── PRODUCT.md           chi/cosa/perché   (template: execution/templates/PRODUCT.template.md)
│   ├── DESIGN.md            come appare        (template: execution/templates/DESIGN.template.md)
│   ├── context/brand/      voce, business, anti-AI, brand guidelines
│   └── context/references/  reference visive (siti, screenshot)
│
├── MEMORY (stato) ──────────────────────────── memoria persistente
│   └── LEARNINGS.md + ROADMAP.md (lezioni + stato progetto)
│
└── output/ (deliverable per-cliente) ───────── un progetto per cartella
    └── <cliente>_<data>/ brief · copy · build
```

Per condividere: `git init` → push su GitHub. I colleghi clonano, installano le skill/plugin, copiano `.env.example`→`.env`, lanciano `/new-project`.

---

## Le fasi

Per ogni fase: input → output, gate (se serve approvazione), comando, skill/MCP.

### Fase 0 — Setup agente (one-time)
Bootstrap dell'agente, non per-progetto.
- **Output:** struttura cartelle, contesto base, skill installate, connettori in `.mcp.json`, commands.
- **Skill/MCP:** —
- **Comando:** (manuale / onboarding) — vedi `SETUP` in fondo.

### Fase 1 — Brief & Discovery  ⟦GATE⟧
Definisci il problema prima di qualsiasi output.
- **Input:** richiesta del cliente.
- **Output:** brief CRO (obiettivo, audience, sorgente traffico, offerta, KPI primario, vincoli). Salvato in `projects/<cliente>/brief/`.
- **Gate:** nessun output prosegue senza brief approvato.
- **Comando:** `/setup`
- **Skill/MCP:** `directives/01_landing_brief`, `directives/08_grill_me` (se requisiti vaghi).

### Fase 2 — Brand DNA
Definisci o estrai l'identità del brand.
- **Input:** brand esistente (URL, asset) o input da zero.
- **Output:** voce + posizionamento in `context/brand/`, reference/asset in `context/references/`.
- **Comando:** `/brand-dna`
- **Skill/MCP:** `brand`, `firecrawl-website-design-clone` / `firecrawl-scrape` (estrai da URL), `the-ai-ad-lab:brand-dna` (color extraction via Playwright).

### Fase 3 — References & inspiration
Raccogli esempi reali che guidano design system e design.
- **Input:** URL/screenshot di riferimento.
- **Output:** reference organizzate in `context/references/` + note.
- **Comando:** (parte di `/brand-dna` o manuale)
- **Skill/MCP:** `firecrawl-scrape`, `firecrawl-website-design-clone`, `firecrawl-competitive-intel`.

### Fase 4 — Design System
Token + regole, esportabili in HTML.
- **Input:** brand DNA + references.
- **Output:** bozza in `output/<slug>/brief/design_system.md` → ⟦GATE⟧ approvazione dell'utente → **promozione** a `DESIGN.md`. Preview HTML opzionale. (Mai scrivere `DESIGN.md` root prima dell'ok.)
- **Comando:** `/brand-dna` (produce il design system)
- **Skill/MCP:** `design-system`, `ui-ux-pro-max`, `design`, Figma MCP (se design-to-code).

### Fase 5 — Architettura & Wireframe
Struttura sezioni, gerarchia informativa, above-the-fold.
- **Input:** brief + design system.
- **Output:** architettura testuale / wireframe in `projects/<cliente>/brief/`.
- **Gate:** approvazione architettura prima del build.
- **Comando:** `/wireframe`
- **Skill/MCP:** `directives/05_frontend_design`, `directives/09_marketing_psychology`, Figma MCP.

### Fase 6 — Copy & content
Headline, sezioni, microcopy, CRO, anti-AI.
- **Input:** architettura + brand voice.
- **Output:** copy per blocco in `projects/<cliente>/copy/`.
- **Comando:** `/copy`
- **Skill/MCP:** `copywriting`, `copy-editing`, `marketing-psychology`, `directives/02_headline_optimization`, `directives/10_advanced_copywriting`, `context/brand/anti-ai-writing-style.md`.

### Fase 7 — Build
Sviluppa la pagina/sito nel design system.
- **Input:** architettura + design system + copy.
- **Output:** HTML/CSS statico self-contained, o app Next.js. In `projects/<cliente>/build/`.
- **Comando:** `/build`
- **Skill/MCP:** `directives/05_frontend_design`, `directives/06_web_artifacts`, `ui-styling`, `impeccable`, `directives/11_framer_motion`.

### Fase 8 — Auth / login  ⟦condizionale⟧
Solo per web app con area riservata.
- **Output:** sign-up/login (Clerk) tematizzati, area protetta.
- **Comando:** `/auth-setup`
- **Skill/MCP:** Clerk MCP (snippet SDK). NB: account+chiavi a mano (no provisioning via MCP).

### Fase 9 — Database / backend  ⟦condizionale⟧
Solo se servono dati per-utente / CRM / tracking.
- **Output:** schema Supabase + webhook + tracking eventi.
- **Comando:** `/db-setup`
- **Skill/MCP:** Supabase MCP (già in `.mcp.json`); integrazione email via API del tool dichiarato in `/setup` (es. Mailchimp/ConvertKit/Brevo/Sendfox…).

### Fase 10 — QA & anti-slop
Qualità prima del deploy.
- **Output:** report QA, fix applicati.
- **Comando:** `/qa`
- **Skill/MCP:** `impeccable` (detector anti-AI-slop), `directives/07_vercel_guidelines`, `directives/03_editing_selfcheck`, a11y WCAG 2.1 AA.

### Fase 11 — Deploy & hosting
Pubblicazione.
- **Output:** sito live su Vercel.
- **Comando:** `/deploy`
- **Skill/MCP:** Vercel MCP, GitHub (repo per deploy continuo).
- **Hardening opzionale:** **Cloudflare** davanti a Vercel (proxy DNS) → WAF, DDoS, bot/scraper mitigation, rate limiting su signup/API, Turnstile sui form. Vedi sezione "Sicurezza & protezione" sotto.

### Fase 12 — Analytics & iterate  ⟦opzionale⟧
Misura e ottimizza.
- **Output:** tracking conversioni, A/B, report.
- **Skill/MCP:** `google-search-console` (SEO), tool analytics esterni (Plausible/PostHog — da valutare).

---

## Comandi del framework

Tutti in `.claude/commands/`. Per ognuno: cosa fa · skill/plugin/MCP attivati · output che ricevi.

**Comandi granulari per-step** (parti da QUALSIASI fase, ognuno lancia il suo subagent con le sue skill): `/brand-dna` (design system), `/wireframe`, `/copy`, `/build`, `/qa`, `/auth-setup`, `/db-setup`, `/deploy`. **Kickoff/orchestratori:** `/setup` (brief + contesto + credenziali), `/new-project` (1→11 in sequenza), `/retro`. Il wireframe produce anche **output HTML visibile**.

### `/setup` — fasi 0-1
- **Fa:** carica il contesto obbligatorio, raccoglie e blocca il brief CRO (obiettivo, audience, traffico, offerta, KPI), scaffolda la cartella progetto, propone la pipeline.
- **Attiva:** `directives/01_landing_brief`, `directives/08_grill_me`.
- **Output:** `output/<slug>_<data>/` (brief/copy/build) + `brief_cro_<slug>.md` approvato + piano dei prossimi passi.

### `/brand-dna` — fasi 2-4
- **Fa:** definisce o estrae l'identità del brand, raccoglie reference, genera il design system.
- **Attiva:** **ricerca** `firecrawl-website-design-clone` / `firecrawl-competitive-intel` / `firecrawl-scrape`; **identità/voce** `brand`; **generazione sistema** `ui-ux-pro-max` + `design-system`; color extraction `the-ai-ad-lab:brand-dna`.
- **Output:** `context/brand/*`, reference in `context/references/`, **`DESIGN.md`** compilato (da `execution/templates/DESIGN.template.md`) + preview HTML opzionale.

### `/wireframe` — fase 5 ⟦GATE⟧
- **Fa:** architettura + wireframe testuale (above-the-fold, sezioni, gerarchia CRO) + output HTML low-fi visibile.
- **Attiva:** `directives/05_frontend_design`, `directives/09_marketing_psychology`, `directives/13_buyer_persona`.
- **Output:** `brief/architettura_<slug>.md` + `brief/wireframe_<slug>.html`. Gate prima del build.

### `/copy` — fase 6
- **Fa:** copy di conversione per blocco (headline, sezioni, microcopy, CTA), in voce brand, anti-AI.
- **Attiva:** `copywriting`, `copy-editing`, `marketing-psychology`, `directives/02_headline_optimization`, `directives/10_advanced_copywriting`, `context/brand/anti-ai-writing-style.md`.
- **Output:** `copy/*.md`.

### `/build` — fase 7
- **Fa:** build del design + HTML/CSS (o app Next.js) nel design system, distintivo, anti-slop.
- **Attiva:** `directives/05_frontend_design`, `directives/06_web_artifacts`, `ui-styling`, `directives/11_framer_motion`, **`impeccable`** (craft + detector).
- **Output:** build in `build/` (HTML statico o app).

### `/qa` — fase 10
- **Fa:** QA qualità + anti-AI-slop + accessibilità + self-check CRO sulla pagina costruita.
- **Attiva:** **`impeccable`** (detector), `directives/07_vercel_guidelines`, `directives/03_editing_selfcheck`.
- **Output:** `build/qa_report.md` + fix applicati.

### `/auth-setup` — fase 8 *(solo web app)*
- **Fa:** sign-up/login Clerk tematizzati + email conferma + middleware + area protetta.
- **Attiva:** Clerk MCP (snippet SDK). Chiavi a mano.
- **Output:** route `/sign-up` `/sign-in`, `middleware.ts`, webhook `user.created`.

### `/db-setup` — fase 9 *(solo web app)*
- **Fa:** schema Supabase + tracking interazioni (chi scarica cosa) + base CRM.
- **Attiva:** **Supabase MCP** (`.mcp.json`).
- **Output:** `schema.sql` (`leads` + `events`, RLS), webhook→insert, tracking download.

### `/deploy` — fase 11
- **Fa:** hosting + deploy su Vercel (landing + app, stesso dominio), preview → production.
- **Attiva:** Vercel MCP, GitHub.
- **Output:** sito live, dominio configurato, URL webhook aggiornati.

### `/new-project` — orchestratore (fasi 1→11)
- **Fa:** lancia l'intero workflow in sequenza fermandosi ai gate; sceglie il branch (statico vs web app).
- **Attiva:** richiama in ordine `/setup` → `/brand-dna` → `/wireframe` → `/copy` → `/build` → [`/auth-setup` → `/db-setup`] → `/qa` → `/deploy`.
- **Output:** progetto completo end-to-end in `output/<slug>_<data>/`.

> **Nota impeccable:** non genera il design system (lo fa `ui-ux-pro-max`/`design-system`), ma lavora sul **design delle pagine vere** in fase di build e QA — sui file HTML/CSS renderizzati. I suoi 23 comandi craft (`/impeccable craft|shape|polish|colorize|typeset|layout|delight…`) migliorano la resa visiva; i 41 detector deterministici bocciano l'AI-slop (gradienti viola, bounce easing, grigio-su-colore, em dash). Quindi sì: impeccable è centrale nel design delle pagine, ma a valle (build + QA), non nella definizione astratta dei token in `DESIGN.md`.

---

## Gap skill/connettori

| Serve | Stato |
|---|---|
| Supabase MCP | ✅ in `.mcp.json` (`@supabase/mcp-server-supabase`) → serve solo `SUPABASE_ACCESS_TOKEN` nel `.env` |
| Email tool (Mailchimp/ConvertKit/Brevo/Sendfox…) | ⚠️ dichiarato dall'utente in `/setup` — API REST diretta |
| Analytics conversioni | ⚠️ solo `google-search-console` (SEO); valutare Plausible/PostHog |
| Clerk provisioning | ⚠️ MCP dà solo snippet, non crea l'app → chiavi a mano |
| Tutto il resto (design, copy, build, QA, deploy) | ✅ coperto |

---

## Ordine del flusso per tipo di progetto

Sequenza in cui l'orchestratore lancia i subagent. ⟦GATE⟧ = serve ok dell'utente.

**Landing page (statica)**
1. Brief & Discovery *(main, inline)* ⟦GATE⟧
2. `design-system-agent` — brand DNA + design system
3. `wireframe-agent` — architettura ⟦GATE⟧
4. `copy-agent`
5. `design-build-agent`
6. `qa-agent`
7. `deploy-agent` ⟦GATE⟧
8. `/retro` — retrospettiva

**Mini-site (più pagine)**
Come landing, ma: wireframe = sitemap + wireframe per pagina; copy e build per ogni pagina. `backend-agent` solo se servono form/CMS/area.
1. Brief ⟦GATE⟧ → 2. `design-system-agent` → 3. `wireframe-agent` (sitemap+pagine) ⟦GATE⟧ → 4. `copy-agent` → 5. `design-build-agent` (multi-pagina) → 6. `qa-agent` → 7. `deploy-agent` ⟦GATE⟧ → 8. `/retro`

**Web app completa (login/dati)**
1. Brief & Discovery ⟦GATE⟧
2. `design-system-agent`
3. `wireframe-agent` (incl. flussi app: signup, area riservata) ⟦GATE⟧
4. `copy-agent`
5. `design-build-agent` (scaffold app + UI)
6. `backend-agent` (Clerk auth + Supabase db + webhook/tracking)
7. `qa-agent` (flusso end-to-end)
8. `deploy-agent` ⟦GATE⟧
9. `/retro`

**Regola d'ordine:** brand DNA sempre presto; copy dopo il wireframe e prima del build; backend dopo lo shell UI; QA prima del deploy; deploy ultimo; retro dopo.

**Step opzionali da PROPORRE all'utente** (non obbligatori, ma migliorano l'output — chiedili al momento giusto, non saltarli in silenzio):
- In **deploy**: `Cloudflare hardening?` (WAF/bot/rate-limit/Turnstile, col dominio reale) → protegge IP e lead.
- In **brand DNA**: `ricerca firecrawl approfondita?` (benchmark reali → design migliore, ma costa crediti).
- Post-lancio: `A/B test / analytics?`.

## Miglioramento continuo (feedback loop)

Il workflow si auto-migliora: ogni feedback diventa una regola riusabile.

1. Durante/dopo un progetto l'utente dà feedback ("copy troppo AI", "poco spazio", "mancava questo step").
2. `/retro` estrae la lezione e la scrive in `LEARNINGS.md` (cosa · perché · come applicarla · dove).
3. Se la lezione tocca un artefatto stabile (un subagent, una directive, `DESIGN.md`, `anti-ai-writing-style.md`), `/retro` propone l'edit mirato **con approvazione** (le directive non si toccano senza ok).
4. `LEARNINGS.md` viene **letto a inizio di ogni progetto** da orchestratore e subagent → le lezioni si applicano subito.

Più pagine costruiamo, più gli agenti migliorano.

## Sicurezza & protezione (Cloudflare) — opzionale ma consigliato

**Cosa è:** Cloudflare si mette **davanti** a Vercel come proxy (cambi i nameserver / punti il DNS su Cloudflare con record "proxied"). Il traffico passa da Cloudflare → poi a Vercel.

**Serve davvero?** Vercel offre già CDN, HTTPS e DDoS di base, quindi non è obbligatorio per un MVP. Diventa utile (e poi importante con traffico vero) per cosa che Vercel **non** copre bene:

- **Hide origin + DDoS/WAF:** l'IP di origine resta nascosto; regole WAF bloccano attacchi e pattern malevoli.
- **Bot & scraper mitigation:** riduce lo scraping automatico dei contenuti → protezione dell'**IP** (la tua proprietà intellettuale: copy, checklist, struttura). NB: nulla rende il contenuto incopiabile al 100% (il browser lo deve pur mostrare), ma alza l'attrito contro i bot.
- **Rate limiting** su `/sign-up` e `/api/*`: blocca abusi e signup spam/fake → protegge il database e la qualità dei lead.
- **Turnstile** (CAPTCHA-free) sui form: ferma i bot di iscrizione senza frizione per gli umani.
- **DNS + cache + analytics** centralizzati.

**Quando aggiungerlo:** non al primo deploy di prova su Vercel. Lo metti quando colleghi il **dominio reale** e/o vedi abusi/scraping. Per una web app con signup pubblico: Turnstile sul form + rate limit sull'API sono il valore più alto.

**Cosa serve:** account Cloudflare (free tier basta), dominio gestito da Cloudflare (nameserver), eventuale `CLOUDFLARE_API_TOKEN` per automazioni. Niente skill/MCP dedicato → config da dashboard.

## SETUP (onboarding per condividere il template)

Per un collega che parte da zero:
1. `git clone` del template.
2. Installare le skill/plugin pesanti via marketplace (impeccable, ui-ux-pro-max, firecrawl, the-ai-ad-lab) — vedi lista in `directives/index.md`.
3. Copiare `.env.example` → `.env` e inserire le chiavi (firecrawl, clerk, supabase, email tool, vercel).
4. Connettori in `.mcp.json` (chiavi via env).
5. Lanciare `/setup` per il primo progetto.

Principio cartelle: engine pulito e brand-agnostic; ogni cliente è una cartella in `projects/` (o un clone separato del template). I segreti non si committano mai.
