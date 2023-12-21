class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        return -min(( starmap(sub, pairwise(sorted(x for x, _ in points)))), default=0)
