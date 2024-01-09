#!/usr/bin/python3
""" This is the 8-json_api module """


import requests
import sys
if __name__ == "__main__":
    if len(sys.argv) == 2:
        q = sys.argv[1]
    else:
        q = ""
    r = requests.post("http://0.0.0.0:5000/search_user", data={'q': q})
    if r.status_code == 200:
        if r.json:
            if r.json() and len(r.json()) > 0:
                print(f'[{r.json()["id"]}] {r.json()["name"]}')
            else:
                print("No result")
        else:
            print("Not a valid JSON")
