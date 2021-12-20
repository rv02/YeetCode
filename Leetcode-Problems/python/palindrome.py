import re


class Solution(object):
    def isPalindrome(self, s:str):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        pattern = re.compile('[\W_]+')
        s = re.sub(pattern, '', s)
        return s == s[::-1]
        

if __name__=='__main__':
    ob = Solution()
    print(ob.isPalindrome("A man, a plan, a canal: Panama_"))