"""test"""
from upload import Upload


def test_answer():
    """upload"""
    api = Upload()

    assert isinstance(api.dataset, dict)