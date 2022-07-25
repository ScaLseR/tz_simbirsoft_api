"""fixtures"""
import pytest
from requests import request
from api_connector import ConnectorAPI


@pytest.fixture(scope='function')
def fch(get_token, url):
    """connection to yandex api"""
    fch = ConnectorAPI(url, get_token)
    return fch


@pytest.fixture(scope='class')
def get_token():
    token = 'AQAAAABjT3cJAADLW8UcQbr98UJct8YGQ9RzV1w'
    return token


@pytest.fixture(scope='function')
def url():
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    return url


@pytest.fixture(scope='function', autouse=True)
def clear(get_token, url):
    """delete folders after tests"""

    yield
    _res = request(method='delete', url=url,
                   params=dict(path='tz_simbirsoft'),
                   headers=dict(authorization=f'OAuth {get_token}'))

