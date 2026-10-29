## ♻️ Opzione D: Sismometro Standalone (Migrazione da progetto SeismoCloud)

Ideale se possiedi già un sismometro costruito per il progetto **[Seismo Cloud](https://www.seismocloud.com/it/)** (basato su ESP8266/NodeMCU + MPU6050) e vuoi riutilizzarlo su **DomHouse Sense** senza modificare i collegamenti.

1. **Verifica il cablaggio:** L'hardware utilizzato da SeismoCloud (ESP8266 + MPU6050 su bus I2C `SDA=D1` / `SCL=D2`) è già compatibile; non serve dissaldare o spostare i cavi (ignora eventuali LED o buzzer aggiuntivi se presenti).

2. Scarica il Firmware: ["DomHouse-Sense-Migration.bin"](https://github.com/SalvatoreITA/DomHouse-Sense/releases/)

2. **Flash del nuovo firmware:** Collega il dispositivo via USB al PC e flasha il file `.bin` precompilato di DomHouse Sense versione **Migration** tramite [ESPHome Web](https://web.esphome.io/).

3. Collegati in Wifi all'AP generato dal sismometro **DomHouseSense-Setup**

4. Dal Browser digita 192.168.4.1 si aprirà una pagina dove inserire le tue credenziali WiFi 

5. Apri nel browser l'indirizzo IP locale del sensore: si aprirà una comoda **pagina web di configurazione** dove potrai inserire la tua **Chiave API**, un **nome generico della stazione** (es. *"Nodo Roma Nord"*, evitando nomi e cognomi reali) e le **coordinate di un punto pubblico vicino a te (`lat` / `lon`)**.

#### 💡 Significato dei LED

| 🟢 Verde | 🟡 Giallo | 🔴 Rosso | Stato |
| :---: | :---: | :---: | :--- |
| **ON** | — | — | Inattivo e in ascolto (connesso al server) |
| **ON** | **ON** | — | Connessione al server persa, sta riprovando |
| **ON** | — | **ON** | **Vibrazione / terremoto rilevato** |
| **ON** | **ON** | **ON** | Si sta collegando alla rete DomHouse Sense (chiave mancante o server non ancora raggiunto) |
| — | **ON** | — | Connessione al WiFi |
| — | — | **ON** | Calibrazione in corso (tienilo fermo 10 s) |

















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

