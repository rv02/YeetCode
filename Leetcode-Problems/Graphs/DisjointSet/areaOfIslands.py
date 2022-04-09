from collections import defaultdict
from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0
        islands = defaultdict(int)
        disjointSet = UnionFind(m * n)
        for i, row in enumerate(grid):
            for j, land in enumerate(grid[i]):
                if land:
                    if i + 1 < m and grid[i + 1][j]:
                        disjointSet.union(i * n + j, (i+1) * n + j)
                    if j + 1 < n and grid[i][j + 1]:
                        disjointSet.union(i * n + j, i * n + j + 1)
        for root in disjointSet.getRoots():
            col = root % n
            row = root // n
            if grid[row][col]:
                islands[root] += 1
        if islands:
            return max(islands.values())
        else:
            return 0
            
    
      
class UnionFind:
    def __init__(self, size) -> None:
        self.root = [i for i in range(size)]
        self.rank = [1] * size
        self.count = size      

    # Path compression optimized
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
            self.count -= 1

    # get total no of roots
    def getCount(self):
        return self.count
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)
    
    def getRoots(self):
        roots = []
        for node in self.root:
            roots.append(self.find(node))
        return roots
        

if __name__=="__main__":
    ob = Solution()
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
    print(ob.maxAreaOfIsland(grid))