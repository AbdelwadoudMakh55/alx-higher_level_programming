#!/usr/bin/python3
""" Connecting to the github API """


import requests
import sys
if __name__ == "__main__":
    url = "https://api.github/" + sys.argv[1]
    header = {
            'Authorization': f'Bearer {sys.argv[2]}'
    }
    r = requests.get(url, headers=header)
    if r.response.status_code == 200:
        if r.json():
            print(r.json()["id"])
    else:
        print(None)
