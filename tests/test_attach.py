"""test"""
from attach import Attach


def test_attach():
    """test"""
    attach = Attach()

    assert isinstance(attach.file, str)
