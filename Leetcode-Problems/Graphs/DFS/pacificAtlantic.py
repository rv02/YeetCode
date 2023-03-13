from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        atlantic = [[False for _ in range(n)] for _ in range(m)]
        pacific = [[False for _ in range(n)] for _ in range(m)]
        res = []
        def dfs(r, c, visited, prevHeight):
            if r < 0 or c < 0 or r == m or c == n or visited[r][c] or heights[r][c] < prevHeight:
                return
            visited[r][c] = True
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])
        for c in range(n):
            dfs(0, c, pacific, heights[0][c])
            dfs(m - 1, c, atlantic, heights[m - 1][c])
        for r in range(m):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, n - 1, atlantic, heights[r][n - 1])
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    res.append([i, j])
        return res
            
obj = Solution()
print(obj.pacificAtlantic([[1,2,3],[5,4,1]]))
            
                
        