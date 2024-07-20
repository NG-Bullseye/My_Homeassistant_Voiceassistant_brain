import logging
from homeassistant.helpers import intent

_LOGGER = logging.getLogger(__name__)

async def async_setup(hass, config):
    hass.helpers.intent.async_register(MyIntentHandler())
    return True

class MyIntentHandler(intent.IntentHandler):
    intent_type = 'HelloWorldIntent'

    async def handle(self, intent_obj):
        _LOGGER.info("Handled intent: %s", intent_obj.intent_type)
        response = intent_obj.create_response()
        response.async_set_speech("Hello World")
        response.async_set_card("Intent handled successfully")
        return response
