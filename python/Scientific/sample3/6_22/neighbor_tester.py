# *************************************
# @Fr4nc3
# 03/06/2015
# file: neighbor_tester.py
# test average neighbor
# *************************************

import neighbor


def main():
    '''test average neighbors '''
    neighbors = [[1, 7, 8, 9, 10],
                 [10, 15, 14, 17, 0],
                 [20, 11, 31, 21, 81],
                 [30, 41, 21, 51, 70],
                 [40, 60, 18, 19, 90]]
    a = neighbor.neighbor_average(neighbors, 0, 0)
    print('computes neighbor average %.3f ' % a)
    a = neighbor.neighbor_average(neighbors, 3, 3)
    print('computes neighbor average %.3f ' % a)
    a = neighbor.neighbor_average(neighbors, 4, 4)
    print('computes neighbor average %.3f ' % a)


main()