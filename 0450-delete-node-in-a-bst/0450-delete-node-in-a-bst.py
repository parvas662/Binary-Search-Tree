# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # optimal t.c O(n)
        # connecting  roots right tree with roots left tree.
        def helper(root):
            if root.left == None:
                return root.right
            elif root.right == None:
                return root.left
            rgtt = None
            rgtt = root.right
            if root.left != None:
                curr = root.left
                while curr.right != None:
                    curr = curr.right 
                curr.right  = rgtt
            

            return root.left

        dummy = root
        
        if root != None and root.val == key:
            return helper(root)
        while root != None:
            if root.val > key:
                if root.left != None and root.left.val == key:
                    root.left = helper(root.left)
                    break
                else:
                    root = root.left 
            else:
                if root.right != None and root.right.val == key:
                    root.right = helper(root.right)
                    break
                else:
                    root = root.right 
        return dummy


