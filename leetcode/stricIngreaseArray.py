# You are given an array of non-negative integers numbers. You are allowed to choose any number from this array and swap any two digits in it. If after the swap operation the number contains leading zeros, they can be omitted and not considered (eg: 010 will be considered just 10).

# Your task is to check whether it is possible to apply the swap operation at most once, so that the elements of the resulting array are strictly increasing.

# Example

# For numbers = [1, 5, 10, 20], the output should be solution(numbers) = true.

# The initial array is already strictly increasing, so no actions are required.

# For numbers = [1, 3, 900, 10], the output should be solution(numbers) = true.

# By choosing numbers[2] = 900 and swapping its first and third digits, the resulting number 009 is considered to be just 9. So the updated array will look like [1, 3, 9, 10], which is strictly increasing.

# For numbers = [13, 31, 30], the output should be solution(numbers) = false.

# The initial array elements are not increasing.
# By swapping the digits of numbers[0] = 13, the array becomes [31, 31, 30] which is not strictly increasing;
# By swapping the digits of numbers[1] = 31, the array becomes [13, 13, 30] which is not strictly increasing;
# By swapping the digits of numbers[2] = 30, the array becomes [13, 31, 3] which is not strictly increasing;
# So, it's not possible to obtain a strictly increasing array, and the answer is false.

# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] array.integer numbers

# An array of non-negative integers.

# Guaranteed constraints:
# 1 ≤ numbers.length ≤ 103,
# 0 ≤ numbers[i] ≤ 103.

def solution(numbers):
    swapped = False
    for i in range(len(numbers)-1):
        if numbers[i] >= numbers[i+1]:
            if swapped: return False

            s = str(numbers[i])
            ss = sorted(s)
            si = int(''.join(ss))
            if si < numbers[i+1]:
                if i > 0 and si > numbers[i-1]: 
                    numbers[i] = si
                    swapped = True
                    continue

            s = str(numbers[i+1])
            ss = sorted(s, reverse = True)
            si = int(''.join(ss))
            if si > numbers[i]: 
                numbers[i+1] = si
                swapped = True
                continue

    return True
