class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        mod = 10**9 + 7
        dp = [[0] * n for _ in range(m)]
        directions = [[0,-1], [0,1], [-1,0], [1,0]]
        def dfs(i,j):
            if dp[i][j]:
                return dp[i][j]
            ans = 1
