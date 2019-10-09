"""test"""
from base64_im import Base64Im


def test_upload():
    """upload"""
    upload = Base64Im()
    assert isinstance(upload.filename, str)
    assert isinstance(upload.image, str)
    assert isinstance(upload.header, str)
