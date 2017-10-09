from .client import BaseClient, MethodMap


ENTRY_POINT = 'profiles'
ME_ENDPOINT = f'{ENTRY_POINT}/me'

class ProfilesClient(BaseClient):
    '''
    APIdoc: https://kokoro.io/apidoc#/profiles
    '''
    name = ENTRY_POINT
    _method_map = MethodMap(
        ('get', 'get', ENTRY_POINT),
        ('me', 'get', ME_ENDPOINT),
        ('update_me', 'put', ME_ENDPOINT),
    )
