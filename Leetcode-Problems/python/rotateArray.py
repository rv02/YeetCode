class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums[k:], nums[:k] = nums[:-k], nums[-k:]

    def rotateReversed(self, nums, k):
        k %= len(nums)
        nums[:-k] = reversed(nums[:-k])
        nums[-k:] = reversed(nums[-k:])
        nums[:] = reversed(nums)

if __name__=='__main__':
    nums = [1, 2, 3, 4, 5]
    ob = Solution()
    ob.rotateReversed(nums, 2)
    print(nums)