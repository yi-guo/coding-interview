#!/usr/bin/python

# Given a collection of intervals, merge all overlapping intervals.

# For example, given [1, 3], [2, 6], [8, 10], [15, 18], return [1, 6], [8, 10], [15, 18].

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

# Sort the array and merge one by one, thus O(nlog(n)).
def merge(intervals):
    if not intervals or len(intervals) < 2:
        return intervals
    intervals = sorted(intervals, key=lambda i : i.start)
    curr, merged = intervals[0], list()
    for i in range(1, len(intervals)):
        if curr.end >= intervals[i].start:
            curr = Interval(curr.start, max(curr.end, intervals[i].end))
        else:
            merged.append(curr)
            curr = intervals[i]
    merged.append(curr)
    return merged

def toString(intervals):
    output = list()
    for i, interval in enumerate(intervals):
        output.append([interval.start, interval.end])
    return ''.join(str(output))

def main():
    intervals = list()
    intervals.append(Interval(8, 10))
    intervals.append(Interval(1, 3))
    intervals.append(Interval(2, 6))
    intervals.append(Interval(15, 18))
    print 'Given --> %s' % toString(intervals)
    print 'Merged -> %s' % toString(merge(intervals))

main()
