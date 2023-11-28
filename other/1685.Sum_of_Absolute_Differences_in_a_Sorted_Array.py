class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        res, nums_sum, col_count, add, temp = [], sum(nums), len(nums), 0, 0
        for i, n in enumerate(nums):
            sub = (col_count-i) * n
            add = i * n - temp
            res.append(nums_sum - sub + add)
            temp += n
            nums_sum -= n
        return res
