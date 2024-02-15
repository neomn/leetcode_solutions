class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        max_permiter = -1
        sum = nums[0]+nums[1]
        for n in nums[2:] :
            if sum > n:
                max_permiter = sum + n
            sum += n
        return max_permiter
