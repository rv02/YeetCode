# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from listNode import ListNode

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_head = l1
        l2_head = l2
        len1 = len2 = 0
        while l1 or l2:
            if l1:
                len1 += 1
                l1 = l1.next
            if l2:
                len2 += 1
                l2 = l2.next
        zeros = zero_head = ListNode(0)
        for _ in range(abs(len1 - len2) - 1):
            zeros.next = ListNode(0)
            zeros = zeros.next
        if len2 > len1:
            zeros.next = l1_head
            l1_head = zero_head
        elif len1 > len2:
            zeros.next = l2_head
            l2_head = zero_head
        prev_sum = self.get_prev_node(l1_head, l2_head)
        if prev_sum.val > 9:
            head = ListNode(prev_sum.val // 10)
            prev_sum.val = prev_sum.val % 10
            head.next = prev_sum
        else:
            head = prev_sum
        return head
        
    def get_prev_node(self, node1, node2):
        if node1.next is None and node2.next is None:
            return ListNode(node1.val + node2.val)
        prev_node = self.get_prev_node(node1.next, node2. next)
        carry = prev_node.val // 10
        prev_node.val = prev_node.val % 10
        curr_node = ListNode(node1.val + node2.val + carry)
        curr_node.next = prev_node
        return curr_node