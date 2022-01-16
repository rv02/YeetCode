from bisect import bisect
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # binary-search
        for i1, num1 in enumerate(numbers[: -1]):
            num2 = target - num1
            i2 = bisect(numbers[i1+1:], num2) + i1
            if numbers[i1] + numbers[i2] == target:
                return [i1 + 1, i2 + 1]

    def twoSum2pointer(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] > target:
                j -= 1
            elif numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
            else:
                i += 1




if __name__=="__main__":
    obj = Solution()
    print(obj.twoSum2pointer([1, 3, 5, 6], 4))