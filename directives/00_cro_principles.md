# 00_cro_principles.md — Principi CRO Non Negoziabili

Questo documento definisce gli standard operativi per ogni landing page o sito prodotto.
Non sono best practice generiche: sono regole CRO collaudate su campagne paid, siti
e-commerce e funnel di conversione. Ogni output viene valutato contro questi principi
prima di essere consegnato.

---

## 1. Above the Fold

La sezione above the fold è l'unica che quasi tutti vedono. Deve rispondere a tre
domande in meno di 5 secondi:

- **Cosa sei?** Proposta di valore chiara. Nessun claim astratto, nessun gioco di parole.
- **Per chi?** Audience esplicita o implicita. Il visitatore deve riconoscersi.
- **Cosa faccio adesso?** Un solo CTA primario, visibile senza scroll.

**Struttura minima above the fold:**
```
[Headline] — benefit principale, specifico, misurabile se possibile
[Subheadline] — espande o qualifica l'headline, max 2 righe
[CTA primario] — azione, non generico
[Trust anchor] — 1 elemento di credibilità (logo, numero, badge)
[Visual] — supporta il messaggio, non decorativo
```

**Regola del 5 secondi:** mostra l'above the fold a qualcuno che non conosce il prodotto.
Se dopo 5 secondi non sa cosa fa e per chi è, riscrivilo.

---

## 2. Message Match

La pagina deve riflettere esattamente il messaggio dell'annuncio o del link che ha
portato il visitatore lì. Il mismatch tra annuncio e landing è la causa principale
di rimbalzo immediato nel traffico paid.

**Regole operative:**
- Se l'annuncio parla di "risparmio del 30%", la headline della landing parla di
  risparmio del 30%. Non di "efficienza" o "ottimizzazione".
- Se la sorgente è branded (utente che cerca il nome del brand), la landing può
  essere più istituzionale.
- Se la sorgente è non-branded o cold (Meta, display, referral), la landing deve
  partire dal problema, non dal prodotto.

**Per ogni progetto, documenta:**
- Sorgente di traffico principale
- Messaggio dell'annuncio o del link di ingresso
- Keyword o interest targeting se rilevante

---

## 3. Gerarchia delle Sezioni

L'ordine delle sezioni non è neutro. Segue la logica cognitiva di un visitatore
scettico che non ti conosce.

**Ordine raccomandato per landing page a risposta diretta:**
1. Above the fold (problema + soluzione + CTA)
2. Proof point rapido (numeri, loghi, social proof brevissimo)
3. Come funziona / Cosa ottieni (benefici, non feature)
4. Prova sociale approfondita (case study, testimonianze con contesto)
5. Gestione obiezioni (FAQ, garanzie, confronto)
6. CTA finale (ripete l'offerta con urgenza o incentivo se presente)

**Regola:** ogni sezione deve avere un'unica funzione. Se una sezione fa due cose,
spezzala o elimina quella secondaria.

---

## 4. CTA — Regole Operative

**Copy del bottone:**
- Usa verbi d'azione specifici: "Richiedi", "Inizia", "Scarica", "Prenota"
- Specifica cosa succede dopo: "Inizia la prova gratuita", "Prenota una call di 30 min"
- Evita: "Scopri di più", "Invia", "Clicca qui", "Contattaci"

**Posizionamento:**
- CTA primario visible above the fold sempre
- Ripeti il CTA ogni 2-3 sezioni di scroll (non ogni sezione)
- CTA finale dopo la gestione obiezioni, mai prima

**Gerarchia:**
- Un solo CTA primario per pagina (stessa azione, stesso copy o minime variazioni)
- Il CTA secondario (es. "Guarda il video") deve essere visivamente subordinato:
  link testuale o bottone outline, mai stesso peso visivo del primario

**Micro-copy sotto il bottone:**
- Rimuovi friction esplicita: "Nessuna carta di credito", "Cancelli quando vuoi",
  "Risposta entro 24h"
- Max 1 riga, testo piccolo, tono factual non promozionale

---

## 5. Social Proof — Standard Minimi

La social proof generica non funziona. "Migliaia di clienti soddisfatti" è invisibile.

**Testimonianze:**
- Includono: nome, ruolo, azienda (o contesto riconoscibile), foto se disponibile
- Citano un risultato specifico o un problema risolto, non solo opinioni positive
- Sono posizionate vicino al CTA o subito dopo una claim forte

**Numeri:**
- Solo numeri verificabili e significativi per l'audience target
- Preferisci numeri relativi a outcome ("riduzione del 40% del CPL") su numeri
  di vanità ("10.000 utenti registrati")
- Marca `[DATO DA VERIFICARE]` se il numero non è confermato dalla fonte

**Loghi clienti:**
- Usa loghi solo se riconoscibili dall'audience target
- Se i clienti non sono noti, sostituisci con categorie ("50+ PMI manifatturiere
  nel nord Italia") o elimina la sezione

---

## 6. Leggibilità e UX Testuale

**Lunghezza dei paragrafi:**
- Max 3-4 righe per blocco di testo nelle sezioni body
- Headline: max 10 parole
- Subheadline: max 20 parole
- Bullet points: max 6 per lista, ognuno max 1 riga

**Lingua:**
- Scrivi come parla l'audience, non come parla il brand
- Evita gergo tecnico a meno che l'audience sia tecnica
- Testa ogni frase: "lo direbbe un essere umano reale?"

**Scannabilità:**
- Il visitatore medio scanna prima di leggere. L'ordine visivo deve comunicare
  il messaggio anche senza leggere il corpo del testo.
- Headline + subheadline + bullet + CTA devono raccontare la storia completa
  anche se il visitatore ignora tutto il resto

---

## 7. Gestione delle Obiezioni

Ogni audience ha obiezioni prevedibili. Vanno identificate nel brief e affrontate
esplicitamente nella pagina, non ignorate o aggirate.

**Categorie standard di obiezioni:**
- **Prezzo**: "È troppo caro" → ROI, confronto costo/beneficio, garanzia
- **Rilevanza**: "Non fa per me" → use case specifici, segmentazione esplicita
- **Complessità**: "È difficile da usare / implementare" → processo chiaro, onboarding
- **Rischio**: "E se non funziona?" → garanzie, trial, case study con risultati
- **Urgenza**: "Ci penso dopo" → incentivo temporale, conseguenza del non agire

**Regola:** non affrontare più di 4-5 obiezioni. Sceglie le più critiche per
quell'audience specifica, non tutte quelle possibili.

---

## 8. Mobile First

Ogni struttura di pagina viene progettata prima per mobile, poi adattata per desktop.

**Checklist mobile:**
- CTA visibile above the fold anche su schermo da 375px
- Nessun testo inferiore a 16px
- Form con max 3 campi visibili (gli altri opzionali o in step successivo)
- Nessun elemento interattivo con tap target inferiore a 44x44px
- Immagini hero ottimizzate: nessun testo embedded nelle immagini

---

## 9. Friction — Cosa Elimina Conversioni

**Friction da eliminare sistematicamente:**
- Form con più di 3 campi obbligatori in fase top-of-funnel
- Navigazione completa su landing page da traffico paid (rimuovere header nav)
- Link esterni o interni che portano via dalla pagina prima del CTA
- Video autoplay con audio
- Pop-up immediati (entro 3 secondi dall'arrivo)
- CAPTCHA visibili (usa honeypot o soluzioni invisibili)
- "Clicca qui per saperne di più" che porta a un'altra pagina invece di espandere
  il contenuto in-page

---

## 10. Strutture per Tipo di Pagina

### Landing page da traffico paid (Google/Meta)
- Rimuovi header navigation
- Single CTA, nessuna distrazione
- Message match con l'annuncio
- Lunghezza: dipende dal commitment richiesto. Lead gen semplice = pagina corta.
  Vendita o demo = pagina lunga con gestione obiezioni completa.

### Homepage
- Deve servire audience multiple (cold, warm, branded)
- Navigation completa necessaria
- CTA primario per il segmento principale, path secondari per gli altri
- Non ottimizzare per una sola azione come una landing page

### Pagina prodotto / feature
- Collega ogni feature a un beneficio esplicito
- Use case concreti con contesto (chi, quando, perché)
- CTA verso trial, demo o acquisto, non verso "scopri di più"

### Pricing page
- Massimo 3-4 piani (oltre diventa paralisi della scelta)
- Piano raccomandato evidenziato visivamente
- Risponde esplicitamente a "quale piano fa per me?"
- FAQ sotto la tabella prezzi per gestire obiezioni standard

---

## Riferimento Rapido — Errori Più Comuni

| Errore | Conseguenza | Fix |
|--------|-------------|-----|
| Headline astratta | Nessuno capisce il prodotto | Benefit specifico + audience |
| CTA generico ("Invia") | Basso click-through | Verbo d'azione + esito |
| Nessun trust anchor above the fold | Alta bounce rate | Logo, numero, badge |
| Mismatch annuncio-landing | CPL alto, ROAS basso | Allinea headline e offerta |
| Troppi CTA | Paralisi della scelta | Un solo primario per pagina |
| Obiezioni ignorate | Abbandono silenzioso | FAQ o sezione dedicata |
| Form con 6+ campi | Drop-off nel form | Max 3 obbligatori in fase 1 |
| Nav completa su landing paid | Fuga dalla pagina | Rimuovi o semplifica header |
