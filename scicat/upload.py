#!/usr/bin/env python3
"""upload to scicat"""
import os
import pwd
import getpass
import datetime
import urllib

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
        self.human_name = pwd_struct.pw_gecos
        split_name = pwd_struct.pw_gecos.split(' ')
        self.email = '.'.join(split_name) + "@esss.se"
        print(self.email)

    def create_json(self):
        """create json"""
        date = datetime.datetime.now().isoformat()
        self.dataset = {
            "pid": "xlfghz",
            "owner": self.human_name,
            "ownerEmail": self.email,
            "contactEmail": self.email,
            "sourceFolder": "/dram/",
            "datasetName": "Test python upload",
            "creationTime": date,
            "keywords": [
                "Test", "Derived", "Science", "Math"
            ],
            "description": "Test uploaded metadata from python",
            "isPublished": False,
            "ownerGroup": "p34123",
            "type": "raw"
        }

    def upload_scicat(self):
        """upload to scicat"""
        # login = Login()
        # token = login.login()
        token = "uhY29G8F1YecRNzSoKeVqxRL5SfYciPxTO0u7ZB6lzyB3Urfv8GZSiSodvORNTkc"
        print(token)
        uri = os.path.join(self.api, "Datasets") + "?access_token=" + token
        print(uri)
        self.create_json()
        pid = urllib.parse.quote_plus("20.500.12269/"+self.dataset["pid"])
        delete_uri = os.path.join(
            self.api, "Datasets", pid) + "?access_token=" + token
        response = requests.delete(delete_uri)
        print(delete_uri)
        print(response.json())
        response = requests.post(uri, json=self.dataset)
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
