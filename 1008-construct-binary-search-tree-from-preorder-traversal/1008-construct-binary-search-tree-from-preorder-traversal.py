# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        # t.c O(n) 

        def solver(preorder,low,high):
            global i 
            if len(preorder) == i:
                return None
            if preorder[i] > low and preorder[i] < high: 
                node = TreeNode(preorder[i])
            else:
                return None
            i+=1
            node.left  = solver (preorder ,low,node.val)
            node.right  = solver(preorder ,node.val,high)
            return node
        global i
        i=0
        return solver(preorder,0,10000)