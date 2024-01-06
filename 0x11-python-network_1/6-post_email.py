#!/usr/bin/python3
""" This is the 6-post_email module """


import requests
import sys
if __name__ == "__main__":
    r = requests.post(sys.argv[1], json={'email': sys.argv[2]})
    print(r.text)
