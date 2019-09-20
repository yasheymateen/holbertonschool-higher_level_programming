#!/usr/bin/python3
def roman_to_int(roman_string):
    my_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    value = 0
    num = 0
    numeral = roman_string
    if type(roman_string) is not str:
        return 0
    if roman_string is None:
        return 0
    for num in range (num, len(numeral)):
        if num < len(numeral) - 1 and my_dict[numeral[num]] < my_dict[numeral[num + 1]]:
            value -= my_dict[numeral[num]]
        else:
            value += my_dict[numeral[num]]
    return value
