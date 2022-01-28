# https://leetcode.com/problems/all-paths-from-source-to-target/
from typing import List

class Solution:
    
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        stack = [[0, i] for i in graph[0]]
        paths = []
        while stack:
            curr_path = stack.pop()
            curr_node = curr_path[-1] 
            if curr_node == n - 1:
                paths.append(curr_path)
            else:
                for i in graph[curr_node]:
                    stack.append(curr_path + [i])
        return paths