"""Costanti del custom component DomHouse Sense."""

DOMAIN = "domhouse_sense"

# Valore DI DEFAULT dell'indirizzo server, precompilato nel form.

DEFAULT_SERVER_URL = ""

# Chiavi di configurazione (config entry)
CONF_URL = "server_url"
CONF_KEY = "api_key"
CONF_NAME = "station_name"
CONF_LAT = "latitude"
CONF_LON = "longitude"
CONF_INTERVAL = "interval"
CONF_DEVICE_ID = "device_id"

# Entità scelte dall'utente
CONF_QUAKE = "quake_entity"
CONF_PGA = "pga_entity"
CONF_TEMP = "temperature_entity"
CONF_HUM = "humidity_entity"
CONF_RAIN = "rain_entity"
CONF_PRESSURE = "pressure_entity"
CONF_WIND = "wind_entity"
CONF_WINDDIR = "wind_dir_entity"
CONF_PM25 = "pm25_entity"
CONF_PM10 = "pm10_entity"

DEFAULT_INTERVAL = 120  # secondi (deve stare sotto offline_after_s del server)

# mappa: chiave-config -> nome metrica inviato al server (riconosciuto dalla mappa)
METRIC_MAP = {
    CONF_TEMP: "temperature",
    CONF_HUM: "humidity",
    CONF_RAIN: "rain",
    CONF_PRESSURE: "pressure",
    CONF_WIND: "wind_speed",
    CONF_WINDDIR: "wind_direction",
    CONF_PM25: "pm25",
    CONF_PM10: "pm10",
}

# --- modalità dell'integrazione ---
CONF_MODE = "mode"
MODE_PUSH = "push"        # invia i sensori di questa HA al server
MODE_FOLLOW = "follow"    # segue le stazioni della rete e le mostra in questa HA

# --- modalità "segui" ---
CONF_STATIONS = "stations"   # elenco device_id da seguire
CONF_POLL = "poll"           # intervallo di polling (s)
DEFAULT_POLL = 120

# metrica -> (nome, unità, device_class HA) per le entità create in modalità "segui"
FOLLOW_METRICS = {
    "temperature":    ("Temperatura", "°C", "temperature"),
    "humidity":       ("Umidità", "%", "humidity"),
    "rain":           ("Pioggia", "mm", "precipitation"),
    "pressure":       ("Pressione", "hPa", "atmospheric_pressure"),
    "wind_speed":     ("Velocità vento", "km/h", "wind_speed"),
    "wind_direction": ("Direzione vento", "°", None),
    "pm25":           ("PM2.5", "µg/m³", "pm25"),
    "pm10":           ("PM10", "µg/m³", "pm10"),
}
