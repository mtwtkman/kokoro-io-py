from .client import BaseClient, MethodMap


ENTRY_POINT = 'devices'


class DevicesClient(BaseClient):
    '''
    APIdoc: https://kokoro.io/apidoc#/devices
    '''
    name = ENTRY_POINT
    _method_map = MethodMap(
        ('get', 'get', ENTRY_POINT),
        ('cerate', 'post', ENTRY_POINT),
        (
            'delete',
            'delete',
            f'{ENTRY_POINT}/{{device_identifier}}'
        ),
    )
