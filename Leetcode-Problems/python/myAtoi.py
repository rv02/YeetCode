class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        pos = True
        q = pow(2, 31) - 1
        ans = 0
        if not s:
            return 0
        while  i < len(s) and s[i] == ' ':
            i += 1
        if s[0] == '-':
            pos = False
            q += 1
        if not s[i].isdigit():
            i += 1
        while i < len(s) and s[i].isdigit():
            ans = ans * 10 + (ord(s[i]) - 48)
            i += 1
        return ans if pos else -ans
        


if __name__ == '__main__':
    obj = Solution()
    print(obj.myAtoi("   567"))


