from .client import Client


ENTRY_POINT = 'channels'


class ChannelsClient:
    '''
    APIdoc: https://kokoro.io/apidoc#/channels
    '''
    name = ENTRY_POINT

    def __init__(self, access_token):
        client = Client(access_token)

        # all channels
        self.get = client.method('get', ENTRY_POINT)
        self.create = client.method('post', ENTRY_POINT)

        # direct_message
        self.send_direct_message = client.method('post', f'{ENTRY_POINT}/direct_message')

        # certain channel
        one_endpoint = f'{ENTRY_POINT}/{{channel_id}}'
        self.get_by = client.method('get', one_endpoint)
        self.update = client.method('put', one_endpoint)

        # (un)archive
        self.archive = client.method('delete', f'{one_endpoint}/archive')
        self.unarchive = client.method('put', f'{one_endpoint}/unarchive')

        # authority
        self.update_authority = client.method(
            'put',
            f'{one_endpoint}/manage_members/{{member_id}}'
        )

        # messages
        message_endpoint = f'{one_endpoint}/messages'
        self.get_messages = client.method('get', message_endpoint)
        self.send_message = client.method('post', message_endpoint)
