#!/usr/bin/python3
""" This is the 7-error_code.py module """


import requests
import sys
if __name__ == "__main__":
    try:
        r = requests.get(sys.argv[1])
        print(r.text)
    except requests.exceptions.RequestException as e:
        print(f'Error code: {e.response.status_code}')
