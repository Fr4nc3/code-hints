
# 1878. Get Biggest Three Rhombus Sums in a Grid

# A rhombus sum is the sum of the elements that form the border of a regular rhombus shape in grid​​​. 
# The rhombus must have the shape of a square rotated 45 degrees with each of the corners centered in a grid cell. Below is an image of four valid rhombus shapes with the corresponding colored cells that should be included in each rhombus sum:


# Note that the rhombus can have an area of 0, which is depicted by the purple rhombus in the bottom right corner.

# Return the biggest three distinct rhombus sums in the grid in descending order. 
# If there are less than three distinct values, return all of them.

 

# Example 1:


# Input: grid = [[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]
# Output: [228,216,211]
# Explanation: The rhombus shapes for the three biggest distinct rhombus sums are depicted above.
# - Blue: 20 + 3 + 200 + 5 = 228
# - Red: 200 + 2 + 10 + 4 = 216
# - Green: 5 + 200 + 4 + 2 = 211
# Example 2:


# Input: grid = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [20,9,8]
# Explanation: The rhombus shapes for the three biggest distinct rhombus sums are depicted above.
# - Blue: 4 + 2 + 6 + 8 = 20
# - Red: 9 (area 0 rhombus in the bottom right corner)
# - Green: 8 (area 0 rhombus in the bottom middle)
# Example 3:

# Input: grid = [[7,7,7]]
# Output: [7]
# Explanation: All three possible rhombus sums are the same, so return [7].
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# 1 <= grid[i][j] <= 105
# Accepted
# 10,336
# Submissions

import heapq


class Solution(object):
    def getBiggestThree(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """	
        K = 3
        left = [[grid[i][j] for j in xrange(len(grid[i]))] for i in xrange(len(grid))]
        right = [[grid[i][j] for j in xrange(len(grid[i]))] for i in xrange(len(grid))]
        for i in xrange(1, len(grid)):
            for j in xrange(len(grid[0])-1):
                left[i][j] += left[i-1][j+1]
        for i in xrange(1, len(grid)):
            for j in xrange(1, len(grid[0])):
                right[i][j] += right[i-1][j-1]
        min_heap = []
        lookup = set()
        for k in xrange((min(len(grid), len(grid[0]))+1)//2):
            for i in xrange(k, len(grid)-k):
                for j in xrange(k, len(grid[0])-k):
                    total = (((left[i][j-k]-left[i-k][j])+(right[i][j+k]-right[i-k][j])+grid[i-k][j]) +  
                             ((left[i+k][j]-left[i][j+k])+(right[i+k][j]-right[i][j-k])-grid[i+k][j])) if k else grid[i][j]
                    if total in lookup:
                        continue
                    lookup.add(total)
                    heapq.heappush(min_heap, total)
                    if len(min_heap) == K+1:                        
                        lookup.remove(heapq.heappop(min_heap))
        min_heap.sort(reverse=True)
        return min_heap