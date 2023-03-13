from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        def dfs(row, col):
            if 0 <= row < ROWS and 0 <= col < COLS and board[row][col] == "O":
                board[row][col] = "T"
                dfs(row + 1, col)
                dfs(row - 1, col)
                dfs(row, col + 1)
                dfs(row, col - 1)                
        for row in range(ROWS):
            dfs(row, 0)
            dfs(row, COLS - 1)
        for col in range(COLS):
            dfs(0, col)
            dfs(ROWS - 1, col)
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "T":
                    board[row][col] = "O"
                elif board[row][col] == "O":
                    board[row][col] = "X"
        
            
        
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
obj = Solution()
obj.solve(board)
print(board)