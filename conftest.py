"""fixtures"""
import pytest
from api_connector import ConnectorAPI


@pytest.fixture(scope='function')
def fch(get_token, url):
    """connection to api use url and token"""
    fch = ConnectorAPI(url, get_token)
    return fch


@pytest.fixture(scope='class')
def get_token():
    """get api token"""
    token = 'AQAAAABjT3cJAADLW8UcQbr98UJct8YGQ9RzV1w'
    return token


@pytest.fixture(scope='function')
def url():
    """get api url """
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    return url


@pytest.fixture(scope='function', autouse=True)
def clear(fch):
    """delete folders after tests"""

    yield
    fch.delete_folder()
