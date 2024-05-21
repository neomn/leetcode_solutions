class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res, self.lenn = [], len(nums)

        def make_res(prev, i):
            if i == self.lenn:
                self.res.append(prev)
                return
            make_res(prev, i+1) 
            make_res(prev+[nums[i]], i+1)

        make_res([], 0)        
        return self.res
