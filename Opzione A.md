# 🌤️ Opzione A: Solo Meteo & Sensori con Home Assistant (Zero Hardware da costruire)

Ideale se non vuoi assemblare il sismometro ma hai già dei sensori ambientali o una stazione meteo su **Home Assistant** o vuoi scambiarne i dati con gli altri utenti e vicini.

## 📦 Installazione

### Opzione A — HACS (consigliata)

1. In HACS apri il menu **⋮ → Repository personalizzate**.
2. Incolla `https://github.com/SalvatoreITA/DomHouse-Sense`, categoria **Integration**, poi **Aggiungi**.
3. Cerca **DomHouse Sense Cloud**, installalo e **riavvia** Home Assistant.

### Opzione B — Manuale

1. Copia la cartella `custom_components/domhouse_sense/` dentro `config/custom_components/`.
2. Riavvia Home Assistant.

## ⚙️ Configurazione

### Opzione A — Condividi Sensori

**Impostazioni → Dispositivi e servizi → Aggiungi integrazione → "DomHouse Sense Cloud"**

1. Invia i miei sensori alla rete 
2. Inserisci la tua **Chiave API** , nome della stazione meteo e le coordinate approssimative del tuo quartiere (vedi nota sopra).
3. Seleziona quali entità meteo condividere sulla mappa (es. temperatura, umidità, pioggia).

### Opzione B — Utilizza sensori vicino a tè

**Impostazioni → Dispositivi e servizi → Aggiungi integrazione → "DomHouse Sense Cloud"**

1. Segui Stazione Vicine
2. Seleziona quali stazioni meteo vuoi seguire

> ⚠️ **Attenzione:** per ogni stazione seguita viene creato anche il sensore **"Scossa recente"**. È un dato **amatoriale e indicativo**: **non usarlo per allarmi, sirene o automazioni di sicurezza** (gas, corrente, cancelli…). Non è un sistema di allerta: per le emergenze fai riferimento solo a **Protezione Civile** e **INGV**.
