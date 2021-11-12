# Definition for singly-linked list.
from typing import Optional

from listNode import ListNode

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # stack = []
        # while (head):
        #     stack.append(head)
        #     head = head.next
        # for i, node in reversed(list(enumerate(stack))):
        #     if i > 0:
        #         node.next = stack[i - 1]
        #     else:
        #         node.next = None
        # return stack.pop() if stack else None
        prev = None
        while (head):
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev