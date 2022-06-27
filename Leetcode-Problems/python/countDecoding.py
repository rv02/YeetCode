class Solution:
    def numDecodings(self, s: str) -> int:
        count1 = count2 = 0
        dig1 = dig2 = 9
        for i, ch in enumerate(s):
            digit = int(ch)
            if digit == 0 and (dig2 != 1 or dig2 != 2):
                return 0
            temp = count2 + 1
            if dig2 == 1 or (dig2 == 2 and digit <= 6):
                temp = temp + count1 + 1
            count1, count2 = count2, temp
            dig1, dig2 = dig2, digit
        return count2
                
                
        