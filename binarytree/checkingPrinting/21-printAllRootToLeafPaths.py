from tree import Node

def printAllRootToLeafPaths(root, path):
    if root is None:
        return
    path.append(root.data)
    if root.left is None and root.right is None:
        print(path)
    printAllRootToLeafPaths(root.left, path)
    printAllRootToLeafPaths(root.right, path)
    path.pop()

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


'''
        8
      /   \
     3     10
   /   \     \
  1    16     14
      /  \   /  \
     4    7 19   2
'''

printAllRootToLeafPaths(root, [])