"""test"""
from attach import Attach


def test_attach():
    """test"""
    attach = Attach()

    assert isinstance(attach.file, str)


def test_uri():
    """test uri"""
    attach = Attach()
    attach.create_uri()
    assert isinstance(attach.uri, str)

def test_json():
    """test uri"""
    attach = Attach()
    attach.create_json()
    assert isinstance(attach.attachment, dict)
