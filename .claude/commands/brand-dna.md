---
description: Costruisce un design system completo (token + regole) a partire dall'input dell'utente — brand, reference o URL da clonare
argument-hint: [brand / colori / font / URL di riferimento]
---

# /brand-dna — Sviluppo Design System

Produci un design system su misura, in stile editoriale anti-slop, pronto per essere passato al build. L'output deve avere la stessa struttura di `DESIGN.md`: frontmatter con i token + prosa con regole nominate.

Input utente: **$ARGUMENTS**

## Step 0 — Contesto brand

Leggi:
- `PRODUCT.md` (brand personality, anti-references, design principles)
- `context/brand/tone_of_voice.md`
- `execution/templates/DESIGN.template.md` come **struttura da compilare**; `DESIGN.md` come esempio già riempito (non copiare i valori)
- `context/brand/` (asset, design system esistenti, foto, guidelines già presenti)
- `context/references/` (reference visivi raccolti)

## Step 1 — Raccogli l'input di design

Da `$ARGUMENTS` o chiedendo all'utente, determina:
- **Palette**: colori brand (hex) o vibe da cui derivarli
- **Tipografia**: font display + body, oppure carattere desiderato (geometrico, grottesco, serif editoriale…)
- **Personalità visiva**: aggettivi, mood, livello di contrasto, densità
- **Reference**: screenshot in `context/references/`, oppure 1+ URL ispirazione

Se è dato un **URL** da clonare/ispirare: usa la skill `firecrawl-website-design-clone` (o `firecrawl-scrape`) per estrarre colori, font, spacing e pattern reali, come evidenza. Niente valori inventati: se un dato non è verificabile, marcalo.

Per generare il sistema sfrutta le skill installate: `design-system`, `ui-ux-pro-max`, `design`, `brand`.

## Step 2 — Produci il design system

Crea un documento con questa struttura (come `DESIGN.md`):

**Frontmatter YAML**: `name`, `description`, `colors` (con scala di superfici/neutri), `typography` (display/headline/title/body/label con size, weight, line-height, tracking), `rounded`, `spacing`, `components` (button primary/secondary, input, card…).

**Prosa**:
1. Overview + creative north star (1 paragrafo, concreto)
2. Colors (primary/secondary/neutral + **regole nominate**, es. "No-Line Rule")
3. Typography (gerarchia + carattere + regole)
4. Elevation (ombre, layering, regole)
5. Components (buttons, chips, cards, inputs, nav)
6. Do's & Don'ts

## Step 3 — Anti-slop check

Il sistema deve **rifiutare esplicitamente** (da `PRODUCT.md` anti-references):
- estetica AI-slop / SaaS generico (gradienti viola/neon, glassmorphism decorativo, bounce esagerato)
- sales page americana da infoprodotto
- guru hype

Se utile, gira il detector impeccable sui valori/esempi generati.

## Step 4 — Salva (processo di approvazione)

1. **Bozza in brief.** Scrivi il design system in `output/<slug>/brief/design_system.md`, struttura da `execution/templates/DESIGN.template.md` (frontmatter token + sezioni 1-7). Questa è la versione da far approvare. **Non scrivere ancora in `DESIGN.md`.**
2. **Approvazione** ⟦GATE⟧. l'utente rivede nel brief e approva (anche con modifiche o mix tra direzioni).
3. **Promozione.** Solo dopo l'ok: promuovi a `DESIGN.md` (root = nuovo default del brand, o DESIGN di progetto in `context/brand/`). Mai sovrascrivere `DESIGN.md` root senza conferma esplicita.
- Opzionale: preview HTML con palette, scala tipografica e componenti chiave.

## Regole
- Mai inventare colori/font se è fornito un brand o un URL: derivali dall'evidenza.
- Coerenza con tono e personalità del brand (non negoziabili).
- Non sovrascrivere `DESIGN.md` senza conferma esplicita.
