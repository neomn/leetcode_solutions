class Solution:
    def maxDepth(self, s: str) -> int:
        _max, depth = 0, 0
        for ch in s:
            if ch == '(': 
                depth += 1
                _max = max(_max, depth)
            elif ch == ')' and depth > 0: 
                depth -= 1
        return _max
