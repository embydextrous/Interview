from tree import Node

def printLeftBoundary(root):
    if root:
        if root.left:
            print(root.data, end = " ")
            printLeftBoundary(root.left)
        elif root.right:
            print(root.data, end = " ")
            printLeftBoundary(root.right)

def printLeaves(root):
    if(root):
        printLeaves(root.left)
         
        # Print it if it is a leaf node
        if root.left is None and root.right is None:
            print(root.data, end = " ")
 
        printLeaves(root.right)

def printRightBoundary(root):
    if root:
        if root.right:
            printRightBoundary(root.right)
            print(root.data, end = " ")
        elif root.left:
            printRightBoundary(root.left)
            print(root.data, end = " ")


def boundaryTraversal(root):
    if root:
        print(root.data, end = " ")
        printLeftBoundary(root.left)
        printLeaves(root.left)
        printLeaves(root.right)
        printRightBoundary(root.right)
    print()

'''
        8
      /   \
     3     10
   /   \     \
  1    16     14
      /  \   /  \
     4    7 19   2
    /
   3 
'''

root = Node(8)
root.left = Node(3)
root.left.left = Node(1)
root.left.right = Node(16)
root.left.right.left = Node(4)
root.left.right.left.left = Node(3)
root.left.right.right = Node(7)
root.right = Node(10)
root.right.right = Node(14)
root.right.right.left = Node(19)
root.right.right.right = Node(2)
boundaryTraversal(root)