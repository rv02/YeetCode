from typing import DefaultDict, List


#https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/674/
class Solution(object):
    def intersect(self, nums1: List[int], nums2: List[int]):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        freq = DefaultDict(int)
        rlist = []
        for num in nums1: freq[num] += 1
        for num in nums2:
            if num in freq and freq[num] > 0:
                freq[num] -= 1
                rlist.append(num)
        return rlist


if __name__=='__main__':
    nums1 = [1, 3, 4, 5, 1, 2, 2, 3]
    nums2 = [1, 2, 1, 3, 6, 7, 5, 2, 2]
    ob = Solution()
    print(ob.intersect(nums1, nums2))