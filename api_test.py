"""api tests"""
import pytest


class TestApi:
    """Yandex rest api tests"""

    @pytest.mark.run
    def test_create_folder(self, fch, url):
        """create folder test"""
        name = 'tz_simbirsoft'
        res = fch.create_folder(name)
        assert res == (201, dict(href=f"{url}?path=disk%3A%2F{name}", method="GET", templated=False))



