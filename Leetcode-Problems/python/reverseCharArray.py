class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            s[i], s[-(i+1)] = s[-(i+1)], s[i]
        

if __name__ == '__main__':
    s = ['a']
    ob = Solution()
    ob.reverseString(s)
    print(s)