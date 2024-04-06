class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack, res = [], ""
        for i,ch in enumerate(s):
            if ch not in ['(',')']:
                res += ch
                continue
            if ch == '(':
                res += ch
                stack.append(len(res)-1)
                continue
            if not stack:
                continue
            res += ch
            stack.pop()

        res = [ch  for i, ch in enumerate(res) if i not in stack]
        return "".join(res)
