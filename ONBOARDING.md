# ONBOARDING — installa e usa il template (VS Code + Claude Code)

Guida passo-passo per scaricare questo template e iniziare un progetto da zero.
Filosofia: **facciamo (quasi) tutto dentro Claude Code**, non da terminale. Dove serve
un'azione in Claude Code trovi il **prompt esatto da copiare** in un blocco.

---

## 0. Configurazione di base (una volta sola)

Queste vanno installate sul sistema (download, non da Claude Code):

- **Node.js ≥ 20** → https://nodejs.org (serve per build/app e per alcuni MCP)
- **Git** → https://git-scm.com
- **(opzionale) GitHub CLI `gh`** → https://cli.github.com (serve solo per il deploy automatico più avanti)

Per **verificare** che siano a posto, puoi chiederlo a Claude Code (dopo averlo installato, step 2):

```
Verifica che node (>= 20) e git siano installati e mostrami le versioni.
```

---

## 1. Installa VS Code
- Scarica da **https://code.visualstudio.com** → installa → apri.

## 2. Installa l'extension Claude Code
1. In VS Code apri **Extensions** (icona nella barra laterale o `Cmd/Ctrl+Shift+X`).
2. Cerca **"Claude Code"** (publisher: Anthropic) → **Install**.
3. Apri il pannello Claude Code (icona nella barra laterale, o `Cmd/Ctrl+Shift+P` → "Claude Code").
4. **Login:** clicca "Sign in" → si apre il browser → accedi con account Anthropic (Claude Pro/Max o API key) → torna in VS Code.

> Se chiede di installare il CLI Claude Code sotto, accetta (richiede Node).

## 3. Permessi / auto mode

**Veloce (in sessione):** premi **`Shift+Tab`** per ciclare le modalità:
`normal` → `auto-accept edits` → `plan`. Per lavorare spedito usa **auto-accept edits**.

**Permanente (file):** crea `.claude/settings.local.json` nella cartella del progetto con:
```json
{
  "permissions": { "defaultMode": "acceptEdits" }
}
```
Valori di `defaultMode`:
- `acceptEdits` — auto-approva le **modifiche ai file** (consigliato: comodo e sicuro).
- `bypassPermissions` — auto-approva **tutto, anche i comandi**. ⚠️ Solo in progetti di cui ti fidi al 100% (es. un tutorial registrato): l'agente esegue qualsiasi cosa senza chiedere.

`settings.local.json` è già nel `.gitignore` → resta sulla tua macchina.

Puoi anche farlo creare a Claude Code:
```
Crea il file .claude/settings.local.json con permissions.defaultMode = "acceptEdits".
```

## 4. Scarica (clona) il template

Apri in VS Code una **cartella vuota** dove vuoi il progetto (**File → Open Folder**), poi
in Claude Code incolla:

```
Clona il repository https://github.com/Simo-Dax/landing-page-agent.git dentro questa cartella, poi leggi README.md e CLAUDE.md e mostrami la struttura.
```

Se lo clona in una sottocartella (`landing-page-agent`), aprila con **File → Open Folder**
così Claude Code lavora dentro il progetto.

## 5. Configura le chiavi (tutto in Claude Code, niente terminale)

**5.1 — Crea il tuo file `.env`.** Incolla in Claude Code:
```
Copia .env.example in un nuovo file .env nella root del progetto. Non inserire nessuna chiave: lascia i valori vuoti, li riempio io a mano.
```

**5.2 — Inserisci le chiavi a mano.** Apri `.env` nell'**editor di VS Code** e incolla i
tuoi valori. ⚠️ **Non incollare le chiavi nella chat di Claude Code** (finirebbero al
modello): scrivile direttamente nel file. Quali chiavi servono e dove prenderle: chiedi a
Claude Code di spiegartelo dal file connettori →
```
Leggi CONNECTORS.md e dimmi, per il tipo di progetto che voglio fare, quali chiavi mi servono ORA e quali posso aggiungere DOPO, e dove prendere ognuna.
```

**5.3 — Abilita i connettori MCP.** Il file `.mcp.json` definisce i server (supabase,
firecrawl, vercel) che leggono le chiavi da `.env`. Quando Claude Code chiede di
**abilitare i server MCP del progetto**, **approva**. Per verificare:
```
Controlla .mcp.json: elenca i server MCP configurati e dimmi quali sono attivi e quali chiavi in .env gli servono.
```

> Se un MCP non vede la sua chiave, assicurati che la variabile sia compilata in `.env`
> (es. `FIRECRAWL_API_KEY`) e riavvia la sessione Claude Code.

## 6. (Se mancano) skill e plugin

Le skill custom sono già nel repo (`.claude/skills/`). I plugin esterni richiamati
(`ui-ux-pro-max`, `impeccable`, `firecrawl`, `the-ai-ad-lab`) si installano dal marketplace
di Claude Code se non li hai già. Per controllare:
```
Leggi README.md e directives/orchestrator_index.md e dimmi quali skill/plugin servono e quali mi mancano da installare.
```

## 7. Parti col progetto

Lancia l'orchestratore:
```
/new-project
```
Ti guida passo-passo: **FASE 0** (tool/chiavi/MCP) → **FASE 0.5** (popola contesto e brand
layer) → **brand DNA → wireframe → copy → build → QA → deploy**, fermandosi ai gate per la
tua approvazione.

**Prompt tutto-in-uno** (se preferisci un avvio guidato esplicito):
```
Leggi README.md e CLAUDE.md di questo template, poi lancia /new-project e guidami step by step: prima setup di tool, chiavi e MCP, poi il popolamento del contesto/brand, infine brand DNA, wireframe, copy, build, QA e deploy. Fermati ai gate e chiedimi conferma.
```

---

## Riepilogo flusso
1. Node ≥ 20 + Git installati
2. VS Code + extension Claude Code (login)
3. Modalità permessi (`acceptEdits`)
4. Clona il repo (prompt in Claude Code)
5. `.env` creato da Claude Code, chiavi inserite a mano nell'editor, MCP approvati
6. Skill/plugin a posto
7. `/new-project` → workflow guidato fino al deploy
