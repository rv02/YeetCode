package com.rv02;

import java.math.BigInteger;

public class ConcatBinary {
    public int concatenatedBinary(int n) {
        int size = 0;
        long result = 0;
        for (int i = 1; i <= n; i++) {
            if((i & (i - 1)) == 0) {
                size += 1;
            }
            result = ((result << size) | i) % 1000000007;

        }
        return (int) result;
    }

    public static void main(String[] args) {
        ConcatBinary obj = new ConcatBinary();
        System.out.println(obj.concatenatedBinary(12));
    }
}
