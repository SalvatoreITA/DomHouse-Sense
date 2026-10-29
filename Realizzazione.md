## 🛠️ Come costruire il Sismometro (Per le Opzioni B e C)

Se decidi di aggiungere anche il rilevamento sismico, ti bastano pochi euro di componenti e nessuna saldatura complessa:

1. **Microcontrollore Wi-Fi:** Un comune **ESP8266** (es. NodeMCU, Wemos D1 Mini) oppure un **ESP32**.

2. **Accelerometro:** Modulo **MPU6050** (sensore giroscopio/accelerometro a 6 assi I2C).

3. **Alimentazione e cavi:** 4 cavetti jumper femmina-femmina e un alimentatore micro-USB / USB-C.

4. ** LED STATO FACOLTATIVO

### Cablaggio (ESP8266 / NodeMCU ↔ MPU6050)

| Pin MPU6050 | Pin NodeMCU (ESP8266) | Funzione |
| ----- | ----- | ----- |
| **VCC** | `3V3` | Alimentazione 3.3V |
| **GND** | `GND` | Massa |
| **SDA** | `D1` (GPIO5) | Dati I2C |
| **SCL** | `D2` (GPIO4) | Clock I2C |

> 💡 **Consiglio di posizionamento:** Fissa il sensore in modo solidale a una parete portante, al pavimento o in un angolo basso della casa (lontano da lavatrici, porte che sbattono o termosifoni). **All'accensione, tieni il sensore completamente fermo per i primi 10 secondi** per permettere la calibrazione automatica degli assi.
