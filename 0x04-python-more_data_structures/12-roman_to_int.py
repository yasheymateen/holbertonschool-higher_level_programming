#!/usr/bin/python3
def roman_to_int(roman_string):
    dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    value = 0
    num = 0
    numer = roman_string
    if type(roman_string) is not str:
        return 0
    if roman_string is None:
        return 0
    for num in range(num, len(numer)):
        if num < len(numer) - 1 and dict[numer[num]] < dict[numer[num + 1]]:
            value -= dict[numer[num]]
        else:
            value += dict[numer[num]]
    return value
