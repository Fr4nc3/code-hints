from collections import defaultdict


class Solution(object):
    def restoreArray(self, adjacentPairs):
        """
        :type adjacentPairs: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        numToAdjs = defaultdict(list)

        for a, b in adjacentPairs:
          numToAdjs[a].append(b)
          numToAdjs[b].append(a)
        print(numToAdjs)
        print(numToAdjs.items())
        for num, adjs in numToAdjs.items():
          if len(adjs) == 1:
            ans.append(num)
            ans.append(adjs[0])
            break

        while len(ans) < len(adjacentPairs) + 1:
          tail = ans[-1]
          prev = ans[-2]
          adjs = numToAdjs[tail]
          if adjs[0] == prev:  # adjs[0] is already used
            ans.append(adjs[1])
          else:
            ans.append(adjs[0])

        return ans
    
    
# Example 1:

# Input: adjacentPairs = [[2,1],[3,4],[3,2]]
# Output: [1,2,3,4]
# Explanation: This array has all its adjacent pairs in adjacentPairs.
# Notice that adjacentPairs[i] may not be in left-to-right order.
# Example 2:

# Input: adjacentPairs = [[4,-2],[1,4],[-3,1]]
# Output: [-2,4,1,-3]
# Explanation: There can be negative numbers.
# Another solution is [-3,1,4,-2], which would also be accepted.
# Example 3:

# Input: adjacentPairs = [[100000,-100000]]
# Output: [100000,-100000]
