# 01_landing_brief.md — Direttiva: Brief CRO per Landing Page

## Scopo

Questa direttiva governa il processo di raccolta informazioni prima di produrre qualsiasi
output su una landing page o sito. Nessun copy, nessuna architettura, nessuna specifica UX
viene prodotta senza un brief validato e approvato dall'utente.

Il brief non è un questionario formale da compilare. È un documento operativo che
l'agente costruisce attivamente, integrando le informazioni fornite dall'utente con
inferenze esplicite e domande mirate solo dove i gap sono bloccanti.

---

## Step 1 — Raccolta Informazioni

### Informazioni obbligatorie (senza queste non si procede)

**1. Obiettivo di conversione primario**
- Cosa deve fare il visitatore sulla pagina?
- Un solo obiettivo. Se l'utente ne indica più di uno, chiedi quale è il primario.
- Esempi: prenotare una call, avviare un trial, acquistare, scaricare un lead magnet,
  iscriversi a una lista, richiedere un preventivo.

**2. Audience target**
- Chi è il visitatore ideale? Ruolo, settore, dimensione azienda (se B2B) o
  demografica e bisogno principale (se B2C).
- Qual è il livello di consapevolezza del problema e del prodotto?
  (Usa il framework Awareness di Eugene Schwartz se utile: unaware / problem aware /
  solution aware / product aware / most aware)
- Quali sono le 2-3 obiezioni principali di questa audience?

**3. Sorgente di traffico**
- Da dove arrivano i visitatori? Google Ads (search / display / PMax), Meta Ads,
  email, SEO organico, referral, social organico, altro.
- Se paid: qual è il messaggio dell'annuncio o il tema della campagna?
- Se SEO: qual è la keyword o l'intent principale?

**4. Offerta**
- Cosa viene offerto nella pagina? Descrivi in modo preciso: prodotto, servizio,
  contenuto, accesso, consulenza, etc.
- C'è un incentivo o una limitazione temporale? (Sconto, bonus, deadline, posti
  limitati, etc.)
- Qual è il prezzo o il commitment richiesto? (Gratuito, a pagamento, demo,
  preventivo, etc.)

**5. KPI primario**
- Come si misura il successo di questa pagina?
- Conversion rate attuale (se è una pagina esistente) o benchmark di riferimento.
- Volume di traffico atteso o attuale.

---

### Informazioni utili (raccoglile se disponibili, inferisci se non lo sono)

**6. Competitor e posizionamento**
- Chi sono i 2-3 competitor principali per questa audience?
- Qual è la differenziazione principale rispetto a loro?
- C'è qualcosa che i competitor fanno meglio nella comunicazione?

**7. Contesto del funnel**
- Questa pagina è un punto di ingresso (top of funnel) o una pagina di conversione
  per traffico già warm?
- Cosa succede dopo la conversione? (Sequenza email, call di vendita, onboarding,
  acquisto diretto)

**8. Vincoli tecnici e di brand**
- Esiste già un visual identity o brand kit da rispettare?
- Ci sono vincoli sul page builder o CMS? (Webflow, Framer, WordPress, Shopify,
  custom, altro)
- Ci sono sezioni o elementi obbligatori richiesti dal cliente o dall'azienda?

**9. Dati esistenti**
- Ci sono heatmap, session recording, feedback utenti o test A/B già eseguiti?
- Ci sono survey o interviste clienti con insight sull'audience?
- Ci sono dati Google Analytics o equivalenti sulla pagina attuale?

**10. Social proof disponibile**
- Testimonianze con nome, ruolo e azienda: quante e di che tipo?
- Case study con risultati misurabili: disponibili?
- Numeri da comunicare: clienti, risultati, anni di attività, etc.?
- Loghi clienti: disponibili e riconoscibili dall'audience target?

---

## Step 2 — Costruzione del Brief

Quando le informazioni obbligatorie sono disponibili (anche parzialmente), l'agente
produce un brief strutturato con questa struttura:

```
## Brief CRO — [Nome Progetto / Pagina]

**Data:** [data]
**Versione:** 1.0

### Obiettivo
[Obiettivo di conversione primario, una frase]

### Audience
[Descrizione dell'audience target con livello di awareness]

### Sorgente di traffico
[Canale/i + messaggio dell'annuncio se paid]

### Offerta
[Descrizione precisa dell'offerta + commitment richiesto]

### KPI
[Metrica principale di successo + baseline se disponibile]

### Obiezioni principali
1. [Obiezione 1]
2. [Obiezione 2]
3. [Obiezione 3]

### Differenziazione
[Perché questa offerta rispetto ai competitor]

### Social proof disponibile
[Elenco di quanto disponibile: testimonianze, numeri, loghi]

### Vincoli
[Tecnici, di brand, di contenuto]

### Assunzioni esplicite
[Tutto ciò che l'agente ha inferito e non confermato dall'utente]
[Marca ogni assunzione con: ASSUNTO — da confermare]

### Gap informativi
[Informazioni mancanti che potrebbero cambiare l'output]
[Marca ogni gap con: GAP — impatto [alto/medio/basso]]
```

---

## Step 3 — Checkpoint Obbligatorio

Dopo aver prodotto il brief, l'agente si ferma e chiede approvazione esplicita.

Non si passa alla fase di architettura senza conferma.

Il checkpoint si formula così:

```
Brief CRO completato. Prima di procedere con l'architettura della pagina, conferma:

1. Le assunzioni segnate come "ASSUNTO" sono corrette?
2. I gap segnati come "GAP — impatto alto" richiedono una risposta prima di procedere?
3. L'obiettivo di conversione e l'audience descritti rispecchiano il progetto?

Se tutto è corretto, rispondi "ok" e passo all'architettura.
Se ci sono correzioni, forniscile e aggiornerò il brief prima di procedere.
```

---

## Step 4 — Output Successivi (dopo approvazione del brief)

Una volta approvato il brief, la sequenza di output è:

1. **Architettura della pagina** (struttura delle sezioni, logica di flusso)
   → Direttiva: `02_landing_architecture.md`

2. **Copy + specifiche UX** (testi per ogni blocco, note per developer)
   → Direttiva: `03_landing_copy.md`

3. **Self-check CRO** (verifica dell'output contro `directives/00_cro_principles.md`)
   → Direttiva: `04_editing_selfcheck.md`

---

## Regole di questa Direttiva

**Non fare:**
- Non produrre copy o architettura prima che il brief sia approvato
- Non assumere che le informazioni fornite siano complete senza verifica
- Non saltare la sezione "Assunzioni esplicite": ogni inferenza deve essere dichiarata
- Non chiedere tutte le informazioni opzionali se quelle obbligatorie non sono ancora
  chiare: prima chiudi i gap bloccanti, poi quelli secondari

**Fare:**
- Se mancano più di 2 informazioni obbligatorie, fai domande in batch (max 3 per volta)
- Se manca solo 1 informazione obbligatoria, dichiara un'assunzione e procedi
- Aggiorna questo documento se nel corso dei progetti emergono pattern ricorrenti
  di informazioni mancanti o assunzioni sbagliate

---

## Riferimento Rapido — Domande per Gap Bloccanti

Se l'utente fornisce un contesto minimo (es. solo "devo fare una landing per X"),
usa queste domande come punto di partenza prioritario:

```
Per costruire il brief ho bisogno di tre informazioni base:

1. Obiettivo: cosa deve fare il visitatore sulla pagina?
   (es. prenotare una call, avviare un trial, acquistare)

2. Traffico: da dove arrivano i visitatori?
   (es. Google Ads su keyword specifica, campagna Meta cold audience, email list warm)

3. Audience: chi è il visitatore ideale e qual è la sua obiezione principale?
```

Queste tre informazioni sono sufficienti per iniziare un brief preliminare con
assunzioni esplicite. Il brief viene poi raffinato iterativamente.
