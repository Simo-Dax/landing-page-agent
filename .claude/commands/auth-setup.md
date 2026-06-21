---
description: Fase 8 — pagine di autenticazione/login con Clerk, tematizzate sul design system
argument-hint: [progetto / route da proteggere]
---

# /auth-setup — Auth & login (Clerk)

Aggiunge sign-up/login e area protetta a una web app. Solo per progetti con area riservata (branch web app del `FRAMEWORK.md`). Per una landing statica si salta.

Input: **$ARGUMENTS**

## Prerequisiti
- App Next.js già scaffoldata (se manca, vedi `/build` / `/new-project`).
- Design system in `DESIGN.md` (per tematizzare i componenti).
- Clerk MCP disponibile per gli snippet SDK aggiornati.

## Step
1. **[S] Account Clerk** → `NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY` + `CLERK_SECRET_KEY` in `.env.local`. **Provider**: attiva Email/Password + Google (+ Facebook) nel dashboard (toggle, zero codice).
2. `ClerkProvider` in `layout.tsx` (con `itIT` localization se IT). `<SignUp>`/`<SignIn>` su route catch-all (`/sign-up/[[...sign-up]]`), email di verifica attiva.
3. **Tematizza** via `appearance` API mappando i token di `DESIGN.md` (colorPrimary, font, bottoni pill, input soft-fill). Niente look default.
4. `middleware.ts` → `clerkMiddleware` + matcher robusto; `auth.protect()` sulle route riservate (es. `/area-membri`, `/api/track`).
5. **Flusso post-signup:** redirect a una **thank-you page** (`/grazie`, stile design system: "controlla l'email"). Il form della landing passa nome+email a `/sign-up` (Clerk `initialValues` per precompilare). Imposta `NEXT_PUBLIC_CLERK_SIGN_UP_FALLBACK_REDIRECT_URL=/grazie`.
6. Webhook `user.created` (verifica svix) → endpoint `/api/webhooks/clerk`. La firma usa **`CLERK_WEBHOOK_SIGNING_SECRET`** (generato in Clerk → Webhooks dopo aver puntato l'endpoint al dominio live). Gancio per `/db-setup` (lead + email tool).

> Stack alternativo: **Firebase Auth** (email/password + Google), UI custom tematizzata, route guard via `onAuthStateChanged`.

## Regole
- Mai auth fatta in casa: usa i componenti del provider.
- Provisioning (account/chiavi) lo fa l'utente.
- Coerenza visiva totale col resto (stesso ambiente premium dietro al login).
