from tree import Node

def sumOfAllParentNodesWithXAsChild(root, x):
    if root is None:
        return 0
    if (root.left and root.left.data == x) or (root.right and root.right.data == x):
        return root.data + sumOfAllParentNodesWithXAsChild(root.left, x) + sumOfAllParentNodesWithXAsChild(root.right, x)
    return sumOfAllParentNodesWithXAsChild(root.left, x) + sumOfAllParentNodesWithXAsChild(root.right, x)



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

print(sumOfAllParentNodesWithXAsChild(root, 1))