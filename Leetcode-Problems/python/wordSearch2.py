from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
        
    def insert(self, word: str):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True
    

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ans = set()
        totRows, totCols = len(board), len(board[0])
        trie = Trie()
        for word in words:
            trie.insert(word)
    
        def dfs(node, row, col, curWord):
            if row < 0 or row >= totRows or col < 0 or col >= totCols or visited[row][col]:
                return
            curLetter = board[row][col]
            curWord += curLetter
            if (not node) or (curLetter not in node.children):
                return
            node = node.children[curLetter]
            if node.endOfWord:
                ans.add(curWord)
            visited[row][col] = True
            dfs(node, row + 1, col, curWord)
            dfs(node, row - 1, col, curWord)    
            dfs(node, row, col + 1, curWord)
            dfs(node, row, col - 1, curWord)
            visited[row][col] = False
            return
        
        for i in range(totRows):
            for j in range(totCols):
                visited = [[False] * totCols for _ in range(totRows)]
                dfs(trie.root, i, j, '')
        return list(ans)
        
        

obj = Solution()
print(obj.findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
["oath","pea","eat","rain","hklf", "hf"]
))