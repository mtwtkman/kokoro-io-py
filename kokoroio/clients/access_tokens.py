from .client import BaseClient, MethodMap


ENTRY_POINT = 'access_tokens'


class AccessTokensClient(BaseClient):
    '''
    APIdoc: https://kokoro.io/apidoc#/access_tokens
    '''
    name = ENTRY_POINT
    _method_map = MethodMap(
        ('get', 'get', ENTRY_POINT),
        ('create', 'post', ENTRY_POINT),
        ('delete', 'delete', f'{ENTRY_POINT}/{{access_token_id}}'),
    )
