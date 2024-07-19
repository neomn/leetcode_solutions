class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        lenrow, lencol = len(matrix), len(matrix[0])
        row_min = [float('inf')]*lenrow
        col_max = [0]*lencol
        for i in range(lenrow):
            for j in range(lencol):
                row_min[i] = min(row_min[i], matrix[i][j])
                col_max[j] = max(col_max[j], matrix[i][j])
        return list(set(row_min).intersection(set(col_max)))
