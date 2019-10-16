#!/usr/bin/python3
""" returns true if object is an instance """


def is_same_class(obj, a_class):
    """ checks object """
    if dir(obj) == dir(a_class):
        return True
    return False
