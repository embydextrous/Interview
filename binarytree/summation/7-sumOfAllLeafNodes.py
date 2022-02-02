from tree import Node

def sumOfLeaves(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return root.data
    return sumOfLeaves(root.left) + sumOfLeaves(root.right)

'''
        8
      /   \
     3     10
   /   \     \
  1    16     14
      /  \   /  \
     4    1 1    2
'''
root = Node(8)
root.left = Node(3)
root.left.left = Node(1)
root.left.right = Node(16)
root.left.right.left = Node(4)
root.left.right.right = Node(1)
root.right = Node(10)
root.right.right = Node(14)
root.right.right.left = Node(1)
root.right.right.right = Node(2)

print(sumOfLeaves(root))


