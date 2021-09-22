package com.rv02;

import java.util.Arrays;

/**
 * @see  <a href = "https://leetcode.com/problems/best-time-to-buy-and-sell-stock/">Problem link</a>
 */
public class BuyAndSellStock {
    public int maxProfit(int[] prices) {
        int minPrice = Integer.MAX_VALUE;
        int maxProfit = 0;
        for (int price : prices) {
            minPrice = Math.min(minPrice, price);
            maxProfit = Math.max(maxProfit, price - minPrice);
        }
        return maxProfit;
    }
}
