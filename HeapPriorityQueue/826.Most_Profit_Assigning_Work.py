class Solution:
    def maxProfitAssignment(self, d: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(d, profit))
        worker.sort()

        ans = j = maxp = 0

        for w in worker:
            while j < len(jobs) and jobs[j][0] <= w:
                maxp = max(maxp, jobs[j][1])
                j+=1
            ans += maxp
        return ans
