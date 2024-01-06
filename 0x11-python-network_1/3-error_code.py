#!/usr/bin/python3
""" This is the 3-error_code module """


from urllib import request
import sys
if __name__ == "__main__":
    import urllib.error
    try:
        with request.urlopen(sys.argv[1]) as req:
            print(req.read().decode())
    except urllib.error.URLError as e:
        print(f'Error code: {e.code}')
