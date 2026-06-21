# 22 — Buyer Persona Creation

Definisce le **buyer personas** del progetto a partire dal contesto brand. Non genera immagini (quello era il vecchio character creator, rimosso): produce profili strategici che guidano copy, architettura e message match.

**Output (doppio):** `output/<slug>/brief/buyer_personas.md` + `output/<slug>/brief/buyer_personas.html` (card visibili, una per persona, tematizzato sul `DESIGN.md`). L'HTML è sempre richiesto: serve all'utente per vedere le personas. (E/o aggiorna `PRODUCT.md` se sono le personas di brand.)
**Usata da:** Fase 1 (brief/discovery), `copy-agent`, `wireframe-agent`.

## Input
`PRODUCT.md`, `context/brand/business_strategy.md` (se ha già personas), brief CRO, eventuale sito/audience reale.

## Processo
Per ogni persona (di solito 2-3, non di più), definisci:

1. **Nome + archetipo** — un'etichetta umana (es. "Marco, il junior che vuole crescere").
2. **Chi è** — età/ruolo/contesto, livello di competenza, situazione lavorativa.
3. **Jobs-to-be-done** — cosa sta cercando di ottenere davvero.
4. **Pain points** — 3-5 frustrazioni concrete (parole sue, non gergo).
5. **Desideri/goal** — lo stato desiderato.
6. **Obiezioni** — perché potrebbe NON convertire (prezzo, tempo, scetticismo, "funziona per me?").
7. **Trigger d'acquisto** — cosa lo spinge ad agire ora.
8. **Canali** — dove lo raggiungiamo (coerente con la sorgente di traffico del brief).
9. **Message angle** — l'angolo che risuona + l'**anti-message** (cosa lo fa scappare, es. hype da guru).

## Regole
- Personas dal contesto/dati reali, non inventate. Se manca un dato: `[DA VERIFICARE]`.
- Specifiche e azionabili: ogni persona deve cambiare una scelta di copy o di struttura, altrimenti è filler.
- Coerenti con `PRODUCT.md` (denominatore comune) e con il tono di voce.
- Max 2-3 personas: meglio poche e nette che dieci generiche.
