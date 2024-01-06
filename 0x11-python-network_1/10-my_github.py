#!/usr/bin/python3
""" Connecting to the github API """


import requests
import sys
if __name__ == "__main__":
    url = "https://api.github/users/" + sys.argv[1]
    header = {
            'Authorization': f'Bearer {sys.argv[2]}'
    }
    r = requests.get(url, header=header)
    if r.json():
        print(r.json()["id"])
