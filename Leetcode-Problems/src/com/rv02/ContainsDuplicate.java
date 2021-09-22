package com.rv02;

import java.util.HashSet;
import java.util.Set;

/**
 * @see <a href = "https://leetcode.com/problems/contains-duplicate/">Problem Link</a>
 */
public class ContainsDuplicate {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> numSet = new HashSet<>();
        for (int num: nums) {
            if (numSet.contains(num)) {
                return true;
            }
            numSet.add(num);
        }
        return false;
    }
}
