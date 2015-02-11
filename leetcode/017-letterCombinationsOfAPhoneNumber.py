#!/usr/bin/python

# Given a digit string, return all possible letter combinations that the number could represent.

# Input: Digit string "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

# Note: Although the above answer is in lexicographical order, your answer could be in any order you want.

# Breath-first search
def letterCombinations(digits):
    table = {'2': 'abc', '3': 'def',  '4': 'ghi', '5': 'jkl',
             '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    combinations = ['']
    for digit in digits:
        size = len(combinations)
        for i in xrange(size):
            for c in table[digit]:
                combinations.append(combinations[i] + c)
        combinations = combinations[size:]
    return combinations

def main():
    print letterCombinations('23')

main()