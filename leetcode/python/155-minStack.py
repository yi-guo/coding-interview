#!/usr/bin/python

# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.

# Use one stack to do the job!
class MinStack:

    def __init__(self):
        self.stack = list()
        self.minimum = float('inf')

    # Push the current minimum first then x if x <= minimum.
    def push(self, x):
        if x <= self.minimum:
            self.stack.append(self.minimum)
            self.minimum = x
        self.stack.append(x)

    # Pop twice when the top one is the minimum.
    def pop(self):
        if not self.stack:
            return
        if self.stack[-1] == self.minimum:
            self.stack.pop()
            self.minimum = self.stack.pop()
        else:
            self.stack.pop()

    def top(self):
        return self.stack[-1] if self.stack else None

    def getMin(self):
        return self.minimum

def main():
    minStack = MinStack()
    minStack.push(0)
    minStack.push(1)
    minStack.push(0)
    print minStack.getMin()
    minStack.pop()
    print minStack.getMin()

main()
