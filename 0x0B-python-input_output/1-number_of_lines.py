#!/usr/bin/python3
""" returns number of lines in text file """


def number_of_lines(filename=""):
    """ number of lines """
    l_count = 0
    with open(filename) as f:
        for line in f:
            l_count += 1
    return l_count
