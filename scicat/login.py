#!/usr/bin/env python3
"""login and get token"""
import os

import getpass
import requests
import keyring

import ipywidgets

from scicat import api


class LoginManager:
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
                self.username = self.username.replace(".", "")
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
        apix = api.Api()
        url = os.path.join(apix.base, "auth/msad")
        token = ""
        response = requests.post(url, json=credentials)
        result = response.json()
        # print(result)
        token = ""
        if response.status_code == 200:
            pass
        else:
            print("Login failed")
            print(response.status_code)
            return token
        if isinstance(result, str):
            pass
            # print("token", token)
        else:
            token = result.get("access_token")
            # print("token", token)
        self.token = token
        return token

    def loginw(self):
        """login widget"""
        user = os.environ['USER']
        self.username = ipywidgets.Text(
            value=user, placeholder=user, description='User:', disabled=False)
        password_widget = ipywidgets.Password(
            description='Password:', placeholder='ess password')
        login_interactive = ipywidgets.interactive(
            self.helper1, user=self.username, password=password_widget)
        button = ipywidgets.Button(description="Login")
        self.output = ipywidgets.Output()
        button.on_click(self.on_button_clicked)

    def helper1(self, user, password):
        """helper"""

    def on_button_clicked(self):
        """on button clicked"""
        with self.output:
            print("Logging into scicat with username ", self.username.value)
            self.login()

    def info(self):
        """get info"""
        if self.token == "":
            self.login()
        apix = api.Api()
        url = apix.api + "Users/userInfos?access_token=" + self.token
        response = requests.get(url)
        requests.get(url)
        info = response.json()
        return info


def login():
    """main login"""
    scicatlogin = LoginManager()
    scicatlogin.login()
    return scicatlogin.token


def accesstoken():
    """get token"""
    scicatlogin = LoginManager()
    if scicatlogin.token == "":
        scicatlogin.login()
    return scicatlogin.token


def userinfo():
    """get info"""
    scicatlogin = LoginManager()
    if scicatlogin.token == "":
        # print("logging in")
        scicatlogin.login()
        # print(scicatlogin.token)
    info = scicatlogin.info()
    return info


if __name__ == "__main__":
    userinfo()
