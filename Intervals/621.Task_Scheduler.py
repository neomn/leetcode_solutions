class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        most_common = Counter(tasks).most_common()
        max_freq = most_common[0][1]
        how_many_max = len( [c for _,c in most_common if c == max_freq] )
        time = (max_freq-1) * (n+1) + how_many_max
        return max(time, len(tasks)) 
