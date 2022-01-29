from tree import Node

def printLeaves(root):
    if root is None:
        return
    if not root.left and not root.right:
        print(root.data, end = " ")
    # Swap line 9 and 10 for left to right
    printLeaves(root.right)
    printLeaves(root.left)

'''
        8
      /   \
     3     10
   /   \     \
  1    16     14
      /  \   /  \
     4    7 19   2
'''
root = Node(8)
root.left = Node(3)
root.left.left = Node(1)
root.left.right = Node(16)
root.left.right.left = Node(4)
root.left.right.right = Node(7)
root.right = Node(10)
root.right.right = Node(14)
root.right.right.left = Node(19)
root.right.right.right = Node(2)

printLeaves(root)
print()