#!/usr/bin/python3
""" This is the 1-hbtn_header module """


from urllib import request
import sys
if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as resp:
        for att in resp.headers.__dict__["_headers"]:
            if att[0] == "X-Request-Id":
                print(att[1])
