# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # t.c O(n) s.c O(n)
        def solver(root):
            if root ==None:
                return 
            solver(root.left)
            inorder.append(root.val)
            solver(root.right)
            
        def bal_bst(inorder):
            if len(inorder) == 0:
                return None
            mid = len(inorder)//2
            node = TreeNode(inorder[mid])
            node.left = bal_bst(inorder[:mid])
            node.right  = bal_bst(inorder[mid+1:])
            return node
            
        inorder = []
        solver(root)
        return bal_bst(inorder)