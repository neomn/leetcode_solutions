class Solution:
    def checkValidString(self, s: str) -> bool:
        leftCount, rightCount = 0, 0
        for ch in s:
            leftCount  = leftCount+1  if ch == '(' else leftCount-1
            rightCount = rightCount-1 if ch == ')' else rightCount+1
            
            if rightCount < 0: 
                break
            
            leftCount = max(leftCount, 0)
        
        return leftCount == 0
