class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res, met = 0,False
        for ch in reversed(s):
            if not met and ch == ' ': continue
            met = True
            if ch == ' ': return res
            res += 1
        return res
