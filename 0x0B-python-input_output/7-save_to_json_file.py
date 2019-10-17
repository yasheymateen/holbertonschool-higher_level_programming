#!/usr/bin/python3
""" writes object to text file """


import json


def save_to_json_file(my_obj, filename):
    """ save to json """
    with open(filename, mode'w') as f:
        f.write(json.dumps(my_obj)
