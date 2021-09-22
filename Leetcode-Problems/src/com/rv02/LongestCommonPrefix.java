package com.rv02;

import java.util.Arrays;

public class LongestCommonPrefix {
    public String longestCommonPrefix(String[] strs) {
        String min = strs[0];
        //find the smallest string
        for (String str : strs) {
            if (str.length() < min.length()) {
                min = str;
            }
        }
        for (int i = 0; i < min.length(); i++) {
            String prefix = min.substring(0, min.length() - i);
            boolean allContainPrefix = true;
            for (String str: strs) {
                if (!str.substring(0, prefix.length()).contains(prefix)) {
                    allContainPrefix = false;
                    break;
                }
            }
            if (allContainPrefix) {
                return prefix;
            }
        }
        return "";
    }

    public static void main(String[] args) {
        LongestCommonPrefix obj = new LongestCommonPrefix();
        System.out.println(obj.longestCommonPrefix(new String[]{"reflower","flow","flight"}));
        System.out.println(obj.longestCommonPrefix(new String[]{"ab", "badabbie", "r"}));
    }
}
