class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], m: int) -> int:
        
        lenc = len(customers)
        not_mad_count = 0
        for i in range(lenc):
            if not grumpy[i]:
                not_mad_count += customers[i]
                customers[i] = 0

        mad_count = sum( customers[0:m])
        new_mad_count = int(mad_count)
        for i in range(m, lenc):
            new_mad_count += customers[i] - customers[i-m]
            mad_count = max( mad_count, new_mad_count )

        return not_mad_count + mad_count
