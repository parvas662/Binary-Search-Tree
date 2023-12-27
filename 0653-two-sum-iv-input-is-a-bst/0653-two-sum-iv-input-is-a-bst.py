# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # approach -> use dfs and while travresing check if k-val is present in hahmap or not if yes then return true.

    # t.c O(n)  we will traverse all nodes of bst.
    # s.c O(n) ans array to need to store all the nodes of bst

        def solver(root):
            if root == None:
                return  False
            if k - root.val in ans:
                return True
            ans.add(root.val)
            return solver(root.left) or solver(root.right)

        ans = set()
        return solver(root)
        