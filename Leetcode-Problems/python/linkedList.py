from typing import List
from listNode import ListNode


class LinkedList:
    def __init__(self, head: ListNode = None) -> None:
        self.head = head

    def __init__(self, ls: List) -> None:
        if not ls:
            self.head = None
        else:
            self.head = ListNode(ls[0])
            node = self.head
            for item in ls[1:]:
                tempNode = ListNode(item)
                node.next = tempNode
                node = node.next

    def __iter__(self):
        currNode: ListNode = self.head
        while currNode:
            yield currNode.val
            currNode = currNode.next

    def __str__(self) -> str:
        list = []
        for item in self:
            list.append(item)
        return str(list)
