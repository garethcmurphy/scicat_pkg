#!/usr/bin/env python3
import getpass
import requests
import keyring

from api import Api


class Login:
    token = ""
    username = ""
    password = ""

    def login(self):
        credentials = {}
        try:
            username = getpass.getuser()
            # username = username.replace(".", "")
            print("Username", username)
        except:
            username = input("Username:")
        credentials["username"] = username
        password = keyring.get_password('scicat', username)
        if not password:
            print("No password found in keychain, please enter it now to store it.")
            password = getpass.getpass()
            keyring.set_password('scicat', username, password)
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
    login = Login()
    login.login()


if __name__ == "__main__":
    login()
