#!/usr/bin/env python3
"""attach a file"""
import os

import requests

from login import Login
from api import Api


class Attach:
    """attach a file"""
    uri = ""
    api = ""

    def __init__(self):
        self.file = ""
        self.pid = ""
        self.token = ""
        self.attachment = {}
        api = Api()
        self.api = api.api

    def get_token(self):
        """get scicat token"""
        self.token = "uhY29G8F1YecRNzSoKeVqxRL5SfYciPxTO0u7ZB6lzyB3Urfv8GZSiSodvORNTkc"
        print(self.token)

    def create_uri(self):
        """create uri"""
        # login = Login()
        # token = login.login()
        self.uri = os.path.join(self.api, "Datasets") + \
            "?access_token=" + self.token
        print(self.uri)

    def base64_encode(self):
        """base 64 encode"""

    def create_json(self):
        """create dict for attachment in scicat format"""
        file_string = self.file
        self.attachment = {
            "thumbnail": file_string,
            "caption": self.file,
            "datasetId": self.pid
        }

    def attach(self, file, pid):
        """attach a file"""
        self.file = file
        self.pid = pid
        self.create_uri()
        self.create_json()
        print(self.attachment)
        print(self.token)
        response = requests.post(self.uri, json=self.attachment)


def attach(file, pid):
    """attach a file"""
    attachment = Attach()
    attachment.attach(file, pid)


def main():
    """main"""
    file = "im.jpg"
    pid = "10.18390/fhuieraehiru"
    attach(file, pid)


if __name__ == "__main__":
    main()
