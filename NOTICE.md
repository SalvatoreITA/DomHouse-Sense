# Componenti di terze parti

Il codice di **DomHouse Sense** (server, integrazione Home Assistant, file YAML dei firmware) è rilasciato sotto licenza **MIT** (vedi `LICENSE`).

Il progetto usa componenti di terze parti, ciascuno con la propria licenza. Questo file li elenca per trasparenza e per rispettare gli obblighi di quelle licenze.

## Firmware ESP (file `.bin`)

I `.bin` distribuiti sono compilati con **ESPHome 2026.10.0** a partire dagli YAML presenti in questo repository. Chiunque può ricompilarli con la stessa versione di ESPHome: tutte le librerie sotto vengono scaricate automaticamente dai loro repository pubblici.

| Componente | Licenza | Sorgenti |
|---|---|---|
| ESPHome (runtime C++) | MIT | https://github.com/esphome/esphome |
| Arduino core per ESP8266 | LGPL-2.1 | https://github.com/esp8266/Arduino |
| ESPAsyncTCP | LGPL-3.0 | https://github.com/ESP32Async/ESPAsyncTCP |
| ESPAsyncWebServer | LGPL-3.0 | https://github.com/ESP32Async/ESPAsyncWebServer |
| NeoPixelBus (solo firmware con LED WS2812) | LGPL-3.0 | https://github.com/Makuna/NeoPixelBus |
| noise-c | MIT | https://github.com/esphome/noise-c |
| libsodium | ISC | https://github.com/jedisct1/libsodium |

**Componenti LGPL:** i loro sorgenti sono disponibili ai link sopra. Per sostituirli o modificarli basta ricompilare il firmware con ESPHome partendo dallo YAML corrispondente in questo repository.

## Origine del progetto

Il firmware "compatibile SeismoCloud" (`firmware-seismo/`) usa lo stesso cablaggio e gli stessi stati LED del progetto [SeismoCloud NodeMCU](https://github.com/sapienzaapps/seismocloud-sensor-nodemcu) di Sapienza Università di Roma, per facilitare il passaggio. Il codice è stato scritto da zero in ESPHome: non contiene codice di SeismoCloud.
