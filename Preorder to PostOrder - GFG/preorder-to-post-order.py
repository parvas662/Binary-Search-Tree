#User function Template for python3

class Node:

    def __init__(self, data=0):
        self.data = data
        self.left = None
        self.right = None

#Function that constructs BST from its preorder traversal.
def post_order(pre, size) -> Node:
    #code here
    
    # approach -> using of upperbound range can solve this problem.
    def solver(high):
        global i
        if i == size or pre[i] > high:      #agar index high se bahar ja rha h to.  # low range is not needed here.
            return None
            
        node = Node(pre[i])
        i+=1
        node.left = solver(node.data)
        node.right = solver(high)
        return node
    
    global i 
    i = 0
    root = solver(100000)
    return root



#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
class Node:
    def __init__(self, data=0):
        self.data = data
        self.left = None
        self.right = None

def postOrd(root):
    if not root:
        return
    postOrd(root.left)
    postOrd(root.right)
    print(root.data,end=' ')

if __name__ == '__main__':
    t=int(input())

    for _tcs in range(t):
        size=int(input())
        pre=[int(x)for x in input().split()]

        root=post_order(pre,size)

        postOrd(root)
        print()
# } Driver Code Ends
