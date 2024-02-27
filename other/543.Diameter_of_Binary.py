class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxD = 0
        
        def helper(node):
            if not node.left and not node.right:
                return 1
            lv, rv = 0, 0
            if node.left:
                lv = helper(node.left)
            if node.right:
                rv = helper(node.right)
            self.maxD = max(self.maxD, (lv+rv))
            return max(lv, rv)+1

        helper(root)
        return self.maxD
