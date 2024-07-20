from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

async def async_setup(hass: HomeAssistant, config: ConfigType):
    async def handle_hello_world(voice_command):
        return "Hello World"

    hass.data["voice_pipeline"].register_brain("hello_world",handle_hello_world)
    return True