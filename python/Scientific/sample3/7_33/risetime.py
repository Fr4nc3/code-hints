# *************************************
# @Fr4nc3
# 03/06/2015
# file: risetime.py
# *************************************


def read_file(file_name):
    '''read a file line by line and return it as a list'''
    in_file = open(file_name)
    a = []

    try:
        for line in in_file.readlines():
            a.append(line.rstrip())  # remove extra spaces
    finally:
        in_file.close()

    return a


def rise_time(B, V_1):
    ''' calculate if V_1 is closet to 0.05B and 0.95B'''
    if V_1 > 0.05 * B or V_1 < 0.95 * B:
        return True
    else:
        return False

