class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum, maxSub = 0, nums[0]
        for num in nums:
            if sum < 0:
                sum = 0
            sum += num
            maxSub = max(maxSub,sum)
        return maxSub
