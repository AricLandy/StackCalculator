


op = {
        '+': opperator.add, 
        '-': opperator.sub, 
        '*': opperator.mul, 
        '/': opperator.floordiv, 
}

def calculate(arg):
    #pass

    stack = arg.split()

    while len(stack) > 1:
        token = stack.pop()
        try:
            value = int(token)
            stack.append(token)
        except ValueError:
            val2 = int(stack.pop())
            val1 = int(stack.pop())

            #look it up in the table
            func = op[token]
            result = func(val1, val2)

            stack.append(str(result))
    return int(stack[0])


def main():
    while True:
        result = calculate(input("rpn calc> "))
        print(result)

if __name__ == '__main__':
    main()
