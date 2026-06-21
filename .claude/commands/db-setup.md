---
description: Fase 9 — database/backend con Supabase (schema, RLS, tracking eventi, CRM)
argument-hint: [cosa tracciare / entità]
---

# /db-setup — Database & backend (Supabase)

Aggiunge persistenza dati: iscritti + tracking interazioni (chi scarica cosa) + base CRM. Solo quando servono dati per-utente (branch web app del `FRAMEWORK.md`).

Input: **$ARGUMENTS**

## Prerequisiti
- **[S] Progetto Supabase** → URL + service_role key + access token. In `.env` (vedi `.env.example`).
- **Supabase MCP** attivo (definito in `.mcp.json`). Verifica che sia abilitato.

## Step
1. Modello dati minimale ed estensibile (provider-agnostico):
   - `leads` — keyed **`auth_user_id`** (unique, l'id dell'auth provider), email, name, source, created_at, tags[], reward_points (default 0), metadata jsonb.
   - `events` — `auth_user_id`, type (`checklist_toggle`/`download`/`login`/…), payload jsonb, created_at. (ledger interazioni)
2. Scrivi la migration in `supabase/migrations/0001_init.sql` e applicala: **SQL Editor** (incolla il contenuto, non il path) **o** Supabase MCP (`apply_migration`). **RLS attiva**: nessuna policy pubblica, accesso solo da service-role lato server. Nessuna password in Supabase (l'auth resta nell'auth provider).
3. Webhook `user.created` (verifica svix) → upsert riga in `leads` **+** push all'**email tool dell'utente** (Sendfox/Mailchimp/… dichiarato in `/setup`) per avviare il corso/automation.
4. **Tracking:** route `/api/track` protetta → ogni azione utile (toggle checklist, download, login) → insert in `events`.
5. **Verifica end-to-end** (senza browser): crea un utente via API auth → controlla lead in Supabase + contatto nell'email tool → pulisci l'utente di test.
6. (Opzionale) Vista CRM `/admin`: chi è iscritto, ultimo login, cosa ha fatto.

> Stack alternativo: **Firestore** (`leads/{uid}` + `events`) con **security rules** + Cloud Function `onCreate`. Stesso modello logico.

## Regole
- DB minimale: niente schema speculativo. Aggiungi colonne quando servono davvero.
- Service-role / chiave privilegiata solo server-side, mai esposta al client.
- DB = layer dati/CRM. Identità e login restano nell'auth provider. Email tool agnostico.
