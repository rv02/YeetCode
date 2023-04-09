from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            while num != 0:
                curr = num - 1
                num = nums[num - 1]
                nums[curr] = 0
        return [i+1 for i, num in enumerate(nums) if num != 0]
    
ob = Solution()
print(ob.findDisappearedNumbers([4,3,2,7,8,2,3,1]))