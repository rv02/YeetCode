package com.rv02;

public class CountAndSay {
    public String countAndSay(int n) {
        return count();
    }

    public String count(String) {
        if (n == 1) {
            return "1";
        } else {
            return count();
        }
    }

    public String say(String s) {
        int count = 0;
        char currNum = s.charAt(0);
        StringBuilder stringBuilder = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) != currNum) {
                stringBuilder.append(count);
                stringBuilder.append(currNum);
                count = 0;
                currNum = s.charAt(i);
            } else {
                count++;
            }
        }
        stringBuilder.append(count);
        stringBuilder.append(currNum);
        return stringBuilder.toString();
    }

    public static void main(String[] args) {
        CountAndSay obj = new CountAndSay();
        System.out.println(obj.countAndSay(4));
    }
}
