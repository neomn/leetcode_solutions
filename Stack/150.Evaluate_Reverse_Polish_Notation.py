
def evalRPN(tokens: list[str]) -> int:
    stack = []
    for element in tokens:
        if element in '+-*/':


print('output should be 9 > ', evalRPN(["2","1","+","3","*"]))
