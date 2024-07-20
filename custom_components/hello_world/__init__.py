import logging
from homeassistant.components.conversation import AbstractConversationAgent
from homeassistant.helpers.typing import HomeAssistantType

_LOGGER = logging.getLogger(__name__)

async def async_setup(hass: HomeAssistantType, config: dict) -> bool:
    """Set up the Hello World conversation agent."""
    _LOGGER.info("Setting up Hello World agent")
    hass.data["conversation_agent"] = HelloWorldAgent()
    return True

class HelloWorldAgent(AbstractConversationAgent):
    """A simple Hello World conversation agent."""

    async def async_process(self, text: str, conversation_id: str):
        """Process a line of text."""
        return "Hello World"
