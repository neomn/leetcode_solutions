class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4: 
            return 0
            
        smallest_4 = sorted(heapq.nsmallest(4, nums))
        largest_4 = sorted(heapq.nlargest(4, nums))
        min_diff = float('inf')

        for i in range(4):
            min_diff = min(min_diff, largest_4[i] - smallest_4[i])

        return min_diff
