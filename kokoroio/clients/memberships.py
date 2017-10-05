from .client import Client


ENTRY_POINT = 'memberships'


class MembershipsClient:
    '''
    APIdoc: https://kokoro.io/apidoc#/memberships
    '''
    name = ENTRY_POINT

    def __init__(self, access_token):
        client = Client(access_token)
        self.get = client.method('get', ENTRY_POINT)
        self.post = client.method('post', ENTRY_POINT)

        one_endpoint = f'{ENTRY_POINT}/{{member_ship_id}}'
        self.delete = client.method('delete', one_endpoint)
        self.put = client.method('put', one_endpoint)
