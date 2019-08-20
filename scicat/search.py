import requests
import json
import urllib

def search(text, max_number_results):
    fields = {'text': text}
    limit = {'limit': max_number_results, 'order': "creationTime:desc"}
    fields_encode = urllib.parse.quote(json.dumps(fields))
    limit_encode = urllib.parse.quote(json.dumps(limit))
    dataset_url = "https://scicatapi.esss.dk/api/v3/Datasets/anonymousquery?fields=" + \
                fields_encode+"&limits="+limit_encode
    r=requests.get(dataset_url).json()
    print(len(r), "result found!")
    return r
