from queue import Queue

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = Queue()
        m, n = len(mat), len(mat[0])
