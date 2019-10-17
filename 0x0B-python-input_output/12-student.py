#!/usr/bin/python3
"""Student module"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Initialize Student instance with first,last,age """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary represt """

        is_list_of_strings = True
        if type(attrs) is not list:
            is_list_of_strings = False
        else:
            for i in attrs:
                if type(i) != str:
                    is_list_of_strings = False
        if not is_list_of_strings:
            return self.__dict__
        else:
            return_val = {}
            for attr in attrs:
                if attr in self.__dict__:
                    return_val[attr] = self.__dict__.get(attr)
            return return_val
