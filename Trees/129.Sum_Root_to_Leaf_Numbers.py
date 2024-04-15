class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res, stack = 0, [(root, str(root.val))]
        while stack:
            node , val = stack.pop()
            if node.right:
                stack.append((node.right, val+str(node.right.val)))
            if node.left:
                stack.append((node.left, val+str(node.left.val)))
            if not node.left and not node.right:
                res += int(val)
        return res
