class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        avgs = [-1] * n
        window_size = 2*k+1
        if n < window_size:
            return avgs
