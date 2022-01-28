from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjacency_list = [[] for _ in range(n)]
        for (a, b) in edges:
            adjacency_list[a].append(b)
            adjacency_list[b].append(a)
        stack = [source]
        seen = set()
        while (stack):
            curr_vertice = stack.pop()
            if curr_vertice == destination:
                return True
            if curr_vertice not in seen:
                stack.extend(adjacency_list[curr_vertice])
                seen.add(curr_vertice)
        return False