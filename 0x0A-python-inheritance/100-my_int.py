#!/usr/bin/python3
""" myint class """


class MyInt(int):
    """ my int class"""

    def __equal__(self, other):
        """ equals """
        return False

    def __notequal__(self, other):
        """ not equal """
        return True
    
