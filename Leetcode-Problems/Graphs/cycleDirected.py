class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        nodes = [[] for _ in range(A)]
        for i in range(len(B)):
            nodes[B[i][0] - 1].append(B[i][1])
        for node in nodes:
            print(node)
        def dfs(node, visited):
            if node in visited:
                return True
            visited.add(node)
            for next in nodes[node - 1]:
                if dfs(next, visited.copy()):
                    return True
            return False


        return dfs(1, set())
        
obj = Solution()
print(obj.solve(5, [
  [1, 2],
  [1, 3],
  [2, 3],
  [1, 4],
  [4, 3],
  [4, 5],
  [3, 5]
]
))