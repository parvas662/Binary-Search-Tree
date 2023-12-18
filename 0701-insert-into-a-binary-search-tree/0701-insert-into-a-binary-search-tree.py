# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def solver(root,val):
            if root == None:
                return None
            if root.val > val:
                lft = solver(root.left,val)
                if lft == None:
                    node = TreeNode(val)
                    root.left = node
                return root
            else:
                rgt = solver(root.right,val)
                if rgt == None:
                    node = TreeNode(val)
                    root.right = node
                return root
        if root == None:
            return TreeNode(val)
        return solver(root,val)