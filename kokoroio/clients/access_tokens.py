from .client import Client


ENTRY_POINT = 'access_tokens'


class AccessTokensClient:
    '''
    APIdoc: https://kokoro.io/apidoc#/access_tokens
    '''
    name = ENTRY_POINT

    def __init__(self, access_token):
        client = Client(access_token)
        self.get = client.method('get', ENTRY_POINT)
        self.post = client.method('post', ENTRY_POINT)
        self.delete = client.method('delete', f'{ENTRY_POINT}/{{access_token_id}}')
