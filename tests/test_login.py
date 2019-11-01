"""test"""
from login import LoginManager


def test_login():
    """test"""
    login = LoginManager()

    assert isinstance(login.token, str)
    assert isinstance(login.username, str)
    assert isinstance(login.password, str)
