#!/usr/bin/python3
""" This is the 8-json_api module """


import requests
import sys
if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    r = requests.post("http://0.0.0.0:5000/search_user", data={'q': q})
    if r.json:
        print(r.json())
