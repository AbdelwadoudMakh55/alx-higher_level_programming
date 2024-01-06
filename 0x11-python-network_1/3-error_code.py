#!/usr/bin/python3
""" This is the 3-error_code module """


import urllib
import sys
if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as req:
            pass
    except urllib.error.HTTPError as e:
        print(e.reason)
