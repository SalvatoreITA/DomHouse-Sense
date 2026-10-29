# 🌤️ Opzione A: Solo Meteo & Sensori con Home Assistant (Zero Hardware da costruire)

Ideale se non vuoi assemblare il sismometro ma hai già dei sensori ambientali o una stazione meteo su **Home Assistant** o vuoi scambiarne i dati con gli altri utenti e vicini.

## 📦 Installazione

### Opzione A — HACS (consigliata)

1. In HACS apri il menu **⋮ → Repository personalizzate**.
2. Incolla `https://github.com/SalvatoreITA/DomSense`, categoria **Integration**, poi **Aggiungi**.
3. Cerca **Domsense Cloud**, installalo e **riavvia** Home Assistant.

### Opzione B — Manuale

1. Copia la cartella `custom_components/domsense/` dentro `config/custom_components/`.
2. Riavvia Home Assistant.

## ⚙️ Opzione A Configurazione ( Condividi Sensori )

**Impostazioni → Dispositivi e servizi → Aggiungi integrazione → "Domsense Cloud"**

1. Invia i miei sensori alla rete 
2. Inserisci la tua **Chiave API** , nome della stazione meteo e le coordinate approssimative del tuo quartiere (vedi nota sopra).
3. Seleziona quali entità meteo condividere sulla mappa (es. temperatura, umidità, pioggia).

## ⚙️ Opzione B Configurazione ( Utilizza Sensori Vicino a tè )

**Impostazioni → Dispositivi e servizi → Aggiungi integrazione → "Domsense Cloud"**

1. Segui Stazione Vicine
2. Seleziona quali stazioni meteo vuoi seguire
