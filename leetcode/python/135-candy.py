#!/usr/bin/python

# There are N children standing in a line. Each child is assigned a rating value.

# You are giving candies to these children subjected to the following requirements:
#   1. Each child must have at least one candy.
#   2. Children with a higher rating get more candies than their neighbors.

# What is the minimum candies you must give?

# Assign 1 candy to each child.
# Scan from left to right and give one more candy to those children that have higher ratings than their previous ones.
# Scan from right to left and give one more candy to those children that have higher ratings but do not have more candies
# than the ones after them.
# Two passes, thus O(n).
def candy(ratings):
    if not ratings: return 0
    candies = [1 for n in ratings]
    for i in range(1, len(candies)):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1
    for i in range(len(candies) - 2, -1, -1):
        if ratings[i] > ratings[i + 1] and candies[i] <= candies[i + 1]:
            candies[i] = candies[i + 1] + 1
    return sum(candies)

def main():
    print candy([3, 8, 5, 4, 3, 3, 6, 2, 7, 4])

main()
