class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res, seen = {}, set()
        for s in strs:
            key = str(sorted(s))
            if key not in seen: 
                res[key] = [s] 
            else: 
                res[key].append(s)
            seen.add(key)
        return res.values()
