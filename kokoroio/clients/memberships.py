from .client import BaseClient, MethodMap


ENTRY_POINT = 'memberships'
ONE_ENDPOINT = f'{ENTRY_POINT}/{{member_ship_id}}'

class MembershipsClient(BaseClient):
    '''
    APIdoc: https://kokoro.io/apidoc#/memberships
    '''
    name = ENTRY_POINT
    _method_map = MethodMap(
        ('get', 'get', ENTRY_POINT),
        ('create', 'post', ENTRY_POINT),
        ('delete', 'delete', ONE_ENDPOINT),
        ('update', 'put', ONE_ENDPOINT),
    )
