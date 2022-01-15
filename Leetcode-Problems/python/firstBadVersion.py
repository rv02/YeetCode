# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version) -> bool:
    pass

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, h = 1, n
        while l <= h:
            m = (h + l) // 2
            if isBadVersion(m):
                h = m - 1
            else:
                l = m + 1
        return l
                
        