"""connector for http server"""
from json import loads
from requests import request

_END_POINT = '/v1/disk/resources'

def request_preparation(base_url, method):
    """request representation"""
    url = base_url + _END_POINT

    def make_request(params=None, headers=None):
        response = request(method=method, url=url,
                           headers=headers, params=params)
        # #response.raise_for_status()
        return response
    return make_request


class ConnectorHttp:
    """class to work with our server"""

    def __init__(self, http_url):
        self._upload = request_preparation(http_url, _END_POINT)
        self._delete = request_preparation(http_url, _END_POINT)

    def create_folder(self):
        """download file without parameters"""
        response = self._upload()
        return response.status_code, response.content.decode('utf-8')

