from homeassistant.helpers import intent

async def async_setup(hass, config):
    hass.helpers.intent.async_register(MyIntentHandler())
    return True

class MyIntentHandler(intent.IntentHandler):
    intent_type = 'HelloWorldIntent'

    async def handle(self, intent_obj):
        # Your intent handling logic here
