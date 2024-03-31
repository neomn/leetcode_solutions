class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        badi, mini, maxi, res = -1, -1, -1, 0
        for i, n in enumerate(nums):
            if not minK <= n <= maxK: badi = i
            if n == minK:             mini = i
            if n == maxK:             maxi = i
            res += max(0, min(mini, maxi) - badi)
        return res
