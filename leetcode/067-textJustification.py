#!/usr/bin/python

# Given an array of words and a length L, format the text such that each line has exactly L characters
# and is fully (left and right) justified.

# You should pack your words in a greedy approach; that is, pack as many words as you can in each line.
# Pad extra spaces ' ' when necessary so that each line has exactly L characters.

# Extra spaces between words should be distributed as evenly as possible. If the number of spaces
# on a line do not divide evenly between words, the empty slots on the left will be assigned more
# spaces than the slots on the right.

# For the last line of text, it should be left justified and no extra space is inserted between words.

# For example,
#   Words: ["This", "is", "an", "example", "of", "text", "justification."]
#   L: 16.

# Return the formatted lines as:
#   ["This    is    an",
#	 "example  of text",
#	 "justification.  "]

# Note: Each word is guaranteed not to exceed L in length.

import pprint

def fullJustify(words, L):
    i, justified = 0, list()
    while i < len(words):
        # Pack as many words as possible. j - 1 is the index of the last word for current line.
        j, length = i + 1, len(words[i])
        while j < len(words) and length + len(words[j]) < L:
            length += len(words[j]) + 1
            j = j + 1
        # If last line, left justify and complement with spaces.
        if j == len(words):
            justified.append(' '.join(words[i:]) + spaces(L - length))
        # If one word only, left justify and complement with spaces.
        elif j - i == 1:
            justified.append(words[i] + spaces(L - length))
        # If two words, add enough spaces in between.
        elif j - i == 2:
            justified.append(words[i] + spaces(L - length + 1) + words[i + 1])
        # If more than two words,
        else:
            line = list()
            # n = the number of spaces that can be evenly distributed among the words.
            n = (L - length) / (j - i - 1)
            # Update length given j - i - 1 gaps, each of which n spaces are added.
            length = length + n * (j - i - 1)
            for k in range(i, j - 1):
                line.append(words[k] + spaces(n + int(length < L) + 1))
                length = length + int(length < L)
            line.append(words[j - 1])
            justified.append(''.join(line))
        i = j
    return justified

# Generate string of spaces of given length.
def spaces(length):
    return ''.join([' ' for i in range(length)])

def main():
    pp = pprint.PrettyPrinter(width=20)
    pp.pprint(fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))

main()
