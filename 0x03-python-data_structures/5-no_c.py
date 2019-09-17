#!/usr/bin/python3
def no_c(my_string):
    my_string = list(my_string)
    try:
        my_string.remove('c')
    except ValueError:
        pass
    try:
        my_string.remove('C')
    except ValueError:
        pass
    my_string = ''.join(my_string)
    return (my_string)
