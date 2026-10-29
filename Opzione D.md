## ♻️ Opzione D: Sismometro Standalone (Migrazione da progetto SeismoCloud)

Ideale se possiedi già un sismometro costruito per il progetto **SeismoCloud** (basato su ESP8266/NodeMCU + MPU6050) e vuoi riutilizzarlo su **DomHouse Sense** senza modificare i collegamenti.

1. **Verifica il cablaggio:** L'hardware utilizzato da SeismoCloud (ESP8266 + MPU6050 su bus I2C `SDA=D1` / `SCL=D2`) è già compatibile; non serve dissaldare o spostare i cavi (ignora eventuali LED o buzzer aggiuntivi se presenti).

2. Scarica il Firmware: ["DomHouse-Sense-HA.bin"](https://github.com/SalvatoreITA/DomHouse-Sense/releases/)

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

