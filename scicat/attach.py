#!/usr/bin/env python3
"""attach a file"""
import os
import urllib

import requests

from scicat import Login
from scicat import Api
from scicat import Base64Im


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
        pid_string = urllib.parse.quote_plus(self.pid)
        self.uri = os.path.join(self.api, "Datasets", pid_string, "attachments") + \
            "?access_token=" + self.token
        print(self.uri)

    def base64_encode(self):
        """base 64 encode"""

    def create_json(self):
        """create dict for attachment in scicat format"""
        base64im = Base64Im()
        base64im.convert(self.file)

        file_string = base64im.image
        self.attachment = {
            "thumbnail": file_string,
            "caption": self.file,
            "datasetId": self.pid
        }

    def attach(self, file, pid):
        """attach a file"""
        self.file = file
        self.pid = pid
        self.get_token()
        self.create_uri()
        self.create_json()
        response = requests.post(self.uri, json=self.attachment)
        print(response.json())


def attach(file, pid):
    """attach a file"""
    attachment = Attach()
    attachment.attach(file, pid)


def main():
    """main"""
    file = "raw_data_3D_detectors.png"
    pid = "20.500.12269/xlfghz"
    attach(file, pid)


if __name__ == "__main__":
    main()
