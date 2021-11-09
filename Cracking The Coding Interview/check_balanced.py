#Page 120-4.4
from binary_tree import BinaryTree
from tree_node import Node
from sys import maxsize

def check_height(root: Node) -> int:
    if not root:
        return -1
    left_height = check_height(root.left)
    if left_height == -maxsize:
        return -maxsize
    right_height = check_height(root.right)
    if right_height == -maxsize:
        return -maxsize
    height_diff = left_height - right_height
    if abs(height_diff) > 1:
        return -maxsize
    else:
        return max(left_height, right_height) + 1


def check_balanced(tree: BinaryTree) -> bool:
    return check_height(tree.root) != -maxsize

