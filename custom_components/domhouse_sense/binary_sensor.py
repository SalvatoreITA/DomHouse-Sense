"""Binary sensor 'scossa recente' per ogni stazione seguita (modalità 'segui')."""
from __future__ import annotations

from homeassistant.components.binary_sensor import (
    BinarySensorDeviceClass,
    BinarySensorEntity,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import CONF_MODE, CONF_STATIONS, DOMAIN, MODE_FOLLOW


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    if entry.data.get(CONF_MODE) != MODE_FOLLOW:
        return
    coordinator = hass.data[DOMAIN][entry.entry_id]
    cfg = {**entry.data, **entry.options}
    followed = cfg.get(CONF_STATIONS, [])

    data = coordinator.data or {"stations": {}}
    entities = []
    for dev in followed:
        st = data["stations"].get(dev)
        name = (st or {}).get("name") or dev
        entities.append(FollowQuake(coordinator, dev, name))
    async_add_entities(entities)


class FollowQuake(CoordinatorEntity, BinarySensorEntity):
    _attr_has_entity_name = True
    _attr_device_class = BinarySensorDeviceClass.VIBRATION

    def __init__(self, coordinator, device_id: str, station_name: str) -> None:
        super().__init__(coordinator)
        self._dev = device_id
        self._attr_name = "Scossa recente"
        self._attr_unique_id = f"domhouse_sense_{device_id}_quake"
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, device_id)},
            name=f"DomHouse Sense · {station_name}",
            manufacturer="DomHouse Sense",
        )

    @property
    def is_on(self) -> bool:
        data = self.coordinator.data
        return bool(data and self._dev in data["quakes"])
