#!/usr/bin/python3
""" takes in URL and email and sends POST requestto passed url as parameter and
displays body of the response
"""
import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    r = requests.post(url, data={'email': email})
    print(r.text)
