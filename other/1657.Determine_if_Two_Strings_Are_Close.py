class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        w1, w2 = Counter(word1), Counter(word2)
        w1k, w1v = sorted(w1.keys()), sorted(w1.values())
        w2k, w2v = sorted(w2.keys()), sorted(w2.values())
        return w1k == w2k and w1v == w2v
