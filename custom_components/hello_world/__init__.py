import logging
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType
from homeassistant.helpers import config_validation as cv
import voluptuous as vol

_LOGGER = logging.getLogger(__name__)
DOMAIN = "hello_world"

CONFIG_SCHEMA = vol.Schema({
    DOMAIN: vol.Schema({
        vol.Optional('response', default='Hello World'): cv.string,
    }),
}, extra=vol.ALLOW_EXTRA)

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the Hello World component."""
    response_text = config[DOMAIN]['response']

    async def handle_say_hello(call):
        """Service to log a response and show it as a notification."""
        _LOGGER.info(f"Hello World Response: {response_text}")
        hass.components.persistent_notification.create(response_text, title="Hello World")

    # Register service within Home Assistant.
    hass.services.async_register(DOMAIN, "say_hello", handle_say_hello)

    return True
