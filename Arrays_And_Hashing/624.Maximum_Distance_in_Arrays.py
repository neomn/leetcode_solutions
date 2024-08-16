class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        MX=float('-inf')
        MI=float('inf')
        ans=0
        for arr in arrays:
            ans=max(ans,MX-arr[0],arr[-1]-MI)
            MI,MX=min(MI,arr[0]),max(MX,arr[-1])
        return ans    
