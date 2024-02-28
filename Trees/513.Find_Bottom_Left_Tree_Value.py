class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        stack = [(root, 0)]
        max_depth = -1
        res = 0
        while stack:
            node, depth = stack.pop()
            if depth > max_depth:
                max_depth = depth
                res = node.val
            if node.right:
                stack.append((node.right, depth+1))
            if node.left:
                stack.append((node.left, depth+1))
        return res
