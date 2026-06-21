# CONNECTORS — connettori, chiavi e cosa fare dentro ognuno

Guida operativa ai servizi/connettori usati dall'agente. Pensata per copia-incolla in slide.
Tutte le chiavi vivono in `.env` / `.env.local` (mai committate) o negli MCP via `${VAR}`. Vedi `.env.example`.

## Quadro d'insieme

| Connettore | A cosa serve | Tipo | Chiave/env | Dove si configura |
|---|---|---|---|---|
| **GitHub** | Repo + auto-deploy | CLI `gh` | OAuth (`gh auth login`) | github.com |
| **Vercel** | Hosting landing + app | MCP + CLI/token | `VERCEL_TOKEN` | vercel.com |
| **Supabase** | DB lead + eventi | MCP + chiavi | `NEXT_PUBLIC_SUPABASE_URL`, `SUPABASE_SERVICE_ROLE_KEY` | supabase.com |
| **Clerk** | Auth/login + webhook | SDK + dashboard | `…CLERK_PUBLISHABLE_KEY`, `CLERK_SECRET_KEY`, `CLERK_WEBHOOK_SIGNING_SECRET` | dashboard.clerk.com |
| **Email tool*** | Corso/automation email | API REST | `EMAIL_TOOL_API_TOKEN`, `EMAIL_TOOL_LIST_ID` | dipende dal tool |
| **Firecrawl** | Ricerca/scrape/design-clone | MCP | `FIRECRAWL_API_KEY` | firecrawl.dev |
| **Cloudflare** (opz.) | WAF/bot/rate-limit davanti a Vercel | dashboard/token | `CLOUDFLARE_API_TOKEN`, Turnstile keys | cloudflare.com |

\* L'email tool si chiede in `/setup` (l'agente è agnostico): Mailchimp / ConvertKit / Brevo / ActiveCampaign / Klaviyo / Sendfox / altro. Usa nomi env neutri (`EMAIL_TOOL_*`) o quelli del provider scelto.

---

## GitHub
**Serve a:** versionare il codice e abilitare l'auto-deploy su Vercel.
- [ ] `gh auth login` (scope: `repo`, `workflow`)
- [ ] `git init` nella cartella app → commit
- [ ] `gh repo create <nome> --private --source=. --push`
- [ ] Verifica: `.env*` e `node_modules` in `.gitignore` (mai committare segreti)

## Vercel
**Serve a:** ospitare landing statica (`/`) + app Next.js (route account/area) sullo stesso dominio.
- [ ] Token: **Account Settings → Tokens → Create Token**
- [ ] `vercel link --project <nome> --scope <team>` (crea progetto + collega repo GitHub)
- [ ] Env: imposta le stesse di `.env.local` su **Production + Preview** (Project → Settings → Environment Variables)
- [ ] Deploy: `vercel deploy` (preview) → `vercel deploy --prod` (production)
- [ ] **Deployment Protection**: se il sito è pubblico (lead capture) va **disattivata** (Settings → Deployment Protection), altrimenti i webhook e i visitatori ricevono 401
- [ ] Dominio custom: Project → Domains

## Supabase
**Serve a:** database lead (`leads`) + eventi di interazione (`events`), con RLS.
- [ ] Crea progetto → **Project URL** + **chiavi** (Settings → API): `publishable` (client) e **`secret`/`service_role`** (server-only)
- [ ] Applica lo schema: **SQL Editor** → incolla `supabase/migrations/0001_init.sql` → Run (NON incollare il path!)
- [ ] RLS **attiva**: nessuna policy pubblica, l'accesso passa solo dal service_role lato server
- [ ] (Opz.) MCP: `.mcp.json` con `https://mcp.supabase.com/mcp?project_ref=<ref>` (OAuth) per gestire il DB da Claude
- [ ] Mai esporre la secret key nel client

## Clerk
**Serve a:** account utente, login, email di verifica, webhook `user.created`.
- [ ] Crea app → **Publishable key** + **Secret key**
- [ ] **Social connections**: attiva Email/Password + Google (+ Facebook) — zero codice, è un toggle
- [ ] **Webhooks → Add Endpoint**: URL `https://<dominio>/api/webhooks/clerk`, evento **`user.created`** → copia **Signing Secret** (`whsec_…`) in env
- [ ] (Opz.) Email verification = **link** se vuoi il gate "conferma via email" prima dell'accesso
- [ ] Tema: `appearance` API mappata sul design system (no look default)

## Email tool (provider a scelta)
**Serve a:** iscrivere automaticamente i nuovi account alla lista → parte il corso/automation email.
Provider agnostico (Mailchimp / ConvertKit / Brevo / ActiveCampaign / Klaviyo / Sendfox / …), si chiede in `/setup`.
- [ ] **Settings → API** del provider scelto → crea **API token**
- [ ] Crea/usa la **lista** del corso → recupera il **List ID** (via API del provider)
- [ ] Collega l'**automation** del corso a quella lista (è qui che parte la sequenza di email)
- [ ] Il webhook Clerk `user.created` chiama l'API e iscrive il contatto alla lista
- [ ] Cambio provider = sostituisci il modulo `lib/<email-tool>.ts` con l'API del tuo tool

## Firecrawl
**Serve a:** ricerca web, scrape, clonazione design system da siti reali (fasi brand/design).
- [ ] **API key** da firecrawl.dev → `FIRECRAWL_API_KEY`
- [ ] MCP in `.mcp.json` (già presente) — usa la suite `firecrawl_*`
- [ ] ⚠️ consuma crediti a pagamento → chiedi conferma prima di ricerche grosse

## Cloudflare (opzionale, col dominio reale)
**Serve a:** sicurezza davanti a Vercel: WAF, DDoS, bot/scraper, rate-limit su signup/API, Turnstile sui form.
- [ ] Dominio su Cloudflare → proxy davanti a Vercel
- [ ] Turnstile keys per i form (`TURNSTILE_SITE_KEY`, `TURNSTILE_SECRET_KEY`)
- [ ] Da proporre, non automatico (free tier sufficiente)

---

## Ordine consigliato (da zero)
1. GitHub (repo) → 2. Clerk (auth) → 3. Supabase (DB + migration) → 4. Email tool (lista + token) → 5. Vercel (env + deploy) → 6. Clerk webhook sull'URL Vercel → 7. test flusso end-to-end → 8. (opz.) Cloudflare col dominio.
