class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        res, map = 0, {}
        for n in nums:
            t = n - ( int(''.join(reversed(str(n)))) )
            map[t]=1 if   t not in map   else map[t]+1
        for v in map.values():
            if v > 1:
                res = res + v*(v-1)//2
        return res % ((10**9)+7)
