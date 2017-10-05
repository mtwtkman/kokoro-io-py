from .client import Client


ENTRY_POINT = 'bot'


class BotClient:
    '''
    APIdoc: https://kokoro.io/apidoc#/bot
    '''
    name = ENTRY_POINT

    def __init__(self, access_token):
        client = Client(access_token)

        self.send_message = client.method('post', f'{ENTRY_POINT}/channels/{{channel_id}}/messages')
