class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        lenn = len(nums)
        for i,n in enumerate(nums): 
            if n < 0: 
                nums[i] = 0

        for i,n in enumerate(nums):
            t = abs(n)
            if 1<=t<=lenn: 
                if nums[t-1] > 0:
                    nums[t-1] *= -1
                elif nums[t-1] == 0:
                    nums[t-1] = -1*(lenn+1)
        
        for i,n in enumerate(nums):
            if n>=0: 
                return i+1
        return lenn+1
