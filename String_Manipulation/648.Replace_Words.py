class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        rootset, res = set(dictionary), ''
        for w in sentence.split():
            added = False
            for i in range(len(w)):
                if w[:i+1] in rootset:
                    res += w[:i+1]+' '
                    added = True
                    break
            if not added:
                res += w + ' '

        return res[:len(res)-1]
