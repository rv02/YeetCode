#https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/549/
#reimplement using bit-manipulation
class Solution(object):
    def singleNumber1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        single = {}
        for n in nums:
            if n in single:
                single.pop(n)
            else:
                single[n] = 1
        return (list(single.keys()))[0]
    
    def singleNumber2(self, nums):
        return 2*sum(set(nums))-sum(nums)

if __name__ == '__main__':
    nums = [2, 2, 1]
    obj = Solution()
    print(obj.singleNumber2(nums))
