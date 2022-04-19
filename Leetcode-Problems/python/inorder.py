from TreeNode import TreeNode

def printInorder(root: TreeNode):
    if root:
        printInorder(root.left)
        print(root.val),
        printInorder(root.right)