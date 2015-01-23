#!/usr/bin/python

# Say you have an array for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit. You may complete as many transactions as you like,
# (i.e., buy one and sell one share of the stock multiple times). However, you may not engage in
# multiple transactions at the same time (ie, you must sell the stock before you buy again).


# Buy at the first increasing price and sell when the increasing sequence ends.
def maxProfit(prices):
    profit = 0
    for i in range(1, len(prices)):
        diff = prices[i] - prices[i - 1]
        if diff > 0: profit += diff
    return profit
