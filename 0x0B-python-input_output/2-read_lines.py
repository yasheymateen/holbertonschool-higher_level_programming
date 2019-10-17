#!/usr/bin/python3
""" reads n lines of text file """


def read_lines(filename="", nb_lines=0):
    """ read lines funct """
    l_count = 0
    with open(filename, encoding = 'utf-8') as f:
        if nb_lines <= 0:
            print(f.read(), end='')
        for line in f:
            if l_count < nb_lines:
                print(line, end='')
                l_count += 1
