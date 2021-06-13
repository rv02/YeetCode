package com.rv02;

import java.util.Arrays;

public class TwoSum {

    public int[] twoSum(int[] nums, int target) {
        int i = 0, j = 0, flag = 0;
        while (i < nums.length - 1 && flag == 0) {
            for (j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    flag = 1;
                    break;
                }
            }
            i++;
        }
        return new int[]{i - 1, j};
    }

    public static void main(String[] args) {
        int[] nums = {2, 7, 11, 15};
        TwoSum obj = new TwoSum();
        System.out.println(Arrays.toString(obj.twoSum(nums, 9)));
    }
}

