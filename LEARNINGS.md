# LEARNINGS — lezioni dai feedback

Si accumulano nel tempo. **Letto a inizio di ogni progetto** da orchestratore e subagent, così le lezioni si applicano subito. Aggiornato da `/retro`. Append-only.

Vale per **agenti, skill e directive**: `/retro` estrae la lezione qui e poi la propaga (con ok) all'artefatto giusto (un subagent, una skill, una directive, `DESIGN.md`, `anti-ai-writing-style.md`). Un solo log centrale invece di tanti file sparsi = meno ridondanza, stessa auto-iterazione.

Formato voce: **cosa** · perché · come applicarla · dove (quale agente/file).

## Copy
- **Zero em dash, zero pattern "non X, ma Y".** Perché: tell #1 di testo AI. Come: punteggiatura vera (due punti, virgole, punti); contrasti contrarian sì ma senza dash. Dove: `copy-agent`, `context/brand/anti-ai-writing-style.md`.

## Design
- **Mai UI basica.** Perché: lo standard di qualità è alto. Come: depth, spacing generoso, reference reali; niente estetica generica AI (gradienti viola, glassmorphism decorativo, bounce). Dove: `design-build-agent`, `DESIGN.md` do/don't, `impeccable`.
- **Fondali = gradiente atmosferico + grana, mai colore solido piatto.** Perché: una landing con hero a colore pieno sembra generata di fretta. Come: hero/final con gradienti stratificati (linear + 2 radiali), aura tenue, grana SVG overlay; depth con ombre stratificate; dettagli editoriali (numeri grandi, marquee, feature card, frame su foto, scroll bar, reveal). Dove: `design-build-agent`, `DESIGN.md` regola "profondità atmosferica, mai piatto".
- **Studia una reference reale prima del build.** Confronta sempre con la migliore versione esistente e replica il livello di craft, non solo la struttura. Dove: `design-build-agent`.

## Processo
- **Piano + approvazione esplicita prima di sviluppare.** Perché: evita lavoro buttato. Come: gate su brief, wireframe, deploy. Dove: orchestrator, `CLAUDE.md`.
- **Ricerca = suite firecrawl, non la skill `brand`.** Perché: `brand` definisce voce/identità, non scrapa il web. Dove: `design-system-agent`.
- **Crediti a pagamento (firecrawl) solo dopo conferma.** Dove: orchestrator, `design-system-agent`.
