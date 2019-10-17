#!/usr/bin/python3
""" Read File """


def read_file(filename=""):
    """ reads text file and prints """
    with open(filename, encoding='utf-8') as f:
        print(f.read())
