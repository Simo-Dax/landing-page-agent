---
name: framer-motion
description: Reference operativa per progettare e specificare animazioni con Motion (ex Framer Motion). Da usare quando una landing/sito richiede reveal allo scroll, micro-interazioni, transizioni di pagina, parallax, stagger o gesture. L'agente produce spec + snippet pronti per dev React o per page builder (Framer/Webflow).
type: reference
source: https://motion.dev — https://www.framer.com/dictionary/framer-motion
---

# Motion (ex Framer Motion) — Reference per Landing Page ad alta conversione

## Cos'è e naming

- Libreria di animazione per il web. Nata come **Framer Motion** (React), oggi il pacchetto si chiama **`motion`** e copre React **e** vanilla JS. Docs ufficiali: **motion.dev**.
- In **Framer** (no-code) le stesse capacità sono native: si specificano via UI, non via codice. Per Webflow/WordPress serve l'integrazione React o un equivalente (GSAP) — vedi `04_references-tecniche-design.md`.

## Quando usarla in una LP (CRO-first)

L'animazione esiste per **guidare l'attenzione e ridurre l'attrito**, mai per decorare. Regole:

- **Reveal allo scroll** sulle sezioni → crea ritmo, non nasconde contenuto critico above the fold.
- **Stagger** su liste (feature, pricing, testimonial) → percezione di ordine e qualità.
- **Micro-interazioni** su CTA (hover/tap) → feedback tattile, aumenta affordance del click.
- **Transizioni di stato** (FAQ, tab, modali) → continuità cognitiva.
- **MAI** animare l'hero in modo che ritardi la lettura della headline o il render della CTA. Il primo paint deve mostrare value prop + CTA.

## Install + import

```bash
npm install motion
```

```javascript
// React
import { motion, AnimatePresence, useScroll, useTransform } from "motion/react"

// Vanilla JS
import { animate, scroll, stagger, inView } from "motion"
```

## API core (React)

Props del componente `<motion.*>`:

| Prop | Scopo |
|---|---|
| `initial` | Stato di partenza prima dell'animazione |
| `animate` | Stato target |
| `exit` | Animazione all'uscita dal DOM (richiede `<AnimatePresence>`) |
| `transition` | Durata, easing, delay, spring physics |
| `variants` | Stati predefiniti riusabili (+ orchestrazione/stagger) |
| `whileHover` / `whileTap` | Trigger su hover / tap |
| `whileInView` | Trigger quando entra nel viewport |

### CTA con micro-interazione

```jsx
<motion.button
  whileHover={{ scale: 1.04 }}
  whileTap={{ scale: 0.96 }}
  transition={{ type: "spring", stiffness: 400, damping: 25 }}
>
  Inizia ora
</motion.button>
```

### Reveal di sezione allo scroll (one-shot)

```jsx
<motion.section
  initial={{ opacity: 0, y: 40 }}
  whileInView={{ opacity: 1, y: 0 }}
  viewport={{ once: true, amount: 0.3 }}
  transition={{ duration: 0.5, ease: "easeOut" }}
>
  {/* contenuto */}
</motion.section>
```

`viewport={{ once: true }}` → anima una sola volta (non al re-scroll). `amount` = quanta parte deve essere visibile.

### Stagger su lista (variants)

```jsx
const container = {
  hidden: {},
  show: { transition: { staggerChildren: 0.08 } },
}
const item = {
  hidden: { opacity: 0, y: 20 },
  show: { opacity: 1, y: 0 },
}

<motion.ul variants={container} initial="hidden" whileInView="show" viewport={{ once: true }}>
  {features.map((f) => (
    <motion.li key={f.id} variants={item}>{f.label}</motion.li>
  ))}
</motion.ul>
```

### Scroll-linked (progress bar / parallax)

```jsx
const { scrollYProgress } = useScroll()
return <motion.div style={{ scaleX: scrollYProgress, transformOrigin: "left" }} />
```

```jsx
// Parallax di un'immagine
const { scrollYProgress } = useScroll({ target: ref, offset: ["start end", "end start"] })
const y = useTransform(scrollYProgress, [0, 1], ["-10%", "10%"])
return <motion.img ref={ref} style={{ y }} />
```

### Exit / AnimatePresence (modali, FAQ, toast)

```jsx
<AnimatePresence>
  {open && (
    <motion.div
      initial={{ opacity: 0, height: 0 }}
      animate={{ opacity: 1, height: "auto" }}
      exit={{ opacity: 0, height: 0 }}
    />
  )}
</AnimatePresence>
```

### Vanilla JS (no React)

```javascript
import { animate, inView, stagger } from "motion"

inView("section", (info) => {
  animate(info.target, { opacity: [0, 1], y: [40, 0] }, { duration: 0.5 })
})

animate(".feature", { opacity: [0, 1], y: [20, 0] }, { delay: stagger(0.08) })
```

## Performance & accessibilità (non negoziabili)

- Anima **solo `transform` e `opacity`** quando possibile (GPU, no layout reflow). Evita animare `width/height/top/left` su elementi grandi.
- Rispetta **`prefers-reduced-motion`**: disattiva o riduci. In React usa `useReducedMotion()`; in CSS fallback `@media (prefers-reduced-motion: reduce)`.
- `viewport={{ once: true }}` di default sui reveal → evita animazioni ripetute fastidiose.
- Mobile: durate brevi (200–500ms), easing `easeOut`. Niente bounce esagerato sulle CTA (anti-pattern segnalato anche da impeccable).

```jsx
const reduce = useReducedMotion()
<motion.div animate={reduce ? {} : { y: 0, opacity: 1 }} />
```

## Come specificare per il dev / page builder

Quando l'output va a un developer o a Framer/Webflow, scrivi la spec così:

```
[Sezione Hero]
- Headline: fade-in + slide-up (y: 24px → 0), 0.5s easeOut, on load
- CTA: hover scale 1.04 (spring), tap scale 0.96
- Reveal: trigger whileInView once, amount 0.3

[Lista Feature]
- Stagger children 0.08s, item fade + slide-up 20px
```

Sempre: **trigger** (load / inView / hover / scroll) · **proprietà** (opacity, y, scale) · **timing** (durata, easing, delay/stagger) · **once?**.

## Anti-pattern (evita)

- Hero che ritarda headline/CTA.
- Animazioni al re-scroll (manca `once: true`).
- Bounce/overshoot sulle CTA.
- Animare proprietà di layout (jank).
- Ignorare `prefers-reduced-motion`.
