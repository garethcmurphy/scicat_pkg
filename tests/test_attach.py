"""test"""
from attach import Attach


def test_answer():
    """test"""
    attach = Attach()

    assert isinstance(attach.file, str)
