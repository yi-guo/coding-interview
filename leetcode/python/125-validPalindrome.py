#!/usr/bin/python

# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# For example,
# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.

# Note:
#   1. Have you consider that the string might be empty? This is a good question to ask during an interview.
#   2. For the purpose of this problem, we define empty string as valid palindrome.

# Two pointers i and j move toward each other, checking if s[i] = s[j].
def isPalindrome(s):
    s = s.lower()
    i, j = 0, len(s) - 1
    while i < j:
        # Skip characters that are not alphanumeric.
        if not s[i].isalnum():
            i = i + 1
            continue
        if not s[j].isalnum():
            j = j - 1
            continue
        if s[i] != s[j]:
            return False
        i = i + 1
        j = j - 1
    return True

def main():
    s = 'A man, a plan, a canal: Panama'
    print isPalindrome(s)

main()
