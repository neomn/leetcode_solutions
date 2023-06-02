class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        helperCell = False
        for i in range(m):
            for j in range(n):
