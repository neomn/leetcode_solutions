class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends: 
            return -1
        q, visited = deque(), set(deadends)

        def children(code):
            response = []
            for i in range(4):
                digit = str((int(code[i]) +1) %10)
                response.append(code[:i]+digit+code[i+1:])
                digit = str((int(code[i]) +10 -1) %10)
                response.append(code[:i]+digit+code[i+1:])
            return response

        q.append(('0000', 0))
        while q:
            code, res = q.pop()
            if code == target: 
                return res
            for child in children(code): 
                if child not in visited: 
                    visited.add(child)
                    q.appendleft((child, res+1))
        return -1
