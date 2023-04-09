from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            if nums[end] == val:
                end -= 1
                continue
            if nums[start] == val:
                nums[start], nums[end] = nums[end], nums[start]
                end -= 1 
            start += 1 
        print(nums)
        return nums.count(val)
    
ob = Solution()
ob.removeElement([0,1,2,2,3,0,4,2], 2)