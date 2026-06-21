# Tecniche di design per Claude Code

Questo file contiene le istruzioni per costruire interfacce web professionali.
Claude Code legge questo file automaticamente e applica queste regole.

## Stack tecnologico

### Tailwind CSS — styling utility-first
Quando costruisci pagine web, usa Tailwind CSS per lo styling. Produce codice
più pulito e veloce del CSS custom. Definisci i colori e font del brand nella
configurazione di Tailwind.

### ShadCN UI — componenti riutilizzabili
Per componenti di interfaccia (bottoni, card, accordion, form, dropdown), usa
ShadCN UI. Copia i componenti direttamente nel progetto. Personalizzali con i
colori e lo stile del brand.

### Quando usarli
- Progetto nuovo con più pagine: Tailwind + ShadCN come base
- Landing page singola veloce: CSS custom è accettabile
- Qualsiasi progetto con componenti ripetuti: ShadCN risparmia ore

## Animazioni

### GSAP + ScrollTrigger — animazioni di scroll
Usa GSAP per le animazioni attivate dallo scroll:
- Elementi che appaiono con fade-in dal basso quando entrano nel viewport
- Stagger di 0.15-0.2s tra elementi di una griglia
- Counter animation per numeri/statistiche (contano da 0 al valore)
- Parallax su elementi decorativi di sfondo

CDN: https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js
CDN: https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js

### Framer Motion — micro-interazioni
Usa Framer Motion (o simulala con CSS transitions) per:
- Hover effects su card e bottoni (scale 1.02-1.03, durata 300ms)
- Toggle e switch animati
- Feedback visivo al click
- Transizioni fluide tra stati

### Regola importante sulle animazioni
Quando lavori su animazioni (background animati, elementi in movimento), NON
usare lo screenshot loop per confrontare. Gli screenshot catturano un frame
statico e il loop impazzisce. Lavora direttamente sul codice.

## Grafica 3D

### Three.js
Per grafiche 3D custom (particelle, geometrie, effetti tipo Stripe.com).
CDN: https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js

### Spline (spline.design)
Per grafiche 3D pre-costruite dalla community. Workflow:
1. spline.design → community → trova grafica
2. Remix → modifica → Export → Code export
3. Incolla il link nel prompt

## Tipografia

Usa Google Fonts. Regole:
- Un font display per i titoli (carattere forte, memorabile)
- Un font leggibile per il body (pulito, professionale)
- Massimo 2-3 font per progetto
- MAI usare Inter, Arial o Roboto per i titoli (troppo generici)

## Puppeteer e screenshot loop

Usa Puppeteer per scattare screenshot durante la costruzione del sito.
Dopo ogni fase importante:
1. Avvia il server locale
2. Scatta screenshot delle sezioni modificate
3. Confronta con il risultato desiderato
4. Fai almeno due passate di revisione e correzione

Installazione: npm install -g puppeteer

## Background e profondità

Non usare MAI sfondi piatti e solidi. Aggiungi sempre profondità:
- Gradienti radiali con 2-3 cerchi sfocati (colori del brand, opacità 10-15%)
- Posizionamento asimmetrico (non centrato)
- Texture grana leggera (mix-blend-mode overlay, opacità bassa)
- Il background crea atmosfera senza distrarre dal contenuto

## Cloning di siti

Quando il cliente fornisce un sito di riferimento:
1. Usa lo screenshot come guida visiva
2. Analizza la struttura HTML/CSS del riferimento
3. Replica il layout con i colori e il brand del cliente
4. Usa lo screenshot loop per confrontare sezione per sezione

## Componenti da 21st.dev

Per upgrade puntuali (bottoni, background, effetti hover), cerca componenti
su 21st.dev. Hanno un "Copy Prompt" che genera codice pronto da integrare.

## Risorse per ispirazione

- Dribbble (dribbble.com) — design di interfacce
- Godly Website (godly.website) — siti web di alta qualità
- Awwwards (awwwards.com) — premi per i migliori siti
- 21st.dev — componenti singoli pronti all'uso

## Regole anti-AI slop

EVITA SEMPRE:
- Font generici (Inter, Arial, Roboto per i titoli)
- Gradienti viola su sfondo bianco
- Layout simmetrici con 3 colonne e icone in cerchio
- Card tutte uguali senza variazione
- Zero animazioni o interazioni
- Sfondi piatti monocromatici

CERCA SEMPRE:
- Tipografia distintiva e memorabile
- Layout asimmetrici e inaspettati
- Animazioni con scopo (non decorative)
- Profondità visiva (gradienti, texture, ombre)
- Micro-interazioni su ogni elemento interattivo
- Una direzione estetica bold e coerente