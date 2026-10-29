# 🌍 DomSense

**La rete collaborativa e amatoriale di monitoraggio sismico e meteo-ambientale per la community e per Home Assistant.**

**DomSense** è un progetto hobbistico e sperimentale che unisce appassionati di domotica e vicini di casa in una rete civica distribuita. Attraverso una **chiave API personale**, puoi partecipare in due modi (o entrambi!):

1. **Monitoraggio Sismico Amatoriale:** Costruendo un piccolo ed economico sismometro domestico (ispirato a progetti come *SeismoCloud*) per rilevare le vibrazioni in tempo reale a scopo didattico e sperimentale.

2. **Rete Meteo Condivisa:** Condividendo i sensori di temperatura o della tua stazione meteo già presenti sul tuo **Home Assistant** (anche senza avere il sismometro!) e **sfruttando i dati condivisi dai tuoi vicini** direttamente dentro il tuo Home Assistant.

## ✨ Perché partecipare a DomSense?

* 🌡️ **Condividi e sfrutta il meteo dei vicini su Home Assistant (Anche senza sismometro!):** Non vuoi costruire il sensore sismico? Nessun problema! Puoi unirti alla rete usando solo l'add-on per **Home Assistant** per condividere temperatura esterna, umidità, pioggia, vento o pressione della tua stazione meteo. A tua volta, potrai **importare sul tuo Home Assistant i dati meteo delle stazioni vicine** (utilissimo se non hai un pluviometro o un sensore esterno ben esposto e vuoi creare automazioni per tende da sole, irrigazione o riscaldamento basate sul meteo del tuo quartiere!).

* 🎯 **Filtro dei falsi allarmi grazie alla Correlazione:** Un singolo accelerometro in casa può vibrare se passa un camion o sbatte una porta. Quando il tuo sensore avverte una vibrazione anomala, DomSense controlla istantaneamente i nodi vicini: se più sensori nella stessa zona scattano contemporaneamente nel giro di pochi secondi, l'evento viene marcato come **Anomalia Correlata / Confermata** e segnalato sulla mappa pubblica con una stima indicativa dell'intensità percepita.

* 🔒 **Doppio livello di Privacy (Nessun indirizzo di casa richiesto):** Partecipare non significa mostrare a tutti dove abiti. Quando configuri il nodo ti chiediamo di **non inserire le coordinate esatte della tua abitazione**, ma quelle di un punto pubblico nelle vicinanze (es. una piazza, un parco o un incrocio a 200-300 metri da casa). Inoltre, sulla mappa pubblica il sistema applica automaticamente un ulteriore **spostamento casuale** entro un raggio di sicurezza (circa 1,5 km).

* 🧠 **Algoritmo intelligente a bordo:** Il firmware del sismometro analizza le vibrazioni in locale usando l'algoritmo **STA/LTA** (rapporto tra energia a breve e lungo termine) calcolato sul **PGA** (*Peak Ground Acceleration*), filtrando già alla radice la maggior parte dei disturbi domestici.

## 🚀 Come partecipare alla rete (Scegli la tua modalità)

Prima di iniziare, richiedi la tua **Chiave API (`api_key`)** personale accettando i termini d'uso del progetto.

> 📍 **Regola d'oro per le coordinate (`lat` / `lon`):** Per la tua tutela e per non inviare dati personali sensibili, **NON inserire mai le coordinate esatte di casa tua**. Apri una mappa e scegli le coordinate di una piazza pubblica, una chiesa, una scuola o un incrocio a 200-500 metri da te. La precisione per il meteo di quartiere e per il calcolo di correlazione tra sensori sarà identica, ma il tuo indirizzo reale resterà completamente privato!

Puoi unirti a DomSense scegliendo una delle seguenti configurazioni (clicca per andare direttamente alla guida):

- [🌤️ Opzione A: Solo Meteo & Sensori con Home Assistant (Zero Hardware da costruire)](#️-opzione-a-solo-meteo--sensori-con-home-assistant-zero-hardware-da-costruire)
- [🌋 Opzione B: Sismometro + Home Assistant (Consigliata per utenti HA)](#-opzione-b-sismometro--home-assistant-consigliata-per-utenti-ha)
- [📡 Opzione C: Sismometro Standalone (Senza Home Assistant)](#-opzione-c-sismometro-standalone-senza-home-assistant)
- [📡 Opzione D: Sismometro Standalone (Migrazione da progetto SeismoCloud)](#-opzione-d-sismometro-standalone-migrazione-da-progetto-seismocloud)

---

### 🌤️ Opzione A: Solo Meteo & Sensori con Home Assistant (Zero Hardware da costruire)

Ideale se non vuoi assemblare il sismometro ma hai già dei sensori ambientali o una stazione meteo su **Home Assistant** e vuoi scambiarne i dati con gli altri utenti e vicini.

1. Installa l'add-on / integrazione **DomSense** sul tuo Home Assistant.

2. Inserisci la tua **Chiave API** e le coordinate approssimative del tuo quartiere (vedi nota sopra).

3. Seleziona quali entità meteo condividere sulla mappa (es. temperatura, umidità, pioggia) e importa sul tuo Home Assistant i dati delle stazioni DomSense vicine a te per usarli nelle tue dashboard e automazioni!

### 🌋 Opzione B: Sismometro + Home Assistant (Consigliata per utenti HA)

Ideale se usi **Home Assistant** e vuoi sia costruire il sismometro, sia condividere/ricevere i dati meteo della community.

1. Costruisci il sensore seguendo lo [schema qui sotto](#️-come-costruire-il-sismometro-per-le-opzioni-b-c-e-d) e flasha sul microcontrollore il file `.bin` precompilato della versione **Home Assistant** (usando ad esempio il browser con [ESPHome Web](https://web.esphome.io/)).

2. Collegalo al Wi-Fi: verrà rilevato automaticamente dalla tua istanza Home Assistant.

3. Tramite l'add-on **DomSense** su Home Assistant, inserisci la tua **Chiave API** e invia alla rete sia gli eventi del sismometro sia i tuoi sensori meteo.

### 📡 Opzione C: Sismometro Standalone (Senza Home Assistant)

Ideale se non usi Home Assistant e vuoi semplicemente un sismometro autonomo che invia i dati direttamente alla mappa della rete.

1. Costruisci il sensore e flasha sul dispositivo il file `.bin` precompilato della versione **Standalone** (ha già l'indirizzo del server configurato al suo interno).

2. Collega il sensore alla tua rete Wi-Fi.

3. Apri nel browser l'indirizzo IP locale del sensore: si aprirà una comoda **pagina web di configurazione** dove potrai inserire la tua **Chiave API**, un **nome generico della stazione** (es. *"Nodo Roma Nord"*, evitando nomi e cognomi reali) e le **coordinate di un punto pubblico vicino a te (`lat` / `lon`)**.

### 📡 Opzione D: Sismometro Standalone (Migrazione da progetto SeismoCloud)

Ideale se possiedi già un sismometro costruito per il progetto **SeismoCloud** (basato su ESP8266/NodeMCU + MPU6050) e vuoi riutilizzarlo su **DomSense** senza modificare i collegamenti.

1. **Verifica il cablaggio:** L'hardware utilizzato da SeismoCloud (ESP8266 + MPU6050 su bus I2C `SDA=D1` / `SCL=D2`) è già compatibile; non serve dissaldare o spostare i cavi (ignora eventuali LED o buzzer aggiuntivi se presenti).

2. **Flash del nuovo firmware:** Collega il dispositivo via USB al PC e flasha il file `.bin` precompilato di DomSense (versione **Standalone** oppure versione **Home Assistant** se preferisci integrarlo in HA) tramite [ESPHome Web](https://web.esphome.io/).

3. **Configurazione:** Collega il sensore al Wi-Fi, apri il suo indirizzo IP nel browser e inserisci la tua **Chiave API**, il nome generico del nodo e le coordinate di un punto pubblico vicino a te (`lat` / `lon`).

## 🛠️ Come costruire il Sismometro (Per le Opzioni B, C e D)

Se decidi di aggiungere anche il rilevamento sismico, ti bastano pochi euro di componenti e nessuna saldatura complessa:

1. **Microcontrollore Wi-Fi:** Un comune **ESP8266** (es. NodeMCU, Wemos D1 Mini) oppure un **ESP32**.

2. **Accelerometro:** Modulo **MPU6050** (sensore giroscopio/accelerometro a 6 assi I2C).

3. **Alimentazione e cavi:** 4 cavetti jumper femmina-femmina e un alimentatore micro-USB / USB-C.

### Cablaggio (ESP8266 / NodeMCU ↔ MPU6050)

| Pin MPU6050 | Pin NodeMCU (ESP8266) | Funzione | 
| ----- | ----- | ----- | 
| **VCC** | `3V3` | Alimentazione 3.3V | 
| **GND** | `GND` | Massa | 
| **SDA** | `D1` (GPIO5) | Dati I2C | 
| **SCL** | `D2` (GPIO4) | Clock I2C | 

> 💡 **Consiglio di posizionamento:** Fissa il sensore in modo solidale a una parete portante, al pavimento o in un angolo basso della casa (lontano da lavatrici, porte che sbattono o termosifoni). **All'accensione, tieni il sensore completamente fermo per i primi 10 secondi** per permettere la calibrazione automatica degli assi.

## 🔍 Trasparenza e Codice Sorgente

Per i sismometri **non devi compilare alcun codice**: forniamo direttamente i due file `.bin` pronti all'uso (versione *Standalone* e versione *Home Assistant*).

Per garantire la massima trasparenza sul funzionamento dell'algoritmo **STA/LTA** e sulla gestione dei dati, in questo repository trovi comunque pubblicati i **codici sorgente YAML** completi di entrambi i firmware.

> **Nota di sicurezza:** Nei codici sorgente pubblici l'indirizzo del server centrale è stato omesso. Per collegarti effettivamente alla rete, utilizza i file `.bin` ufficiali precompilati o l'add-on Home Assistant insieme alla tua chiave API.

## ⚠️ Disclaimer Importante ed Esclusione di Responsabilità

**DomSense è un progetto puramente hobbistico, amatoriale, didattico e sperimentale, gestito senza scopo di lucro.** Chiunque decida di scaricare i firmware, installare l'add-on, assemblare l'hardware, consultare la mappa o utilizzare i dati forniti dalla rete accetta integralmente le seguenti condizioni:

1. **NON è un sistema di allerta precoce o salvavita (No Early Warning / No Safety-Critical):**

   * Il sistema utilizza componenti elettronici consumer a basso costo (accelerometri MEMS come l'MPU6050) e connessioni internet domestiche. **Non è uno strumento sismologico certificato**, non misura la magnitudo Richter e le stime di PGA (in $g$) o intensità Mercalli hanno valore puramente indicativo e ludico-sperimentale.

   * **Non utilizzare mai DomSense come mezzo empirico di sicurezza, allarme o protezione personale/strutturale in caso di terremoto o calamità naturali.** Il sistema può generare falsi positivi o, al contrario, **non rilevare affatto** un evento sismico reale a causa di limiti hardware, bug software, assenza di corrente elettrica, ritardi di rete o indisponibilità del server.

   * Per informazioni ufficiali, allerte e direttive di sicurezza, fare **esclusivamente** riferimento agli enti preposti (es. **INGV** - Istituto Nazionale di Geofisica e Vulcanologia e **Protezione Civile**).

2. **Nessuna responsabilità per Automazioni Domotiche e Dati Meteo/Sismici:**

   * I dati meteorologici, ambientali e sismici condivisi dagli utenti non sono verificati né garantiti.

   * Gli autori e i gestori del progetto **declinano ogni responsabilità** per eventuali danni materiali, malfunzionamenti o disagi derivanti da automazioni su Home Assistant basate sui dati di DomSense (es. mancata chiusura di tende da sole con vento forte, allagamenti dovuti a irrigazione errata, sgancio intempestivo o mancato sgancio di forniture di gas/corrente/acqua o apertura di varchi/cancelli in seguito a falsi positivi o mancati rilevamenti). Si sconsiglia vivamente di collegare azioni critiche o potenzialmente pericolose ai dati della rete.

3. **Sicurezza Hardware ed Elettrica (Fai-da-te):**

   * La realizzazione e il cablaggio del sensore avvengono a totale rischio e pericolo dell'utente. Gli autori non rispondono di cortocircuiti, danni a schede elettroniche, alimentatori, impianti domestici o danni a cose e persone derivanti dall'assemblaggio o dall'uso continuativo dei dispositivi.

4. **Privacy, Coordinate e Dati Condivisi:**

   * Agli utenti è espressamente richiesto di **non inserire dati personali identificativi** (come nome e cognome nel nome del nodo) né le coordinate esatte della propria abitazione privata, utilizzando esclusivamente coordinate approssimative riferite a luoghi pubblici del proprio quartiere.

   * I dati inviati dai nodi (letture ambientali, picchi di accelerazione e coordinate approssimative) vengono elaborati al solo scopo tecnico di calcolare la correlazione tra stazioni e popolare la mappa condivisa (con ulteriore offuscamento di sicurezza). L'utente può interrompere l'invio dei dati e richiedere la revoca della propria chiave API e la rimozione del nodo in qualsiasi momento.

5. **Fornitura "AS IS" (Così com'è) e Continuità del Servizio:**

   * Tutto il software, i firmware precompilati (`.bin`), gli add-on e l'infrastruttura sono forniti *"AS IS"* (così come sono), sotto licenza Open Source (vedi file `LICENSE`), senza alcuna garanzia esplicita o implicita di funzionamento, accuratezza o sicurezza informatica. Il servizio può subire interruzioni, perdite di dati o essere modificato/sospeso in qualsiasi momento senza preavviso.