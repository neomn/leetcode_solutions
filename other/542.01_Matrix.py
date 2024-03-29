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
        while not q.empty():
            i, j = q.get()
            for r, c in directions:
                new_i, new_j = i + r, j + c
                if (0 <= new_i < m)  and  (0 <= new_j < n):
                    if mat[i][j] + 1 < mat[new_i][new_j]:
                        mat[new_i][new_j] = mat[i][j] + 1
                        q.put((new_i, new_j))
        
        return mat
