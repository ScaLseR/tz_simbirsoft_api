from requests import request
import pytest
import json


URL = 'https://cloud-api.yandex.net/v1/disk/resources'
token = 'AQAAAABjT3cJAADLW8UcQbr98UJct8YGQ9RzV1w'
name = 'tz_simbirsoft'
params = dict(path=name)
headers = dict(authorization=f'OAuth {token}')
resp_body = dict(href=f"{URL}?path=disk%3A%2F{name}", method="GET",
                 templated=False)


class TestApi:
    """Yandex rest api tests"""

    @pytest.mark.run
    def test_create_folder(self):
        """create folder test"""
        res = request(method='put', url=URL, headers=headers, params=params)
        assert res.status_code == 201
        assert json.loads(res.content.decode('utf-8')) == resp_body


