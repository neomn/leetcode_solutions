class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        res = 0
        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
            if node.left:
                if not node.left.left and not node.left.right:
                    res += node.left.val
                stack.append(node.left)
        return res
