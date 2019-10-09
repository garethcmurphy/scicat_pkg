"""test"""
from api import Api


def test_api():
    """test"""
    api = Api()

    assert isinstance(api.api, str)
