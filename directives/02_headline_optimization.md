# 03b - Headline & Subheading Optimization

## Obiettivo
Generare headline e subheading ottimizzati per massimizzare aperture, lettura e condivisioni dell'email/newsletter.

## Quando si usa
Dopo che la newsletter (Step 3) è stata approvata. Prima di passare ai post social (Step 4).

## Input
- `output/[data]-[slug]/newsletter-[slug].md` (newsletter approvata)
- `.tmp/brief.md`
- `context/brand/tone_of_voice.md`

## Processo

### 1. Genera varianti headline (minimo 8)

Per ogni variante, applica una leva diversa:

| # | Leva | Esempio pattern |
|---|------|-----------------|
| 1 | **Numero specifico** | "7 errori che il 90% dei marketer fa con il ROAS" |
| 2 | **Curiosity gap** | "Quello che nessuno ti dice sul budget allocation" |
| 3 | **Controintuitivo** | "Abbiamo spento tutte le campagne. I risultati sono migliorati." |
| 4 | **Problema diretto** | "Stai perdendo soldi sulle Ads e non lo sai" |
| 5 | **How-to pratico** | "Come fare un'analisi di mercato in 60 minuti con l'AI" |
| 6 | **Risultato concreto** | "+44% di conversioni con un singolo cambio nel funnel" |
| 7 | **Domanda provocatoria** | "Il ROAS è davvero la metrica che conta?" |
| 8 | **Framework/metodo** | "Il metodo ICE: come prioritizzare le tue campagne" |

### 2. Valuta ogni variante

Per ciascuna headline, assegna un punteggio 1-5 su:

- **Specificità** — contiene numeri, nomi, dettagli concreti?
- **Curiosity** — crea abbastanza tensione da voler cliccare?
- **Chiarezza** — si capisce di cosa parla in <3 secondi?
- **Coerenza col tono** — suona come il brand o come un guru americano?
- **Lunghezza** — ideale: 6-12 parole. la piattaforma email tronca dopo ~60 caratteri nell'anteprima email.

### 3. Genera varianti subheading (3-5)

Il subheading appare sotto il titolo nell'anteprima email. Deve:
- Completare la promessa del titolo (non ripeterla)
- Aggiungere contesto: per chi è, cosa ottieni, perché ora
- Max 100 caratteri
- Tono: diretto, specifico, zero hype

**Pattern efficaci:**
- "[Cosa impari] + [in quanto tempo/con quale metodo]"
- "[Il problema] che ti costa [conseguenza]"
- "Una guida pratica per [target] che [condizione]"

### 4. Proponi combinazione finale

Presenta la top 3 combinazioni headline + subheading con motivazione.

## Output

Salva in: `.tmp/headlines-[slug].md`

```markdown
# Headline Optimization: [slug]

## Top 3 combinazioni raccomandate

### Opzione A (raccomandata)
- **Headline:** [testo]
- **Subheading:** [testo]
- **Perché:** [1 riga di motivazione]

### Opzione B
- **Headline:** [testo]
- **Subheading:** [testo]
- **Perché:** [1 riga di motivazione]

### Opzione C
- **Headline:** [testo]
- **Subheading:** [testo]
- **Perché:** [1 riga di motivazione]

## Tutte le varianti generate

| # | Headline | Specificità | Curiosity | Chiarezza | Tono | Lunghezza | Score |
|---|----------|------------|-----------|-----------|------|-----------|-------|
| 1 | ... | /5 | /5 | /5 | /5 | /5 | /25 |
| ... |
```

## Regole

1. **Mai clickbait vuoto.** La headline deve promettere qualcosa che l'articolo mantiene.
2. **Mai superlativo non supportato.** "La migliore strategia di sempre" è bandito.
3. **Mai copiare pattern da guru.** "Il segreto che nessuno ti dice" è abusato. Sii originale.
4. **Testa il "test bar".** Immagina di vedere il titolo nella inbox tra altre 30 email. Cliccheresti?
5. **Il subheading non è un riassunto.** È un acceleratore di click. Deve aggiungere, non ripetere.

## Edge case
- **Articolo molto tecnico:** usa headline che bilanci tecnicità con accessibilità
- **Tema già trattato:** differenzia con l'angolo specifico di questa edizione
- **Headline troppo lunga:** versione breve per l'email + versione estesa come titolo H1 nell'articolo
