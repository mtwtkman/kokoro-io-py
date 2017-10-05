import requests


API_VERSION = 'v1'


class Client:
    base_url = f'https://kokoro.io/api/{API_VERSION}'

    def __init__(self, access_token):
        self.access_token = access_token

    def __request(self, url, method, attrs, **path_params):
        return getattr(requests, method)(
            url.format(**path_params) if path_params else url,
            headers={'X-Access-Token': self.access_token},
            **attrs
        )

    def method(self, name, endpoint):
        param_key = 'params' if name in ['get', 'delete'] else 'data'
        def req(params=None, **path_params):
            return self.__request(
                f'{self.base_url}/{endpoint}',
                name,
                {param_key: params or {}},
                **path_params,
            )
        return req
