#https://leetcode.com/problems/clone-graph/
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []




class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        graph = {node: Node(node.val)}
        stack = [node]
        while stack:
            n = stack.pop()
            for i in n.neighbors:
                if i not in graph:
                    stack.append(i)
                    graph[i] = Node(i.val)
                graph[n].neighbors.append(graph[i])
        return graph[node]
        
        
        