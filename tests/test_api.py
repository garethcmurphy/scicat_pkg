"""test"""
from api import Api


def test_answer():
    """test"""
    api = Api()

    assert isinstance(api.api, str)
