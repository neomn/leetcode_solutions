class Solution:
    def maxScore(self, s: str) -> int:
        score, ones, zeros = 0, s.count('1'), 0
        for i in range(len(s)-1):
            if s[i] == '0':
                zeros += 1
                score = max(score, zeros+ones)
            else:
                ones -= 1
                score = max(score, zeros+ones)
        return score
