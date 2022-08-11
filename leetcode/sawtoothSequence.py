# A sawtooth sequence is a sequence of numbers that alternate between increasing and decreasing. In other words, each element is either strictly greater than its neighbouring elements or strictly less than its neighbouring elements.

# examples

# Given an array of integers arr, your task is to count the number of contiguous subarrays that represent a sawtooth sequence of at least two elements.

# Example

# For arr = [9, 8, 7, 6, 5], the output should be solution(arr) = 4.

# Since all the elements are arranged in decreasing order, it won't be possible to form any sawtooth subarrays of length 3 or more. There are 4 possible subarrays containing two elements, so the answer is 4.

# For arr = [10, 10, 10], the output should be solution(arr) = 0.

# Since all of the elements are equal, none of subarrays can be sawtooth, so the answer is 0.

# For arr = [1, 2, 1, 2, 1], the output should be solution(arr) = 10.

# All contiguous subarrays containing at least two elements satisfy the condition of problem. There are 10 possible contiguous subarrays containing at least two elements, so the answer is 10.

# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] array.integer arr

# An array of integers.

# Guaranteed constraints:
# 2 ≤ arr.length ≤ 105,
# -109 ≤ arr[i] ≤ 109.

# [output] integer64

# Return the number of sawtooth subarrays.

# [Python 3] Syntax Tips
def solution(arr):
    saws = [0 for x in range(0, len(arr))]
    # the resulting total sawtooth counts
    totalSawCounts = 0
    previousCount = 0

    for currIdx in range(1, len(arr)):
        currCount = 0
        before = currIdx -1
        if (arr[currIdx] > arr[before]):
            goingUp = True
        elif (arr[currIdx] < arr[before]):
            goingUp = False
        else:
            break

        # if we made it here, we have at least one sawtooth
        currCount =  1

        # see if there was a previous solution (the DP part)
        # and if it continues our current sawtooth
        if before >= 1:
            if goingUp:
                if arr[before-1] > arr[before]:
                    currCount = previousCount + currCount
            else:
                if arr[before-1] < arr[before]:
                    currCount = previousCount + currCount
        previousCount = currCount
        totalSawCounts = totalSawCounts + currCount

    return totalSawCounts