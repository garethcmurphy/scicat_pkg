#!/usr/bin/env python3
"""login and get token"""
import getpass
import requests
import keyring

from api import Api


class Login:
    """login and get token"""
    token = ""
    username = ""
    password = ""

    def login(self):
        """login and return token"""
        credentials = {}
        try:
            self.username = getpass.getuser()
            # username = username.replace(".", "")
            print("Username", self.username)
        except Exception as error:
            self.username = input("Username:")
        credentials["username"] = self.username
        password = keyring.get_password('scicat', self.username)
        if not password:
            print("No password found in keychain, please enter it now to store it.")
            password = getpass.getpass()
            keyring.set_password('scicat', self.username, password)
        credentials["password"] = password
        api = Api()
        url = api.base + "auth/msad"
        token = ""
        response = requests.post(url, json=credentials)
        result = response.json()
        print(result)
        token = ""
        if isinstance(token, str):
            print(token)
        else:
            token = result.get("access_token")

        return token


def login():
    """main login"""
    scicatlogin = Login()
    scicatlogin.login()


if __name__ == "__main__":
    login()
