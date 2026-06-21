# Web Artifacts Builder — README

## Overview
Skill per la creazione di componenti web interattivi ottimizzati per Claude Artifacts: React + Tailwind CSS + shadcn/ui.

## Quick Start
```bash
# Quando l'utente chiede:
"Mostrami come appare questa hero section"
"Crea un prototipo interattivo del pricing table"
"Voglio vedere il form in azione"

# Tu rispondi con un artifact React completo e funzionante
```

## Output Type
- Codice React/TypeScript pronto per il viewer Artifacts di Claude
- Componenti self-contained, interattivi, responsive
- Dati realistici (no placeholder)

## Integration con il Workflow Landing Page
1. Brief → Copy → **Web Artifact** per validare visivamente → Passaggio a developer
2. Utile per checkpoint visivi durante il processo di creazione

## Limitazioni
- Max ~500 righe di codice per artifact
- Solo dipendenze disponibili in Claude (React, Tailwind, shadcn/ui, Lucide icons)
- No immagini esterne (usa SVG inline o gradient)
