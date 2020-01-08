#!/usr/bin/python3
# Find a peak in a list of unsorted integers


def find_peak(list_of_integers):
    """Find a peak in a list of unsorted integers """
    int_list = list_of_integers
    if int_list is None or len(int_list) == 0:
        return None
    length = len(int_list)
    midpoint = length // 2
    if length > 2:
        if int_list[midpoint-1] < int_list[midpoint] > int_list[midpoint+1]:
            return int_list[midpoint]
        else:
            if int_list[midpoint - 1] > int_list[midpoint + 1]:
                return find_peak(int_list[:midpoint+1])
            else:
                return find_peak(int_list[midpoint:])
    else:
        if int_list[midpoint-1] > int_list[midpoint]:
            return int_list[midpoint-1]
        else:
            return int_list[midpoint]
