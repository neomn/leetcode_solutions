class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if n==0: return 1
            if x==0: return 0
            temp = helper(x*x, n//2)
