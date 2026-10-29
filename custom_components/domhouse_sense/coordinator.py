"""Coordinator della modalità 'segui': legge periodicamente le stazioni dal server DomHouse Sense."""
from __future__ import annotations

import logging
import time
from datetime import timedelta

import aiohttp
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .const import CONF_POLL, CONF_URL, DEFAULT_POLL

_LOGGER = logging.getLogger(__name__)

# una stazione e' "in scossa" se ha un evento negli ultimi N secondi
QUAKE_WINDOW_S = 150


class DomHouseSenseFollowCoordinator(DataUpdateCoordinator):
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry) -> None:
        cfg = {**entry.data, **entry.options}
        self._url = str(cfg[CONF_URL]).rstrip("/")
        poll = int(cfg.get(CONF_POLL, DEFAULT_POLL))
        self._session = async_get_clientsession(hass)
        super().__init__(
            hass,
            _LOGGER,
            name="DomHouse Sense follow",
            update_interval=timedelta(seconds=max(30, poll)),
        )

    async def _async_update_data(self) -> dict:
        try:
            stations: dict = {}
            async with self._session.get(
                self._url + "/api/sensors", timeout=aiohttp.ClientTimeout(total=15)
            ) as resp:
                data = await resp.json()
                for s in data.get("sensors", []):
                    stations[s["device_id"]] = s

            quakes: set[str] = set()
            now = time.time()
            async with self._session.get(
                self._url + "/api/events/recent?since=0&limit=100",
                timeout=aiohttp.ClientTimeout(total=15),
            ) as resp:
                data = await resp.json()
                for e in data.get("events", []):
                    ra = e.get("received_at") or 0
                    if now - ra < QUAKE_WINDOW_S:
                        quakes.add(e["device_id"])

            return {"stations": stations, "quakes": quakes}
        except Exception as err:  # noqa: BLE001
            raise UpdateFailed(f"Errore leggendo dal server DomHouse Sense: {err}") from err
