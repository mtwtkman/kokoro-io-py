from .clients import clients
from .utils import config


class RequireAccessToken(Exception):
    pass


class Kokoroio:
    def __init__(self, env_path=None, access_token=None):
        token = access_token or config.get(env_path)
        if not token:
            raise RequireAccessToken(
                'You must set access token to request to kokro.io.'
            )
        for name, client_cls in clients.items():
            setattr(self, name, client_cls(access_token))
