"""Config flow + Options flow per DomHouse Sense.

Due modalità scelte da un menu:
  - push   : invia i sensori di questa HA al server (come prima)
  - follow : segue le stazioni della rete e le mostra in questa HA
"""
from __future__ import annotations

import uuid

import aiohttp
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.helpers import selector
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .const import (
    CONF_DEVICE_ID,
    CONF_HUM,
    CONF_INTERVAL,
    CONF_KEY,
    CONF_LAT,
    CONF_LON,
    CONF_MODE,
    CONF_NAME,
    CONF_PGA,
    CONF_PM10,
    CONF_PM25,
    CONF_POLL,
    CONF_PRESSURE,
    CONF_QUAKE,
    CONF_RAIN,
    CONF_STATIONS,
    CONF_TEMP,
    CONF_URL,
    CONF_WIND,
    CONF_WINDDIR,
    DEFAULT_INTERVAL,
    DEFAULT_POLL,
    DEFAULT_SERVER_URL,
    DOMAIN,
    MODE_FOLLOW,
    MODE_PUSH,
)

_SENSOR_KEYS = (
    CONF_TEMP,
    CONF_HUM,
    CONF_RAIN,
    CONF_PRESSURE,
    CONF_WIND,
    CONF_WINDDIR,
    CONF_PM25,
    CONF_PM10,
)


def _entity_selector(domain: str) -> selector.EntitySelector:
    return selector.EntitySelector(selector.EntitySelectorConfig(domain=domain))


def _build_push_schema(defaults: dict) -> vol.Schema:
    """Schema della modalità 'invia'."""
    fields: dict = {
        vol.Required(CONF_URL, default=defaults.get(CONF_URL) or DEFAULT_SERVER_URL): str,
        vol.Required(CONF_KEY, default=defaults.get(CONF_KEY, "")): str,
        vol.Required(CONF_NAME, default=defaults.get(CONF_NAME) or "DomHouse Sense"): str,
        vol.Required(CONF_LAT, default=float(defaults.get(CONF_LAT) or 0.0)): vol.Coerce(float),
        vol.Required(CONF_LON, default=float(defaults.get(CONF_LON) or 0.0)): vol.Coerce(float),
    }
    for key in (CONF_QUAKE, CONF_PGA, *_SENSOR_KEYS):
        dom = "binary_sensor" if key == CONF_QUAKE else "sensor"
        cur = defaults.get(key)
        marker = (
            vol.Optional(key, description={"suggested_value": cur}) if cur else vol.Optional(key)
        )
        fields[marker] = _entity_selector(dom)
    fields[
        vol.Optional(CONF_INTERVAL, default=int(defaults.get(CONF_INTERVAL) or DEFAULT_INTERVAL))
    ] = vol.Coerce(int)
    return vol.Schema(fields)


async def _fetch_stations(hass, url: str):
    """Scarica l'elenco stazioni pubbliche dal server; None se non raggiungibile."""
    session = async_get_clientsession(hass)
    try:
        async with session.get(
            url.rstrip("/") + "/api/sensors", timeout=aiohttp.ClientTimeout(total=15)
        ) as resp:
            if resp.status != 200:
                return None
            data = await resp.json()
            return [
                {"device_id": s["device_id"], "name": s.get("name") or s["device_id"]}
                for s in data.get("sensors", [])
            ]
    except Exception:  # noqa: BLE001
        return None


class DomHouseSenseConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    def __init__(self) -> None:
        self._follow_url = DEFAULT_SERVER_URL
        self._follow_poll = DEFAULT_POLL
        self._stations: list = []

    async def async_step_user(self, user_input=None):
        # menu: invia o segui
        return self.async_show_menu(step_id="user", menu_options=[MODE_PUSH, MODE_FOLLOW])

    # ---------------- modalità INVIA ----------------
    async def async_step_push(self, user_input=None):
        if user_input is not None:
            data = dict(user_input)
            data[CONF_MODE] = MODE_PUSH
            data[CONF_DEVICE_ID] = f"ha-{uuid.uuid4().hex[:12]}"
            await self.async_set_unique_id(data[CONF_DEVICE_ID])
            return self.async_create_entry(title=data.get(CONF_NAME, "DomHouse Sense"), data=data)

        lat = self.hass.config.latitude if self.hass.config.latitude is not None else 0.0
        lon = self.hass.config.longitude if self.hass.config.longitude is not None else 0.0
        defaults = {
            CONF_URL: DEFAULT_SERVER_URL,
            CONF_NAME: self.hass.config.location_name or "DomHouse Sense",
            CONF_LAT: round(float(lat), 5),
            CONF_LON: round(float(lon), 5),
            CONF_INTERVAL: DEFAULT_INTERVAL,
        }
        return self.async_show_form(step_id="push", data_schema=_build_push_schema(defaults))

    # ---------------- modalità SEGUI ----------------
    async def async_step_follow(self, user_input=None):
        errors = {}
        if user_input is not None:
            self._follow_url = user_input[CONF_URL].rstrip("/")
            self._follow_poll = int(user_input.get(CONF_POLL, DEFAULT_POLL))
            stations = await _fetch_stations(self.hass, self._follow_url)
            if stations is None:
                errors["base"] = "cannot_connect"
            elif not stations:
                errors["base"] = "no_stations"
            else:
                self._stations = stations
                return await self.async_step_pick()
        schema = vol.Schema(
            {
                vol.Required(CONF_URL, default=DEFAULT_SERVER_URL): str,
                vol.Optional(CONF_POLL, default=DEFAULT_POLL): vol.Coerce(int),
            }
        )
        return self.async_show_form(step_id="follow", data_schema=schema, errors=errors)

    async def async_step_pick(self, user_input=None):
        if user_input is not None:
            data = {
                CONF_MODE: MODE_FOLLOW,
                CONF_URL: self._follow_url,
                CONF_POLL: self._follow_poll,
                CONF_STATIONS: user_input[CONF_STATIONS],
                CONF_DEVICE_ID: f"follow-{uuid.uuid4().hex[:8]}",
            }
            await self.async_set_unique_id(data[CONF_DEVICE_ID])
            return self.async_create_entry(title="DomHouse Sense (segui)", data=data)

        options = [{"value": s["device_id"], "label": s["name"]} for s in self._stations]
        schema = vol.Schema(
            {
                vol.Required(CONF_STATIONS): selector.SelectSelector(
                    selector.SelectSelectorConfig(options=options, multiple=True, mode="list")
                ),
            }
        )
        return self.async_show_form(step_id="pick", data_schema=schema)

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        return DomHouseSenseOptionsFlow(config_entry)


class DomHouseSenseOptionsFlow(config_entries.OptionsFlow):
    def __init__(self, config_entry) -> None:
        self._entry = config_entry

    async def async_step_init(self, user_input=None):
        if self._entry.data.get(CONF_MODE) == MODE_FOLLOW:
            return await self._step_follow(user_input)
        # push
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)
        defaults = {**self._entry.data, **self._entry.options}
        return self.async_show_form(step_id="init", data_schema=_build_push_schema(defaults))

    async def _step_follow(self, user_input):
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)
        cfg = {**self._entry.data, **self._entry.options}
        stations = await _fetch_stations(self.hass, str(cfg[CONF_URL])) or []
        options = [{"value": s["device_id"], "label": s["name"]} for s in stations]
        current = cfg.get(CONF_STATIONS, [])
        schema = vol.Schema(
            {
                vol.Optional(
                    CONF_POLL, default=int(cfg.get(CONF_POLL, DEFAULT_POLL))
                ): vol.Coerce(int),
                vol.Required(CONF_STATIONS, default=current): selector.SelectSelector(
                    selector.SelectSelectorConfig(options=options, multiple=True, mode="list")
                ),
            }
        )
        return self.async_show_form(step_id="init", data_schema=schema)
