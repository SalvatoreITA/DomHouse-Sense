# 🌋 Opzione B: Sismometro + Home Assistant (Consigliata per utenti HA)

Ideale se usi **Home Assistant** e vuoi sia costruire il sismometro, sia condividere/ricevere i dati meteo della community.

1. Costruisci il sensore seguendo lo [schema qui sotto](#️-come-costruire-il-sismometro-per-le-opzioni-b-c-e-d) e flasha sul microcontrollore il file `.bin` precompilato della versione **Home Assistant** (usando ad esempio il browser con [ESPHome Web](https://web.esphome.io/)).

2. Collegalo al Wi-Fi: verrà rilevato automaticamente dalla tua istanza Home Assistant.

3. Tramite l'add-on **DomSense** su Home Assistant, inserisci la tua **Chiave API** e invia alla rete sia gli eventi del sismometro sia i tuoi sensori meteo.
