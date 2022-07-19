#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    plus = 0
    minus = 0
    zero = 0
    n = len(arr)
    for i in arr:
        if i >0:
            plus+=1
        elif i <0:
            minus+=1
        else:
            zero+=1
    print("{:.6f}".format(plus/n))
    print("{:.6f}".format(minus/n))
    print("{:.6f}".format(zero/n))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
