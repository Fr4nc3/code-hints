class Solution(object):
    def twoSumLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        answer = -1
        left = 0
        right = len(nums) -1
        while left < right:
            sum = nums[left] + nums[right]
            if (sum < k):
                answer = max(answer, sum)
                left += 1
            else:
                right -= 1
        return answer
    
# You are given an array of integers a and an integer k. 
# Your task is to calculate the number of ways to pick two different indices i < j, such that a[i] + a[j] is divisible by k.

# Example

# For a = [1, 2, 3, 4, 5] and k = 3, the output should be solution(a, k) = 4.

# There are 4 pairs of numbers that sum to a multiple of k = 3:

# a[0] + a[1] = 1 + 2 = 3
# a[0] + a[4] = 1 + 5 = 6
# a[1] + a[3] = 2 + 4 = 6
# a[3] + a[4] = 4 + 5 = 9

def solution(a, k):
    K=k
    freq = [0] * K
    n = len(a)
    A =a
     
    # Count occurrences of all remainders
    for i in range(n):
        freq[A[i] % K]+= 1
         
    # If both pairs are divisible by 'K'
    sum = freq[0] * (freq[0] - 1) / 2;
     
    # count for all i and (k-i)
    # freq pairs
    i = 1
    while(i <= K//2 and i != (K - i) ):
        sum += freq[i] * freq[K-i]
        i+= 1
 
    # If K is even
    if( K % 2 == 0 ):
        sum += (freq[K//2] * (freq[K//2]-1)/2);
     
    return int(sum)
