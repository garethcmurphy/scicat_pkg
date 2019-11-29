#!/usr/bin/env python3
"""search scicat"""
import os
import json
import urllib

import requests

from scicat import api


def search(text, limit=10):
    """search scicat"""
    fields = {'text': text}
    limits = {'limit': limit, 'order': "creationTime:desc"}
    fields_encode = urllib.parse.quote(json.dumps(fields))
    limit_encode = urllib.parse.quote(json.dumps(limits))
    apix = api.Api()
    dataset_url = os.path.join(apix.api, "Datasets/anonymousquery?fields=") + \
        fields_encode+"&limits="+limit_encode
    response = requests.get(dataset_url).json()
    print(len(response), "result found!")
    return response


def main():
    """main"""
    search("v20", 1)


if __name__ == "__main__":
    main()
