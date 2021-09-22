package com.rv02;

public class MinInRotatedArray {
    public int findMin(int[] nums) {
        int high = nums.length - 1, low = 0;
        while (low < high) {
            if (nums[low] < nums[high]) {
                return nums[low];
            }
            int mid = (low + high) / 2;
            if (nums[mid] >= nums[low]) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }
        return nums[low];
    }
}
