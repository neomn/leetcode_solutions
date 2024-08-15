class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cash = {
            5: 0,
            10: 0,
            20: 0
        }
        for b in bills: 
            cash[b] += 1
            if b == 10:
                cash[5] -= 1
                if cash[5] < 0:
                    return False
            if b == 20:
                if cash[10] and cash[5]:
                    cash[10] -= 1
                    cash[5] -= 1
                    continue
                if not cash[10] and cash[5] >= 3:
                    cash[5] -= 3
                    continue
                return False
        return True
        
