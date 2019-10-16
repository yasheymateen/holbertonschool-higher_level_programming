#!/usr/bin/python3
""" returns true if obj is instance of class inherited directly"""


def inherits_from(obj, a_class):
    """ True if so """
    if type(obj) == a_class:
        return False
    return isinstance(obj, a_class)
