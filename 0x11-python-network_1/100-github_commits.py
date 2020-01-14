#!/usr/bin/python3
""" list 10 commits from the recent to the oldest of the repository "rails" by
the user rails. You must use the github API
"""
import requests
import sys


def commitDate(coms):
    """ helper function to sort github commit """
    return coms.get("commit").get("author").get("date")

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)

    r = requests.get(url)
    try:
        result = r.json()
    except:
        print("Not a valid JSON")
    result.sort(key=commitDate, reverse=True)

    try:
        for i in range(10):
            sha = result[i].get("sha")
            name = result[i].get("commit").get("author").get("name")
            print("{}: {}".format(sha, name))
    except:
        pass
