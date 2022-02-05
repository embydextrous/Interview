from tree import Node, preorder

def replaceWithDepth(root, depth):
    if root:
        root.data = depth
        replaceWithDepth(root.left, depth + 1)
        replaceWithDepth(root.right, depth + 1)

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
replaceWithDepth(root, 0)
preorder(root)
print()