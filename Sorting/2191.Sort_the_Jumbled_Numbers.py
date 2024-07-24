class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        trans_rule = str.maketrans({str(i):str(x) for i,x in enumerate(mapping)})
        return sorted(nums, key=lambda x: int(str(x).translate(trans_rule)))
