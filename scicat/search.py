#!/usr/bin/env python3
"""search scicat"""
import json
import urllib

import requests


def search(text, max_number_results):
    """search scicat"""
    fields = {'text': text}
    limit = {'limit': max_number_results, 'order': "creationTime:desc"}
    fields_encode = urllib.parse.quote(json.dumps(fields))
    limit_encode = urllib.parse.quote(json.dumps(limit))
    dataset_url = "https://scicat.esss.se/api/v3/Datasets/anonymousquery?fields=" + \
        fields_encode+"&limits="+limit_encode
    response = requests.get(dataset_url).json()
    print(len(response), "result found!")
    return response
