#!/usr/bin/env python3
import getpass
import requests
from api import Api
import json

def login():
    credentials = {}
    credentials["username"] = input("Username:")
    try: 
        credentials["password"] =  getpass.getpass() 
    except Exception as error: 
        print('ERROR', error) 
    else: 
        print('Password entered:' ) 
    
    api = Api()
    
    url = api.base + "auth/msad"


    print(url)
    token =""
    response = requests.post(url, json=credentials)
    result = response.json()
    print(result)
    token = ""
    token = result["access_token"]

    return token

def main():
    login()
    
if __name__ == "__main__":
    main()

