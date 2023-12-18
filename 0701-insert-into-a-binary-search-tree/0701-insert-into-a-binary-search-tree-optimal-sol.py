# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        curr = root
        if root == None:
            return TreeNode(val)
        while root != None:
            if root.val > val:
                if root.left == None:
                    node = TreeNode(val)
                    root.left = node
                    return curr
                root = root.left
                
            else:
                if root.right == None:
                    node = TreeNode(val)
                    root.right = node
                    return curr
                root = root.right
