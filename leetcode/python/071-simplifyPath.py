#/!usr/bin/python

# Given an absolute path for a file (Unix-style), simplify it.

# For example,
#   path = "/home/", => "/home"
#   path = "/a/./b/../../c/", => "/c"

# Use stack to store all directories retrieved from path.
# From left to right, for each directory, if '.', then ignore; if '..', then pop the stack;
# otherwise, push the current directory into the stack. Hence, O(n).
def simplifyPath(path):
    i, stack = 0, list()
    while i < len(path):
        j = i
        while j < len(path) and path[j] == '/':
            j = j + 1
        if j == len(path):
            break
        k = j + 1
        while k < len(path) and path[k] != '/':
            k = k + 1
        curr = path[j:k]
        if curr == '.':
            pass
        elif curr == '..':
            if stack:
                stack.pop()
        else:
            stack.append(curr)
        i = k
    return '/' + '/'.join(stack)

def main():
    path = '/a/./b/../../c/'
    print simplifyPath(path)

main()
