from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[: n], nums1[n:] = [0] * n, nums1[: m]
        i, j, k = n, 0, 0
        while (i < m + n) and (j < n):
            if nums1[i] < nums2[j]:
                nums1[k], nums1[i] = nums1[i], nums1[k]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
            k += 1
        while j < n:
            nums1[k] = nums2[j]
            j += 1 
            k += 1

    def merge1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp = nums1.copy()
        i, j, k = 0, 0, 0
        while i < m and j < n:
            if temp[i] <= nums2[j]:
                nums1[k] = temp[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
            k += 1
        while i < m:
            nums1[k] = temp[i]
            i += 1
            k += 1
        while j < n:
            nums1[k] = nums2[j]
            j += 1
            k += 1
        


if __name__=='__main__':
    obj = Solution()
    nums1 = [1, 2, 3, 0, 0]
    nums2 = [3, 9]
    obj.merge(nums1, 3, nums2, 2)
    print(nums1)
        