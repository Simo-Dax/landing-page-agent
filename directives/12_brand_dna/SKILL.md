# Pre-Pipeline — Brand DNA (Playwright 3.0)

**Agente:** Pre-pipeline (eseguito prima di SA1-SA7)
**Output:** `02_Brand_DNA/brand-dna-[brand-slug].html`
**Prerequisiti:** Playwright MCP + Web search

---

## Input richiesti

Chiedi all'utente:
> "Quale brand vuoi analizzare? Dimmi il **nome del brand** e la **URL target** (sito web)."

---

## Protezione cartella

```bash
PWD_ABS="$(pwd)"
TARGET="${PWD_ABS}"
PROTECTED=0
case "$PWD_ABS" in
  "$HOME"|"$HOME/"|"/"|"/tmp"|"/tmp/"|"$HOME/Downloads"|"$HOME/Desktop")
    PROTECTED=1 ;;
esac
if [ "$PROTECTED" = "1" ] && [ ! -d "$TARGET" ]; then
  echo "PROTECTED:$PWD_ABS"
elif [ ! -f "$TARGET/_meta/folder-confirmed.flag" ] && [ ! -d "$TARGET" ]; then
  echo "FIRSTRUN:$TARGET"
else
  mkdir -p "$TARGET/02_Brand_DNA" "$TARGET/_meta"
  echo "READY:$TARGET"
fi
```

---

## Step 1 — Verifica Playwright MCP

Cerca i tool Playwright (`browser_navigate`, `browser_take_screenshot`, `browser_evaluate`). Testa navigando all'homepage del brand.

**Se Playwright è connesso:** procedi allo Step 2.

**Se Playwright NON è connesso:** STOP. Mostra istruzioni setup:
> "Il Playwright MCP è necessario per l'estrazione accurata dei colori dal CSS live.
>
> Setup:
> 1. `claude mcp add playwright npx @playwright/mcp@latest`
> 2. Riavvia Claude Code
> 3. Rispondi "pronto" per riprovare"

---

## Step 2 — Estrazione colori live con Playwright (SOLO colori)

Playwright è usato ESCLUSIVAMENTE per i colori. NON usarlo per copy, tipografia, tone of voice — quelli vengono da web search.

1. Naviga all'URL target con `browser_navigate`
2. Screenshot con `browser_take_screenshot`
3. Clicca almeno 3-5 pagine aggiuntive (About, Prodotti, PDP, Sustainability, Footer)
4. Su ogni pagina esegui `browser_evaluate` per estrarre CSS computed:
   ```javascript
   // Background di body, header, footer, .btn, [class*="cta"]
   // Colori testo su h1, h2, h3
   // CSS custom properties: getComputedStyle(document.documentElement).getPropertyValue('--primary')
   ```
5. Aggrega hex unici, identifica:
   - **Colore primario** (su logo/CTA)
   - **Colore secondario**
   - **Colore accent**
   - **Background** (pagina/sezione)
   - **CTA color** (background + testo)

---

## Step 3 — Ricerca web (tutto il resto)

Con web search attivo, raccogli:
- Storia brand, rebranding, agenzia design
- Brand guidelines / press kit
- Stack tipografico (logo font, display font, body font)
- Voce e tono (5 aggettivi)
- Stile fotografico
- Dettagli packaging
- Differenziazione competitiva
- Brand story, mission, posizionamento
- Stile ad creative (Meta Ad Library)

**I colori Playwright hanno la precedenza** su qualsiasi fonte web.

---

## Output

Documento HTML Brand DNA che:
- Usa la palette colori reale estratta via Playwright (hex live)
- Usa la tipografia del brand nello stile del documento
- Ha layout professionale con sezioni chiare
- Include sezione "Colori Live dal Sito" con hex esatti
- È completamente scaricabile (self-contained)

Salva in: `<pwd>/02_Brand_DNA/brand-dna-[brand-slug].html`

---

## Dopo la consegna

> "Brand DNA completato! Quando sei pronto per generare i 40 prompt statici, usa la skill `/static` e carica questo documento Brand DNA insieme al VOC e alle immagini prodotto."

---

## Regole critiche

- **Playwright SOLO per colori** — screenshot + click + CSS. Non usarlo per copy o research.
- **Web search obbligatorio** per tutto il resto
- **Visita almeno 3-5 pagine diverse** con Playwright (non solo homepage)
- **Colori live vincono** — quando hex da Playwright confligge con web search, usa Playwright
- **Output DEVE essere HTML** — non markdown, non plain text

---

## Validazione output

1. File esiste in `02_Brand_DNA/brand-dna-[brand-slug].html`
2. Dimensione > 25.000 byte
3. Almeno 3 hex nella sezione "Colori Live"
4. Almeno 2 typeface nello stack tipografico
5. Nessun placeholder (`[BRAND]`, `[TARGET URL]`, `<TODO>`)
6. Tutte le sezioni popolate: Colori, Tipografia, Voce/Tono, Fotografia, Brand Story, Differenziazione
