# Page 120-4.2
from typing import List, Optional
from binary_tree import BinaryTree
from tree_node import Node
from inorder import inorder


def minimal_tree(nums: List[int]):
    return BinaryTree(make_tree(nums, 0, len(nums) - 1))


def make_tree(arr: List[int], start: int, end: int) -> Optional[Node]:
    if start > end:
        return
    mid = (start + end) // 2
    root = Node(arr[mid])
    root.left = make_tree(arr, start, mid - 1)
    root.right = make_tree(arr, mid + 1, end)
    return root


if __name__ == '__main__':
    print(inorder(minimal_tree([1, 5, 10, 25, 36, 45, 89]).root))
