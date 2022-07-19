#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    array_sum = sum(arr)
    minNum = math.inf
    maxNum = -math.inf
    for i in arr:
        temp = array_sum-i
        minNum = min(temp, minNum)
        maxNum = max(temp, maxNum)
    
    print (minNum, maxNum)
    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
