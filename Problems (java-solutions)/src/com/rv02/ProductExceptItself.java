package com.rv02;

import java.util.Arrays;
import java.util.Optional;

/**
 * @see <a href = "https://leetcode.com/problems/product-of-array-except-self/">Problem link</a>
 * Yuck solution but damn its 100% faster and 90% less memory consumption so suck my D
 */
public class ProductExceptItself {
    public int[] productExceptSelf(int[] nums) {
        int[] result = new int[nums.length];
        int productOfNums = 1;
        int countZeroes = 0;
        Integer zeroPos = null;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0) {
                countZeroes++;
                if (countZeroes > 1) {
                    return result;
                }
                zeroPos = i;
            } else {
                productOfNums *= nums[i];
            }
        }
        if (countZeroes == 1) {
            result[zeroPos] = productOfNums;
            return result;
        }
        for (int i = 0; i < nums.length; i++) {
            result[i] = productOfNums/nums[i];
        }
        return result;
    }
}
