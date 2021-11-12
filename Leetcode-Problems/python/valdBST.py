from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    last_checked: Optional[int] = None
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if not self.isValidBST(root.left):
            return False
        if self.last_checked is not None and root.val <= self.last_checked:
            return False
        self.last_checked = root.val
        return self.isValidBST(root.right)
            
        