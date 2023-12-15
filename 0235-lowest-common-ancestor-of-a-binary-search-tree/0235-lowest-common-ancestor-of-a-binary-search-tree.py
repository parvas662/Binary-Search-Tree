# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # optimal code
        def solver(root,p,q):
            if root == None:
                return None     
            if root.val > p.val and root.val > q.val:
                return solver(root.left,p,q)
            elif root.val < p.val and root.val < q.val:
                return solver(root.right,p,q) 
            return root 

        return solver(root,p,q)