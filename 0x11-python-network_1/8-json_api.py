#!/usr/bin/python3
"""Takes in a letter and sends POST  request to http://0.0.0.0:5000/search_user
with letter as a parameter
"""
import requests
import sys

if __name__ == '__main__':
    url = 'http://831dbdfb081b.41.hbtn-cod.io:5000/search_user'
    if len(sys.argv) == 1:
        letter = ""
    else:
        letter = sys.argv[1]
    r = requests.post(url, data={'q': letter})
    try:
        instance = r.json()
        if not instance:
            print("No result")
        else:
            print("[{}] {}".format(instance.get('id'), instance.get('name')))
    except:
        print("Not a valid JSON")
