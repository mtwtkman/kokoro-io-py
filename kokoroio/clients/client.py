from collections import namedtuple
from contextlib import closing
import asyncio

import requests
import aiohttp


API_VERSION = 'v1'
BASE_URL = f'https://kokoro.io/api/{API_VERSION}'
GET_OR_DELETE = ['get', 'delete']


class IClient:
    def __init__(self, access_token):
        self.access_token = access_token

    def _build_param(self, method, params):
        return {
            'params' if method in GET_OR_DELETE else 'data': params or {}
        }

    def _build_url(self, endpoint, **path_params):
        url = f'{BASE_URL}/{endpoint}'
        return url.format(**path_params) if path_params else url

    def _build_request(self, url, method, **params):
        raise NotImplementedError

    def method(self, name, endpoint):
        raise NotImplementedError

    def method_with_path_params(self, name, endpoint):
        raise NotImplementedError

    @property
    def headers(self):
        return {'X-Access-Token': self.access_token}


class Client(IClient):
    def _request(self, url, method, attrs):
        return getattr(requests, method)(
            url,
            headers=self.headers,
            **attrs,
        )

    def _build_request(self, url, method, **params):
        return self._request(
            url,
            method,
            self._build_param(method, params),
        )

    def method_with_path_params(self, name, endpoint):
        def _req(**path_params):
            def __req(**params):
                return self._build_request(
                    self._build_url(endpoint, **path_params),
                    name,
                    **params
                )
            return __req
        return _req

    def method(self, name, endpoint):
        def _req(**params):
            return self._build_request(
                self._build_url(endpoint),
                name,
                **params
            )
        return _req


class AsyncClient(IClient):
    async def _request(self, url, method, attrs):
        async with aiohttp.ClientSession() as session:
            async with getattr(session, method)(
                url,
                headers=self.headers, **attrs
            ) as response:
                return response

    def _build_request(self, url, method, **params):
        with closing(asyncio.get_event_loop()) as loop:
            return loop.run_until_complete(
                self._request(
                    url,
                    method,
                    self._build_param(method, params),
                )
            )

    def method(self, name, endpoint):
        def _req(**params):
            return self._build_request(
                self._build_url(endpoint),
                name,
                **params,
            )
        return _req

    def method_with_path_params(self, name, endpoint):
        def _req(**path_params):
            def __req(**params):
                return self._build_request(
                    self._build_url(endpoint, **path_params),
                    name,
                    **params,
                )
            return __req
        return _req


class MissingMethodMapError(Exception):
    pass


MetaMap = namedtuple('MetaMap', ('method url'))


class MethodMap(dict):
    def __init__(self, *tuples):
        for name, method, url in tuples:
            self[name] = MetaMap(method, url)

    @property
    def method_names(self):
        return self.keys()


class BaseClient:
    _method_map = MethodMap()

    def __init__(self, access_token):
        if not hasattr(self, '_method_map'):
            raise MissingMethodMapError(
                    f'{self.__class__.__name__}: missing `_method_map`'
            )

        client = Client(access_token)
        async_client = AsyncClient(access_token)

        for name, meta in self._method_map.items():
            m = meta.method
            u = meta.url
            client_method = 'method_with_path_params' if '{' in u else 'method'
            setattr(self, name, getattr(client, client_method)(m, u))
            setattr(
                self,
                f'a{name}',
                getattr(async_client, client_method)(m, u)
            )

    @property
    def method_names(self):
        return self._method_map.method_names

    @property
    def methods(self):
        return self._method_map
