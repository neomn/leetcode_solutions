class Solution:
    def longestPalindrome(self, s: str) -> int:

        map = {}
        for ch in s:
            map[ch] = map[ch]+1 if ch in map else 1

        res, odd = 0, False
        for k, v in map.items():
            if v % 2 != 0:
                odd = True
            res += v // 2
            
        return res*2 if not odd else (res*2)+1
