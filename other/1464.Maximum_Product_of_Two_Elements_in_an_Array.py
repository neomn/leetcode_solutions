class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m1, m2 = 0,0
        for n in nums:
            if n > m1:
                m2 = m1
                m1 = n
            elif n > m2:
                m2 = n
        return (m1-1)*(m2-1)
