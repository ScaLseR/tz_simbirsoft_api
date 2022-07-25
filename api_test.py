from requests import request
import pytest

URL = 'https://cloud-api.yandex.net/v1/disk/resources'
TOKEN = 'OAuth AQAAAABjT3cJAADLW8UcQbr98UJct8YGQ9RzV1w'
params = dict(path='tz_simbirsoft')
headers = dict(accept='application/json', authorization='OAuth AQAAAABjT3cJAADLW8UcQbr98UJct8YGQ9RzV1w')
resp_body = {"href":"https://cloud-api.yandex.net/v1/disk/resources?path=disk%3A%2Ftz_simbirsoft","method":"GET","templated":false}


class TestApi:
    """ тесткейс на созданеи новой папки с названием"""

    def test_create_folder(self):
        res = request(method='put', url=URL, headers=headers, params=params)
        print('status code', res.status_code)
        print('telo otveta', res.content.decode('utf-8'))
        assert str(res.status_code) == '201'


