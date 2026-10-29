## 🛠️ Come costruire il Sismometro (Per le Opzioni B e C)

Se decidi di aggiungere anche il rilevamento sismico, ti bastano pochi euro di componenti e nessuna saldatura complessa:

1. **Microcontrollore Wi-Fi:** Un comune **ESP8266** (es. NodeMCU, Wemos D1 Mini).

2. **Accelerometro:** Modulo **MPU6050** (sensore giroscopio/accelerometro a 6 assi I2C).

3. **Alimentazione e cavi:** 4 cavetti jumper femmina-femmina e un alimentatore micro-USB / USB-C.

4. *(Facoltativo)* **1x Modulo LED RGB indirizzabile WS2812B (NeoPixel)** (da 1 a 10 LED) per avere un riscontro visivo immediato dello stato del sensore.

### 1️⃣ Schema collegamenti Sensore Sismico (Obbligatorio)

Collega il modulo **MPU6050** alla scheda **NodeMCU (ESP8266)** seguendo questa tabella:

| Pin MPU6050 | Pin NodeMCU (ESP8266) | Pin ESP32 (se usi ESP32) | Funzione |
| :--- | :--- | :--- | :--- |
| **VCC** | `3V3` (3.3V) | `3V3` (3.3V) | Alimentazione |
| **GND** | `GND` | `GND` | Massa (Terra) |
| **SDA** | `D2` (GPIO4) | `GPIO21` | Dati I2C |
| **SCL** | `D1` (GPIO5) | `GPIO22` | Clock I2C |

```text
   [ NodeMCU ESP8266 ]               [ Sensore MPU6050 ]
  +-------------------+             +-------------------+
  |               3V3 |------------>| VCC               |
  |               GND |------------>| GND               |
  |        D2 (GPIO4) |------------>| SDA               |
  |        D1 (GPIO5) |------------>| SCL               |
  +-------------------+             +-------------------+
```

### 2️⃣ Schema collegamenti LED di Stato WS2812B / NeoPixel (Facoltativo)

Il firmware supporta nativamente un LED RGB indirizzabile **WS2812B (NeoPixel)** (singolo o striscia/anello fino a 6 LED) collegato sul pin `D4` (`GPIO2`) per mostrarti a colpo d'occhio cosa sta facendo il sismometro senza dover aprire l'app. Se non lo colleghi, il sismometro funzionerà comunque regolarmente!

| Pin LED WS2812B | Pin NodeMCU (ESP8266) | Funzione |
| :--- | :--- | :--- |
| **VCC / 5V / +** | `VIN` (5V da USB) o `3V3` | Alimentazione LED |
| **GND / -** | `GND` | Massa (Terra) |
| **DIN (Data In)** | `D4` (GPIO2) | Segnale dati digitale |

```text
   [ NodeMCU ESP8266 ]               [ LED WS2812B (Opzionale) ]
  +-------------------+             +---------------------------+
  |        VIN (o 3V3)|------------>| VCC / 5V                  |
  |               GND |------------>| GND                       |
  |        D4 (GPIO2) |------------>| DIN (Data In)             |
  +-------------------+             +---------------------------+
```

#### 🎨 Significato dei colori del LED:
* 🟣 **Viola lampeggiante:** Calibrazione iniziale in corso (primi 10 secondi dall'accensione: **non toccare il sensore!**).
* 🔵 **Blu lampeggiante:** Sensore non connesso al Wi-Fi o in attesa di configurazione (modalità Setup AP `DomHouse Sense-Setup`).
* 🟡 **Giallo fisso:** Connesso al Wi-Fi ma in attesa di connessione a Home Assistant / Server.
* 🟢 **Verde fisso (luce soffusa):** Tutto OK! Sensore operativo, calibrato e connesso correttamente.
* 🔴 **Rosso lampeggiante veloce:** **ALLARME!** Scossa o anomalia vibratoria rilevata in corso!

---

### 📌 Consigli fondamentali per il posizionamento
Per far lavorare bene l'algoritmo sismico **STA/LTA** ed evitare falsi allarmi:
1. **Fissa bene il sensore:** incollalo (con biadesivo forte o colla a caldo) o avvitalo dentro una scatoletta poggiata su una **superficie solida, rigida e in piano**, meglio se vicino a un muro portante o al pavimento, lontano da porte che sbattono, lavatrici o luoghi di passaggio.
2. **Calibrazione all'avvio (10 secondi):** ogni volta che dai corrente al sensore, **non toccarlo per i primi 10 secondi** (se hai montato il LED, vedrai una luce **viola lampeggiante**). In questa fase il dispositivo calcola lo zero sugli assi X, Y e Z per compensare l'inclinazione.
