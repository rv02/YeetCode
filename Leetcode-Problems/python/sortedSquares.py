from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        firstPositive = 0
        for i, num in enumerate(nums):
            if num >= 0:
                firstPositive = i
                break
        if nums[-1] < 0:
            firstPositive = len(nums)
        i, j = firstPositive, firstPositive - 1
        while i < len(nums) and j >= 0:
            if nums[i] < abs(nums[j]):
                result.append(nums[i] * nums[i])
                i += 1
            else:
                result.append(nums[j] * nums[j])
                j -= 1
        while i < len(nums):
            result.append(nums[i] * nums[i])
            i += 1
        while j >= 0:
            result.append(nums[j] * nums[j])
            j -= 1
        return result



if __name__=="__main__":
    obj = Solution()
    arr = [-7, -3, -2]
    print(obj.sortedSquares(arr))