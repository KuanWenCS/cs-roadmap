# Best Time to Buy and Sell Stock

# You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

# You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

# Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

# Constraints:

# 1 <= prices.length <= 100
# 0 <= prices[i] <= 100

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]
        for price in prices:
            if min_price > price:
                min_price = price
            if price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit
