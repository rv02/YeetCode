from typing import List
from TreeNode import TreeNode
from inorder import printInorder
from levelOrder import levelOrder

def listToTree(l: List[int|None]) -> TreeNode:
    if not l:
        return None
    root = node = TreeNode(val=l[0])
    levelNodes = []
    for i, vals in enumerate(l[:-1]):
        if i % 2 == 1:
            node.right = TreeNode(val=l[i+1])
            levelNodes.append(node.right)
            node = levelNodes.pop(0)
        else:
            node.left = TreeNode(val=l[i+1])
            levelNodes.append(node.left)
    return root


if __name__=='__main__':
    root = listToTree([1, None, 1])
    printInorder(root)
    print(levelOrder(root))
    
        


      
