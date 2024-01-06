#!/usr/bin/python3
""" This is the 0-hbtn_status module """


from urllib import request
with request.urlopen('https://alx-intranet.hbtn.io/status') as resp:
    content = resp.read()
    print("Body response:")
    print(f"\t- type: {type(content)}")
    print(f"\t- content: {content}")
    print(f"\t- utf8 content: {content.decode()}")
