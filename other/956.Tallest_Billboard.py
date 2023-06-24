class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = {0:0}
        for r in rods:
            new_dp = dp.copy()
