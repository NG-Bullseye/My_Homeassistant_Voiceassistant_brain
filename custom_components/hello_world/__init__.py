import logging
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType
from homeassistant.components.conversation import AbstractConversationAgent

_LOGGER = logging.getLogger(__name__)
DOMAIN = "hello_world"

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the Hello World conversation agent."""
    hass.data[DOMAIN] = HelloWorldAgent()
    hass.components.conversation.async_register(hass.data[DOMAIN])
    return True

class HelloWorldAgent(AbstractConversationAgent):
    """A simple Hello World conversation agent."""

    async def async_process(self, text: str, conversation_id: str) -> str:
        """Process a line of text and return 'Hello World'."""
        _LOGGER.info("Received text for processing: %s", text)
        return "Hello World"
