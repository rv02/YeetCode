from array import array
from bisect import bisect, bisect_left
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col0 = [row[0] for row in matrix]
        row = bisect(col0, target) - 1
        if col0[row] == target:
            return True
        index = bisect(matrix[row], target) - 1
        return matrix[row][index] == target
        

if __name__=="__main__":
    obj = Solution()
    matrix = [[1,3,5,7],[1,11,16,20],[23,30,34,60]]
    target = 1
    obj.searchMatrix(matrix, target)