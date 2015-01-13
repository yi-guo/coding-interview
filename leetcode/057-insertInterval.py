#!/usr/bin/python

# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

# You may assume that the intervals were initially sorted according to their start times.

# Example 1:
# Given intervals [1, 3], [6, 9], insert and merge [2, 5] in as [1, 5], [6, 9].

# Example 2:
# Given [1, 2], [3, 5], [6, 7], [8, 10], [12, 16], insert and merge [4, 9] in as [1, 2], [3, 10], [12, 16].

# This is because the new interval [4, 9] overlaps with [3, 5], [6, 7], [8, 10].

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

# Traverse the array until an overlap is found. Merge and insert. O(n).
def insert(intervals, newInterval):
    if not intervals:
        return [newInterval]
    # Insert directly to the front.
    if newInterval.end < intervals[0].start:
        intervals.insert(0, newInterval)
        return intervals
    # Insert directly at the end.
    elif newInterval.start > intervals[len(intervals) - 1].end:
        intervals.append(newInterval)
        return intervals
    # Otherwise, start traversing.
    newIntervals, merged = list(), False
    for i, interval in enumerate(intervals):
        # Overlap found, continue merging until no overlap.
        if not (newInterval.end < interval.start or newInterval.start > interval.end):
            merged = True   # Indicating at least one merge has occurred.
            newInterval.start = min(interval.start, newInterval.start)
            newInterval.end = max(interval.end, newInterval.end)
            continue
        # Overlap stops and/or current interval is strictly greater than the one to be inserted.
        elif merged or newInterval.start < interval.start:
            newIntervals.append(newInterval)
            newIntervals.extend(intervals[i:])
            return newIntervals
        # Append those intervals that are strictly smaller than the one to be inserted.
        newIntervals.append(interval)
    if not newIntervals or newIntervals[len(newIntervals) - 1] != newInterval:
        newIntervals.append(newInterval)
    return newIntervals

def toString(intervals):
    output = list()
    for i, interval in enumerate(intervals):
        output.append([interval.start, interval.end])
    return ''.join(str(output))

def main():
    intervals = list()
    newInterval = Interval(4, 9)
    intervals.append(Interval(1, 2))
    intervals.append(Interval(3, 5))
    intervals.append(Interval(6, 7))
    intervals.append(Interval(8, 10))
    intervals.append(Interval(12, 16))
    print 'Given ----> %s, insert: [%d, %d]' % (toString(intervals), newInterval.start, newInterval.end)
    print 'Inserted -> %s' % toString(insert(intervals, newInterval))

main()
