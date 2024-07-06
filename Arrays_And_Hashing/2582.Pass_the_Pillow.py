class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        x = time // (n-1)
        r = time % (n-1)
        return r+1 if x % 2 == 0 else n-r
