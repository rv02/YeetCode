from UnionByRank import UnionFind
from typing import List

# 94.30 speed beat **flex**
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        uf = UnionFind(len(s))
        ans = ""
        connections = {}
        # make pairs
        for i, j in pairs:
            uf.union(i, j)
        # make each index point to its root
        # store chars in respective dicts
        for i, x in enumerate(uf.root):
            x = uf.find(x)
            uf.root[i] = x
            ls = connections.get(x)
            if not ls:
                connections[x] = [s[i]]
            else:
                ls.append(s[i])
        # sort the chars in diff connections
        for item in connections.values():
            item.sort(reverse=True)
        for i, x in enumerate(uf.root):
            ans += connections.get(x).pop()
        return ans
