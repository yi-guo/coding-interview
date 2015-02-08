#!/usr/bin/python

# Given n non-negative integers representing the histogram's bar height where the width of each bar is 1,
# find the area of largest rectangle in the histogram.

# Suppose a histogram where width of each bar is 1, given height = [2, 1, 5, 6, 2, 3].

# The largest rectangle is shown in the shaded area, which has area = 10 unit.

# For example, given height = [2, 1, 5, 6, 2, 3], return 10.

# Use stack to keep track of heights. One pass, thus O(n)
def largestRectangleArea(height):
    height.append(0)
    stack, maximum = [0], 0
    for i in xrange(len(height)):
        while stack and height[i] < height[stack[-1]]:
            h = height[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            maximum = max(maximum, w * h)
        stack.append(i)
    return maximum

def main():
    height = [2, 1, 5, 6, 2, 3]
    print largestRectangleArea(height)

main()
