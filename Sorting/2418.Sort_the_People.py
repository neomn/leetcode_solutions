class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        name_heights = []
        for i in range(len(names)):
            name_heights.append((names[i], heights[i]))
        res = sorted(name_heights, key=lambda x: x[1])
        return [r[0] for r in reversed(res)]
