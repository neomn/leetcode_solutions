class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        return sum( [n-i if n-i>0 else 0  for i,n in enumerate(sorted(happiness)[::-1][:k])] )
