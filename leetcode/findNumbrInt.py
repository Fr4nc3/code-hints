# Given an array of distinct integers a, your task is to find the number of pairs of indices (i, j) such that i ≤ j and the sum a[i] + a[j] is equal to some power of two.

# Note: numbers 20 = 1, 21 = 2, 22 = 4, 23 = 8, etc. are considered to be powers of two.

# Example

# For a = [1, -1, 2, 3], the output should be solution(a) = 5.
# There is one pair of indices where the corresponding elements sum up to 20 = 1:
# (1, 2): a[1] + a[2] = -1 + 2 = 1.
# There are two pairs of indices where the corresponding elements sum up to 21 = 2:
# (0, 0): a[0] + a[0] = 1 + 1 = 2;
# (1, 3): a[1] + a[3] = -1 + 3 = 2.
# There are two pairs of indices where the corresponding elements sum up to 22 = 4:
# (0, 3): a[0] + a[3] = 1 + 3 = 4;
# (2, 2): a[2] + a[2] = 2 + 2 = 4;
# In total, there are 1 + 2 + 2 = 5 pairs summing up to powers of two.
# For a = [2], the output should be solution(a) = 1.
# The only pair of indices is (0, 0) and the sum of corresponding elements is equal to 22 = 4. So the answer is 1.
# For a = [-2, -1, 0, 1, 2], the output should be solution(a) = 5.
# There are two pairs of indices where the corresponding elements sum up to 20 = 1: (2, 3) and (1, 4).
# There are two pairs of indices where the corresponding elements sum up to 21 = 2: (2, 4) and (3, 3).
# There is one pair of indices where the corresponding elements sum up to 22 = 4: (4, 4).
# In total, there are 2 + 2 + 1 = 5 pairs summing up to powers of two.
def solution(a):
    n = len(a)
    m = {}
    arr = a
 
    for i in range(n):
        m[arr[i]] = m.get(arr[i], 0) + 1

    ans = 0
 
    for i in range(31):
         
        key = int(pow(2, i))

        for j in range(n):
            k = key - arr[j]
 
            if k not in m:
                continue
 
            else:
                ans += m.get(k, 0)
 
            if (k == arr[j]):
                ans += 1
 
    return ans // 2