
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


print('output should be 9 > ', evalRPN(["2","1","+","3","*"]))
