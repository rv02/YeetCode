package com.rv02;

/**
 * See <a href = "https://leetcode.com/problems/maximum-product-subarray/">Problem link</a>
 */
public class MaxProductSubArray {
    public int maxProduct(int[] nums) {
        int res = nums[0];
        for (int i = 1, imax = res, imin = res; i < nums.length; i++) {
            if (nums[i] < 0) {
                int temp = imax;
                imax = imin;
                imin = temp;
            }
            imax = Math.max(nums[i], nums[i] * imax);
            imin = Math.min(nums[i], nums[i] * imin);
            res = Math.max(res, imax);
        }
        return res;
    }
}
