class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        end = len(s)//2-1 if len(s)%2==0 else len(s)//2
        left = 0
        for right in range(len(s)-1, end, -1):
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            left += 1

        
