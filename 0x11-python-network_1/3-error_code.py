#!/usr/bin/python3
""" This is the 3-error_code module """


import urllib
import sys
if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as req:
            print(req.read())
    except urllib.error.URLError as e:
        print(f'Error code: {e.reason}')
