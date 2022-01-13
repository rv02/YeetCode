from listNode import ListNode
from linkedList import LinkedList

class Solution(object):
    def removeNthFromEnd(self, head: ListNode, n) -> ListNode:
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        count = 0
        currNode = head
        delayedNode = head
        while currNode.next:
            currNode = currNode.next
            count += 1
            if count > n:
                delayedNode = delayedNode.next
        if count == n - 1:
            head = head.next
        else:
            delayedNode.next = delayedNode.next.next
        return head



if __name__=='__main__':
    ob = Solution()
    ls = [1, 2, 6, 7]
    ll = LinkedList(ls)
    print(ll)
    ll.head = ob.removeNthFromEnd(ll.head, 1)
    print(ll)