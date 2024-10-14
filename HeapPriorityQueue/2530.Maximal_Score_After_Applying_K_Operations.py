class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = heapq.nlargest(k, nums)
        nums = [-n for n in nums]
        heapq.heapify(nums)
        score = 0
        for i in range(k):
            num = heapq.heappop(nums) * -1
            score += num
            heapq.heappush(nums, ceil(num/3) * -1)
        return score
