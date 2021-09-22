package com.rv02;

/**
 * 101 1.3
 */
class URLify {

    public static void main(String[] args) {
        replaceSpaces("A Simple Blog URL      ".toCharArray(), 17);
    }

    public static void replaceSpaces(char[] str, int trueLength) {
        int noOfSpaces = 0, index, i = 0;
        for (i = 0; i < trueLength; i++) {
            if (str[i] == ' ') {
                noOfSpaces++;
            }
        }
        index = trueLength + noOfSpaces * 2;
        if (trueLength < str.length) {
            str[trueLength] = '\0';
        }
        for (i = trueLength - 1; i > 0; i--) {
            if (str[i] == ' ') {
                str[index - 1] = '0';
                str[index - 2] = '2';
                str[index - 3] = '%';
                index = index - 3;
            } else {
                str[index - 1] = str[i];
                index--;
            }
        }
        System.out.println(str);
    }
}