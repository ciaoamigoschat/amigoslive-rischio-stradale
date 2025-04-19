# Relazione descrittiva

## Premessa

Durante il periodo di osservazione, sono stati raccolti e generati dati che hanno costituito un dataset di notevoli dimensioni. Il veicolo dotato di sistema di monitoraggio ha effettuato regolarmente tre registrazioni settimanali lungo il tragitto della tangenziale BreBeMi. 
Ogni sessione ha previsto la cattura dei dati GPS a intervalli di 30 secondi, garantendo così una mappatura ad alta frequenza del comportamento stradale e dell'ambiente circostante.


È stata sviluppata e installata un'applicazione mobile personalizzata, posizionata a bordo di un veicolo dedicato, in grado di:
- registrare in tempo reale i dati GPS del tragitto,
- osservare il comportamento degli automobilisti in prossimità di specifici segnali stradali,
- rilevare frenate, cambi corsia e infrazioni,
- mappare dinamicamente le condizioni del traffico urbano e autostradale.

L'obiettivo principale è quello di simulare scenari realistici di rischio stradale, con l'intento di produrre dati utili anche per applicazioni in ambito di:
- previsione del traffico urbano,
- analisi preventiva dei punti critici sulla rete stradale,
- studio comportamentale degli utenti della strada in relazione alla segnaletica esistente.

---

## Analisi simulata del rischio di incidenti stradali

**Autore**: Pippo Messina  
**Progetto**: Studio sul comportamento stradale in orari critici  
**Periodo di osservazione simulata**: Dicembre 2020 - oggi

---

## Obiettivo

Analizzare, tramite dati simulati, il comportamento dei veicoli e l'incidenza di eventi critici e incidenti stradali in tre momenti della settimana ritenuti strategici:
Le ore di punta del mattino nei giorni feriali (07:00–09:30)
La fascia pre-serale nei giorni feriali (18:00–20:00)
Il sabato sera in contesto urbano (22:00–01:00)
Lo scopo è comprendere come la densità del traffico e il comportamento dei conducenti influenzino il rischio stradale, per poi fornire raccomandazioni strategiche in ambito di sicurezza.
Analizzare, tramite dati simulati, il comportamento dei veicoli e l'incidenza di eventi critici e incidenti stradali in due momenti della settimana ritenuti strategici:
Le ore di punta del mattino nei giorni feriali (07:00–09:30)
Il sabato sera in contesto urbano (22:00–01:00)
Lo scopo è comprendere come la densità del traffico e il comportamento dei conducenti influenzino il rischio stradale, per poi fornire raccomandazioni strategiche in ambito di sicurezza.


---

## Metodo e strumenti

Per simulare le condizioni reali, è stato utilizzato un veicolo appositamente allestito con:
- **App mobile** per registrazione GPS e telemetria
- **Due iPhone posteriori + uno anteriore** per il riconoscimento visivo dei segnali stradali
- Analisi dei comportamenti alla guida (frenate, cambi corsia, stop ignorati)

Le simulazioni sono basate su:
- Dati in Real Time
- Osservazioni qualitative reali
- Generazione di scenari tramite modelli comportamentali e stime probabilistiche

---

## Sintesi dei dati simulati

| Indicatore                         | Mattino (feriale) | Sabato Sera |
|------------------------------------|-------------------|-------------|
| Veicoli in transito (media/h)      | 2.300             | 1.000       |
| Eventi critici/h                   | 85                | 67          |
| Incidenti lievi/ora                | 4,2               | 3,5         |
| Incidenti gravi/ora                | 0,6               | 1,1         |
| Frenate brusche (media/h)          | 160               | 92          |
| Violazioni segnali STOP/ora        | 8                 | 14          |
| Probabile guida distratta (%)      | 14%               | 37%         |
| Probabile guida alterata (%)       | 3%                | 26%         |

---

## Analisi

### Mattino feriale
- Alta densità veicolare, ma guidatori esperti
- Comportamenti aggressivi per fretta o ritardo
- Rischi legati alla distrazione (es. uso dello smartphone)
- Incidenti legati a traffico intenso e frenate improvvise

### Sabato sera
- Meno traffico ma utenti più disattenti o alterati
- Aumento delle infrazioni ai segnali
- Elevato tasso di guida sotto effetto di alcol
- Più incidenti gravi rispetto al mattino

---

## Conclusioni

Il valore di questa ricerca risiede nella capacità di unire tecnologie accessibili (smartphone, GPS, app personalizzate) con un approccio metodologico rigoroso per la raccolta e l'analisi di dati relativi alla sicurezza stradale. Il dataset generato costituisce una base concreta per:
- analisi predittive,
- simulazioni avanzate,
- addestramento di algoritmi di Intelligenza Artificiale dedicati alla mobilità.

Il sistema proposto si presta anche ad un utilizzo futuro in diversi contesti:
- **Prevenzione degli incidenti** in aree urbane tramite analisi predittiva dei comportamenti a rischio;
- **Ottimizzazione della segnaletica** sulla base dei punti in cui si riscontra maggiore disattenzione o infrazioni;
- **Supporto alle amministrazioni locali** per pianificare interventi mirati sulla viabilità;
- **Sviluppo di software per la guida assistita**, integrando i dati in ambienti di simulazione realistici;
- **Monitoraggio ambientale e traffico in tempo reale**, integrabile con smart city e sistemi IoT.


- Il mattino ha una maggiore incidenza numerica di incidenti, ma con minor gravità
- Il sabato sera mostra una frequenza inferiore ma un rischio qualitativo più alto
- Necessario distinguere tra "intensità" e "pericolosità" del traffico

---

## Raccomandazioni

1. Monitoraggio intelligente con dashcam e IA nei punti critici
2. Rafforzamento dei controlli serali del weekend
3. Campagne anti-distrazione nei giorni feriali e anti-alcolici nel weekend
4. Ottimizzazione della segnaletica e introduzione di alert visivi intelligenti

---

## Licenza

Questo progetto e i dati simulati sono distribuiti con licenza MIT. I dati non rappresentano eventi reali, ma scenari generati a scopo di ricerca e sviluppo.

> Progetto di Pippo Messina - HelpSoftware

