class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        lenn = len(matrix)
        dp = matrix[0]
        temp = [0]*lenn
        for i in range(1, lenn):
            temp = list(dp)
            for j in range(lenn):
                l = 0      if j-1 < 0      else j-1
                r = lenn-1 if j+1 > lenn-1 else j+1
                dp[j] = min(temp[l:r+1]) + matrix[i][j]
        return min(dp)
