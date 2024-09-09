from collections import deque

class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        res = [[-1]*n  for _ in range(m)]
        i, j = 0, 0
        direction = deque(['r','d','l','u']) 
        while True:

            while direction[0] == 'r' and head and j < n and res[i][j] == -1:
                res[i][j] = head.val
                j += 1
                head = head.next
                if not head: 
                    return res
            j -= 1
            if i < m-1: i += 1
            direction.rotate(-1)

            while direction[0] == 'd' and head and i < m and res[i][j] == -1:
                res[i][j] = head.val
                i += 1
                head = head.next
                if not head: 
                    return res
            i -= 1
            if j > 0: j -= 1
            direction.rotate(-1)

            while direction[0] == 'l' and head and j >= 0 and res[i][j] == -1:
                res[i][j] = head.val
                j -= 1
                head = head.next
                if not head: 
                    return res
            j += 1
            if i > 0: i -= 1
            direction.rotate(-1)

            while direction[0] == 'u' and head and i >= 0 and res[i][j] == -1:
                res[i][j] = head.val
                i -= 1
                head = head.next
                if not head: 
                    return res
            i += 1
            if j < n: j += 1
            direction.rotate(-1)
