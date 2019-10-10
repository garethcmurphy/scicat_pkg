#!/usr/bin/env python3
"""login and get token"""
import os
import sys

import getpass
import requests
import keyring

from scicat import Api


class Login:
    """login and get token"""
    token = ""
    username = ""
    password = ""

    def get_username(self):
        """get username"""
        if "JUPYTERHUB_USER" in os.environ:
            self.username = os.environ["JUPYTERHUB_USER"]
        else:
            try:
                self.username = getpass.getuser()
                # username = username.replace(".", "")
                print("Username", self.username)
            except Exception as error:
                print(error)
                self.username = input("Username:")

    def login(self):
        """login and return token"""
        credentials = {}
        self.get_username()
        credentials["username"] = self.username
        password = keyring.get_password('scicat', self.username)
        if not password:
            print("No password found in keychain, please enter it now to store it.")
            password = getpass.getpass()
            keyring.set_password('scicat', self.username, password)
        credentials["password"] = password
        api = Api()
        url = os.path.join(api.base, "auth/msad")
        token = ""
        response = requests.post(url, json=credentials)
        result = response.json()
        print(result)
        token = ""
        if response.status_code == 200:
            pass
        else:
            print("Login failed")
            print(response.status_code)
            return token
        if isinstance(result, str):
            print("token", token)
        else:
            token = result.get("access_token")
            print("token", token)

        return token


def login():
    """main login"""
    scicatlogin = Login()
    scicatlogin.login()


if __name__ == "__main__":
    login()
