package com.rv02;

public class PlusOne {
    public static int[] plusOne(int[] digits) {
        for (int i = digits.length - 1; i >= 0; i--) {
            digits[i]++;
            if (digits[i] == 10) {
                digits[i] = 0;
            } else {
                break;
            }
        }
        if (digits[0] == 0) {
            int[] temp = new int[digits.length + 1];
            temp[0] = 1;
            int j = 1;
            for (int i: digits) {
                temp[j] = i;
            }
            digits = temp;
        }
        return digits;
    }

    public static void main(String[] args) {
        int[] arr = plusOne(new int[]{4, 3, 2, 1});
        for (int j : arr) {
            System.out.println(j);
        }
    }
}
