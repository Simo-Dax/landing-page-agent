---
description: Retrospettiva — trasforma il feedback in una lezione riusabile (LEARNINGS.md) e propone update mirati agli agenti/directive. Lancialo a fine fase o fine progetto.
argument-hint: [feedback o area]
---

# /retro — miglioramento continuo

Chiude il loop: il feedback diventa regola, così il workflow migliora a ogni progetto.

Input: **$ARGUMENTS** (feedback grezzo, o area su cui riflettere)

## Step
1. **Raccogli il feedback.** Da `$ARGUMENTS` o chiedendo all'utente: cosa è andato bene, cosa no, cosa mancava. Sii specifico (quale fase, quale output).
2. **Estrai la lezione.** Per ogni punto: *cosa* è successo · *perché* conta · *come* applicarla la prossima volta · *dove* (quale agente/file).
3. **Scrivi in `LEARNINGS.md`.** Append nella sezione giusta (Copy / Design / Processo / nuova). Niente duplicati: se esiste una voce simile, affinala.
4. **Propaga (con approvazione).** Se la lezione riguarda un artefatto stabile, proponi l'edit mirato:
   - subagent → `.claude/agents/<agente>.md`
   - copy/voce → `context/brand/anti-ai-writing-style.md`
   - design → `DESIGN.md` (do/don't)
   - processo/fasi → `FRAMEWORK.md` o `directives/` (⚠️ le directive non si toccano senza ok esplicito — CLAUDE.md regola 6)
   Mostra il diff proposto e applica solo dopo conferma.
5. **Memoria personale (opzionale).** Se è una preferenza durevole dell'utente, salvala anche come memory `feedback`.

## Regole
- Una lezione = azionabile e specifica, non genérica.
- Mai modificare directive/agenti senza approvazione.
- `LEARNINGS.md` resta la fonte append-only; gli edit propagati sono la "messa in pratica".
