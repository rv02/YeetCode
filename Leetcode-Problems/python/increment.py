#https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/559/
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits) - 1
        for i in range(n, -1, -1):
            digits[i] += 1
            if digits[i] == 10:
                digits[i] = 0
            else:
                break
        if digits[0] == 0:
            digits.insert(0, 1)
        return digits


if __name__=='__main__':
    digits = [9]
    ob = Solution()
    print(ob.plusOne(digits))
    