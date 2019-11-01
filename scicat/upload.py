#!/usr/bin/env python3
"""upload to scicat"""
import os
import datetime
import urllib

import requests

from scicat import api
from scicat import login
from scicat.login import LoginManager


class Upload:
    """upload"""
    dataset = {}
    token = ""
    uri = ""
    delete_uri = ""
    email = ""
    owner = ""
    ownerGroup = ""

    def __init__(self):
        apix = api.Api()
        self.api = apix.api
        loginx = LoginManager()
        userinfo = loginx.info()
        self.email = userinfo["currentUserEmail"]
        self.owner = userinfo["currentUser"]
        groups = userinfo["currentGroups"]
        self.ownerGroup = groups[0]

    def create_json(self):
        """create json"""
        date = datetime.datetime.now().isoformat()
        self.dataset = {
            "pid": "xlfghz",
            "owner": self.owner,
            "ownerEmail": self.email,
            "contactEmail": self.email,
            "sourceFolder": "/dram/",
            "datasetName": "Test python upload",
            "creationTime": date,
            "keywords": [
                "Test", "Derived", "Science"
            ],
            "description": "Test uploaded metadata from python",
            "isPublished": False,
            "ownerGroup": self.ownerGroup,
            "type": "raw"
        }

    def get_token(self):
        """get scicat token"""
        loginx = LoginManager()
        self.token = loginx.login()
        print("token", self.token)

    def create_uri(self):
        """create uri"""
        # login = Login()
        # token = login.login()
        self.uri = os.path.join(self.api, "Datasets") + \
            "?access_token=" + self.token
        print(self.uri)

    def upload_scicat(self):
        """upload to scicat"""
        self.get_token()
        self.create_uri()
        self.create_json()
        pid = urllib.parse.quote_plus("20.500.12269/"+self.dataset["pid"])
        delete_uri = os.path.join(
            self.api, "Datasets", pid) + "?access_token=" + self.token
        response = requests.delete(delete_uri)
        print(delete_uri)
        print(response.json())
        response = requests.post(self.uri, json=self.dataset)
        print(response.json())


    def widget(self):
        """upload widget"""
        

def upload(name):
    """upload to scicat"""
    print("uploading to scicat")
    dataset = {
        "datasetName": name
    }
    uploader = Upload()
    uploader.get_token()
    uploader.upload_scicat()

    print(dataset)


def main():
    """main"""
    name = "nexus"
    upload(name)


if __name__ == "__main__":
    main()
