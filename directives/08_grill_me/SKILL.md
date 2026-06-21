---
name: grill-me
description: Requirements handshake through structured interrogation. Forces thorough requirement gathering before any creation work begins, reducing ambiguity and preventing wasted iterations. Use when project requirements are vague, incomplete, or when you need to clarify the full scope before starting.
license: Complete terms in LICENSE.txt
---

# Grill Me — Requirements Handshake Skill

Questa skill implementa un processo di "interrogatorio strutturato" per raccogliere requirements completi prima di iniziare qualsiasi lavoro creativo. Previene iterazioni inutili, allineamenti tardivi e output che non matchano le aspettative.

## Quando Usare Questa Skill

**Usa Grill Me quando:**
- L'utente fornisce un task vago o generico (es. "Crea una landing page per il mio prodotto")
- Mancano 3+ informazioni obbligatorie del brief CRO
- Il progetto è complesso e multi-fase (es. sito completo, funnel multi-step)
- Ci sono stakeholder multipli con aspettative non allineate
- Vuoi evitare "sorprese" a metà progetto

**NON usare quando:**
- L'utente ha già fornito un brief dettagliato e completo
- Il task è semplice e le informazioni essenziali sono chiare
- Sei a metà di un progetto già avviato (usa domande mirate, non full handshake)

**Relazione con 01_landing_brief.md:**
- Grill Me è la versione "interrogativa" del brief CRO
- Se il brief ha 3+ gap bloccanti → usa Grill Me
- Se il brief ha 1-2 gap → domande mirate dirette, senza Grill Me

---

## Filosofia del Requirements Handshake

Il problema comune:
```
Utente: "Fammi una landing page"
Agent: [crea output basato su assunzioni]
Utente: "No, non è questo che volevo"
Agent: [riciclo]
```

Il processo Grill Me:
```
Utente: "Fammi una landing page"
Agent: "Prima di iniziare, ho bisogno di chiarire alcuni punti fondamentali. Ti faccio alcune domande mirate."
[Grill Me session: 5-10 minuti di Q&A]
Agent: "Perfetto, ora ho tutto chiaro. Procedo con [output specifico]."
Utente: "Esattamente quello che volevo!"
```

**ROI del Grill Me:**
- 5-10 minuti di domande iniziali risparmiano ore di rework
- Output allineato al primo tentativo (o quasi)
- Riduce frustrazione da entrambe le parti

---

## Processo Grill Me — 4 Fasi

### Fase 1: Context Discovery (Contesto di Business)

**Obiettivo:** Capire il "perché" prima del "cosa".

Domande obbligatorie:
1. **Business model e obiettivo**
   - "Qual è il business model principale? (SaaS, e-commerce, consulenza, lead gen, etc.)"
   - "Qual è l'obiettivo primario di questa landing page? (Lead acquisition, trial signup, direct purchase, brand awareness, event registration, etc.)"
   - "Come misuri il successo? Qual è il KPI primario?"

2. **Stage del business**
   - "Sei in fase di lancio (pre-product/market fit) o di scale (post-PMF)?"
   - "Hai già traffico da portare sulla pagina o la pagina è il punto di partenza?"
   - "Budget per traffico: quanto puoi spendere per acquisire un lead/cliente?"

3. **Contesto competitivo**
   - "Chi sono i 2-3 competitor principali per questa audience?"
   - "Cosa fanno meglio di te nei loro messaging/landing page?"
   - "Qual è la tua differenziazione unica? (No generic value props, be specific)"

**Output Fase 1:** Business Context Summary (2-3 bullet points)

---

### Fase 2: Audience & Positioning Deep Dive

**Obiettivo:** Definire chi è l'audience e a che livello di awareness si trova.

Domande obbligatorie:
1. **Audience primaria**
   - "Chi è il tuo cliente ideale? (Ruolo, settore, company size se B2B; demografica e bisogno se B2C)"
   - "Descrivi il problema principale che questa persona ha e che il tuo prodotto/servizio risolve."
   - "Questa persona è consapevole di avere questo problema? (Scala: unaware → problem aware → solution aware → product aware → most aware)"

2. **Jobs to Be Done**
   - "Quando qualcuno 'hires' il tuo prodotto, qual è il job che sta cercando di fare?"
   - "Quali alternative usa oggi per fare questo job? (Include 'doing nothing')"
   - "Perché quelle alternative non funzionano bene?"

3. **Obiezioni & Friction**
   - "Quali sono le 3 obiezioni principali che questa persona ha prima di comprare/iscriversi?"
     - Es. Prezzo troppo alto, troppo complesso, 'non per me', non si fida, timing sbagliato, etc.
   - "Qual è la friction più grande nel processo di decisione?"

**Output Fase 2:** Audience Profile + Obiezioni Top 3

---

### Fase 3: Offer & Conversion Mechanics

**Obiettivo:** Definire cosa offri, come lo offri, e quale commitment richiedi.

Domande obbligatorie:
1. **Offerta specifica**
   - "Descrivi l'offerta in una frase: 'I give you [X], you give me [Y]'."
   - "Questa offerta è free trial, freemium, paid demo, lead magnet, direct purchase, consultation request, altro?"
   - "Se c'è un prezzo, qual è? Se è free, qual è il 'prezzo' implicito (tempo, dati, commitment)?"

2. **Urgency & Scarcity**
   - "C'è una ragione urgente per agire ora? (Deadline, sconto limitato, posti limitati, problema critico da risolvere subito)"
   - "Se no, come crei motivazione ad agire ora invece che 'ci penso e torno più tardi'?"

3. **Conversion funnel**
   - "Cosa succede dopo che l'utente converte? (Email sequence, sales call, onboarding automatico, accesso immediato, altro)"
   - "Quanto è lungo il sales cycle? (Immediate purchase, 1-2 call, 3+ touchpoint, enterprise 6+ mesi?)"
   - "Chi è coinvolto nella decisione finale? (Solo l'utente, team, manager approval, procurement, etc.)"

**Output Fase 3:** Offer Statement + Conversion Path

---

### Fase 4: Traffic Source & Message Match

**Obiettivo:** Assicurarsi che la landing page parli la stessa lingua del traffico che arriva.

Domande obbligatorie:
1. **Sorgente di traffico primaria**
   - "Da dove arrivano i visitatori? (Google Ads search, Meta Ads cold audience, email warm list, SEO organico, referral, social organico, altro)"
   - "Se paid: qual è il messaggio dell'annuncio o il tema della campagna?"
   - "Se SEO: qual è la keyword principale o l'intent di ricerca?"

2. **Message match**
   - "Quale parola/frase chiave l'utente ha appena letto/pensato prima di cliccare?"
   - "Qual è lo stato emotivo dell'utente quando arriva sulla pagina? (Curioso, frustrato, urgente, esplorativo, scettico, etc.)"

3. **Awareness level**
   - "L'utente sa già chi sei? (Brand awareness: mai sentito parlare → conosce bene)"
   - "L'utente ha già interagito con te? (Cold traffic → warm → hot → existing customer)"

**Output Fase 4:** Traffic Source + Message Match Statement

---

## Step 5: Assets & Constraints Check

**Obiettivo:** Capire cosa hai già e cosa manca.

Domande rapide:
1. **Social proof disponibile**
   - "Hai testimonianze clienti con nome, ruolo, azienda?"
   - "Hai case study con risultati misurabili?"
   - "Hai numeri da comunicare (X clienti, Y risultati, Z anni di attività)?"
   - "Hai loghi di clienti riconoscibili dall'audience target?"

2. **Visual assets**
   - "Hai screenshot del prodotto, foto, video, demo?"
   - "Hai brand guidelines (colori, font, logo) da rispettare?"

3. **Vincoli tecnici**
   - "Che page builder/CMS usi? (Webflow, Framer, WordPress, Shopify, custom, etc.)"
   - "Ci sono sezioni obbligatorie richieste (legal, compliance, corporate policy)?"

4. **Timeline & Budget**
   - "Quando serve questa pagina live?"
   - "C'è budget per design/development esterno o fai tutto in-house?"

**Output Fase 5:** Assets Checklist + Constraints Summary

---

## Output Finale: Requirements Doc

Al termine del Grill Me, produci un documento strutturato:

```markdown
# Requirements Doc — [Nome Progetto]
**Data:** [data]
**Stakeholder:** [nome utente/cliente]

---

## 1. Business Context
- **Business model:** [SaaS, e-commerce, etc.]
- **Obiettivo primario:** [lead gen, trial, purchase, etc.]
- **KPI primario:** [conversion rate, cost per lead, etc.]
- **Stage:** [pre-PMF, scale, etc.]
- **Competitor:** [2-3 nomi]
- **Differenziazione:** [unique selling point]

---

## 2. Audience & Positioning
- **Audience primaria:** [ruolo, settore, pain principale]
- **Awareness level:** [unaware → most aware]
- **Job to be done:** [cosa l'utente cerca di fare]
- **Alternative attuali:** [cosa usa oggi]
- **Obiezioni top 3:**
  1. [Obiezione 1]
  2. [Obiezione 2]
  3. [Obiezione 3]

---

## 3. Offer & Conversion
- **Offerta:** [I give you X, you give me Y]
- **Prezzo/Commitment:** [free, trial, $X, etc.]
- **Urgency:** [deadline, scarcity, altro]
- **Post-conversion:** [cosa succede dopo: email, call, accesso, etc.]
- **Sales cycle:** [immediato, 1-2 call, lungo, enterprise]

---

## 4. Traffic Source & Message Match
- **Sorgente primaria:** [Google Ads, Meta, email, SEO, etc.]
- **Messaggio pre-click:** [headline annuncio, keyword, etc.]
- **Stato emotivo:** [curioso, frustrato, urgente, etc.]
- **Brand awareness:** [cold, warm, hot]

---

## 5. Assets & Constraints
### Social Proof Disponibile
- [ ] Testimonianze: [quante, con nome/ruolo?]
- [ ] Case study: [quanti, con risultati?]
- [ ] Numeri: [clienti, risultati, anni]
- [ ] Loghi clienti: [disponibili?]

### Visual Assets
- [ ] Screenshot prodotto: [sì/no]
- [ ] Video/demo: [sì/no]
- [ ] Brand kit: [sì/no, link se disponibile]

### Vincoli
- **Page builder:** [Webflow, Framer, etc.]
- **Sezioni obbligatorie:** [legal, compliance, etc.]
- **Timeline:** [deadline]
- **Budget:** [in-house, esterno, etc.]

---

## 6. Open Questions (se rimangono gap)
1. [Domanda ancora senza risposta]
2. [...]

---

## Next Steps
Basandomi su questi requirements, procedo con:
1. [Step 1: es. Brief CRO formale]
2. [Step 2: es. Architettura pagina]
3. [Step 3: es. Copy + wireframe]
```

**Checkpoint obbligatorio:**
Prima di procedere con qualsiasi output creativo, chiedi conferma esplicita:
```
"Requirements Doc completato. Prima di procedere, conferma:
1. Le informazioni raccolte rispecchiano il progetto?
2. Ci sono correzioni o aggiunte?
3. Posso procedere con [prossimo step]?"
```

---

## Regole del Grill Me

### ✅ Fare
- **Fai domande a batch**: max 3-4 domande per volta, poi aspetta risposte
- **Sii specifico**: no domande generiche tipo "parlami del tuo prodotto"
- **Chiedi esempi**: "Puoi darmi un esempio di cliente ideale?" è meglio di "Chi è il tuo target?"
- **Challenge vague answers**: Se l'utente dice "tutti", chiedi "Se dovessi scegliere UN segmento prioritario, quale sarebbe?"
- **Recap progressivo**: Dopo ogni fase, riassumi quanto raccolto per conferma

### ❌ Non Fare
- **Non fare tutte le domande in un colpo**: overwhelm garantito
- **Non accettare "non lo so"** come risposta finale: se non sanno, aiutali a inferire o fai domande alternative
- **Non saltare fasi**: anche se alcune info sembrano ovvie, verifica
- **Non procedere senza conferma finale**: il Requirements Doc deve essere approvato

---

## Varianti del Grill Me

### Grill Me Lite (per progetti semplici)
Se il progetto è relativamente semplice, usa versione ridotta con solo domande core:
1. Obiettivo di conversione
2. Audience primaria
3. Sorgente di traffico
4. Offerta
5. Obiezione principale

Tempo: 2-3 minuti invece di 5-10.

### Grill Me Deep (per progetti complessi/enterprise)
Aggiungi sezioni:
- **Stakeholder map**: Chi sono tutti i decisori coinvolti?
- **Compliance & Legal**: Requisiti GDPR, accessibility, settore-specific?
- **Localization**: Serve traduzione o adattamento multi-market?
- **Integration**: API, CRM, analytics da integrare?

---

## Edge Cases

### "Non so ancora" / "Devo decidere"
Se l'utente non ha risposta a domande critiche:
1. Offri opzioni basate su best practice: "Tipicamente in questo scenario, si fa X o Y. Quale ti sembra più adatto?"
2. Segna come "DA DECIDERE" nel Requirements Doc
3. Procedi con assunzioni esplicite dichiarate, da validare poi

### Stakeholder multipli con opinioni divergenti
Se emergono contraddizioni (es. marketing vuole X, sales vuole Y):
1. Segnala la divergenza esplicitamente
2. Chiedi priorità: "Se dovessimo scegliere una direzione, quale ha priorità?"
3. Documenta il trade-off nel Requirements Doc

### Utente vuole saltare il Grill Me
Se l'utente dice "Non ho tempo, inizia e vediamo":
1. Spiega il rischio: "Posso procedere con assunzioni, ma potrebbe richiedere rework se non allineate. Preferirei 5 minuti ora per evitare 1 ora di iterazioni dopo."
2. Se insiste, procedi con assunzioni dichiarate nel brief e marca TUTTE come "NON CONFERMATE — da validare"

---

## Integration nel Workflow

### Scenario A: Nuovo progetto, brief vago
1. **Grill Me** (questa skill) → Requirements Doc
2. Brief CRO (01_landing_brief.md) → usando info da Requirements Doc
3. Procedi con architettura, copy, design

### Scenario B: Brief parziale già fornito
1. Leggi brief esistente
2. Identifica gap (3+ informazioni mancanti)
3. **Grill Me parziale**: solo domande per gap bloccanti
4. Completa brief CRO
5. Procedi

### Scenario C: Progetto già avviato, ma stallo
1. **Grill Me** come "reset" → Re-align su requirements
2. Aggiorna brief CRO con nuove info
3. Pivot output se necessario

---

## Riferimenti

### Framework di Awareness (Eugene Schwartz)
1. **Unaware**: Non sa di avere il problema
2. **Problem Aware**: Sa di avere il problema, non sa che esistono soluzioni
3. **Solution Aware**: Sa che esistono soluzioni, non conosce la tua
4. **Product Aware**: Conosce il tuo prodotto, non è convinto a comprare
5. **Most Aware**: Pronto a comprare, serve solo il push finale

### Jobs to Be Done Framework
- **Job**: Cosa l'utente cerca di fare (progress, not product)
- **Hire**: Perché sceglie il tuo prodotto per fare quel job
- **Fire**: Cosa abbandona quando sceglie te (alternative)

---

## Changelog
- **2026-04-10**: Skill creata basata su best practice di requirements gathering
