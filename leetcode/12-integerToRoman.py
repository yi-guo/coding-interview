#!/usr/bin/python

# Given an integer, convert it to a roman numeral.

# Input is guaranteed to be within the range from 1 to 3999.

import sys

# Greedy algorithm.
def intToRoman(num):
    if num < 0 or num > 3999:
        return None
    table = {  1 : 'I',   4 : 'IV',   5 : 'V',   9 : 'IX',
              10 : 'X',  40 : 'XL',  50 : 'L',  90 : 'XC',
             100 : 'C', 400 : 'CD', 500 : 'D', 900 : 'CM', 1000 : 'M'}
    if num in table:
        return table[num]
    roman, nums = list(), sorted(table.keys())
    while num > 0:
        key = 0
        for i in range(len(nums)):
            if nums[i] <= num and (i == len(nums) - 1 or nums[i + 1] > num):
                key = nums[i]
                break
        roman.append(table[key])
        num = num - key
    return ''.join(roman)

def main():
    print intToRoman(int(sys.argv[1]))

main()
