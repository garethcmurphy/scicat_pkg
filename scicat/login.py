import requests
import json
import urllib
import getpass

def login(text, max_number_results):
    username = getpass.getuser() 
    try: 
        p = getpass.getpass() 
    except Exception as error: 
        print('ERROR', error) 
    else: 
        print('Password entered:', p) 
    
