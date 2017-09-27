# *************************************
# @Fr4nc3
# 03/06/2015
# file: circuit.py
# *************************************
import math


def capacitator_voltage(B, R, C, t):
    ''' calculate capacitator voltage '''
    return B * (1 - math.e ** (- t / (R * C)))


def read_file(file_name):
    ''' read a file line by line and stored in an list '''
    in_file = open(file_name)
    a = []
    try:
        for line in in_file.readlines():
            a.append(line.rstrip())  # remove extra spaces
    finally:
        in_file.close()

    return a
