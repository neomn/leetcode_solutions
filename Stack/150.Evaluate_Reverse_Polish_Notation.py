
def evalRPN(tokens: list[str]) -> int:
    stack = []
    for element in tokens:
        if element in '+-*/':
            a, b = stack.pop(), stack.pop()


print('output should be 9 > ', evalRPN(["2","1","+","3","*"]))
