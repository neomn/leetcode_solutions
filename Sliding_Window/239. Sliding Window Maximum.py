import collections


def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
    deque = collections.deque
    left = right = 0


print(maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))