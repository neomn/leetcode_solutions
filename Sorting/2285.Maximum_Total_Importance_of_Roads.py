class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        freq = {}
        for a,b in roads:
            freq[a] = 1 if a not in freq else freq[a]+1
            freq[b] = 1 if b not in freq else freq[b]+1

        freq = sorted(freq.items(), key=lambda x: x[1])

        ans, lenn = 0, len(freq)
        for i in range(lenn):
            ans += (n-i)*freq[lenn-1-i][1]

        return ans
        
