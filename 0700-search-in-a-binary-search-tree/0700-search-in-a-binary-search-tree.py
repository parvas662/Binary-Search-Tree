# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def solver(root,k):
            if root == None:
                return None
            if root.val == k:
                return root
            if root.val > k:
                lft = solver(root.left,k)
                return lft
            if root.val <= k:
                rgt = solver(root.right,k)
                return rgt

        return solver(root,val)