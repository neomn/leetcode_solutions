class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and log2(n)%1 == 0
