from typing import List
from UnionByRank import UnionFind


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        ans = 0
        obj = UnionFind(n)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    obj.union(i, j)
        for i, x in enumerate(obj.root):
            if i == x:
                ans += 1
        return ans