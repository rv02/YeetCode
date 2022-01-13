class Solution(object):
    def strStr(self, haystack: str, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        flag = -1
        step = len(needle)
        for i in range(len(haystack) - step + 1):
            if needle == haystack[i: i + step]:
                flag = i
                break
        return flag

    def strStr1(self, haystack: str, needle):
        return haystack.find(needle)

    def strStr2(self, haystack: str, needle):
        # rolling hash.. later
        if not needle:
            return 0
        flag = -1
        step = len(needle)
        needleHash = hash(needle)
        for i in range(len(haystack) - step + 1):
            if needleHash == hash(haystack[i: i + step]):
                if needle == haystack[i: i + step]:
                    flag = i
                    break
        return flag
