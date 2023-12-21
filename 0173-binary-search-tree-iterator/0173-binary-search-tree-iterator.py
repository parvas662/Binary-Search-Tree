# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
    t.c O(h) because we are not pushing all the nodes into stack. we  push those nodes that we want. 
    s.c O(h)
 
optimal approach -> use of a stack, 
    step 1 -> push all the nodes left of root into the stack.
    step 2 -> when next() is called node = pop() elment from stack. and check if nodes right is not null. then repeat step 1. and then return value of poped node.
    step3  -> can eaisly check hasnext() by checking stack is empty or not.

another approach -> we can also use of inorder list. by storing all the elements into a list using inorder. but tc. O(1) for next() and hasnext() but. s.c (n)
"""
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        while root != None:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        curr = self.stack.pop()
        node = curr.right
        while node != None:
            self.stack.append(node)
            node = node.left

        return curr.val

    def hasNext(self) -> bool:
        if len(self.stack)  == 0:
            return False
        return True
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()