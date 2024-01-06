#!/usr/bin/python3
""" This is the 1-hbtn_header module """


from urllib import request
import sys
if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as resp:
        if "_headers" in resp.headers.__dict__:
            print(resp.headers.__dict__["_headers"][-3][1])
