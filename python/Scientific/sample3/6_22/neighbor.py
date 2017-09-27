# *************************************
# @Fr4nc3
# 03/06/2015
# file: neighbor.py
# implements methods neighbor_average, neighbors
# ************************************


def neighbor_average(values, row, column):
    ''' computes the average of the neighbor of a table '''
    if row >= len(values) or column >= len(values[0]):
        exit("out of range")

    a = neighbors(values, row, column)
    return sum(a) / len(a)


def neighbors(values, row, column):
    """computes the  neighbor of a given position """
    #calculate limits
    startRow = row if (row - 1 < 0) else row - 1
    startColumn = column if (column - 1 < 0) else column - 1
    endRow = row if (row + 1 > len(values) - 1) else row + 1
    endColumn = column if (column + 1 > len(values[0]) - 1) else column + 1
    a = []  # storage the neighbors
    for rowNum in range(startRow, endRow + 1):
        for colNum in range(startColumn, endColumn + 1):
            if not (rowNum == row and colNum == column):
                a.append(values[rowNum][colNum])

    return a




