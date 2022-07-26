"""connector for yandex api"""
from json import loads
from requests import request


class ConnectorAPI:
    """class to work with api"""
    _name = ''

    def __init__(self, url, token):
        self.url = url
        self.token = token

    def create_folder(self, name):
        """create folder with name = name"""
        ConnectorAPI._name = name
        response = request(method='put', url=self.url,
                           headers=dict(authorization=f'OAuth {self.token}'),
                           params=dict(path=name))
        return response.status_code, loads(response.content.decode('utf-8'))

    def delete_folder(self):
        """delete folder with name = name"""
        _response = request(method='delete', url=self.url,
                            headers=dict(authorization=f'OAuth {self.token}'),
                            params=dict(path=ConnectorAPI._name))
