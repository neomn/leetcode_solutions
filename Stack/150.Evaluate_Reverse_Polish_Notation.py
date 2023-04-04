
def evalRPN(tokens: list[str]) -> int:
    stack = []
    for element in tokens:
        if element in '+-*/':
            a, b = stack.pop(), stack.pop()
        if element == '+':
            stack.append(b + a)
        elif element == '-':
            stack.append(b - a)
        elif element == '*':
            stack.append(b * a)
        elif element == '/':
            stack.append(b // a)
        else:
            stack.append(int(element))
    return stack[0]


print('output should be 9 > ', evalRPN(["2","1","+","3","*"]))
print('output should be 6 > ', evalRPN(["4","13","5","/","+"]))
