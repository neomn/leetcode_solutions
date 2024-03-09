class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        set1, set2 = set(nums1), set(nums2)
        c = set1 & set2 # equivalent to -> common = set1.intersection(set2)
        return min(c) if c else -1
