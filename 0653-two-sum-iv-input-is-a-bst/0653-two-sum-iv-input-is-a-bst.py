# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # approach -> using inorder property of bst, which give sorted array. then use of two pointers i and j and move them accordingly to k.

    # t.c O(n)  we will traverse all nodes of bst.
    # s.c O(n) ans array to need to store all the nodes of bst

        def solver(root):
            if root == None:
                return 
            solver(root.left)
            ans.append(root.val)
            solver(root.right)

        ans = []
        solver(root)
        i=0
        j = len(ans)-1
        while i < j:
            if ans[i] + ans[j] ==k:
                return True
            elif ans[i] + ans[j] < k: 
                i+=1
            else:
                j-=1
        return False