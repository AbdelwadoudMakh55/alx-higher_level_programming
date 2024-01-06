#!/usr/bin/python3
""" This is the 7-error_code.py module """


import requests
import sys
if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    if (r.status_code >= 400):
        print(f'Error code: {r.status_code}')
    else:
        print(r.text)
