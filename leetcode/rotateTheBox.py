# 1861. Rotating the Box

# You are given an m x n matrix of characters box representing a side-view of a box. Each cell of the box is one of the following:

# A stone '#'
# A stationary obstacle '*'
# Empty '.'
# The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity. Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. Gravity does not affect the obstacles' positions, and the inertia from the box's rotation does not affect the stones' horizontal positions.

# It is guaranteed that each stone in box rests on an obstacle, another stone, or the bottom of the box.

# Return an n x m matrix representing the box after the rotation described above.

# Input: box = [["#",".","#"]]
# Output: [["."],
#          ["#"],
#          ["#"]]


#  public char[][] rotateTheBox(char[][] box) {
#         int m = box.length, n = box[0].length;
#         char[][] res = new char[n][m];
#         for(int i = 0; i < m; i++) {
#             for(int j = n-1, k = n-1; j >= 0; j--) {
#                 res[j][m-1-i] = '.';
#                 if(box[i][j] != '.') {
#                     if(box[i][j] == '*') {
#                         k = j;
#                     }
#                     res[k--][m-1-i] = box[i][j];
#                 }
#             }
#         }
#         return res;
class Solution(object):
    def rotateTheBox(self, box):
        n, m = len(box), len(box[0])
        
        for row in box:
            move_position = m - 1
            for j in range(m - 1, -1, -1):
                if row[j] == '*':
                    move_position = j - 1
                elif row[j] == '#':
                    swap(row, move_position, j)
                    move_position -= 1

        return rotate_90(box)

def swap(row, i, j):
    temp = row[i]
    row[i] = row[j]
    row[j] = temp
    
def rotate_90(box):
    n, m = len(box), len(box[0])
    
    ans = [[None] * n for _ in range(m)]
    
    for x in range(n):
        for y in range(m):
            ans[y][n - 1 - x] = box[x][y]
            
    return ans