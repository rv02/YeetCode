# https://www.hackerrank.com/challenges/bfsshortreach/problem
from typing import List, Tuple
from collections import deque


def bfs(n: int, m: int, edges: List[Tuple[int, int]], s: int):
    """
    BFS on an undirected graph
    :param n: the number of nodes
    :param m: the number of edges
    :param edges: start and end nodes for edges
    :param s: the node to start traversals from
    :return: the distances to nodes in increasing node number order, not including the start node (-1 if a node is not reachable)
    """
    graph = {}
    for i in range(1, n+1):
        graph[i] = set()
    for i, j in edges:
        graph[i].add(j)
        graph[j].add(i)
    queue = deque([(s, 0)])
    visited = {s}
    reached = {s: 0}
    while queue:
        curr_node, curr_cost = queue.popleft()
        for ngbors in graph[curr_node]:
            if ngbors not in visited:
                visited.add(ngbors)
                reached[ngbors] = curr_cost + 6
                queue.append((ngbors, curr_cost + 6))

    result = []
    for node in range(1, n+1):
        if s != node:
            result.append(reached.get(node, -1))

    return result
