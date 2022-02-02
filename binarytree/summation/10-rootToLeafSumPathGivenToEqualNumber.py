from tree import Node

def rootToLeafPathSum(root, k, s):
    if root is None:
        return False
    s += root.data
    if root.right is None and root.left is None and s == k:
        return True
    return rootToLeafPathSum(root.left, k, s) or rootToLeafPathSum(root.right, k, s)

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

print(rootToLeafPathSum(root, 0, 0))