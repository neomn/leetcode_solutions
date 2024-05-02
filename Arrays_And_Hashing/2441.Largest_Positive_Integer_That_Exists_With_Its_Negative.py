class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        _max, negatives = 0, set(nums)
        for n in nums:
            if n > 0 and n > _max and (n * -1) in negatives:
                _max = n
        return _max if _max else -1
