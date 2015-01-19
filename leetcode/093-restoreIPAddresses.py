#!/usr/bin/python

# Given a string containing only digits, restore it by returning all possible valid IP address combinations.

# For example, given "25525511135", return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)

# BFS until no address left or all the addresses are valid.
def restoreIpAddresses(s):
    # Only allows input s to be of length [4, 12]
    if len(s) < 4 or len(s) > 12:
        return list()
    # Hold all valid IP addresses
    addresses = [[]]
    # BFS until no address left or all the addresses are valid
    while addresses and len(addresses[0]) != 4:
        curr = addresses.pop(0)
        # For each of what we have, generate the next part of length of 1 - 3
        for i in range(1, 4):
            if not curr:
                next = s[:i]
                if isValid(next):
                    addresses.append([next])
            else:
                start = len(''.join(curr))
                # When the current one has three parts, validate the rest only once.
                if len(curr) == 3:
                    next = s[start:]
                    if isValid(next):
                        addresses.append(curr + [next])
                    break
                next = s[start : start + i]
                if isValid(next):
                    addresses.append(curr + [next])
    return ['.'.join(address) for address in addresses]

# Return true if the address part is valid
def isValid(s):
    if not s:
        return False
    if s[0] == '0':
        return s == '0'
    return 0 < int(s) <= 255

def main():
    print restoreIpAddresses("25525511135")

main()
