from UnionByRank import UnionFind

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        # write your code here
        obj = UnionFind(n)
        for edge in edges:
            obj.union(edge[0], edge[1])
        # A tree is an undirected graph if following 2 cond. are satisfied
        # 1. Every node is connected i.e one single root
        # 2. # of nodes == # of edges + 1 
        return obj.getCount() == 1 and n == len(edges) + 1


