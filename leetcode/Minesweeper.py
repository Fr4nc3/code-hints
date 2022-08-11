# Let's play the minesweeper game (Wikipedia, online game)!

# You are given an m x n char matrix board representing the game board where:

# 'M' represents an unrevealed mine,
# 'E' represents an unrevealed empty square,
# 'B' represents a revealed blank square that has no adjacent mines (i.e., above, below, left, right, and all 4 diagonals),
# digit ('1' to '8') represents how many mines are adjacent to this revealed square, and
# 'X' represents a revealed mine.
# You are also given an integer array click where click = [clickr, clickc] represents the next click position among all the unrevealed squares ('M' or 'E').

# Return the board after revealing this position according to the following rules:

# If a mine 'M' is revealed, then the game is over. You should change it to 'X'.
# If an empty square 'E' with no adjacent mines is revealed, then change it to a revealed blank 'B' and all of its adjacent unrevealed squares should be revealed recursively.
# If an empty square 'E' with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
# Return the board when no more squares will be revealed.

class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        def findMines(neighbours):
            mineCount = 0
            for r,c in neighbours:
                if board[r][c] == 'M':
                    mineCount += 1
            return mineCount
            
        def getNeighbours(row,col,board):
            neighbours = []
            if row > 0 and board[row-1][col] in ['E','M']:
                neighbours.append([row-1,col])
            if row < len(board)-1 and board[row+1][col] in ['E','M']:
                neighbours.append([row+1,col])
            if col > 0 and board[row][col-1] in ['E','M']:
                neighbours.append([row,col-1])
            if col < len(board[0])-1 and board[row][col+1] in ['E','M']:
                neighbours.append([row,col+1])
                
            if row > 0 and col > 0 and board[row-1][col-1] in ['E','M']:
                neighbours.append([row-1,col-1])
            if row < len(board)-1 and col < len(board[0])-1 and board[row+1][col+1] in ['E','M']:
                neighbours.append([row+1,col+1])
            if row > 0 and col < len(board[0])-1 and board[row-1][col+1] in ['E','M']:
                neighbours.append([row-1,col+1])
            if row < len(board)-1 and col > 0 and board[row+1][col-1] in ['E','M']:
                neighbours.append([row+1,col-1])
            return neighbours
            
        def dfs(row,col,board,mineFound):
            if mineFound:
                return 
            elif board[row][col] == 'M':
                board[row][col] = 'X'
                mineFound = True
            else:
                neighbours = getNeighbours(row,col,board)
                totalMines = findMines(neighbours)
                if totalMines > 0:
                    board[row][col] = str(totalMines)
                else:
                    board[row][col] = 'B'
                    for r,c in neighbours:
                        dfs(r,c,board,mineFound)
        dfs(click[0],click[1],board,False)
        return board