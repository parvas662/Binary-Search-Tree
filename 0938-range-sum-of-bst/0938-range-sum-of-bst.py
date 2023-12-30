# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # approach -> when node lies in the range we have to move both side, bcz we dont know which side we have a node whose value lies in the range. and if node > low, we know we have to move right bcz of bst property. and if node < high we  will move left. 
        def solver(root,l,h):
            if root == None:
                return 0 
                    
            if root.val >= l and root.val <= high:
                return root.val + solver(root.right,l,h) + solver(root.left,l,h)
            if root.val < l:
                return solver(root.right,l,h)
            else:
                return solver(root.left,l,h)

        return solver(root,low,high)
