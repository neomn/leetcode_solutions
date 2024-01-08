class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = 0
        q = []
        q.append(root)
        while(q):
            element = q.pop()
            if element.left:
                q.append(element.left)
            if element.right:
                q.append(element.right)
            if element.val in range(low, high+1):
                res += element.val
        return res
