"""test"""
from login import Login


def test_login():
    """test"""
    login = Login()

    assert isinstance(login.token, str)
    assert isinstance(login.username, str)
    assert isinstance(login.password, str)
