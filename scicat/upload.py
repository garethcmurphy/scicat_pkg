#!/usr/bin/env python3
"""upload to scicat"""
import os
import datetime
import urllib

import requests
import ipywidgets

from IPython.display import display
from scicat import api
from scicat.login import LoginManager


class Upload:
    """upload"""
    dataset = {}
    token = ""
    uri = ""
    delete_uri = ""
    email = ""
    owner = ""
    owner_group = ""

    def __init__(self):
        apix = api.Api()
        self.api = apix.api
        loginx = LoginManager()
        userinfo = loginx.info()
        self.email = userinfo["currentUserEmail"]
        self.owner = userinfo["currentUser"]
        groups = userinfo["currentGroups"]
        self.owner_group = groups[0]

    def create_json(self):
        """create json"""
        date = datetime.datetime.now().isoformat()
        self.dataset = {
            "pid": "xlfghz",
            "owner": self.owner,
            "investigator": self.owner,
            "principalInvestigator": self.owner,
            "inputDatasets": ["string"],
            "usedSoftware": ["Mantid v4"],
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
            "ownerGroup": self.owner_group,
            "type": "derived"
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

        style = {'description_width': '150px', 'width': '200px'}
        layout = {'width': '500px'}

        dataset_name = ipywidgets.Text(value='Reduced neutron data',
                                       placeholder='Reduced neutron data',
                                       description='dataset Name:', disabled=False,
                                       style=style, layout=layout)
        software_used = ipywidgets.Text(value='Mantid v4.0', placeholder='Mantid',
                                        description='Software used:', disabled=False,
                                        style=style, layout=layout)
        email = ipywidgets.Text(value=self.email, placeholder=self.email,
                                description='Email:', disabled=False,
                                style=style, layout=layout)
        username = ipywidgets.Text(value=self.owner, placeholder=self.owner,
                                   description='Username:', disabled=False,
                                   style=style, layout=layout)
        orcid = ipywidgets.Text(value='', placeholder='orcid',
                                description='ORCiD:', disabled=False,
                                style=style, layout=layout)
        source_folder = ipywidgets.Text(value='/nfs/dram', placeholder='/nfs/dram',
                                        description='Source Folder', disabled=False,
                                        style=style, layout=layout)
        description = ipywidgets.Text(value='Reduced neutron data', placeholder='Reduced neutron data',
                                      description='Description:', disabled=False,
                                      style=style, layout=layout)
        group = ipywidgets.Text(value=self.owner_group, placeholder=self.owner_group,
                                description='Group', disabled=False,
                                style=style, layout=layout)

        upload_widget = ipywidgets.interactive(self.helper, a=dataset_name, b=software_used,
                                               c=email, d=username, e=orcid, f=source_folder,
                                               g=group, h=description)
        display(upload_widget)

    def helper(self, a, b, c, d, e, f, g, h):
        """helper"""


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

def widget():
    """widget"""
    uploader = Upload()
    uploader.widget()

def main():
    """main"""
    name = "nexus"
    upload(name)


if __name__ == "__main__":
    main()
