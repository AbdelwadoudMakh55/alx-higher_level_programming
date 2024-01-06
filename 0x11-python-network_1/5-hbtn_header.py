#!/usr/bin/python3
""" This is the 5-hbtn_header module """


import requests
if __name__ == "__main__":
    r = requests.get("https://alx-intranet.hbtn.io/status")
    print(r.headers["X-Request-Id"])
