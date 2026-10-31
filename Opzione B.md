# 🌋 Opzione B: Sismometro + Home Assistant (Consigliata per utenti HA)

Ideale se usi **Home Assistant** e vuoi sia costruire il sismometro, sia condividere/ricevere i dati meteo della community.

1. Scarica il Firmware: ["DomHouse-Sense-HA.bin"](https://github.com/SalvatoreITA/DomHouse-Sense/tree/main/Firmware%20Pre%20Compilati)

2. Costruisci il sensore seguendo lo ["Schema Realizzazione"](https://github.com/SalvatoreITA/DomHouse-Sense/blob/main/Realizzazione.md) e flasha sul microcontrollore il file `.bin` precompilato della versione **Home Assistant** (usando ad esempio il browser con [ESPHome Web](https://web.esphome.io/)).

3. Collegati in Wifi all'AP generato dal sismometro **DomHouseSense-Setup**

4. Dal Browser digita 192.168.4.1 si aprirà una pagina dove inserire le tue credenziali WiFi 

5. Collegalo al Wi-Fi: verrà rilevato automaticamente dalla tua istanza Home Assistant.

6. Tramite l'add-on **[DomHouse Sense](https://github.com/SalvatoreITA/DomHouse-Sense/blob/main/Opzione%20A.md).** su Home Assistant, inserisci la tua **Chiave API** e invia alla rete sia gli eventi del sismometro sia i tuoi sensori meteo.
