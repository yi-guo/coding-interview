#!/usr/bin/python

# Say you have an array for which the ith element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock),
# design an algorithm to find the maximum profit.

# Find two numbers with the maximum difference. One pass, thus O(n).
def maxProfit(prices):
    minPrice, maxProfit = float('inf'), 0
    for i in range(len(prices)):
        minPrice = min(minPrice, prices[i])
        maxProfit = max(maxProfit, prices[i] - minPrice)
    return maxProfit
