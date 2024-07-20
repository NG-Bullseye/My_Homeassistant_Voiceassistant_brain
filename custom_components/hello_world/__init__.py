import logging
from homeassistant.components.conversation import AbstractConversationAgent
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
    """Set up the Hello World conversation agent from configuration.yaml."""
    response_text = config[DOMAIN].get('response')
    agent = HelloWorldAgent(response_text)
    hass.components.conversation.async_register(agent)
    return True

class HelloWorldAgent(AbstractConversationAgent):
    """A simple Hello World conversation agent."""

    def __init__(self, response_text):
        """Initialize with the configured response text."""
        self.response_text = response_text

    async def async_process(self, text: str, conversation_id: str) -> dict:
        """Process a line of text and return the configured response."""
        _LOGGER.info(f"Received text for processing: {text}")
        return {
            "speech": {"plain": {"text": self.response_text}},
            "text": self.response_text
        }

    def supported_languages(self):
        """Return the list of supported languages."""
        return ["en"]  # Assuming English is supported. Adjust as necessary.
