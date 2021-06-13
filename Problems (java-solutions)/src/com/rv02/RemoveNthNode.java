package com.rv02;

public class RemoveNthNode {

    public ListNode removeNthFromEnd(ListNode head, int n) {
        int count = 1;
        ListNode node = head;
        while (node.next != null) {
            count++;
            node = node.next;
        }
        node = head;
        ListNode prev = node;
        while (count > n) {
            prev = node;
            node = node.next;
            count--;
        }
        System.out.println(node.val + " " + prev.val);
        if (prev == node) {
            head = head.next;
        } else {
            prev.next = node.next;
        }
        return head;
    }

}
