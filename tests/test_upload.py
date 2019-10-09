"""test"""
from upload import Upload


def test_upload():
    """upload"""
    upload = Upload()
    assert isinstance(upload.dataset, dict)
