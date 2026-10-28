# 🌍 DomSense

**La rete civica collaborativa di monitoraggio sismico e ambientale.**

**DomSense** è un progetto di *citizen science* che trasforma piccoli ed economici microcontrollori domestici in una rete sismica ed ecologica distribuita (ispirata a progetti come *SeismoCloud*). Collegando un sensore da casa tua tramite una **chiave API personale**, contribuisci a rilevare le scosse sismiche e a condividere dati meteo-ambientali in tempo reale sulla mappa interattiva della community.

---

## ✨ Perché partecipare a DomSense?

Un singolo accelerometro economico in casa può rilevare una vibrazione se passa un camion pesante o se qualcuno sbatte una porta. **La vera forza di DomSense è l'unione dei sensori.**

* 🎯 **Zero falsi allarmi grazie alla Correlazione:** Quando il tuo sensore avverte una vibrazione anomala, la rete controlla istantaneamente i nodi vicini. Se più sensori nella stessa zona scattano contemporaneamente nel giro di pochi secondi, l'evento viene marcato come **Sisma Confermato** e segnalato sulla mappa pubblica con una stima dell'intensità Mercalli percepita.
* 🔒 **Privacy al primo posto:** Partecipare non significa mostrare a tutti dove abiti. Sulla mappa pubblica la posizione del tuo sensore viene **spostata casualmente** entro un raggio di sicurezza (circa 1,5 km). La posizione esatta non è mai visibile né ricalcolabile dall'esterno e viene usata unicamente dietro le quinte per verificare la distanza tra i sensori durante una scossa.
* 🌡️ **Non solo terremoti (Integrazione Home Assistant):** Oltre al sismometro, puoi arricchire la tua stazione condividendo dati ambientali locali (temperatura, umidità, pioggia, pressione) direttamente dalla tua istanza **Home Assistant**, trasformando il tuo nodo in una vera mini-stazione meteo sulla mappa.
* 🧠 **Algoritmo intelligente a bordo:** Il sensore non invia un flusso continuo di dati, ma analizza le vibrazioni in locale usando l'algoritmo sismologico **STA/LTA** (rapporto tra energia a breve e lungo termine) calcolato sul **PGA** (*Peak Ground Acceleration*), filtrando già alla radice la maggior parte dei disturbi domestici.

---

## 🛠️ Cosa ti serve per costruire il sensore

Realizzare un nodo sismico DomSense costa pochi euro e non richiede saldature complesse:

1. **Microcontrollore Wi-Fi:** Un comune **ESP8266** (es. NodeMCU, Wemos D1 Mini) oppure un **ESP32**.
2. **Accelerometro:** Modulo **MPU6050** (sensore giroscopio/accelerometro a 6 assi I2C).
3. **Alimentazione e cavi:** 4 cavetti jumper femmina-femmina e un alimentatore micro-USB / USB-C.

### Cablaggio (ESP8266 / NodeMCU ↔ MPU6050)

| Pin MPU6050 | Pin NodeMCU (ESP8266) | Funzione |
| :--- | :--- | :--- |
| **VCC** | `3V3` | Alimentazione 3.3V |
| **GND** | `GND` | Massa |
| **SDA** | `D1` (GPIO5) | Dati I2C |
| **SCL** | `D2` (GPIO4) | Clock I2C |

> 💡 **Consiglio di posizionamento:** Fissa il sensore in modo solidale a una parete portante, al pavimento o in un angolo basso della casa (lontano da lavatrici, porte che sbattono o termosifoni). **All'accensione, tieni il sensore completamente fermo per i primi 10 secondi** per permettere la calibrazione automatica degli assi.

---

## 🚀 Come collegarsi alla rete (3 modalità)

Prima di iniziare, richiedi la tua **Chiave API (`api_key`)** per abilitare la tua stazione. Puoi poi scegliere il metodo di installazione che preferisci:

### Opzione 1: Firmware pronto all'uso (Consigliato e Veloce)
Se non usi ESPHome o vuoi un'installazione immediata senza scrivere codice:
1. Scarica il file binario `.bin` precompilato dalla cartella `firmware/` e caricalo sull'ESP tramite cavo USB (usando ad esempio [ESPHome Web](https://web.esphome.io/)).
2. Collega il dispositivo al tuo Wi-Fi.
3. Apri nel browser l'indirizzo IP locale del sensore: troverai una comoda **pagina web di configurazione** dove incollare la tua **Chiave API**, il **nome della stazione** e le tue **coordinate (`lat` / `lon`)**.

### Opzione 2: Configurazione tramite ESPHome (YAML)
Se gestisci già i tuoi dispositivi con ESPHome, usa il file `esphome/sismometro-rete.yaml` e personalizza solo il blocco iniziale `substitutions`:

```yaml
substitutions:
  node_name: "Sismometro di Mario"
  server_url: "https://URL_DELLA_RETE"
  api_key: "<la_tua_chiave_api>"
  lat: "41.90"
  lon: "12.49"
```

Assicurati di avere nel tuo `secrets.yaml` le credenziali `wifi_ssid`, `wifi_password`, `api_encryption_key` e `ota_password`, quindi compila e installa con:
```bash
esphome run sismometro-rete.yaml
```

### Opzione 3: Nodo nativo Home Assistant + Dati Meteo
Vuoi avere tutti i grafici e i sensori del sismometro dentro la tua **Home Assistant** e condividere sulla mappa anche temperatura, umidità o pioggia dei tuoi sensori domestici?
1. Flasha sul microcontrollore il firmware `esphome/domsense-ha.yaml` (espone i sensori direttamente alla tua Home Assistant locale, senza richiedere chiavi sul chip).
2. Installa sulla tua Home Assistant il componente **DomSense** (disponibile in `ha-integration/`, installabile comodamente via **HACS** e configurabile da interfaccia grafica, oppure tramite il pacchetto YAML in `homeassistant/`).
3. Inserisci la tua Chiave API nell'integrazione e seleziona quali entità sismiche e meteo inviare alla mappa!

---

## ℹ️ Note sul rilevamento sismico

* Il sensore misura il **PGA** (*Peak Ground Acceleration*, accelerazione di picco in $g$) tramite un accelerometro consumer MEMS e permette di stimare l'**intensità Mercalli** percepita sul posto.
* **Non** si tratta di una misura di magnitudo Richter né di uno strumento sismologico professionale certificato: lo scopo del progetto è il monitoraggio civico collaborativo e il confronto relativo dell'intensità percepita tra diverse zone.
