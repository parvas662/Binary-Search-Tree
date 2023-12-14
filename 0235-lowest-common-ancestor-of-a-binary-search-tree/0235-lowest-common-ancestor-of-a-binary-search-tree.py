# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def solver(root,p,q):
            lbool = False
            rbool = False
            if root == None:
                return None , False     
            if root.val == p.val or root.val == q.val:
                return root , True
            elif root.val > p.val and root.val > q.val:
                lft ,lbool = solver(root.left,p,q)
            elif root.val < p.val and root.val < q.val:
                rgt ,rbool = solver(root.right,p,q)
            else:
                lft ,lbool = solver(root.left,p,q)
                rgt ,rbool = solver(root.right,p,q)
            if lbool == True and rbool == True:
                return root , True
            if lbool == True:
                return lft , True
            if rbool == True:
                return rgt , True
            return None , False

        ans , boolean = solver(root,p,q)
        return ans