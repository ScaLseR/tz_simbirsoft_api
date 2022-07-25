"""fixtures"""
import pytest

@pytest.fixture(scope="class")
def get_token():
    token = 'AQAAAABjT3cJAADLW8UcQbr98UJct8YGQ9RzV1w'
    return token


@pytest.fixture(scope="function", autouse=True)
def clear():
    """delete folders after tests"""

    yield
    print('fixture end')
