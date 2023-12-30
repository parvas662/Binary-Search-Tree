"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        """apporach -> similar to flatten a bst to sorted list question but in this using level order traversal. think tree as linkedlist.
        make prev and move prev as we move in linkedlist. """

        q = []
        if root != None:
            q.append(root)
        while len(q) != 0:
            qlen = len(q)
            prev = None
            for i in range(qlen):
                front = q.pop(0)
                if prev == None:
                    prev = front
                else:
                    prev.next  = front
                prev = front

                if front.left != None:
                    q.append(front.left)
                if  front.right != None:
                    q.append(front.right)

            prev.next = None
        return root
