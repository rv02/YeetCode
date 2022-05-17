from typing import Optional
from listNode import ListNode


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small_list = fs = ListNode(0)
        big_list = fb = ListNode(0)
        while head:
            if head.val < x:
                small_list.next = head
                head = head.next
                small_list = small_list.next
                small_list.next = None
            else:
                big_list.next = head
                head = head.next
                big_list = big_list.next
                big_list.next = None
        small_list.next = fb.next
        return fs.next
        
        