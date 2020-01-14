#!/usr/bin/python3
"""Takes in a URL, sends request to  URL, displays the body of the response
"""
if __name__ == "__main__":
    import urllib.request as ur
    import urllib.error as ure
    from sys import argv
    req = ur.Request(argv[1])

    try:
        with ur.urlopen(req) as response:
            print(str(response.read(), 'utf-8'))
    except ure.HTTPError as err:
        print('Error code: {}'.format(err.getcode()))
