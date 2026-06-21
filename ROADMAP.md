# Roadmap — [PROGETTO CORRENTE]

> Piano del progetto attivo. Vuoto nel template: lo compila `/setup` quando parte un progetto.
> Legenda: ☐ da fare · ☑ fatto · **[U]** = serve l'utente (chiavi/decisioni) · **[C]** = lo fa Claude

---

## Decisioni confermate
[Tabella delle scelte di progetto: tipo (landing statica / mini-site / web app), stack, hosting, auth, email tool, dati.]

| Tema | Decisione |
|---|---|
| Tipo progetto | [landing statica / mini-site / web app] |
| Hosting | [Vercel / Firebase Hosting] |
| Auth | [Clerk / Firebase Auth / nessuno] |
| Database | [Supabase / Firestore / nessuno] |
| Email tool | [Mailchimp / ConvertKit / Brevo / Klaviyo / Sendfox / …] |

---

## Architettura target
[Schema del funnel/architettura: landing → azione → (area riservata) → tracking. Branch statico vs web app.]

---

## Fasi (adatta al tipo di progetto)

### FASE 0 — Brief & prep
- ☐ **[C]** Brief CRO approvato (`/setup`)
- ☐ **[U]** Lista credenziali disponibili ora / dopo

### FASE 1 — Brand DNA + design system
- ☐ **[C]** `DESIGN.md` compilato e approvato ⟦gate⟧

### FASE 2 — Wireframe + copy + build
- ☐ **[C]** Wireframe ⟦gate⟧ → copy anti-AI → build nel design system

### FASE 3 — (web app) Auth + DB + tracking
- ☐ **[U]** Chiavi auth/DB + email tool
- ☐ **[C]** Sign-up/login, webhook, schema, tracking eventi

### FASE 4 — QA + Deploy
- ☐ **[C]** QA anti-slop + a11y + self-check CRO
- ☐ **[U]** Repo GitHub + dominio
- ☐ **[C]** Deploy preview → production ⟦gate⟧
- ☐ **[CHIEDI]** Cloudflare hardening? (col dominio reale)

---

## Chiavi necessarie (riepilogo)
[Compila per il progetto: servizio · cosa serve · quando.]
