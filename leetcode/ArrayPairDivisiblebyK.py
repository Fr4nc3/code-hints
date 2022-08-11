# 1497. Check If Array Pairs Are Divisible by k

# Given an array of integers arr of even length n and an integer k.

# We want to divide the array into exactly n / 2 pairs such that the sum of each pair is divisible by k.

# Return true If you can find a way to do that or false otherwise.

 

# Example 1:

# Input: arr = [1,2,3,4,5,10,6,7,8,9], k = 5
# Output: true
# Explanation: Pairs are (1,9),(2,8),(3,7),(4,6) and (5,10).
# Example 2:

# Input: arr = [1,2,3,4,5,6], k = 7
# Output: true
# Explanation: Pairs are (1,6),(2,5) and(3,4).
# Example 3:

# Input: arr = [1,2,3,4,5,6], k = 10
# Output: false
# Explanation: You can try all possible pairs to see that 
# there is no way to divide arr into 3 pairs each with sum divisible by 10.

class Solution(object):
    def canArrange(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: bool
        """
        count_of_pairs = [0]*k  #Create an array of length k. Use this to track the pairs.
        
        #For each element in input array, calculate it's modulo with k.
        #Use the modulo value as index to increment value in count_of_pairs.
        for _, ele in enumerate(arr):
            count_of_pairs[ele%k] += 1 
        
        if count_of_pairs[0] >0 and count_of_pairs[0]%2 !=0:
            return False      #Count of numbers with modulo=0 should be even.
            
        #Using k=5, count at index 1 and index 4 of count_of_pairs should be same.
        #Using k=6, count at index 3 should be even.
        left = 1
        right = k-1
        while left <= right:
            if left != right and count_of_pairs[left] != count_of_pairs[right]:
                return False
            elif left == right and count_of_pairs[left]%2 != 0:
                return False
            left += 1
            right -= 1
            
        return True