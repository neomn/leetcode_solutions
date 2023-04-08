
def dailyTemperatures(temperatures: list[int]) -> list[int]:
    result, stack = [0] * len(temperatures), []
    for index, temp in enumerate(temperatures):


