---
# Brand layer, per-cliente. Questo file è vuoto nel template.
# /brand-dna lo compila e lo scrive qui (root). DESIGN.md = come appare (contratto visivo).
# Frontmatter = token machine-readable. Skeleton: execution/templates/DESIGN.template.md
name: "[Brand] — [autore]"
description: "[1 riga: stile, palette in sintesi, regola distintiva]"
colors:
  primary: "#______"
  accent: "#______"
  surface: "#______"
  text: "#______"
typography:
  display: { fontFamily: "", fontSize: "", fontWeight: 0, lineHeight: 0, letterSpacing: "" }
  body: { fontFamily: "", fontSize: "", fontWeight: 0, lineHeight: 0 }
  label: { fontFamily: "", fontSize: "", fontWeight: 0, letterSpacing: "" }
rounded: { sm: "", md: "", lg: "", xl: "", full: "9999px" }
spacing: { sm: "", md: "", lg: "", xl: "" }
components:
  button-primary: { backgroundColor: "", textColor: "", rounded: "", padding: "" }
  input-field: { backgroundColor: "", textColor: "", rounded: "", padding: "" }
  card: { backgroundColor: "", textColor: "", rounded: "", padding: "" }
---

# Design System: [Brand] — [DA COMPILARE]

> **Brand layer, per-cliente.** Vuoto nel template. Lo compila `/brand-dna` (fasi 2-4),
> dopo il gate di approvazione. Skeleton di riferimento: `execution/templates/DESIGN.template.md`.

## 1. Overview
[Creative north star. 1 paragrafo concreto. Cosa rifiuta esplicitamente (anti-slop).]

## 2. Colors
[Primary / Secondary / Neutral + **regole nominate** (es. "No-Line Rule").]

## 3. Typography
[Display/body/label, carattere, gerarchia + regole.]

## 4. Elevation
[Ombre, layering, regole (es. flat-by-default).]

## 5. Components
[Buttons, chips, cards, inputs, nav.]

## 6. Do's & Don'ts
[Liste concrete.]

## 7. Application UI (se c'è app/area riservata)
[Come tematizzare i componenti auth (Clerk appearance) e l'area riservata sui token sopra.]
