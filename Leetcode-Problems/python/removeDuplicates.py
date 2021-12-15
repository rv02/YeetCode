#https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        curr = nums[0]
        curr_pos = 0
        for i, n in enumerate(nums):
            if n > curr:
                nums[curr_pos+1], nums[i] = nums[i], nums[curr_pos+1]
                curr_pos += 1
                curr = n
        return curr_pos+1


if __name__ == '__main__':
    mylist = [1, 23, 45, 45, 56]
    obj = Solution()
    k = obj.removeDuplicates(nums=mylist)
    print(mylist[:k])

        