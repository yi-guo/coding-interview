#!/usr/bin/python

# Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines
# are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis
# forms a container, such that the container contains the most water.

# Note: You may not slant the container.

# Two pointers i and j move toward each other. If height[i] < height[j], move i one unit to the right.
# Do so until i = j, thus O(n).
def maxArea(height):
    if len(height) < 2:
        return 0
    maxArea = 0
    i, j = 0, len(height) - 1
    while i < j:
        maxArea = max(maxArea, min(height[i], height[j]) * (j - i))
        if height[i] < height[j]:
            i = i + 1
        else:
            j = j - 1
    return maxArea

def main():
    print maxArea([3, 5, 8, 1, 4, 9, 11, 7])

main()
