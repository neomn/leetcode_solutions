class Solution:
    sum=0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if not root: return root
        self.bstToGst(root.right)
        self.sum+=root.val
        root.val=self.sum
        self.bstToGst(root.left)
        return root  
