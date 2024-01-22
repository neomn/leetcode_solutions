class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        lenn, map = len(nums), {}
        second = set(range(1,lenn+1))
        for n in nums:
            if n in second: second.remove(n)
            map[n] = 1 if n not in map.keys() else map[n]+1

        inv_map = {v:k for k,v in map.items()}
        return [inv_map[2],list(second)[0]]
