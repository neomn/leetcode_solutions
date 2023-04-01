import collections


def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
    deque = collections.deque
    left = right = 0
    output = []
    while right < len(nums):

print(maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))