from .client import Client


ENTRY_POINT = 'devices'


class DevicesClient:
    '''
    APIdoc: https://kokoro.io/apidoc#/devices
    '''
    name = ENTRY_POINT

    def __init__(self, access_token):
        client = Client(access_token)
        self.get = client.method('get', ENTRY_POINT)
        self.post = client.method('post', ENTRY_POINT)

        one_endpoint = f'{ENTRY_POINT}/{{device_identifier}}'
        self.delete = client.method('delete', one_endpoint)

