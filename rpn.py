#!/usr/bin/env python3

import operator
import readline
import colored
from colored import stylize

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow
    '|': operator.xor,
    '&': operator.concat
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

def main():
    while True:
        result = calculate(input("rpn calc> "))
        if result < 0:
            color = fg('#C0C0C0') + bg('#00005f')
            res = attr('reset')
            print (color + "Result: " + str(result) + res)
        else:        
            print("Result: ", result)

if __name__ == '__main__':
    main()

