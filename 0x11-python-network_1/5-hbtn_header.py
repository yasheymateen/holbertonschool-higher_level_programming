#!/usr/bin/python3
"""Takes in a URL, sends request to URL, & displays value of var X-RequestId
"""
import requests
import sys
if __name__ == '__main__':
    url = sys.argv[1]
    r = requests.get(url)
    print(r.headers.get('X-Request-Id'))
