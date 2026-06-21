# Index & Skill Orchestrator — Landing Page & CRO Agent

Questo file è l'**indice statico** di directives e skill + la mappa di **quale agente usa cosa**. Il routing a runtime (fase → subagent → skill → gate) vive nella skill `orchestrator` (`.claude/skills/orchestrator/`). Niente doppione: qui il catalogo, lì la guida operativa.

> **Workflow completo:** vedi [`FRAMEWORK.md`](../FRAMEWORK.md) nel root — il processo step-by-step in 12 fasi (brief → brand DNA → references → design system → wireframe → copy → build → [auth/db] → QA → deploy → analytics), templatizzabile e condivisibile.
>
> **Comandi che lanciano le fasi:** `/setup` (fasi 0-1), `/brand-dna` (2-4), `/wireframe`, `/copy`, `/build`, `/auth-setup`, `/db-setup`, `/qa`, `/deploy`, `/new-project` (orchestratore), `/retro`.
>
> Le directives qui sotto sono le **procedure** richiamate dalle fasi. Questo agente è un **template a due livelli**: engine riusabile (directives, commands, skills, `.mcp.json`) + brand layer per-cliente (`PRODUCT.md`, `DESIGN.md`, `context/`).

## Directives Core (Processo Landing Page)

0. **[00_cro_principles.md](00_cro_principles.md)** — Principi CRO non negoziabili
   - Le regole di base che ogni output deve rispettare (lette per prime, sempre)
   - Riferimento per il self-check (`03_editing_selfcheck.md`)

1. **[01_landing_brief.md](01_landing_brief.md)** — Brief CRO per Landing Page
   - Raccolta informazioni obbligatorie (obiettivo, audience, traffico, offerta, KPI)
   - Costruzione del brief strutturato con checkpoint obbligatorio
   - Gateway: nessun output viene prodotto senza brief approvato

2. **[02_headline_optimization.md](02_headline_optimization.md)** — Headline & Subheading Optimization
   - Generazione varianti headline (8+ opzioni con leve diverse)
   - Valutazione basata su specificità, curiosity, chiarezza, tono
   - Combinazioni headline + subheading ottimizzate

3. **[03_editing_selfcheck.md](03_editing_selfcheck.md)** — Editing & Self-Check CRO
   - Verifica dell'output contro i principi CRO
   - Self-check prima del delivery finale

4. **[04_references-tecniche-design.md](04_references-tecniche-design.md)** — References per Tecniche di Design
   - Pattern e riferimenti per design di landing page

## Skills Specializzate

### 05 — Frontend Design
- **[05_frontend_design/](05_frontend_design/)** — Frontend Design Skill
  - Creazione di interfacce frontend distintive e production-grade
  - Evita estetica generica "AI slop"
  - Focus su tipografia, colore, motion, composizione spaziale

### 06 — Web Artifacts Builder
- **[06_web_artifacts/](06_web_artifacts/)** — Web Artifacts Builder Skill
  - Generazione di componenti React + Tailwind CSS interattivi e funzionali
  - Integrazione con shadcn/ui
  - Output pronti per l'uso diretto nell'interfaccia di Claude

### 07 — Vercel Web Design Guidelines
- **[07_vercel_guidelines/](07_vercel_guidelines/)** — Vercel Web Design Guidelines
  - Audit di interfacce contro 100+ regole di accessibilità, UX e qualità production-grade
  - Checklist per verifica standard Vercel
  - Garanzia di conformità best practice

### 08 — Grill Me (Requirements Handshake)
- **[08_grill_me/](08_grill_me/)** — Grill Me Skill
  - Raccolta approfondita dei requisiti attraverso domande mirate
  - "Requirements handshake" per ridurre ambiguità prima della creazione
  - Previene iterazioni inutili e garantisce allineamento

### 09 — Marketing Psychology & Persuasion
- **[09_marketing_psychology/](09_marketing_psychology/)** — Marketing Psychology Skill
  - 70+ mental models organizzati per applicazione marketing
  - Principi psicologici, bias cognitivi, behavioral science
  - Framework di persuasione per landing page ad alta conversione

### 10 — Advanced Copywriting Framework
- **[10_advanced_copywriting/](10_advanced_copywriting/)** — Advanced Copywriting Skill
  - Framework avanzati per copy di conversione
  - Integrazione con headline optimization
  - Copy per homepage, landing page, pricing, feature pages

### Skill installata — UI/UX Pro Max (→ `.claude/skills/`)
- **Skill funzionale** (non una directive) installata in `.claude/skills/ui-ux-pro-max/` (+ skill companion: `design`, `design-system`, `ui-styling`, `brand`, `banner-design`, `slides`)
  - Design intelligence: 67 stili UI, 161 palette, 57 font pairing, 161 regole per industry
  - Genera design system su misura; si auto-attiva quando chiedi lavoro UI/UX
  - Fonte: github.com/nextlevelbuilder/ui-ux-pro-max-skill

### Skill installata — Impeccable (→ `.claude/skills/`)
- **Skill funzionale** (non una directive) installata in `.claude/skills/impeccable/` (+ agent in `.claude/agents/`)
  - 23 comandi `/impeccable` (craft, shape, critique, audit, polish, animate, colorize, typeset, layout, delight…)
  - 41 detector deterministici anti-AI-slop (gradienti viola, bounce easing, grigio su colore…)
  - Setup: `node .claude/skills/impeccable/scripts/context.mjs` a inizio sessione
  - Fonte: github.com/pbakaus/impeccable

### 11 — Framer Motion / Motion (reference directive)
- **[11_framer_motion/](11_framer_motion/)** — Reference animazioni Motion (ex Framer Motion)
  - API motion.dev (React + vanilla): reveal scroll, stagger, gesture, AnimatePresence, scroll-linked
  - Pattern CRO-first + come specificare animazioni per dev / Framer / Webflow
  - Regole performance e `prefers-reduced-motion`

---

## Come Usare Questo Sistema

### Workflow Standard per Nuova Landing Page
1. Parti sempre da **01_landing_brief.md** — nessun output senza brief approvato
2. Usa **08_grill_me** se i requisiti non sono chiari o completi
3. Applica **09_marketing_psychology** per identificare leve persuasive
4. Genera copy con **02_headline_optimization** e **10_advanced_copywriting**
5. Crea l'interfaccia con **05_frontend_design** o **06_web_artifacts**
6. Verifica qualità con **07_vercel_guidelines**
7. Self-check finale con **03_editing_selfcheck**

### Quando Usare Ogni Skill
- **05_frontend_design**: per design custom distintivo e unico
- **06_web_artifacts**: per componenti React/Tailwind rapidi e funzionali
- **07_vercel_guidelines**: per audit di qualità pre-produzione
- **08_grill_me**: quando i requisiti iniziali sono vaghi o incompleti
- **09_marketing_psychology**: per applicare principi psicologici al copy
- **10_advanced_copywriting**: per copy avanzato oltre le headline

---

## Note
- Tutte le directives core (01-04) sono **obbligatorie** nel processo
- Le skills (05-10) sono **opzionali** e si usano in base al contesto del progetto
- Consulta sempre `context/brand/tone_of_voice.md` e `context/brand/business_strategy.md` prima di iniziare

---

## Brand DNA & Personas (directives 12-13)

### 12 — Brand DNA da URL (`12_brand_dna/`)
- Reverse-engineering del DNA di un brand **esistente** da nome + URL (Playwright + web search) → **output HTML** `brand-dna-[slug].html`.
- Usalo quando parti da un brand reale da analizzare/clonare. Per il nostro framework, adatta l'output a `output/<slug>/brief/`.
- **Agente:** `design-system-agent` (Fase 2).
- Nota: nasce in contesto ad-creative; per landing/CRO serve la parte identità/visual, non la generazione di prompt immagine.

### 13 — Buyer Persona Creation (`13_buyer_persona.md`)
- Definisce le buyer personas dal contesto brand (pain, desideri, obiezioni, trigger, canali, message angle). Non genera immagini.
- **Agente:** Fase 1 (brief/discovery), `copy-agent`, `wireframe-agent`.

## Skill orchestrator — quale agente usa cosa

La mappa completa fase → skill/MCP è in `CLAUDE.md` (sezione "Framework operativo") e nella skill `orchestrator`. In sintesi:

| Subagent | Directives / Skill / MCP |
|---|---|
| `design-system-agent` | `brand`, `design-system`, `ui-ux-pro-max`, `firecrawl-website-design-clone`, `12_brand_dna` |
| `wireframe-agent` | `05_frontend_design`, `09_marketing_psychology`, `13_buyer_persona` |
| `copy-agent` | `copywriting`, `copy-editing`, `marketing-psychology`, `02_*`, `10_*`, `13_buyer_persona`, anti-ai |
| `design-build-agent` | `05_frontend_design`, `06_web_artifacts`, `ui-styling`, `impeccable`, `11_framer_motion` |
| `qa-agent` | `impeccable`, `07_vercel_guidelines`, `03_editing_selfcheck` |
| `backend-agent` | Clerk MCP, Supabase MCP |
| `deploy-agent` | Vercel MCP, Cloudflare (opz.) |
