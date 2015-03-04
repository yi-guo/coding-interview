#!/usr/bin/python

# Given a list of non negative integers, arrange them such that they form the largest number.

# For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

# Note: The result may be very large, so you need to return a string instead of an integer.

# Sort the given list with a customed comparator, then join all the numbers. Thus, O(nlog(n)).
def largestNumber(num):
    # If empty list, then return no number is returned.
    if not num:
        return str()
    # Convert every integer to string.
    num = [str(n) for n in num]
    # If only one number given, then return the number.
    if len(num) == 1:
        return num[0]
    # Sort the list with the comparator given below, then combine all numbers.
    ret = ''.join(sorted(num, cmp=comparator, reverse=True)).lstrip('0')
    # Remove the leading 0's if any.
    return ret if ret else '0'

# Customize a comparator specifically for this question.
def comparator(x, y):
    # To compare x and y, simply compare xy and yx.
    xy, yx = x + y, y + x
    for i in range(len(x) + len(y)):
        diff = ord(xy[i]) - ord(yx[i])
        if diff: return diff
    return 0

def main():
    print largestNumber([3, 30, 34, 5, 9])

main()
