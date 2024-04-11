class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n=len(num)
        if n==k: return "0"
        st=[]
        for c in num:
            while st and c<st[-1] and k>0:
                k-=1
                st.pop()
            st.append(c)
        while k>0:
            st.pop()
            k-=1
        j=0
        m=len(st)
        while st[j]=='0' and j<m-1:
            j+=1
        if j==n-1 or st==None: return "0"
        return ''.join(st[j:])

        
