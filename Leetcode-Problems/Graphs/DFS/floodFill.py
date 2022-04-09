# https://leetcode.com/problems/flood-fill/

from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if not image:
            return
        m = len(image)
        n = len(image[0])
        stack = [(sr, sc)]
        color = image[sr][sc]
        seen = []
        while (stack):
            (curr_row, curr_col) = stack.pop()
            image[curr_row][curr_col] = newColor
            if (curr_row, curr_col) not in seen:
                if ((curr_row+1) < m and image[curr_row+1][curr_col] == color):
                    stack.append((curr_row+1, curr_col))
                if ((curr_col+1) < n and image[curr_row][curr_col+1] == color):
                    stack.append((curr_row, curr_col+1))
                if ((curr_row-1) >= 0 and image[curr_row-1][curr_col] == color):
                    stack.append((curr_row-1, curr_col))
                if ((curr_col-1) >= 0 and image[curr_row][curr_col-1] == color):
                    stack.append((curr_row, curr_col-1))
                seen.append((curr_row, curr_col))       
        return image

if __name__=='__main__':
    obj = Solution()
    matrix = [[1,1,1],[1,1,0],[1,0,1]]
    print(obj.floodFill(matrix, 1, 1, 2))