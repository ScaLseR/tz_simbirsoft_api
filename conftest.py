"""fixtures"""
import pytest
from requests import request


@pytest.fixture(scope="class")
def get_token():
    token = 'AQAAAABjT3cJAADLW8UcQbr98UJct8YGQ9RzV1w'
    return token


@pytest.fixture(scope="function", autouse=True)
def clear(get_token):
    """delete folders after tests"""

    yield
    _res = request(method='delete', url='https://cloud-api.yandex.net/v1/disk/resources',
                   params=dict(path='tz_simbirsoft'),
                   headers=dict(authorization=f'OAuth {get_token}'))

