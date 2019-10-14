#!/usr/bin/python3
""" N Queens file """


class nQueens:
    def __init__(self, n):
        """ sets variable"""
        self.n = n

    def play(self, n):
        chess_board = [[0 for i in range(n)] for y in range(n)]
        for i in range(n):
            self.solve(chess_board, i)

    def solve(self, c_board, column):
        """ recursive solve """
        for row in range(self.n):
            if column >= self.n:
                if self.check_queens(c_board):
                    self.matrix_to_list(c_board)
                    return
            else:
                c_board[row][column] = 1

            if (self.safety_check(c_board, row, column)):
                self.solve(c_board, column + 1)
            if column >= self.n:
                return
            c_board[row][column] = 0

    def matrix_to_list(self, c_board):
        q_list = []
        for i in range(len(c_board)):
            for j in range(len(c_board)):
                if c_board[i][j] == 1:
                    q_list.append([j, i])
        print(q_list)

    def check_queens(self, c_board):
        count = 0
        for i in range(len(c_board)):
            for j in range(len(c_board)):
                if c_board[i][j] == 1:
                    count += 1
        if count == len(c_board):
            return True

    def safety_check(self, c_board, row, column):
        count_a = 0
        count_b = 0
        for i in c_board[row]:
            if i == 1:
                count_a += 1
            if count_a == 2:
                return False
        for r in c_board:
            count = 0
            for item in r:
                if count == column:
                    if item == 1:
                        count_b += 1
                    if count_b == 2:
                        return False
                count += 1
        for i in range(len(c_board)):
            for j in range(len(c_board)):
                if c_board[i][j] == 1:
                    height = row - i
                    width = column - j
                    if width != 0:
                        slope = abs(height / width)
                        if slope == 1:
                            return False
        if column == len(c_board):
            exit(1)
        return True

    @property
    def n(self):
        return self.__n

    @n.setter
    def n(self, value):
        if value < 4:
            print("N must be at least 4")
            exit(1)
        self.__n = value

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        n = int(sys.argv[1])
    except:
        print("N must be a number")
        exit(1)

    nQueens = nQueens(n)
    nQueens.play(n)
