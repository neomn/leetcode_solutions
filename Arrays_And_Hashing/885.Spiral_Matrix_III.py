class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        direct = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        res = []
        step = 0
        while len(res) < rows * cols:
            drow, dcol = direct[step % 4]
            step += 1
            for _ in range((step + 1) // 2):
                if 0 <= rStart < rows and 0 <= cStart < cols:
                    res.append([rStart, cStart])
                rStart += drow
                cStart += dcol
        return res
