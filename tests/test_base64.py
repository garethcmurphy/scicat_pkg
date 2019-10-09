"""test"""
from base64_im import Base64Im


def test_upload():
    """upload"""
    upload = Base64Im()
    assert isinstance(upload.filename, str)
