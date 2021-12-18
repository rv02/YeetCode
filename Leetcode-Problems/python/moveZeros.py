#https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/567/
from typing import List


class Solution(object):
    def moveZeroes(self, nums: List[int]):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        try:
            i = nums.index(0)
        except ValueError:
            return
        j = i
        while j < len(nums):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1                



if __name__ == '__main__':
    mylist = [1, 23, 0, 45, 45, 56]
    mylist1 = [3, 12, 1]
    obj = Solution()
    k = obj.moveZeroes(nums=mylist1)
    print(mylist1)