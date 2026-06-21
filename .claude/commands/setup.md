---
description: Avvia un nuovo progetto landing page — carica il contesto, raccoglie il brief CRO e prepara il workflow design+sviluppo
argument-hint: [nome progetto o brief rapido]
---

# /setup — Kickoff progetto Landing Page

Sei il landing page engine dell'utente. Questo comando avvia un nuovo progetto e imposta il workflow completo. NON produrre design o copy qui: questo step serve a caricare il contesto, allineare il brief e scaffoldare le cartelle.

Input utente: **$ARGUMENTS**

## Step 0 — Carica il contesto (obbligatorio, non saltabile)

Leggi prima di tutto:
- `CLAUDE.md` (regole operative)
- `context/brand/tone_of_voice.md`
- `context/brand/business_strategy.md`
- `context/brand/anti-ai-writing-style.md`
- `PRODUCT.md` (utenti, brand personality, anti-references, design principles)
- `directives/00_cro_principles.md`
- `directives/index.md` (mappa di directives e skill)

Se questi file non esistono o sono vuoti, fermati e segnalalo.

## Step 1 — Cosa vuoi costruire? (prima domanda, sempre)

Chiedi all'utente, in chiaro, **cosa intende costruire** e adatta tutto il resto a questo. Tre tipi:
- **Landing statica** — una pagina, niente login/dati. Serve solo: design + copy + hosting.
- **Mini-site** — più pagine statiche. Come landing, iterato per pagina.
- **Web-app** — landing + area riservata con **login + dati** (es. corso, membership). Serve in più: **auth + database + email tool + webhook**.

Spiega tu all'utente, in 4-5 bullet, **l'intero percorso** che faremo (le fasi/command) e **tutte le credenziali** che serviranno per il tipo scelto, così sa cosa procurare. Non dare per scontato che le conosca: elencagliele.

## Step 1b — Brief CRO (checkpoint obbligatorio)

Segui `directives/01_landing_brief.md`. Raccogli e blocca:
- Obiettivo di conversione + KPI primario
- Audience (quale buyer persona dal brand layer / `PRODUCT.md`, o da definire con `directives/13_buyer_persona.md`)
- Sorgente di traffico (Google Ads, Meta, SEO, email, referral) → il message match è un requisito
- Offerta e proposta di valore
- Vincoli (lingua, tool, deadline, page builder di destinazione)

Se i requisiti sono vaghi o incompleti, usa `directives/08_grill_me/` per un requirements handshake prima di procedere. Massimo le domande che servono, poi proponi assunzioni esplicite e vai avanti.

**Gate:** non si passa allo step successivo senza brief approvato esplicitamente dall'utente.

## Step 1c — Credenziali & stack (raccolta anticipata)

Prima di scaffoldare, **elenca la lista completa di tutte le credenziali** che il progetto potrebbe richiedere (in base al tipo scelto nello Step 1) e chiedi per ognuna se è **disponibile ora** o si affronta **dopo**. Rimanda a `CONNECTORS.md` per "dove prenderle + cosa fare dentro ogni servizio". Obiettivo: chi usa l'agente arriva a backend/deploy con tutto pronto, senza blocchi a metà.

Checklist credenziali da spuntare (disponibile ora / dopo):
- **Auth:** Clerk (pk + sk + webhook secret) **oppure** Firebase Auth (config + service account)
- **Database:** Supabase (URL + service_role + access token MCP) **oppure** Firestore (Firebase project)
- **Email marketing tool:** ⚠️ **chiedi SEMPRE quale usa l'utente** — non assumere. Può essere Mailchimp / ConvertKit / Brevo / ActiveCampaign / Klaviyo / Sendfox / altro. Raccogli API token + ID lista del tool dichiarato. Il webhook `user.created` punterà a quel tool.
- **Hosting:** Vercel (token/OAuth) **oppure** Firebase Hosting
- **Dominio** (opzionale) · **Cloudflare/Turnstile** (opzionale) · **Firecrawl** (ricerca)

Registra in una tabella "servizio · cosa serve · disponibile ora?/dopo" e salvala nel brief. Non bloccare il progetto per le chiavi "dopo": scaffolda con placeholder in `.env.local.example`.

## Step 2 — Scaffold del progetto

Una volta approvato il brief, crea la struttura output (slug kebab-case + data):

```
output/<slug>_<YYYY-MM-DD>/
├── brief/        # brief_cro, architettura, self_check
├── copy/         # copy per blocco
└── build/        # HTML/CSS finali
```

Salva il brief approvato in `brief/brief_cro_<slug>.md`.

## Step 3 — Definisci il workflow e i prossimi passi

Proponi la pipeline per questo progetto, indicando i checkpoint:

1. **Design system** → serve un nuovo design system? Se sì lancia `/brand-dna`. Se esiste già (`DESIGN.md` o `context/brand/`), confermalo e riusalo.
2. **Architettura + copy** → above the fold, struttura sezioni, gerarchia (directive 01 → 09 marketing psychology → 02/10 copy).
3. **Build** → `/build` per il design e l'HTML.
4. **QA** → `directives/07_vercel_guidelines/` + impeccable anti-slop, poi `directives/03_editing_selfcheck.md`.

Chiudi elencando in 3-5 bullet "cosa facciamo adesso" e quale comando lanciare per primo.

## Regole
- Mai produrre output senza aver letto il contesto (Step 0).
- Mai procedere oltre lo Step 1 senza brief approvato.
- Mai inventare dati: numeri e social proof solo dal contesto o dalla sorgente; altrimenti `[DATO DA VERIFICARE]`.
- Italiano salvo diversa indicazione dell'audience target.
