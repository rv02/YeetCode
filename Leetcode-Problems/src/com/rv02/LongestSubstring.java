package com.rv02;

import java.util.ArrayList;
import java.util.Collections;

public class LongestSubstring {
    public static int lengthOfLongestSubstring(String s) {
        int count = 0;
        ArrayList<Character> substring = new ArrayList<>();
        ArrayList<Integer> substringLength = new ArrayList<>();
        int jump;
        for (int i = 0; i < s.length(); i++) {
            char curr = s.charAt(i);
            if (substring.contains(curr)) {
                jump = substring.indexOf(curr);
                substringLength.add(substring.size());
                substring.subList(0, jump + 1).clear();
            }
            substring.add(curr);
        }
        substringLength.add(substring.size());
        return Collections.max(substringLength);
    }

    public static void main(String[] args) {
        System.out.println(lengthOfLongestSubstring(""));
    }

}
