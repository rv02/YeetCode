package com.rv02;

public class ReverseInteger {

    public int reverse(int x) {
        long rev = 0, rem;
        for (int i = x; i != 0; i = i/10) {
            rem = i % 10;
            rev = rev * 10 + rem;
        }
        if (rev > Integer.MAX_VALUE || rev < Integer.MIN_VALUE) {
            rev = 0;
        }
        return (int)rev;
    }

    public static void main(String[] args) {
        ReverseInteger obj = new ReverseInteger();
        System.out.println(obj.reverse(-1534236469));
    }
}
