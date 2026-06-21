# 03c - Editing & Self-Check: Suona come il brand?

## Obiettivo
Rivedere ogni pezzo di scrittura per eliminare tracce di linguaggio AI-generated e assicurare che suoni esattamente come il brand.

## Quando si usa
**Dopo ogni draft di testo** — newsletter, post LinkedIn, caption Instagram, script reel. Questa direttiva è obbligatoria, non opzionale.

## Input
- Il draft appena scritto
- `context/brand/tone_of_voice.md` (DEVE essere aperto e confrontato riga per riga)

## Processo di revisione

### Pass 1: Detector AI-speak

Cerca e riscrivi qualsiasi occorrenza di:

**Frasi generiche da eliminare:**
- "In un mondo sempre più..." → TAGLIA o riscrivi con dato specifico
- "È fondamentale..." → sostituisci con "Serve [cosa specifica]"
- "Non si può sottovalutare..." → TAGLIA, vai dritto al punto
- "Questo rappresenta un'opportunità..." → riscrivi con azione concreta
- "Nell'era dell'AI / della digital transformation..." → TAGLIA
- "Come professionisti, dobbiamo..." → riscrivi in prima persona
- "È importante sottolineare che..." → TAGLIA, dillo e basta
- "Senza ombra di dubbio..." → TAGLIA
- "Un approccio olistico..." → specifica cosa intendi
- Qualsiasi frase che potrebbe stare in una brochure aziendale

**Pattern strutturali AI da correggere:**
- Tre punti che iniziano tutti con la stessa struttura grammaticale → varia
- Paragrafo che "riassume" quello precedente → TAGLIA, è ridondante
- Conclusioni che riformulano l'introduzione → riscrivi con next step concreto
- "In conclusione..." / "Per riassumere..." → mai usare
- Elenchi dove ogni punto inizia con un gerundio → varia la struttura

### Pass 2: Confronto col tone of voice

Controlla punto per punto con `context/brand/tone_of_voice.md`:

| Check | Domanda | Se NO → |
|-------|---------|---------|
| Diretto | Vai al punto nelle prime 2 righe? | Riscrivi hook |
| Specifico | Ci sono numeri, nomi, tool reali? | Aggiungi dettagli concreti |
| Framework | C'è una struttura replicabile? | Aggiungi step o schema |
| Azione | Il lettore sa cosa fare dopo? | Aggiungi takeaway pratico |
| Umano | Suona come una persona che parla? | Riscrivi come se lo dicessi a un collega |
| No hype | C'è qualcosa da "guru"? | Elimina o riformula |
| Paragrafi | Qualche paragrafo supera le 4 righe? | Spezza |
| Frasi | Qualche frase supera le 25 parole? | Spezza |

### Pass 3: Test delle espressioni

Verifica che il testo includa almeno 2-3 espressioni tipiche del brand (da `tone_of_voice.md`):
- "Dal mio punto di vista..."
- "Facciamo un esempio pratico..."
- "Il motivo è molto semplice..."
- "Puoi usare... / Prova a fare..."
- "La cosa più interessante è..."

E che NON includa espressioni bandite:
- "Il segreto è..."
- "Non perdere questa opportunità..."
- "Tutti i top marketer sanno che..."
- "Ecco la verità che nessuno ti dice..."
- Qualsiasi espressione da pitch infoprodotto

### Pass 4: Ritmo e leggibilità

- Leggi il testo ad alta voce (mentalmente). Dove inciampi, riscrivi.
- Verifica alternanza: frase lunga → frase corta → domanda → affermazione
- Verifica che i grassetti siano usati con parsimonia (1-2 per paragrafo, max)
- Verifica che le emoji siano max 2-3 in tutto (se presenti)

## Output

Non produce un file separato. Modifica il draft direttamente e segnala all'utente:

```
## Self-check completato

### Modifiche apportate:
- [X] Rimossa frase AI-speak: "[frase originale]" → "[frase corretta]"
- [X] Aggiunto esempio concreto in sezione [N]
- [X] Spezzato paragrafo troppo lungo in sezione [N]
- [X] Aggiunta espressione tipica: "[espressione]"

### Punteggio tono di voce: [X]/10
- [dettaglio su cosa funziona e cosa potrebbe migliorare]
```

## Regole

1. **Questa direttiva non è opzionale.** Ogni draft passa da qui prima di essere presentato all'utente.
2. **Non edulcorare il feedback.** Se il testo suona come AI, dillo e correggilo. L'obiettivo è zero tracce di artificialità.
3. **Preferisci tagliare che aggiungere.** Un testo più corto e autentico batte un testo lungo e generico.
4. **Il test finale:** se leggi il testo e non puoi dire con certezza se l'ha scritto dal brand o un AI, non è ancora pronto.
