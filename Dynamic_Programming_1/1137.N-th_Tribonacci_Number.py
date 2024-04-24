class Solution:
    def tribonacci(self, n: int) -> int:
        d, i = deque([0,1,1,0]), 0
        if n <= 2: return d[n]
        while i < n-2:
            d[3] = sum(list(d)[0:3])
            d.rotate(-1)
            i += 1
        return d[2]
