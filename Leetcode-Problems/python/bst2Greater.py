from typing import Optional
from TreeNode import TreeNode


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ob = Solution()
        ob.modifyTree(root, 0)
        return root
    
    def modifyTree(self, node: TreeNode, sum: int):
        if not node:
            return sum
        sum = self.modifyTree(node.right, sum)
        sum = node.val = sum + node.val
        sum = self.modifyTree(node.left, sum)
        return sum       