---
description: Fase 11 — deploy online (GitHub + Vercel; o Firebase Hosting). Landing + app stesso dominio.
argument-hint: [progetto / dominio]
---

# /deploy — Hosting & deploy

Pubblica online. Un solo progetto: landing statica a `/`, app per le route account/area. **Mai pubblicare senza ok esplicito.** Deploy = azione esterna: conferma prima, preview prima di production.

Input: **$ARGUMENTS**

## Prerequisiti
- Build passata dalla QA (Fase 10).
- `gh` autenticato (`gh auth status`). **Vercel token** (Account Settings → Tokens) o MCP Vercel.
- Env di produzione pronte (Clerk/Supabase/email tool). Vedi `CONNECTORS.md`.

## Stack A — Vercel (Next.js) — procedura testata
1. **Git identity (CRITICO):** imposta `git config user.email` con **l'email dell'account GitHub/Vercel** dell'utente. Se il commit ha un'email a caso (es. `nome@host.local`), Vercel **blocca** il deploy: *"no git user associated with the commit"*. Verifica `git log -1 --format=%ae` prima di pushare.
2. **Repo:** `git init` nella cartella app → `.gitignore` esclude `node_modules`, `.next`, `.env*` → commit → `gh repo create <nome> --private --source=. --push`.
3. **Link Vercel:** `vercel link --yes --project <nome> --scope <team> --token=$VERCEL_TOKEN` (crea progetto + collega il repo GitHub = auto-deploy attivo).
4. **Env:** imposta tutte le variabili di `.env.local` su **Production + Preview** (API `POST /v10/projects/{id}/env` o `vercel env add`). Il `webhook secret` si aggiunge dopo lo step 7.
5. **Deployment Protection:** se il sito è pubblico (lead capture / webhook in arrivo), **disattivala** (`PATCH /v9/projects/{id}` `{"ssoProtection":null}`), altrimenti tutto risponde 401.
6. **Deploy:** `vercel deploy --prod --yes --scope <team> --token=$VERCEL_TOKEN`. ⚠️ non lanciare CLI **e** git-push insieme: due deploy concorrenti vanno in `BLOCKED` su Hobby. Uno solo per volta. Poll fino a `READY`.
7. **Webhook auth:** nel dashboard auth (Clerk) crea l'endpoint `https://<dominio>/api/webhooks/clerk`, evento `user.created` → copia `whsec_…` → aggiungilo alle env Vercel → redeploy.
8. **Dominio custom** se fornito (`[S]`) → aggiorna gli URL webhook al dominio prod.

## Stack B — Firebase Hosting (React/Vite)
`firebase deploy --only hosting` su canale **preview** (`hosting:channel:deploy`) prima, poi production dopo ok. Rewrites in `firebase.json` per same-domain.

## Verifica end-to-end (senza browser)
- Route pubbliche → HTTP 200 (landing, /grazie, /sign-up). Area → redirect auth. Webhook → 400 senza firma (vivo + secret presente).
- **Test del cerchio completo:** crea un utente via **Clerk API** (`POST /v1/users` con secret key) → fa scattare `user.created` → verifica **lead in Supabase** + **contatto nell'email tool** (lista corso). Poi **pulisci** (delete utente Clerk + riga Supabase + contatto).

## Regole
- Conferma prima del production. Preview prima. Segreti solo in env (mai committati). Cloudflare hardening = proponi col dominio reale, non automatico.
