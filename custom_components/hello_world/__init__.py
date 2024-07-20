import logging
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType
import voluptuous as vol
from homeassistant.helpers import config_validation as cv

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
        """Handle say hello service calls."""
        _LOGGER.info(f"Responding with: {response_text}")
        hass.components.persistent_notification.create(response_text, title="Hello World")

    hass.services.async_register(DOMAIN, "say_hello", handle_say_hello)

    return True
