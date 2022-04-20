from tree import Node

'''
Given a binary tree, print boundary nodes of the binary tree Anti-Clockwise starting from the root. 
The boundary includes left boundary, leaves, and right boundary in order without duplicate nodes. 
(The values of the nodes may still be duplicates.)
The left boundary is defined as the path from the root to the left-most node. The right boundary is defined 
as the path from the root to the right-most node. If the root doesn't have left subtree or right subtree, 
then the root itself is left boundary or right boundary. Note this definition only applies to the input binary 
tree, and not apply to any subtrees.
The left-most node is defined as a leaf node you could reach when you always firstly travel to the left subtree
if it exists. If not, travel to the right subtree. Repeat until you reach a leaf node.
The right-most node is also defined in the same way with left and right exchanged. 
'''

def printLeftBoundary(root):
    if root:
        if root.left or root.right:
            print(root.data, end = " ")
            printLeftBoundary(root.left)

def printLeaves(root):
    if(root):
        printLeaves(root.left)
         
        # Print it if it is a leaf node
        if root.left is None and root.right is None:
            print(root.data, end = " ")
 
        printLeaves(root.right)

def printRightBoundary(root):
    if root:
        if root.right or root.left:
            printRightBoundary(root.right)
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