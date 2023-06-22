class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        lenP, free, hold = len(prices), 0, -prices[0]
        for i in range(1, lenP):
            tmp = hold
            hold = max(hold, free - prices[i])
            free = max(free, tmp + prices[i] - fee)
