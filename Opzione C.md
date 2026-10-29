# 📡 Opzione C: Sismometro Standalone (Senza Home Assistant)

Ideale se non usi Home Assistant e vuoi semplicemente un sismometro autonomo che invia i dati direttamente alla mappa della rete.

1. Scarica il Firmware: ["DomHouse-Sense-Standalone.bin"](https://github.com/SalvatoreITA/DomHouse-Sense/releases/)

2. Costruisci il sensore seguendo lo ["Schema Realizzazione"](https://github.com/SalvatoreITA/DomHouse-Sense/blob/main/Realizzazione.md) e flasha sul microcontrollore il file `.bin` precompilato della versione **Standalone** (usando ad esempio il browser con [ESPHome Web](https://web.esphome.io/)).

3. Collegati in Wifi all'AP generato dal sismometro **DomHouseSense-Setup**

4. Dal Browser digita 192.168.4.1 si aprirà una pagina dove inserire le tue credenziali WiFi 

5. Apri nel browser l'indirizzo IP locale del sensore: si aprirà una comoda **pagina web di configurazione** dove potrai inserire la tua **Chiave API**, un **nome generico della stazione** (es. *"Nodo Roma Nord"*, evitando nomi e cognomi reali) e le **coordinate di un punto pubblico vicino a te (`lat` / `lon`)**.
