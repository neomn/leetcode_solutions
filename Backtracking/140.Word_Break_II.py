class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.res, self.lens = [], len(s)
        wordDict = set(wordDict)

        def dfs(prev, i):
            for j in range(i, self.lens):
                if s[i:j] in wordDict:
                    word = s[i:j] if prev=='' else ' '+s[i:j]
                    dfs(prev+word, j)
            if s[i:] in wordDict:
                word = s[i:] if prev=='' else ' '+s[i:]
                self.res.append(prev+word)
                return 

        dfs('', 0)
        return self.res
