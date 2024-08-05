class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counts = Counter(arr)
        counter = 0
        for s in arr:
            if counts[s] == 1:
                counter += 1
                if counter == k:
                    return s
        return ''     
