class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        def get_cost(base):
            return sum(abs(base - num) * c for num, c in zip(nums, cost))
        left, right = min(nums), max(nums)