package com.rv02;

/**
 * @see <a href = "https://leetcode.com/problems/maximum-subarray/">Problem link</a>
 * <p>Using Kadane's Algorithm</p>
 */
public class MaxSubArray {
    public int maxSubArray(int[] nums) {
        int max = Integer.MIN_VALUE;
        int sum = 0;
        for (int num: nums) {
            sum += num;
            if (max < sum) {
                max = sum;
            }
            if (sum < 0) {
                sum = 0;
            }
        }
        return max;
    }
}
