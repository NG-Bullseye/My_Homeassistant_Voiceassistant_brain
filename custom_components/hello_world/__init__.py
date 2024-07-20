from homeassistant.core import HomeAssistant, ServiceCall
from homeassistant.helpers.typing import ConfigType

async def async_setup(hass: HomeAssistant, config: ConfigType):
    # Funktion, die auf Sprachbefehle antwortet
    async def handle_conversation(voice_command: str) -> str:
        # Hier könntest du eine Logik einbauen, um auf verschiedene Befehle zu reagieren
        if "wie spät ist es" in voice_command:
            return "Es ist jetzt " + datetime.now().strftime("%H:%M")
        elif "wie ist das wetter" in voice_command:
            return "Es ist momentan sonnig"
        else:
            return "Hello World"

    # Registriere die 'brain'-Funktion im Voice Pipeline System
    hass.data["voice_pipeline"].register_brain("my_conversation_brain", handle_conversation)
    return True