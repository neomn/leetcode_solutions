class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ans = 0
        for string in details: 
            if int(string[11:13]) > 60:
                ans += 1
        return ans
