#!/usr/bin/python

# Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

from collections import defaultdict

class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

# Use hashmap to count the number of points for each unique line determined by (k, b) as in y = kx + b.
def maxPoints(points):
    if len(points) < 3: return len(points)
    lines = defaultdict(set)
    for i in range(len(points)):
        for j in range(len(points)):
            p1, p2 = points[i], points[j]
            k, b = float('inf'), p1.x
            if p1.x != p2.x:
                k = float(p2.y - p1.y) / (p2.x - p1.x)
                b = p1.y - k * p1.x
            lines[(k, b)].add(i)
            lines[(k, b)].add(j)
    return len(max(lines.values(), key=len))

def main():
    points = [Point(1, 2), Point(2, 2), Point(2, 3), Point(3, 3), Point(0, 0), Point(3, 0), Point(0, 3)]
    print maxPoints(points)

main()
