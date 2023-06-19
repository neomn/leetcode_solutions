class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        m, temp = 0, 0
        for alt in gain:
            temp += alt
