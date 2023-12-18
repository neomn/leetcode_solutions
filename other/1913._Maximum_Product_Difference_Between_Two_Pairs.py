class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        max_1 = max(nums)
        nums.remove(max_1)
        min_1 = min(nums)
        nums.remove(min_1)

        return (max_1 * max(nums)) - (min_1 * min(nums))
