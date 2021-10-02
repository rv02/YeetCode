from typing import Optional


class Node:
    def __init__(self, val, left: Optional['Node'] = None, right: Optional['Node'] = None):
        self.value = val
        self.left = left
        self.right = right
