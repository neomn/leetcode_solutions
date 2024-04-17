class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        result = []
        stack = [(root, chr(97+root.val))]
        while stack:
            node, text = stack.pop()
            if not node.left and not node.right:
                result.append(text[::-1])
            if node.right:
                stack.append((node.right, text + chr(97+node.right.val)))
            if node.left:
                stack.append((node.left, text + chr(97+node.left.val)))

        return sorted(result)[0]
