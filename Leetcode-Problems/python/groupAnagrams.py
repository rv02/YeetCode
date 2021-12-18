from collections import defaultdict

class Solution(object):
    #https://leetcode.com/problems/group-anagrams/
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)     
        return ans.values()   


if __name__=='__main__':
    strs = ["eat","tea","tan","ate","nat","bat", "f"]
    ob = Solution()
    print(ob.groupAnagrams(strs))