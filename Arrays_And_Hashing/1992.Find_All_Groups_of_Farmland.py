class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        res, lenrow, lencol = [], len(land), len(land[0])
        
        def find_range(r,c):
            start = (r,c)
            while True:
                while True: 
                    land[r][c] = 0
                    c += 1
                    if c >= lencol or land[r][c] != 1: break
                r += 1
                if r >= lenrow or land[r][start[1]] != 1: break 
                c = start[1]
            return [start[0],start[1],r-1,c-1]

        for r in range(lenrow):
            for c in range(lencol):
                if land[r][c] == 1: res.append(find_range(r,c))
        return res
