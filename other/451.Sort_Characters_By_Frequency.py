class Solution:
    def frequencySort(self, s: str) -> str:
        return ''.join([ch*c for ch,c in Counter(s).most_common()])
