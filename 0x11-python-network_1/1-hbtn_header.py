#!/usr/bin/python3
""" Script that takes in URL and sends equest to the URL and displays the value
of x request id
"""
import sys
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        headers = response.info()
        print(headers.get('X-Request-Id'))
