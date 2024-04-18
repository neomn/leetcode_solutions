class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0
        len_row, len_col = len(grid), len(grid[0])
        for i in range(len_row):
            for j in range(len_col):
                if grid[i][j] == 1:
                    if i-1<0 or grid[i-1][j] == 0:
                        res += 1
                    if i+1>len_row-1 or grid[i+1][j] == 0:
                        res += 1
                    if j-1<0 or grid[i][j-1] == 0:
                        res +=1
                    if j+1>len_col-1 or grid[i][j+1] == 0:
                        res += 1
        return res    
