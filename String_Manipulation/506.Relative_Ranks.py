class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        sorted_score = sorted(score)[::-1]
        score[score.index(sorted_score[0])] = 'Gold Medal'
        if n > 1: score[score.index(sorted_score[1])] = 'Silver Medal'
        if n > 2: score[score.index(sorted_score[2])] = 'Bronze Medal'
        if n > 3:
            for i in range(3, n):
                score[score.index(sorted_score[i])] = str(i+1)
        return score
