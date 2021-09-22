package com.rv02.incomplete;

import java.util.Arrays;

public class FirstAndLastIndex {
    public int[] searchRange(int[] nums, int target) {
        int index = Arrays.binarySearch(nums, target);
        if (index < 0) {
            return new int[]{-1, -1};
        }
        int leftIndex = index - 1;
        int rightIndex = index + 1;
        return new int[]{};
    }
}
