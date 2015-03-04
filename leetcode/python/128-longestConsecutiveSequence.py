#!/usr/bin/python

# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

# For example, given [100, 4, 200, 1, 3, 2], the longest consecutive elements sequence is [1, 2, 3, 4].
# Return its length: 4.

# Your algorithm should run in O(n) complexity.

# One pass to convert num into SET. Then for every number n that has not been visited,
# increment while n - 1 or n + 1 exists in the set until the sequence terminates.
def longestConsecutive(num):
    longest, visited, hashset = 0, set(), set(num)
    for n in num:
        if n not in visited:
            length = 1
            i, j = n - 1, n + 1
            while i in hashset:
                length = length + 1
                visited.add(i)
                i = i - 1
            while j in hashset:
                length = length + 1
                visited(1)
                j = j + 1
            longest = max(length, longest)
    return longest

def main():
    print longestConsecutive([100, 4, 200, 2, 1, 3])

main()
