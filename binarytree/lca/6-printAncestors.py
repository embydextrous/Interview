from tree import Node

def printAncestors(root, path, node):
    if root is None:
        return
    if root == node:
        print(path)
    path.append(root.data)
    printAncestors(root.left, path, node)
    printAncestors(root.right, path, node)
    path.pop()

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

printAncestors(root, [], root.left.right.left)