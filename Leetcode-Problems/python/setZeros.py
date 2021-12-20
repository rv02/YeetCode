#https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/777/
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        m = len(matrix)
        n = len(matrix[0])
        address = [(i, j) for i in range(m) for j in range(n) if matrix[i][j] == 0]
        rows = {i[0] for i in address}
        cols = {i[1] for i in address}
        for i in rows:
            matrix[i] = [0] * n
        for j in cols:
            for i in range(m):
                matrix[i][j] = 0

if __name__=='__main__':
    ob = Solution()
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    zeromat = []
    ob.setZeroes(matrix)
    print(matrix)