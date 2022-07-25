"""connector for http server"""
from json import loads
from requests import request

_UPLOAD_END_POINT = '/api/upload'
_DELETE_END_POINT = '/api/delete'

ENDPOINTS = {_UPLOAD_END_POINT: 'put', _DELETE_END_POINT: 'delete'}


def request_preparation(base_url, endpoint):
    """request representation"""
    method = ENDPOINTS[endpoint]
    url = base_url + endpoint

    def make_request(params=None, headers=None, data=None):
        response = request(method=method, url=url,
                           headers=headers, params=params, data=data)
        # #response.raise_for_status()
        return response
    return make_request


class ConnectorHttp:
    """class to work with our server"""

    def __init__(self, http_url):
        self._upload = request_preparation(http_url, _UPLOAD_END_POINT)
        self._delete = request_preparation(http_url, _DELETE_END_POINT)

    def download_without_param(self):
        """download file without parameters"""
        response = self._download()
        return response.status_code, response.content.decode('utf-8')

