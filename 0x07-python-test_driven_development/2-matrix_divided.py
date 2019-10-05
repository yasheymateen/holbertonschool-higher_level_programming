#!/usr/bin/python3
""" matrix_divided module"""


def matrix_divided(matrix, div):
    """ function that divides all elements of matrix"""

    def check_size(matrix):
        size = len(matrix[0])
        for i in range(1, len(matrix)):
            if len(matrix[i]) != size:
                return False
        return True

    def list_checker(matrix):
        if matrix is None:
            return False
        for row in matrix:
            if type(row) is not list:
                return False
            for i in row:
                if type(i) is not int and type(i) is not float:
                   return False
        return True

    if matrix == [[]] or matrix == []:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if check_size(matrix) is False:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if check_size(matrix) is False:
        raise TypeError("Each row of the matrix must have the same size")
    if div is None or (type(div) is not int and type(div) is not float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(i/div, 2) for i in row] for row in matrix]
