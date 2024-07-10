class Solution:
    def minOperations(self, logs: List[str]) -> int:
        min_ops = 0
        for string in logs:
            if string != '../' and string != './':
                min_ops += 1
            if min_ops and string == '../':
                min_ops -= 1
        return min_ops
