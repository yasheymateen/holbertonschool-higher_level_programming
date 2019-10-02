#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    for item in my_list:
        if i in range(x):
            try:
                print(item, end='')
                i += 1
            except:
                break
    print('')
    return i
