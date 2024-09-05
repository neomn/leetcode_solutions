class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        # m+n // count of m+n == mean, so : 
        m = len(rolls)
        count = m+n
        sum_m = sum(rolls)
        min_mean = (sum_m + n) // count
        max_mean = (sum_m + (n*6)) // count

        if not (min_mean <= mean <= max_mean):
            return []

        sum_n = (mean * count) - sum_m
        if not (n <= sum_n <= n*6):
            return []

        res = [1]*n
        i = 0
        sum_so_far = n
        while sum_so_far != sum_n:
            res[i] += 1
            sum_so_far += 1
            if res[i] == 6:
                i += 1
        return res
