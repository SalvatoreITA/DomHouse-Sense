"""DomHouse Sense: due modalità.

- push   : inoltra sisma (evento) e meteo (periodico) di questa HA al server.
- follow : segue le stazioni della rete e le espone come entità in questa HA.
"""
from __future__ import annotations

import logging
from datetime import timedelta

import aiohttp
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import Event, HomeAssistant, callback
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.event import (
    async_track_state_change_event,
    async_track_time_interval,
)

from .const import (
    CONF_DEVICE_ID,
    CONF_INTERVAL,
    CONF_KEY,
    CONF_LAT,
    CONF_LON,
    CONF_MODE,
    CONF_NAME,
    CONF_PGA,
    CONF_QUAKE,
    CONF_URL,
    DEFAULT_INTERVAL,
    DOMAIN,
    METRIC_MAP,
    MODE_FOLLOW,
)
from .coordinator import DomHouseSenseFollowCoordinator

_LOGGER = logging.getLogger(__name__)

PLATFORMS_FOLLOW = ["sensor", "binary_sensor"]


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    hass.data.setdefault(DOMAIN, {})

    if entry.data.get(CONF_MODE) == MODE_FOLLOW:
        coordinator = DomHouseSenseFollowCoordinator(hass, entry)
        await coordinator.async_config_entry_first_refresh()
        hass.data[DOMAIN][entry.entry_id] = coordinator
        await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS_FOLLOW)
        entry.async_on_unload(entry.add_update_listener(_async_update_listener))
        return True

    # modalità push (default)
    mgr = DomHouseSense(hass, entry)
    await mgr.async_start()
    hass.data[DOMAIN][entry.entry_id] = mgr
    entry.async_on_unload(entry.add_update_listener(_async_update_listener))
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    if entry.data.get(CONF_MODE) == MODE_FOLLOW:
        ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS_FOLLOW)
        hass.data.get(DOMAIN, {}).pop(entry.entry_id, None)
        return ok

    mgr = hass.data.get(DOMAIN, {}).pop(entry.entry_id, None)
    if mgr is not None:
        mgr.async_stop()
    return True


async def _async_update_listener(hass: HomeAssistant, entry: ConfigEntry) -> None:
    await hass.config_entries.async_reload(entry.entry_id)


# ============================================================================
#  Modalità PUSH
# ============================================================================
class DomHouseSense:
    """Inoltra i dati di questa HA verso il server DomHouse Sense."""

    def __init__(self, hass: HomeAssistant, entry: ConfigEntry) -> None:
        self.hass = hass
        self.entry = entry
        self.cfg = {**entry.data, **entry.options}
        self._session = async_get_clientsession(hass)
        self._unsubs: list = []

    async def async_start(self) -> None:
        c = self.cfg
        interval = int(c.get(CONF_INTERVAL, DEFAULT_INTERVAL))
        self._unsubs.append(
            async_track_time_interval(self.hass, self._push_measure, timedelta(seconds=interval))
        )
        quake = c.get(CONF_QUAKE)
        if quake:
            self._unsubs.append(
                async_track_state_change_event(self.hass, [quake], self._on_quake)
            )
        await self._push_measure(None)

    @callback
    def async_stop(self) -> None:
        for unsub in self._unsubs:
            unsub()
        self._unsubs.clear()

    def _num(self, entity_id: str | None):
        if not entity_id:
            return None
        st = self.hass.states.get(entity_id)
        if st is None or st.state in ("unknown", "unavailable", "none", ""):
            return None
        try:
            return float(st.state)
        except (ValueError, TypeError):
            return None

    async def _post(self, path: str, payload: dict) -> None:
        c = self.cfg
        base = str(c[CONF_URL]).rstrip("/")
        body = {"device_id": c[CONF_DEVICE_ID], "key": c[CONF_KEY], **payload}
        try:
            async with self._session.post(
                base + path,
                json=body,
                headers={"X-API-Key": c[CONF_KEY]},
                timeout=aiohttp.ClientTimeout(total=15),
            ) as resp:
                if resp.status >= 400:
                    _LOGGER.warning("DomHouse Sense %s -> HTTP %s", path, resp.status)
        except Exception as err:  # noqa: BLE001
            _LOGGER.warning("DomHouse Sense invio fallito (%s): %s", path, err)

    async def _push_measure(self, _now) -> None:
        c = self.cfg
        metrics = {}
        for conf_key, metric in METRIC_MAP.items():
            value = self._num(c.get(conf_key))
            if value is not None:
                metrics[metric] = value
        payload = {"name": c.get(CONF_NAME), "lat": c.get(CONF_LAT), "lon": c.get(CONF_LON)}
        if metrics:
            payload["metrics"] = metrics
        await self._post("/api/measure", payload)

    async def _on_quake(self, event: Event) -> None:
        new_state = event.data.get("new_state")
        if new_state is None or new_state.state != "on":
            return
        pga = self._num(self.cfg.get(CONF_PGA))
        _LOGGER.info("DomHouse Sense: scossa rilevata (PGA=%s), inoltro al server", pga)
        await self._post("/api/event", {"magnitude": pga})
