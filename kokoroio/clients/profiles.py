from .client import Client


ENTRY_POINT = 'profiles'


class ProfilesClient:
    '''
    APIdoc: https://kokoro.io/apidoc#/profiles
    '''
    name = ENTRY_POINT

    def __init__(self, access_token):
        client = Client(access_token)
        self.get = client.method('get', ENTRY_POINT)

        # me
        me_endpoint = f'{ENTRY_POINT}/me'
        self.me = client.method('get', me_endpoint)
        self.update_me = client.method('put', me_endpoint)
