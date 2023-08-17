from queue import Queue

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = Queue()
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.put((i, j))
                else:
                    mat[i][j] = float('inf')
                    
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
