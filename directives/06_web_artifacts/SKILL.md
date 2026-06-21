---
name: web-artifacts-builder
description: Generate functional, interactive React + Tailwind CSS and shadcn/ui components optimized for Claude's artifact interface. Use when the user needs working UI components, interactive demos, or landing page sections that can be previewed directly in Claude.
license: Complete terms in LICENSE.txt
---

# Web Artifacts Builder — Claude Artifacts Optimization

Questa skill è specializzata nella creazione di componenti web interattivi e funzionali ottimizzati per l'interfaccia Artifacts di Claude. Produce React + Tailwind CSS + shadcn/ui components pronti all'uso, testabili direttamente nell'interfaccia di Claude.

## Quando Usare Questa Skill

- L'utente chiede di "vedere" o "provare" un componente/sezione di landing page
- Serve un prototipo interattivo rapido per validare un'idea
- Il componente richiede interattività (form, accordion, tab, carousel, etc.)
- Si vuole testare un pattern UI prima di passarlo al developer
- Serve un demo funzionante per presentare un concept al cliente

**NON usare questa skill se:**
- Serve solo il copy testuale (usa copywriting directives)
- Serve un design statico completo (usa frontend-design)
- Il componente è troppo complesso per un artifact singolo (>500 righe di codice)

---

## Principi di Design per Artifacts

### 1. Self-Contained & Functional
Ogni artifact deve essere completamente autonomo:
- Nessuna dipendenza esterna che non sia già disponibile in Claude artifacts
- Tailwind CSS integrato (classi inline)
- shadcn/ui components se necessario
- Tutti gli stati e le logiche contenuti nel componente

### 2. Immediate Visual Impact
L'utente deve capire cosa fa il componente in <3 secondi:
- Design pulito e chiaro
- Dati di esempio realistici (non "Lorem ipsum" o "Example content")
- Stati interattivi visibili (hover, focus, active)
- Feedback visivo immediato alle azioni utente

### 3. Production-Ready Code
Anche se è un prototipo, il codice deve essere:
- Leggibile e ben strutturato
- Accessibile (ARIA labels, keyboard navigation)
- Responsive (mobile-first)
- Performante (no re-renders inutili, lazy loading dove serve)

---

## Stack Tecnologico Supportato

### Core
- **React 18+** (con hooks: useState, useEffect, useRef, useMemo, useCallback)
- **Tailwind CSS 3+** (utility-first, responsive, dark mode support)
- **TypeScript** (opzionale ma raccomandato per componenti complessi)

### UI Components (shadcn/ui)
Usa shadcn/ui per componenti comuni:
- Button, Input, Textarea, Select, Checkbox, Radio
- Dialog, Sheet, Popover, Tooltip
- Accordion, Tabs, Card, Badge
- Alert, Toast (per feedback)
- Form (con react-hook-form integration)

### Icons & Visual Assets
- **Lucide React** per icone (preferito, già disponibile in artifacts)
- **Hero Icons** (alternativa)
- Evita immagini esterne: usa placeholder SVG o gradient backgrounds

### Animations
- **Tailwind transitions** per micro-interactions
- **Framer Motion** per animazioni complesse (se necessario)
- **CSS keyframes** per animazioni custom semplici

---

## Processo di Creazione

### Step 1 — Analisi del Contesto
Prima di scrivere codice, chiarisci:
- **Scopo**: Cosa deve fare questo componente?
- **Contesto**: Dove appare nella landing page? (Hero, features, pricing, CTA, footer?)
- **Dati**: Che contenuti deve mostrare? (Usa dati realistici dal brief o dal copy)
- **Interazioni**: Quali azioni deve supportare? (Click, hover, scroll, form submit?)

### Step 2 — Definisci la Struttura
Scegli il pattern UI appropriato:
- **Hero Section**: Grande titolo, CTA primaria, visual/video, optional trust badges
- **Features Grid**: 3-4 colonne, icone, titolo, descrizione breve
- **Pricing Table**: Confronto affiancato, highlight piano consigliato
- **Testimonial Carousel**: Slider con foto, nome, ruolo, quote
- **FAQ Accordion**: Domande espandibili, max 6-8 item
- **CTA Section**: Titolo bold, sub, CTA primaria + secondaria, sfondo a contrasto
- **Form**: Input validati, error states, success feedback

### Step 3 — Scrivi il Codice
Template standard per un artifact React:

```tsx
import React, { useState } from 'react';
import { Button } from '@/components/ui/button';
import { ChevronDown, Check } from 'lucide-react';

export default function ComponentName() {
  const [activeState, setActiveState] = useState(false);

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 to-slate-100 p-8">
      <div className="max-w-7xl mx-auto">
        {/* Component content */}
        <section className="space-y-6">
          <h1 className="text-4xl font-bold tracking-tight text-slate-900">
            Headline Here
          </h1>
          <p className="text-xl text-slate-600">
            Subheadline or description
          </p>
          <Button
            onClick={() => setActiveState(!activeState)}
            className="bg-blue-600 hover:bg-blue-700"
          >
            Primary CTA
          </Button>
        </section>
      </div>
    </div>
  );
}
```

**Checklist codice:**
- [ ] Imports corretti e disponibili in Claude artifacts
- [ ] Component esportato come default
- [ ] Stati inizializzati con valori sensati
- [ ] Classi Tailwind responsive (sm:, md:, lg:)
- [ ] Dark mode support se rilevante (dark:)
- [ ] Accessibilità (aria-label, role, keyboard nav)
- [ ] Dati realistici (no placeholder generici)

### Step 4 — Ottimizza per l'Artifact Viewer
Claude artifacts ha viewport limitato:
- **Desktop**: ~800px width max visibile senza scroll orizzontale
- **Mobile**: supporta breakpoint responsive

**Best practices:**
- Container: `max-w-7xl mx-auto px-4 sm:px-6 lg:px-8`
- Padding generoso: `p-8` o `py-16 px-6`
- Font size: `text-base` (16px) come base, `text-4xl` per headline
- Spacing: `space-y-6` per sezioni, `gap-4` per grid

### Step 5 — Aggiungi Note per il Developer
Dopo il codice, fornisci sempre:
- **Descrizione**: Cosa fa il componente, dove va usato
- **Customization notes**: Cosa può essere facilmente modificato (colori, testi, layout)
- **Integration tips**: Come integrarlo in un progetto esistente
- **Dependencies**: Librerie necessarie se non già in artifacts

---

## Pattern Library — Componenti Comuni

### Hero Section con CTA Dual
```tsx
<section className="relative bg-gradient-to-br from-blue-50 to-indigo-100 py-20">
  <div className="max-w-4xl mx-auto px-6 text-center">
    <h1 className="text-5xl font-extrabold text-gray-900 mb-6">
      Your Main Value Proposition
    </h1>
    <p className="text-xl text-gray-600 mb-10 max-w-2xl mx-auto">
      Supporting headline that clarifies the promise
    </p>
    <div className="flex gap-4 justify-center">
      <Button size="lg" className="bg-blue-600 hover:bg-blue-700">
        Primary CTA
      </Button>
      <Button size="lg" variant="outline">
        Secondary CTA
      </Button>
    </div>
  </div>
</section>
```

### Features Grid (3 colonne)
```tsx
const features = [
  { icon: Zap, title: "Fast", description: "Lightning-fast performance" },
  { icon: Shield, title: "Secure", description: "Bank-level security" },
  { icon: Heart, title: "Easy", description: "Simple to use" }
];

<div className="grid md:grid-cols-3 gap-8">
  {features.map((feature, idx) => (
    <div key={idx} className="p-6 bg-white rounded-lg shadow-sm hover:shadow-md transition">
      <feature.icon className="w-10 h-10 text-blue-600 mb-4" />
      <h3 className="text-xl font-semibold mb-2">{feature.title}</h3>
      <p className="text-gray-600">{feature.description}</p>
    </div>
  ))}
</div>
```

### Pricing Table Comparison
```tsx
const plans = [
  { name: "Starter", price: "$29", features: ["Feature A", "Feature B"], popular: false },
  { name: "Pro", price: "$99", features: ["Everything in Starter", "Feature C", "Feature D"], popular: true },
  { name: "Enterprise", price: "Custom", features: ["Everything in Pro", "Feature E", "Priority Support"], popular: false }
];

<div className="grid md:grid-cols-3 gap-6">
  {plans.map((plan, idx) => (
    <div key={idx} className={`p-8 rounded-lg border-2 ${plan.popular ? 'border-blue-600 shadow-xl' : 'border-gray-200'}`}>
      {plan.popular && <span className="bg-blue-600 text-white px-3 py-1 rounded-full text-sm mb-4 inline-block">Most Popular</span>}
      <h3 className="text-2xl font-bold mb-2">{plan.name}</h3>
      <div className="text-4xl font-extrabold mb-6">{plan.price}<span className="text-lg text-gray-500">/mo</span></div>
      <ul className="space-y-3 mb-8">
        {plan.features.map((f, i) => (
          <li key={i} className="flex items-center gap-2">
            <Check className="w-5 h-5 text-green-600" />
            <span>{f}</span>
          </li>
        ))}
      </ul>
      <Button className={plan.popular ? 'w-full bg-blue-600' : 'w-full'} variant={plan.popular ? 'default' : 'outline'}>
        Get Started
      </Button>
    </div>
  ))}
</div>
```

---

## Regole di Questa Skill

### ✅ Fare
- Usare dati realistici dal brief/copy della landing page
- Responsive mobile-first (test a 375px width)
- Accessibilità: keyboard navigation, ARIA labels, focus states
- Stati visivi chiari: loading, error, success, empty state
- Transizioni fluide con Tailwind (transition-all, duration-200)
- Comments nel codice per sezioni complesse

### ❌ Non Fare
- Non usare immagini esterne (usa SVG, gradient, o placeholder inline)
- Non importare librerie non disponibili in Claude artifacts
- Non creare componenti troppo complessi (>500 righe)
- Non usare placeholder generici ("Lorem ipsum", "Example", "Test")
- Non ignorare dark mode se il design lo supporta
- Non scrivere codice non funzionante o con errori sintattici

---

## Output Finale

Dopo aver generato l'artifact, fornisci sempre:

```markdown
## 🎨 Componente: [Nome]

**Tipo:** [Hero / Features / Pricing / Form / CTA / etc.]
**Tech Stack:** React 18 + Tailwind CSS 3 + shadcn/ui

### Descrizione
[1-2 righe: cosa fa, dove va usato nella landing]

### Customization Quick Guide
- **Colori**: Modifica `bg-blue-600` con il colore del brand
- **Testi**: [Indica dove sono i testi da personalizzare]
- **Layout**: [Indica breakpoint responsive e come modificarli]

### Integrazione
Per usare questo componente in un progetto:
1. Copia il codice nell'artifact viewer
2. Installa dependencies: `npm install lucide-react @radix-ui/react-*`
3. Configura Tailwind CSS (se non già fatto)
4. Importa shadcn/ui components necessari

### Note per il Developer
[Eventuali note tecniche aggiuntive, edge case, performance tips]
```

---

## Edge Cases & Troubleshooting

### Component troppo complesso per un artifact singolo
Se il componente supera 500 righe o ha troppa logica:
- Spezza in sub-components più piccoli
- Crea artifacts separati per ogni sezione (Hero, Features, Pricing, etc.)
- Fornisci istruzioni su come assemblarli

### Dati dinamici / API integration
Se il componente richiede dati da API esterne:
- Usa dati mock hardcoded nell'artifact
- Fornisci esempio di come sostituire con fetch/API call
- Aggiungi loading state con skeleton UI

### Animation performance
Se le animazioni sono lag:
- Preferisci CSS transitions a JavaScript animations
- Usa `will-change` property per elementi animati
- Limita animazioni a transform e opacity (GPU-accelerated)

---

## Riferimenti Rapidi

### Tailwind Spacing Scale
- `p-4` = 1rem (16px)
- `p-6` = 1.5rem (24px)
- `p-8` = 2rem (32px)
- `p-12` = 3rem (48px)
- `p-16` = 4rem (64px)

### Font Size Scale
- `text-sm` = 0.875rem (14px)
- `text-base` = 1rem (16px)
- `text-lg` = 1.125rem (18px)
- `text-xl` = 1.25rem (20px)
- `text-2xl` = 1.5rem (24px)
- `text-4xl` = 2.25rem (36px)
- `text-5xl` = 3rem (48px)

### Responsive Breakpoints
- `sm:` = 640px
- `md:` = 768px
- `lg:` = 1024px
- `xl:` = 1280px
- `2xl:` = 1536px
