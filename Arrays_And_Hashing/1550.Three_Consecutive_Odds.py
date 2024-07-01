class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        tsum = 0
        for n in arr:
            tsum = 0 if n % 2 == 0 else tsum+1
            if tsum == 3: return True
        return False
