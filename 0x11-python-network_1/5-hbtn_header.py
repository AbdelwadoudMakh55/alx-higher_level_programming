#!/usr/bin/python3
""" This is the 5-hbtn_header module """


import requests
import sys
if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    r_id = r.headers.get["X-Request-Id"]
    print(r_id)
