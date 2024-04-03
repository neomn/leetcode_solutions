class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapst, mapts = dict(), dict()
        for i in range(len(s)):
            if s[i] in mapst and mapst[s[i]] != t[i]: return False
            if t[i] in mapts and mapts[t[i]] != s[i]: return False
            mapst[s[i]], mapts[t[i]] = t[i], s[i]
        return True
