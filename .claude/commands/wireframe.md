---
description: Lancia il wireframe-agent — architettura + wireframe (output MD + HTML low-fi visibile)
argument-hint: [progetto o superficie]
---

# /wireframe

Avvia il `wireframe-agent` (Fase 5). Step indipendente.

Input: $ARGUMENTS

## Cosa fare
1. Leggi brief, `buyer_personas.md`, `DESIGN.md`, `PRODUCT.md`, `directives/00_cro_principles.md`.
2. Produci l'architettura testuale (above-the-fold, sezioni, gerarchia, leva, CTA, social proof, message match).
3. **Output doppio:**
   - `output/<slug>/brief/architettura_<slug>.md`
   - `output/<slug>/brief/wireframe_<slug>.html` (wireframe **low-fi** visibile: box etichettati, gerarchia, annotazioni per sezione, mobile + desktop). Serve all'utente per vedere e approvare prima del design.
4. ⟦GATE⟧ approvazione prima del build. Niente design visivo finale qui (quello è del `design-build-agent`).
