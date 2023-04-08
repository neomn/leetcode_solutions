
def dailyTemperatures(temperatures: list[int]) -> list[int]:
    result, stack = [0] * len(temperatures), []
    for index, temp in enumerate(temperatures):
        while stack and temp > temperatures[stack[-1]]:
            result[stack.pop()] = index - stack[-1]
        stack.append(index)
    return result


print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
print(dailyTemperatures([30,40,50,60]))
print(dailyTemperatures([30,60,90]))