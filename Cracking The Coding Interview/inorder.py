from binary_tree import Node

def inorder(root: Node):
    res = []
    if root:
        res = inorder(root.left)
        res.append(root.value)
        res = res + inorder(root.right)
    return res


