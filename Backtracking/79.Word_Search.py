class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])

        vis = set()

        def dfs(i, j, curr):
            if curr == len(word):
                return True            
            if i >= n or i < 0 or j >= m or j < 0 or \
                board[i][j] != word[curr] or (i, j) in vis:
                return False
            vis.add((i, j))
            ans = dfs(i+1, j, curr+1) or dfs(i, j-1, curr+1) \
                    or dfs(i-1, j, curr+1) or dfs(i, j+1, curr+1)
            vis.remove((i, j))
            return ans

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        
        return False
