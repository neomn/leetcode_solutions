class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c = Counter(nums).most_common()
        max_freq = c[0][1]
        return sum( [f for n,f in c if f == max_freq] )        
