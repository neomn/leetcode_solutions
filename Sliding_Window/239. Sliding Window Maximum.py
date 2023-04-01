import collections


def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
    deque = collections.deque
    left = right = 0
    output = []
    while right < len(nums):
        while deque and nums[deque[-1]] < nums[right]:
            deque.pop()
        deque.append(right)
        if left > deque[0]:
            deque.popleft()
        if (right + 1) >= k:


print(maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))