from .client import BaseClient, MethodMap


ENTRY_POINT = 'bot'
ONE_ENDPOINT = f'{ENTRY_POINT}/channels/{{channel_id}}'


class BotClient(BaseClient):
    '''
    APIdoc: https://kokoro.io/apidoc#/bot
    '''
    name = ENTRY_POINT
    _method_map = MethodMap(
        ('send_message', 'post', f'{ONE_ENDPOINT}/messages')
    )
