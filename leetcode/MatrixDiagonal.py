# Given a matrix of integers, we'd like to consider the sum of the elements within the area of a 45°
# rotated rectangle. More formally, the area is bounded by two diagonals parallel to the main diagonal 
# and two diagonals parallel to the secondary diagonal. The dimensions of the rotated rectangle are defined 
# by the number of elements along the borders of the rectangle.


# Given integers a and b representing the dimensions of the rotated rectangle, 
# and matrix (a matrix of integers), your task is to find the greatest sum of integers 
# contained within an a x b rotated rectangle.

# Note: The order of the dimensions is not important - consider all a x b and b x a rectangles.

# Example
# a = 2, and b = 3, the output should be solution(matrix, a, b) = 36.
# For

# matrix = [[1, 2, 3, 4, 0],
#           [5, 6, 7, 8, 1],
#           [3, 2, 4, 1, 4],
#           [4, 3, 5, 1, 6]]


def solution(matrix, a, b):
    result = 0
    n = b
    m = a
    ctr = 0

    li = matrix
    while(ctr < 2 * n-1):
        lst = []
        # Iterate [0, m]
        for i in range(m):
                # Iterate [0, n]
            for j in range(n):

                # Diagonal Elements
                # Condition
                if i + j == ctr:
                    # Appending the
                    # Diagonal Elements
                    lst.append(li[i][j])
        
        ctr += 1
    print(ctr)
    return sum(lst)
    
    m = len(matrix)
    n = len(matrix[0])
    maxSum = float('-inf')
    # If we make a diagnoal line at the current index a and b represents
    # the number of element we can to include with respect to that line.
    # Since we have at least 1 element by being on an index, we subtract
    # 1 from both a and b to represent the index
    for x,y in ((a-1,b-1),(b-1,a-1)):
        # Slide through possible rectangles
        for row_min in range(0, m - x - y):
            for col_min in range(0, n - x - y):
                # Find sum of rectangle
                rec_sum = matrix[row_min][col_min+x]
                corner_left  = [row_min+x,col_min]
                corner_right = [row_min+y,col_min+x+y]
                j_min_step = -1
                j_max_step = 1
                # Start with top corner
                prev_index_left = prev_index_right = [row_min,col_min+x]
                for i in range(row_min+1,row_min+x+y+1):
                    j_min_step = j_min_step * -1 if prev_index_left == corner_left else j_min_step
                    j_max_step = j_max_step * -1 if prev_index_right == corner_right else j_max_step
                    j_min = prev_index_left[1] + j_min_step
                    j_max = prev_index_right[1] + j_max_step
                    for j in range (j_min,j_max+1):
                        rec_sum += matrix[i][j]
                    prev_index_left = [i, j_min]
                    prev_index_right = [i, j_max]
                maxSum = rec_sum if rec_sum > maxSum else maxSum
    
    return maxSum

def rotatedRectSum(grid, a, b):
    if a + b - 1 > min(len(grid), len(grid[0])):
        return 0

    ret = 0
    for w, h in ((a, b), (b, a)):
        # for every possible leftmost axb/bxa rectangle...
        for start in range(min(len(grid), len(grid[0])) - (a + b - 1) + 1):
            i = start
            cur = 0
            deques = []
            j1 = j2 = w - 1
            # build the rectangle 
            while j1 <= j2:
                for k in range(j1, j2 + 1):
                    cur += grid[i][k]
                deques.append((j1, j2)) 
                j1 += (-1 if i - start < w - 1 else 1)
                j2 += (1 if i - start < h - 1 else -1)
                i += 1
            
            stop = False
            # slide it to the right until you can't anymore
            while True:
                ret = max(ret, cur)
                
                for ind, tup in enumerate(deques):
                    j1, j2 = tup
                    i = start + ind
                    if j2 == len(grid[0]) - 1:
                        stop = True
                        break
                    j2 += 1
                    cur += grid[i][j2] - grid[i][j1]
                    j1 += 1
                    deques[ind] = (j1, j2)

                if stop:
                    break
    
    return ret