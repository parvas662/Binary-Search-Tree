# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def solver(root):
            if root == None:
                return 
            solver(root.left)
            tar[0] -=1
            if tar[0] == 0:
                ans[0] = root.val
                return 
            solver(root.right)
           
        tar = [k]
        ans = [0]
        solver(root)
        return ans[0]