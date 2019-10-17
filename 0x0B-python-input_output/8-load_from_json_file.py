#!/usr/bin/python3
""" creates an object from json file """


def load_from_json_file(filename):
    """ creating object"""
    with open(filename, mode='r') as f:
        return json.load(f)
