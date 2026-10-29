# 🌍 DomHouse-Sense

**La rete collaborativa di monitoraggio sismico e meteo-ambientale per la community e per Home Assistant.**

**DomHouse Sense** è un progetto condiviso che unisce appassionati e vicini di casa in una rete civica distribuita. Attraverso una **chiave API personale**, puoi partecipare in due modi (o entrambi!):
1. **Monitoraggio Sismico:** Costruendo un piccolo ed economico sismometro domestico (ispirato a progetti come *SeismoCloud*) per rilevare le scosse in tempo reale.
2. **Rete Meteo Condivisa:** Condividendo i sensori di temperatura o della tua stazione meteo già presenti sul tuo **Home Assistant** (anche senza avere il sismometro!) e **sfruttando i dati condivisi dai tuoi vicini** direttamente dentro il tuo Home Assistant.

## ✨ Perché partecipare a DomHouse Sense?

* 🌡️ **Condividi e sfrutta il meteo dei vicini su Home Assistant (Anche senza sismometro!):** Non vuoi costruire il sensore sismico? Nessun problema! Puoi unirti alla rete usando solo l'add-on per **Home Assistant** per condividere temperatura esterna, umidità, pioggia, vento o pressione della tua stazione meteo. A tua volta, potrai **importare sul tuo Home Assistant i dati meteo delle stazioni vicine** (utilissimo se non hai un pluviometro o un sensore esterno ben esposto e vuoi creare automazioni per tende da sole, irrigazione o riscaldamento basate sul meteo reale del tuo quartiere!).
* 🎯 **Zero falsi allarmi sismici grazie alla Correlazione:** Un singolo accelerometro in casa può vibrare se passa un camion o sbatte una porta. Quando il tuo sensore avverte una vibrazione anomala, DomHouse Sense controlla istantaneamente i nodi vicini: se più sensori nella stessa zona scattano contemporaneamente nel giro di pochi secondi, l'evento viene marcato come **Sisma Confermato** e segnalato sulla mappa pubblica con una stima dell'intensità Mercalli percepita.
* 🔒 **Doppio livello di Privacy (Nessun indirizzo di casa richiesto):** Partecipare non significa mostrare a tutti dove abiti. Quando configuri il nodo ti chiediamo di **non inserire le coordinate esatte della tua abitazione**, ma quelle di un punto pubblico nelle vicinanze (es. una piazza, un parco o un incrocio a 200-300 metri da casa). Inoltre, sulla mappa pubblica il sistema applica automaticamente un ulteriore **spostamento casuale** entro un raggio di sicurezza (circa 1,5 km).
* 🧠 **Algoritmo sismico intelligente a bordo:** Il firmware del sismometro analizza le vibrazioni in locale usando l'algoritmo sismologico **STA/LTA** (rapporto tra energia a breve e lungo termine) calcolato sul **PGA** (*Peak Ground Acceleration*), filtrando già alla radice la maggior parte dei disturbi domestici.

## 🚀 Come partecipare alla rete (Scegli la tua modalità)

Prima di iniziare, richiedi la tua **Chiave API (`api_key`)** personale accettando i termini d'uso del progetto.

> 📍 **Regola d'oro per le coordinate (`lat` / `lon`):** Per la tua tutela e per non inviare dati personali sensibili, **NON inserire mai le coordinate esatte di casa tua**. Apri una mappa e scegli le coordinate di una piazza pubblica, una chiesa, una scuola o un incrocio a 200-500 metri da te. La precisione per il meteo di quartiere e per il calcolo di correlazione tra sensori sarà identica, ma il tuo indirizzo reale resterà completamente privato!

### Puoi unirti a DomHouse Sense scegliendo una delle seguenti configurazioni:

* 🛠️ Come costruire il Sismometro (Per le Opzioni B e C)

* 🌤️ Opzione A: Solo Meteo & Sensori con Home Assistant (Zero Hardware da costruire)

* 🌋 Opzione B: Sismometro + Home Assistant (Consigliata per utenti HA)

* 📡 Opzione C: Sismometro Standalone (Senza Home Assistant)

* ♻️ Opzione D: Sismometro Standalone (Migrazione da progetto SeismoCloud)


## 🔍 Trasparenza e Codice Sorgente

Per i sismometri **non devi compilare alcun codice**: forniamo direttamente i `.bin` pronti all'uso.

Per garantire la massima trasparenza sul funzionamento dell'algoritmo **STA/LTA** e sulla gestione dei dati, in questo repository trovi comunque pubblicati i **codici sorgente YAML** completi di entrambi i firmware.

> **Nota di sicurezza:** Nei codici sorgente pubblici l'indirizzo del server centrale è stato omesso. Per collegarti effettivamente alla rete, utilizza i file `.bin` ufficiali precompilati o l'add-on Home Assistant insieme alla tua chiave API.

## ℹ️ Note sul rilevamento sismico

* Il sensore misura il **PGA** (*Peak Ground Acceleration*, accelerazione di picco in $g$) tramite un accelerometro consumer MEMS e permette di stimare l'**intensità Mercalli** percepita sul posto.
* **Non** si tratta di una misura di magnitudo Richter né di uno strumento sismologico professionale certificato: lo scopo del progetto è il monitoraggio civico collaborativo e il confronto relativo dell'intensità percepita tra diverse zone.

## ⚠️ Disclaimer Importante ed Esclusione di Responsabilità

**DomHouse Sense è un progetto puramente hobbistico, amatoriale, didattico e sperimentale, gestito senza scopo di lucro.** Chiunque decida di scaricare i firmware, installare l'add-on, assemblare l'hardware, consultare la mappa o utilizzare i dati forniti dalla rete accetta integralmente le seguenti condizioni:

1. **NON è un sistema di allerta precoce o salvavita (No Early Warning / No Safety-Critical):**

   * Il sistema utilizza componenti elettronici consumer a basso costo (accelerometri MEMS come l'MPU6050) e connessioni internet domestiche. **Non è uno strumento sismologico certificato**, non misura la magnitudo Richter e le stime di PGA (in $g$) o intensità Mercalli hanno valore puramente indicativo e ludico-sperimentale.

   * **Non utilizzare mai DomHouse Sense come mezzo empirico di sicurezza, allarme o protezione personale/strutturale in caso di terremoto o calamità naturali.** Il sistema può generare falsi positivi o, al contrario, **non rilevare affatto** un evento sismico reale a causa di limiti hardware, bug software, assenza di corrente elettrica, ritardi di rete o indisponibilità del server.

   * Per informazioni ufficiali, allerte e direttive di sicurezza, fare **esclusivamente** riferimento agli enti preposti (es. **INGV** - Istituto Nazionale di Geofisica e Vulcanologia e **Protezione Civile**).

2. **Nessuna responsabilità per Automazioni Domotiche e Dati Meteo/Sismici:**

   * I dati meteorologici, ambientali e sismici condivisi dagli utenti non sono verificati né garantiti.

   * Gli autori e i gestori del progetto **declinano ogni responsabilità** per eventuali danni materiali, malfunzionamenti o disagi derivanti da automazioni su Home Assistant basate sui dati di DomHouse Sense (es. mancata chiusura di tende da sole con vento forte, allagamenti dovuti a irrigazione errata, sgancio intempestivo o mancato sgancio di forniture di gas/corrente/acqua o apertura di varchi/cancelli in seguito a falsi positivi o mancati rilevamenti). Si sconsiglia vivamente di collegare azioni critiche o potenzialmente pericolose ai dati della rete.

3. **Sicurezza Hardware ed Elettrica (Fai-da-te):**

   * La realizzazione e il cablaggio del sensore avvengono a totale rischio e pericolo dell'utente. Gli autori non rispondono di cortocircuiti, danni a schede elettroniche, alimentatori, impianti domestici o danni a cose e persone derivanti dall'assemblaggio o dall'uso continuativo dei dispositivi.

4. **Privacy, Coordinate e Dati Condivisi:**

   * Agli utenti è espressamente richiesto di **non inserire dati personali identificativi** (come nome e cognome nel nome del nodo) né le coordinate esatte della propria abitazione privata, utilizzando esclusivamente coordinate approssimative riferite a luoghi pubblici del proprio quartiere.

   * I dati inviati dai nodi (letture ambientali, picchi di accelerazione e coordinate approssimative) vengono elaborati al solo scopo tecnico di calcolare la correlazione tra stazioni e popolare la mappa condivisa (con ulteriore offuscamento di sicurezza). L'utente può interrompere l'invio dei dati e richiedere la revoca della propria chiave API e la rimozione del nodo in qualsiasi momento.

5. **Fornitura "AS IS" (Così com'è) e Continuità del Servizio:**

   * Tutto il software, i firmware precompilati (`.bin`), gli add-on e l'infrastruttura sono forniti *"AS IS"* (così come sono), sotto licenza Open Source (vedi file `LICENSE`), senza alcuna garanzia esplicita o implicita di funzionamento, accuratezza o sicurezza informatica. Il servizio può subire interruzioni, perdite di dati o essere modificato/sospeso in qualsiasi momento senza preavviso.
