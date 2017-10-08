from .client import BaseClient, MethodMap


ENTRY_POINT = 'channels'
ONE_ENDPONIT = f'{ENTRY_POINT}/{{channel_id}}'
MESSAGE_ENDPOINT = f'{ONE_ENDPONIT}/messages'


class ChannelsClient(BaseClient):
    '''
    APIdoc: https://kokoro.io/apidoc#/channels
    '''
    name = ENTRY_POINT
    _method_map = MethodMap(
        # all channels
        ('get', 'get', ENTRY_POINT),
        ('create', 'post', ENTRY_POINT),
        # direct_message
        (
            'send_direct_messag',
            'post',
            f'{ENTRY_POINT}/direct_message'
        ),
        # certain channel
        ('get_one', 'get', ONE_ENDPONIT),
        ('update', 'put', ONE_ENDPONIT),
        # (un)archive
        ('archive', 'delete', f'{ONE_ENDPONIT}/archive'),
        ('unarchive', 'put', f'{ONE_ENDPONIT}/unarchive'),
        # authority
        (
            'update_authority',
            'put',
            f'{ONE_ENDPONIT}/manage_members/{{member_id}}'
        ),
        # messages
        ('get_messages', 'get', MESSAGE_ENDPOINT),
        ('send_message', 'post', MESSAGE_ENDPOINT),
    )
