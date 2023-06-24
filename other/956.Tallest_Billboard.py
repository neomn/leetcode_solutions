class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = {0:0}
        for r in rods:
            new_dp = dp.copy()
            for diff, taller in dp.items():
                shorter = taller - diff
                new_dp[diff + r] = max(new_dp.get(diff + r, 0), taller + r)                
                new_diff = abs(shorter + r - taller)
