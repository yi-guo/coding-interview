#!/usr/bin/python

# Evaluate the value of an arithmetic expression in Reverse Polish Notation.

# Valid operators are +, -, *, /. Each operand may be an integer or another expression.

# Some examples:
#   ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
#   ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

def evalRPN(tokens):
    stack = list()
    for token in tokens:
        # Token is an integer or negative integer
        if token.isdigit() or token[1:].isdigit():
            stack.append(int(token))
            continue
        if token == '+':
            stack.append(stack.pop() + stack.pop())
        elif token == '-':
            n = stack.pop()
            stack.append(stack.pop() - n)
        elif token == '*':
            stack.append(stack.pop() * stack.pop())
        else:
            n = stack.pop()
            m = stack.pop()
            stack.append(0 - abs(m) / abs(n) if m * n < 0 else m / n)
    return stack.pop()

def main():
    print evalRPN(["4","-2","/","2","-3","-","-"])

main()
