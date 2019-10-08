#!/usr/bin/env python3
"""upload to scicat"""
import os
import pwd
import getpass
import datetime

import requests

from api import Api
from login import Login


class Upload:
    """upload"""
    dataset = {}

    def __init__(self):
        api = Api()
        self.api = api.api
        username = getpass.getuser()
        pwd_struct = pwd.getpwnam(username)
        print(pwd_struct)
        human_name = pwd_struct.pw_gecos.split(' ')
        self.email = '.'.join(human_name) + "@esss.se"
        print(self.email)

    def create_json(self):
        """create json"""
        date = datetime.datetime.now().isoformat()
        self.dataset = {
            "pid": "10.17199/xlfghz",
            "owner": "Egon Meier",
            "ownerEmail": self.email,
            "contactEmail": self.email,
            "sourceFolder": "/dram/",
            "creationTime": date,
            "keywords": [
                "Test", "Derived", "Science", "Math"
            ],
            "description": "Some fancy description",
            "isPublished": False,
            "ownerGroup": "p34123"
        }

    def upload_scicat(self):
        """upload to scicat"""
        login = Login()
        token = login.login()
        print(token)
        uri = os.path.join(self.api, "Users/jwt") + "&access_token=" + token
        print(uri)
        response = requests.post(uri)
        print(response.json())


def upload(name):
    """upload to scicat"""
    print("uploading to scicat")
    dataset = {
        "datasetName": name
    }
    uploader = Upload()
    uploader.upload_scicat()

    print(dataset)


def main():
    """main"""
    name = "nexus"
    upload(name)


if __name__ == "__main__":
    main()
