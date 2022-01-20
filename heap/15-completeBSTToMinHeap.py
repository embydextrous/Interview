def inorder(root, a):
    if root:
        inorder(root.left, a)
        a.append(root.data)
        inorder(root.right, a)
    
def preorder(root, a, i):
    if root:
        root.data = a[i[0]]
        i[0] += 1
        preorder(root.left, a, i)
        preorder(root.right, a, i)

def printTree(root):
    if root:
        printTree(root.left)
        print(root.data, end = " ")
        printTree(root.right)

def convertToMinHeap(bstRoot):
    a = []
    inorder(bstRoot, a)
    print(a)
    preorder(bstRoot, a, [0])

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

'''
                 4
               /   \
              2     6
            /  \   /  \
           1   3  5    7 
'''
root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)

convertToMinHeap(root)
printTree(root)
print()

