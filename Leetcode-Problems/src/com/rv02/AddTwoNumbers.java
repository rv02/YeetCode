package com.rv02;

import java.util.LinkedList;

public class AddTwoNumbers {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        LinkedList<Integer> sum = new LinkedList<>();
        int carry = 0;
        int a, b;
        while (!(l1 == null && l2 == null)) {
            if (l1 == null) {
                a = 0;
            } else {
                a = l1.val;
                l1 = l1.next;
            }
            if (l2 == null) {
                b = 0;
            } else {
                b = l2.val;
                l2 = l2.next;
            }
            sum.push((a + b + carry) % 10);
            carry = (a + b + carry) / 10;
        }
        if (carry == 1) {
            sum.push(1);
        }
        ListNode pointer = new ListNode(sum.remove());
        while (!sum.isEmpty()) {
            pointer = new ListNode(sum.remove(), pointer);
        }
        return pointer;
    }

    public static void main(String[] args) {
        ListNode l13 = new ListNode(3);
        ListNode l12 = new ListNode(4, l13);
        ListNode l11 = new ListNode(2, l12);
        ListNode l23 = new ListNode(4);
        ListNode l22 = new ListNode(6, l23);
        ListNode l21 = new ListNode(5, l22);
        AddTwoNumbers obj = new AddTwoNumbers();
        System.out.println(obj.addTwoNumbers(l11, l21));
    }
}
