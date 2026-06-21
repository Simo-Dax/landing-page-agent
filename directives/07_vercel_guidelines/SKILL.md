---
name: vercel-design-audit
description: Audit interfaces against 100+ production-grade rules covering accessibility, UX, performance, and design quality inspired by Vercel's design standards. Use when reviewing landing pages, components, or full interfaces before production deployment.
license: Complete terms in LICENSE.txt
---

# Vercel Web Design Guidelines — Production-Grade Audit Skill

Questa skill implementa un sistema di audit completo basato sugli standard di design di Vercel, verificando oltre 100 regole suddivise in accessibilità, UX, performance e qualità visiva. Usa questa skill per garantire che ogni landing page o interfaccia sia pronta per la produzione.

## Quando Usare Questa Skill

- Prima del deployment in produzione di una landing page
- Dopo aver completato il copy e il design, come ultimo checkpoint
- Quando il cliente richiede standard enterprise o compliance accessibility
- Per validare lavoro di developer esterni o junior
- Come parte del self-check CRO (integra con `03_editing_selfcheck.md`)

**NON usare se:**
- La pagina è ancora in fase di bozza (usa prima copywriting e design skills)
- Serve solo feedback sul copy (usa copy-editing skill)
- Il progetto ha requisiti custom che contraddicono standard UX consolidati

---

## Framework di Audit — 4 Pilastri

### 1. Accessibility (A11Y) — 30+ regole
Conformità WCAG 2.1 AA + best practice oltre lo standard:
- Contrasto colori (4.5:1 per testo normale, 3:1 per large text)
- Keyboard navigation completa (tab order logico, focus visible)
- ARIA labels e semantic HTML
- Form accessibility (labels, error messages, validation)
- Screen reader support (alt text, heading hierarchy)

### 2. User Experience (UX) — 40+ regole
Pattern di interazione testati e consolidati:
- Visual hierarchy chiara (F-pattern, Z-pattern)
- CTA visibility e posizionamento
- Form UX (validation in tempo reale, error states chiari)
- Loading states e feedback (skeleton, spinner, success/error messages)
- Mobile-first responsive design
- Touch target size (min 44×44px)
- Gestione errori user-friendly

### 3. Performance — 20+ regole
Ottimizzazione per Core Web Vitals:
- Image optimization (lazy loading, modern formats, dimensioni appropriate)
- Font loading strategy (preload, font-display)
- CSS/JS bundle size (eliminare unused code)
- Render-blocking resources minimizzati
- LCP <2.5s, FID <100ms, CLS <0.1

### 4. Visual Quality — 30+ regole
Design polish e coerenza visiva:
- Spacing consistency (8pt grid system)
- Typography scale coerente
- Color palette limitata e coerente
- Component consistency (button styles, card design, etc.)
- Micro-interactions e transitions
- Dark mode support (se applicabile)

---

## Processo di Audit

### Step 1 — Analisi Automatica (Checklist Rapida)

Esegui questa checklist prima dell'audit approfondito. Se più di 3 item falliscono, blocca e correggi prima di procedere:

#### Critical Issues (blockers)
- [ ] **Contrasto testo**: Tutti i testi hanno contrasto ≥4.5:1 (normal) o ≥3:1 (large)?
- [ ] **CTA visibility**: La CTA primaria è immediatamente visibile above the fold?
- [ ] **Mobile responsive**: La pagina è usabile su viewport 375px senza scroll orizzontale?
- [ ] **Form labels**: Ogni input ha una label visibile e associata correttamente?
- [ ] **Alt text**: Tutte le immagini hanno alt text descrittivo o decorativo `alt=""`?
- [ ] **Heading hierarchy**: Gli heading seguono ordine logico (h1 → h2 → h3, senza salti)?
- [ ] **Focus states**: Tutti gli elementi interattivi hanno focus visible su keyboard navigation?

Se tutti i critical issues passano, procedi con audit approfondito.

---

### Step 2 — Audit Approfondito per Categoria

#### A. Accessibility Audit

**1. Color & Contrast**
- [ ] Testo su sfondo: contrasto ≥4.5:1 (AA) o ≥7:1 (AAA preferred)
- [ ] Large text (18pt+ o 14pt bold): contrasto ≥3:1
- [ ] UI elements (border, icons): contrasto ≥3:1
- [ ] Non affidarsi solo al colore per trasmettere informazioni (es. errori rossi + icona)

**2. Keyboard Navigation**
- [ ] Tab order logico e prevedibile (segue visual flow)
- [ ] Focus visible su tutti elementi interattivi (outline personalizzato ok, ma visibile)
- [ ] Skip to main content link presente (per screen reader)
- [ ] Nessun keyboard trap (possibile uscire da ogni componente con tab/shift+tab)
- [ ] Enter/Space attivano button e link
- [ ] ESC chiude modal e dropdown

**3. Semantic HTML & ARIA**
- [ ] Heading hierarchy corretta: un solo h1, poi h2, h3, etc.
- [ ] Landmarks HTML5: header, nav, main, aside, footer
- [ ] Button vs Link: button per azioni, link per navigazione
- [ ] Form: label associati a input (`for` attribute o wrapping)
- [ ] ARIA labels dove necessario (icon button, decorative elements)
- [ ] Live regions per aggiornamenti dinamici (es. errori form)

**4. Images & Media**
- [ ] Alt text descrittivo per immagini informative
- [ ] `alt=""` per immagini decorative
- [ ] Video: sottotitoli disponibili, no autoplay con audio
- [ ] Icon: accompagnati da testo o aria-label

**5. Forms**
- [ ] Label visibili per ogni input
- [ ] Placeholder non sostituisce label
- [ ] Error messages specifici e associati all'input (`aria-describedby`)
- [ ] Required fields marcati visualmente e con `required` attribute
- [ ] Validation in tempo reale senza bloccare l'utente
- [ ] Success state chiaro dopo submit

---

#### B. UX Audit

**1. Visual Hierarchy**
- [ ] Headline primaria immediatamente riconoscibile (size, weight, position)
- [ ] CTA primaria ha massimo contrasto e dimensione prominente
- [ ] CTA secondarie visivamente subordinate (outline button, colore più tenue)
- [ ] White space generoso attorno a elementi importanti
- [ ] Sezioni distinte con spacing consistente

**2. Above the Fold**
- [ ] Value proposition chiara in <3 secondi
- [ ] CTA primaria visibile senza scroll
- [ ] Trust signal visibile (logo clienti, rating, numeri)
- [ ] No necessità di scroll per capire di cosa si tratta

**3. CTA & Conversion Elements**
- [ ] CTA copy: action-oriented, specifico (no "Click here", sì "Inizia il trial gratuito")
- [ ] CTA dimensione: min 44×44px per touch target
- [ ] CTA contrasto: massima visibilità rispetto allo sfondo
- [ ] CTA position: logica nel flusso (dopo spiegazione beneficio, non prima)
- [ ] Secondary CTA disponibile se CTA primaria è high-commitment

**4. Forms & Input**
- [ ] Campi form: max 5-7 visibili insieme (break in steps se più lungo)
- [ ] Input type corretto (email, tel, number) per keyboard mobile
- [ ] Auto-complete attributes per dati comuni (name, email, phone)
- [ ] Error validation: specific, helpful, real-time
- [ ] Success feedback: chiaro e rassicurante
- [ ] Submit button disabled durante invio (prevent double submit)

**5. Mobile UX**
- [ ] Responsive breakpoint: 375px (iPhone SE), 768px (tablet), 1024px+ (desktop)
- [ ] Touch target: min 44×44px con spacing adeguato
- [ ] Font size mobile: min 16px per body text (prevent zoom su focus iOS)
- [ ] Navigation mobile: hamburger menu o bottom nav (se complessa)
- [ ] Sticky CTA su mobile (se scroll lungo)

**6. Loading & Feedback**
- [ ] Loading states: skeleton o spinner per contenuti dinamici
- [ ] Error states: messaggi user-friendly, azione suggerita
- [ ] Empty states: guida utente su cosa fare (no pagina bianca)
- [ ] Success states: conferma visiva chiara

**7. Content Readability**
- [ ] Line length: 50-75 caratteri per riga (max leggibilità)
- [ ] Line height: 1.5-1.7 per body text
- [ ] Paragraph spacing: maggiore di line height
- [ ] No wall of text: break in paragrafi brevi, liste, headings

---

#### C. Performance Audit

**1. Images**
- [ ] Lazy loading per immagini below the fold
- [ ] Responsive images: `srcset` e `sizes` per diverse risoluzioni
- [ ] Modern formats: WebP o AVIF con fallback
- [ ] Dimensioni appropriate: no 4K image scalata a 300px
- [ ] Alt text presente (doppia funzione: a11y + SEO)

**2. Fonts**
- [ ] Preload per font critici: `<link rel="preload" as="font">`
- [ ] `font-display: swap` per evitare FOIT (Flash of Invisible Text)
- [ ] Max 2-3 font families
- [ ] Max 4-6 font weights/styles caricati

**3. CSS & JavaScript**
- [ ] Critical CSS inline per above the fold
- [ ] CSS e JS non-critical: lazy o defer
- [ ] Minification: CSS e JS compressi
- [ ] Rimozione unused CSS (PurgeCSS con Tailwind)

**4. Core Web Vitals (target)**
- [ ] **LCP** (Largest Contentful Paint): <2.5s
- [ ] **FID** (First Input Delay): <100ms
- [ ] **CLS** (Cumulative Layout Shift): <0.1
- [ ] Verifica con PageSpeed Insights o Lighthouse

**5. Caching & CDN**
- [ ] Static assets serviti da CDN
- [ ] Cache headers appropriati (immutable per assets con hash)
- [ ] Compression: Gzip o Brotli per text assets

---

#### D. Visual Quality Audit

**1. Spacing & Layout**
- [ ] Spacing system consistente: multipli di 4px o 8px (8pt grid)
- [ ] Padding simmetrico nei componenti
- [ ] Vertical rhythm: spacing tra sezioni consistente
- [ ] Max-width container per leggibilità (max-w-7xl = 1280px)

**2. Typography**
- [ ] Font scale consistente: usa scale predefinita (es. Tailwind default)
- [ ] Heading hierarchy visibile: h1 >> h2 > h3
- [ ] Font weight appropriato: bold per heading, regular/medium per body
- [ ] Letter spacing (tracking): leggera espansione per uppercase text

**3. Color System**
- [ ] Palette limitata: 1 primary, 1 accent, grigi per testo/background
- [ ] Tinte consistenti: usa scale (50, 100, 200... 900) non colori random
- [ ] Background: preferisci grigi molto chiari (slate-50, gray-50) a bianco puro
- [ ] Accent color usato con parsimonia (CTA, links, highlights)

**4. Components Consistency**
- [ ] Button styles: max 2-3 varianti (primary, secondary, outline)
- [ ] Card design: stesso border-radius, shadow, padding
- [ ] Icons: stesso style pack (es. tutti Lucide, tutti outline o tutti solid)
- [ ] Input fields: stesso height, padding, border style

**5. Micro-interactions**
- [ ] Hover states: su tutti elementi interattivi
- [ ] Transition smooth: `transition-all duration-200` o simili
- [ ] Active/pressed states: visual feedback su click
- [ ] Disabled states: ridotta opacity, cursor not-allowed

**6. Dark Mode (opzionale ma raccomandato)**
- [ ] Colori dark mode non sono inversione semplice (usa grigi caldi, non puro nero)
- [ ] Contrasto dark mode: rispetta stessi ratio di light mode
- [ ] Toggle dark mode persistente (localStorage)
- [ ] Images/illustrations: versioni ottimizzate per dark mode se necessario

---

### Step 3 — Scoring & Report

Dopo l'audit, assegna un punteggio per ogni categoria:

**Scoring System:**
- **A (90-100%)**: Production-ready, nessun issue critico
- **B (80-89%)**: Buono, solo issue minori da fixare
- **C (70-79%)**: Accettabile, ma con issue che impattano UX
- **D (60-69%)**: Sotto standard, fix obbligatori prima del deploy
- **F (<60%)**: Non production-ready, rework necessario

**Report Template:**

```markdown
# Audit Report — [Nome Pagina/Progetto]
**Data:** [data]
**Auditor:** Landing Page UX Agent

## Summary Score
- **Accessibility:** [A/B/C/D/F] — [score]%
- **UX:** [A/B/C/D/F] — [score]%
- **Performance:** [A/B/C/D/F] — [score]%
- **Visual Quality:** [A/B/C/D/F] — [score]%

**Overall Score:** [score]% — [A/B/C/D/F]

---

## Critical Issues (fix before deploy)
1. [Issue description] — **Impact:** [High/Medium/Low]
   - **Location:** [dove appare l'issue]
   - **Fix:** [come risolvere]

2. [...]

---

## Recommended Improvements
1. [Issue description] — **Impact:** [High/Medium/Low]
   - **Location:** [dove appare]
   - **Fix:** [come risolvere]
   - **Effort:** [Low/Medium/High]

---

## Strengths
- [Cosa funziona bene nella pagina]
- [Pattern UX efficaci]
- [Design choices ben eseguiti]

---

## Next Steps
1. [Azione prioritaria]
2. [Azione secondaria]
3. [Nice-to-have]
```

---

## Regole di Questa Skill

### ✅ Fare
- Audit completo, non superficiale: testa ogni regola applicabile
- Prioritizza issue per impatto: Critical → High → Medium → Low
- Fornisci fix concreti, non solo "migliora l'accessibilità"
- Testa su dispositivi reali o DevTools responsive mode
- Usa tool automatici come complemento (Lighthouse, axe), non sostituto

### ❌ Non Fare
- Non ignorare accessibility anche se "il cliente non l'ha chiesto"
- Non dare pass ad issue solo perché "è comune nel settore"
- Non sovraccaricare di issue minori: max 10 recommended, focus su impact
- Non dare feedback stilistici soggettivi (es. "non mi piace questo colore")
- Non auditare contro preferenze personali: usa standard consolidati (WCAG, best practice Vercel/Stripe/Linear)

---

## Tool Complementari Raccomandati

### Automatici (run prima dell'audit manuale)
- **Lighthouse** (Chrome DevTools): Performance, A11Y, Best Practices, SEO
- **axe DevTools**: Accessibility audit approfondito
- **WAVE**: Web accessibility evaluation tool
- **PageSpeed Insights**: Core Web Vitals e suggerimenti performance

### Manuali (durante audit)
- **Keyboard navigation test**: Tab attraverso tutta la pagina
- **Screen reader test**: VoiceOver (Mac), NVDA (Windows), JAWS
- **Color contrast checker**: Contrast Ratio tool, WebAIM Contrast Checker
- **Responsive test**: Chrome DevTools responsive mode + dispositivi reali

---

## Edge Cases & Exceptions

### Quando è OK violare una regola
Alcune regole possono essere infrante con giustificazione valida:

- **Contrasto colori**: Se il brand ha colori istituzionali a basso contrasto, proponi alternative (versione più scura per testo, outline per button)
- **Heading hierarchy**: Se il design richiede heading non sequenziali, usa ARIA (`role="heading" aria-level="2"`)
- **Mobile font size <16px**: Usa `user-scalable=no` solo se assolutamente necessario (no per form!)

**Regola d'oro:** Se violi uno standard, documenta il perché e proponi mitigazione.

---

## Integration con il Workflow

Questa skill si integra come ultimo step prima del deployment:

1. **Brief CRO** → 01_landing_brief.md
2. **Copy** → 02_headline_optimization.md + copywriting
3. **Design/Dev** → frontend-design o web-artifacts-builder
4. **Self-check CRO** → 03_editing_selfcheck.md
5. **👉 Vercel Audit** → 07_vercel_guidelines (questa skill)
6. **Deploy** → Go live

Se l'audit score è ≥80% (B), procedi con deployment.
Se <80%, fix issue critici e re-audit prima di deploy.

---

## Riferimenti

### WCAG 2.1 Quick Reference
- **Level A**: Minimum accessibility (must-have)
- **Level AA**: Recommended for most websites (target standard)
- **Level AAA**: Enhanced accessibility (nice-to-have, spesso difficile per design)

### Core Web Vitals Thresholds
- **LCP** (Largest Contentful Paint): <2.5s (good), 2.5-4s (needs improvement), >4s (poor)
- **FID** (First Input Delay): <100ms (good), 100-300ms (needs improvement), >300ms (poor)
- **CLS** (Cumulative Layout Shift): <0.1 (good), 0.1-0.25 (needs improvement), >0.25 (poor)

### Vercel Design Resources
- [Vercel Design System](https://vercel.com/design)
- [Geist Font](https://vercel.com/font) — Recommended for Vercel-style aesthetics
- [shadcn/ui](https://ui.shadcn.com) — Production-ready components

---

## Changelog

- **2026-04-10**: Skill creata con 100+ regole di audit
