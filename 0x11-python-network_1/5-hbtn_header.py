#!/usr/bin/python3
""" This is the 5-hbtn_header module """


import requests
import sys
if __name__ == "__main__":
    try:
        r = requests.get(sys.argv[1])
        r_id = r.headers["X-Request-Id"]
        if r_id is not None:
            print(r_id)
    except Exception:
        pass
