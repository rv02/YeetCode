package com.rv02;

public class PalindromeNumber {
    public boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        }

        int rev = 0, rem, i;
        for (i = x; i != 0; i = i / 10) {
            rem = i % 10;
            rev = rev * 10 + rem;
        }

        return rev == x;
    }

    public static void main(String[] args) {
        PalindromeNumber palin = new PalindromeNumber();
        System.out.println(palin.isPalindrome(219999912));
    }
}
