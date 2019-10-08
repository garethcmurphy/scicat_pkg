#!/usr/bin/env python3
"""upload to scicat"""
from api import Api


class Upload:
    """upload"""
    dataset = {}

    def __init__(self):
        api = Api()
        self.api = api.api

    def create_json(self):
        """create json"""
        self.dataset = {
            "pid": "10.17199/xlfghz"
        }

    def upload_scicat(self):
        """upload to scicat"""

def upload(name):
    """upload to scicat"""
    print("uploading to scicat")
    dataset = {
        "datasetName": name
    }
    print(dataset)


def main():
    """main"""
    name = "nexus"
    upload(name)


if __name__ == "__main__":
    main()
