from typing import Counter


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return Counter(s) == Counter(t)


if __name__=='__main__':
    ob = Solution()
    print(ob.isAnagram("lawda", "awdl"))
