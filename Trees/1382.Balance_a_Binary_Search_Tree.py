# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        # read node values
        values = []
        stack = [root]
        while stack: 
            node = stack.pop()
            values.append(node.val)
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)

        # sort them 
        values.sort()

        # build a balanced tree
        def btree(nodes):
            if not nodes: return 
            l, r = 0, len(nodes)-1
            m = (l+r)//2
            leftNode = btree(nodes[l:m])
            rightNode = btree(nodes[m+1:r+1])
            return TreeNode(nodes[m], leftNode, rightNode)

        return btree(values)
