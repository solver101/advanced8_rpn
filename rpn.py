#!/usr/bin/env python3

import operator
import colored
from colored import stylize


operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}

def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
        print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def extrafunction():
    print("extra func with no coverage")
    print("extra func with no coverage")
    print("extra func with no coverage")
    print("extra func with no coverage")
    print("extra func with no coverage")

def main():
    while True:
        result = calculate(input("rpn calc> "))
        print(stylize(result, colored.fg("red")))

if __name__ == '__main__':
    main()

