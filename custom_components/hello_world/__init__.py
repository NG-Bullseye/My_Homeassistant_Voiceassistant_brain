import logging
from homeassistant.components.conversation import AbstractConversationAgent
from homeassistant.helpers.typing import HomeAssistantType

_LOGGER = logging.getLogger(__name__)

async def async_setup(hass: HomeAssistantType, config: dict) -> bool:
    """Set up the Hello World conversation agent."""
    _LOGGER.info("Setting up Hello World agent")
    agent = HelloWorldAgent()
    hass.data["conversation_agent"] = agent  # Optional: store agent in hass data
    hass.components.conversation.async_register(agent)
    return True

class HelloWorldAgent(AbstractConversationAgent):
    """A simple Hello World conversation agent."""

    async def async_process(self, text: str, conversation_id: str) -> str:
        """Process a line of text and return a response."""
        return "Hello World"
