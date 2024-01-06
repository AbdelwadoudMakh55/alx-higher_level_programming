#!/usr/bin/python3
""" This is the 2-post_email module """


from urllib import request, parse
import sys
data = parse.urlencode({'email': sys.argv[2]i}).encode()
req = request.Request(sys.argv[1], data=data)
with request.urlopen(req) as res:
    print(f"Your email is: {resp.read().decode()}")
