# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # tc. O(n)
        # approach -> there is a range for every left and right subtree. every node should lie in that range.
        
        def solver(root,minn,maxx):

            if root == None:
                return True
            if root.val <= minn or root.val >= maxx:
                return False
            return solver(root.left,minn,root.val) and solver(root.right,root.val,maxx) 
            
        return solver(root,-2**31-1,2**31 +1)