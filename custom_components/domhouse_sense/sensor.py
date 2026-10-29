"""Entità sensore create in modalità 'segui' (una per metrica per stazione seguita)."""
from __future__ import annotations

from homeassistant.components.sensor import SensorEntity, SensorStateClass
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import CONF_MODE, CONF_STATIONS, DOMAIN, FOLLOW_METRICS, MODE_FOLLOW


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    if entry.data.get(CONF_MODE) != MODE_FOLLOW:
        return
    coordinator = hass.data[DOMAIN][entry.entry_id]
    cfg = {**entry.data, **entry.options}
    followed = cfg.get(CONF_STATIONS, [])

    entities = []
    data = coordinator.data or {"stations": {}}
    for dev in followed:
        st = data["stations"].get(dev)
        name = (st or {}).get("name") or dev
        metrics = (st or {}).get("metrics") or {}
        for metric in FOLLOW_METRICS:
            if metric in metrics:
                entities.append(FollowSensor(coordinator, dev, name, metric))
    async_add_entities(entities)


class FollowSensor(CoordinatorEntity, SensorEntity):
    _attr_has_entity_name = True
    _attr_state_class = SensorStateClass.MEASUREMENT

    def __init__(self, coordinator, device_id: str, station_name: str, metric: str) -> None:
        super().__init__(coordinator)
        self._dev = device_id
        self._metric = metric
        friendly, unit, dclass = FOLLOW_METRICS[metric]
        self._attr_name = friendly
        self._attr_native_unit_of_measurement = unit
        if dclass:
            self._attr_device_class = dclass
        self._attr_unique_id = f"domhouse_sense_{device_id}_{metric}"
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, device_id)},
            name=f"DomHouse Sense · {station_name}",
            manufacturer="DomHouse Sense",
        )

    @property
    def native_value(self):
        data = self.coordinator.data
        st = data["stations"].get(self._dev) if data else None
        if not st:
            return None
        m = (st.get("metrics") or {}).get(self._metric)
        return m.get("value") if m else None

    @property
    def available(self) -> bool:
        data = self.coordinator.data
        return bool(data and self._dev in data["stations"])
