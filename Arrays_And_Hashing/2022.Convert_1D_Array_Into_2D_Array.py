class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n != len(original):
            return []
        res = []
        prev = 0
        for i in range(n, len(original)+1, n ):
            print(i, original[prev:i])
            res.append(original[prev:i])
            prev = i
        return res
