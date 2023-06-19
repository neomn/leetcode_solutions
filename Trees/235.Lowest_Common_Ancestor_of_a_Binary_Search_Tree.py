class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while True:
            if min(p.val, q.val) <= root.val and root.val <= max(p.val, q.val): return root
            root = root.left if p.val < root.val and q.val < root.val else root.right
