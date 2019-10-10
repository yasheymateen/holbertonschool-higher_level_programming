#!/usr/bin/python3
""" Locked Class Module """


class LockedClass:
    """ prevents user from creating new instance attributes """

    __slots__ = ['first_name']

    def __init__(self, fn=""):
        self.first_name = fn
