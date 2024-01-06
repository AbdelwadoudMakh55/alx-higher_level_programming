#!/usr/bin/python3
""" This is the 1-hbtn_header module """


from urllib import request
import sys
with request.urlopen(sys.argv[1]) as resp:
    print(resp.headers.__dict__["_headers"][-3][1])
