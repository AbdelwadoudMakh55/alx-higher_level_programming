#!/usr/bin/python3
""" This is the 3-error_code module """


from urllib import request
import sys
if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as req:
            pass
    except urllib.error.HTTPError as e:
        print(e.reason)