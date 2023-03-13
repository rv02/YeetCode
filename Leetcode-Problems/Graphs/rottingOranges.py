from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        count = 0
        q = deque()
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    q.append((row, col))
        if q:
            q.append('level')
        while(q):
            cur = q.popleft()
            if cur == 'level':
                for row in grid:
                    print(row)
                if q:
                    q.append('level')
                    count += 1
                    print(count, q)
                    continue
                else:
                    break
            row, col = cur
            if row + 1 < ROWS and grid[row + 1][col] == 1:
                grid[row + 1][col] = 2
                q.append((row + 1, col))
            if row - 1 >= 0 and grid[row - 1][col] == 1:
                grid[row - 1][col] = 2
                q.append((row - 1, col))
            if col + 1 < COLS and grid[row][col + 1] == 1:
                grid[row][col + 1] = 2
                q.append((row, col + 1))
            if col - 1 >= 0 and grid[row][col - 1] == 1:
                grid[row][col - 1] = 2
                q.append((row, col - 1))
        for row in grid:
            if 1 in row:
                return -1
        return count

grid = [[2,0,1,1,1,1,1,1,1,1],[1,0,1,0,0,0,0,0,0,1],[1,0,1,0,1,1,1,1,0,1],[1,0,1,0,1,0,0,1,0,1],[1,0,1,0,1,0,0,1,0,1],[1,0,1,0,1,1,0,1,0,1],[1,0,1,0,0,0,0,1,0,1],[1,0,1,1,1,1,1,1,0,1],[1,0,0,0,0,0,0,0,0,1],[1,1,1,1,1,1,1,1,1,1]]
obj = Solution()
print(obj.orangesRotting(grid))