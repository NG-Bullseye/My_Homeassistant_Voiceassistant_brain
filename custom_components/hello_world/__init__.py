import logging
from homeassistant.helpers import intent

_LOGGER = logging.getLogger(__name__)

async def async_setup(hass, config):
    intent.async_register(hass, HelloWorldIntentHandler())
    return True

class HelloWorldIntentHandler(intent.IntentHandler):
    intent_type = 'HelloWorld'

    async def async_handle(self, intent_obj):
        response = intent_obj.create_response()
        response.async_set_speech("Hello World from your conversation agent.")
        return response
