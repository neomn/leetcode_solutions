class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        dp, lenn = grid[0], len(grid)
        for i in range(1, lenn):
            new_dp = [0]*lenn
            for r,num in enumerate(grid[i]):
                new_dp[r] = ( num + min ( dp[:r]+dp[r+1:]) )
            dp = new_dp
        return min(dp)
