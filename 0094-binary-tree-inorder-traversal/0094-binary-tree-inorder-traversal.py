# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
            # morris traversal, 
            # approach -> threading 
        ans = []
        curr = root
        while curr != None:
            if curr.left  == None:
                ans.append(curr.val)
                curr = curr.right
            else:
                node = curr.left
                while node.right != None and node.right != curr:   # when we came back after traversing left. nodes right should not point to curr. because nodes right is threaded already and we need to break that thread. so that bt structure will remainn same .
                    node = node.right 
                if node.right  == None:
                    node.right  = curr
                    curr = curr.left
                elif node.right  == curr:   # when comming back after traversing left.we have to break that thread we made earlier.
                    node.right  = None
                    ans.append(curr.val)
                    curr = curr.right 
        return ans
                











