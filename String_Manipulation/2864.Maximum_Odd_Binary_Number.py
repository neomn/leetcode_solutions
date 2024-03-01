class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        lens, c =len(s), s.count('1')
        return '1'*(c-1)+ '0'*(lens-c) + '1'
