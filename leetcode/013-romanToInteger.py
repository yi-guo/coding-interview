#!/usr/bin/python

# Given a roman numeral, convert it to an integer.

# Input is guaranteed to be within the range from 1 to 3999.

# Greedy algorithm.
def romanToInt(s):
    if not s:
        return None
    table = {'I' : 1,   'IV' : 4,   'V' : 5,   'IX' : 9,
             'X' : 10,  'XL' : 40,  'L' : 50,  'XC' : 90,
             'C' : 100, 'CD' : 400, 'D' : 500, 'CM' : 900, 'M' : 1000}
    if len(s) == 1:
        return table[s]
    i = num = 0
    while i < len(s):
        if i != len(s) - 1 and s[i : i + 2] in table:
            num = num + table[s[i : i + 2]]
            i = i + 2
        else:
            num  = num + table[s[i]]
            i = i + 1
    return num

def main():
    print romanToInt('MMMCMXCIX')

main()
