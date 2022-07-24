# Given an array of integers a, your task is to calculate the digits that occur the most number of times in the array. 
# Return the array of these digits in ascending order.

# Example

# For a = [25, 2, 3, 57, 38, 41], the output should be solution(a) = [2, 3, 5].

# Here are the number of times each digit appears in the array:

# 0 -> 0
# 1 -> 1
# 2 -> 2
# 3 -> 2
# 4 -> 1
# 5 -> 2
# 6 -> 0
# 7 -> 1
# 8 -> 1
# The most number of times any number occurs in the array is 2, 
# and the digits which appear 2 times are 2, 3 and 5. So the answer is [2, 3, 5].

from collections import defaultdict
import operator

def solution(a):
        numCount = defaultdict(list)
        
        for e in a:
            e_s = str(e)
            for ei in e_s: 
                i = int(ei)
                if i in numCount.keys():
                    numCount[i] +=1
                else:
                    numCount[i] = 1
        sorted_d = dict(sorted(numCount.items(),  key=lambda kv:
                 (kv[1], kv[0]), reverse=True)) # dict(sorted(numCount.items(), key=operator.itemgetter(1),reverse=True))
        asw = []
        i =0
        print(sorted_d)
        for k, v in sorted_d.items():

            if v >= i:
                i = v
                asw.append(k)
            
        
        return sorted(asw)

