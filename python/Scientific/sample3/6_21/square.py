# *************************************
# @Fr4nc3
# 03/06/2015
# file: square.py
# magic_square implemented for odd numbers
# *************************************


def magic_square(n):
    """implement magic square algorithm."""
    if n % 2 == 0:
        exit("Only odd numbers")

    row = n - 1
    column = int(n / 2)
    square = [[0 for i in range(n)] for j in range(n)]  # square with zeros

    for k in range(1, n * n + 1):  # add 1 to complete the range
        square[row][column] = k
        row += 1
        column += 1

        if row == n:
            row = 0
        if column == n:
            column = 0

        if square[row][column] != 0:
            row -= 1
            column -= 1
            row -= 1

    for r in square:
        print(r)

