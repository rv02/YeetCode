from collections import Counter

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = Counter(s)
        ans = -1
        for i, c in enumerate(s):
            if count.get(c) == 1:
                ans = i
                break
        return ans


if __name__=='__main__':
    ob = Solution()
    print(ob.firstUniqChar('leel'))