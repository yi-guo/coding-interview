#!/usr/bin/python

# Given an input string, reverse the string word by word.

# For example, given s = "the sky is blue", return "blue is sky the".

# Clarification:
#   1. What constitutes a word?
#      A sequence of non-space characters constitutes a word.
#   2. Could the input string contain leading or trailing spaces?
#      Yes. However, your reversed string should not contain leading or trailing spaces.
#   3. How about multiple spaces between two words?
#      Reduce them to a single space in the reversed string.


def reverseWords1(s):
    end, reverse = -1, list()
    for i in xrange(len(s) - 1, -2, -1):
        if i == -1 or s[i].isspace():
            if end != -1:
                reverse.append(s[i+1:end+1])
                end = -1
        else:
            end = max(i, end)
    return ' '.join(reverse)


# Kinda cheating?
def reverseWords2(s):
    return ' '.join(s.split()[::-1])


def main():
    print reverseWords1(' the sky  is blue ')
    print reverseWords2(' the sky  is blue ')


main()
