from tree import Node

def printPath(path, minHd, maxHd):
    for (data, hd) in path:
        print(f"{'-' * (hd - minHd)}{data}{'-' * (maxHd - hd)}")
    print()

def printNodesAtDistanceKFromLeaf(root, path, hd, maxHd, minHd):
    if root is None:
        return
    path.append((root.data, hd))
    if root.left is None and root.right is None:
        printPath(path, minHd, maxHd)
    printNodesAtDistanceKFromLeaf(root.left, path, hd - 1, maxHd, min(minHd, hd - 1))
    printNodesAtDistanceKFromLeaf(root.right, path, hd + 1, max(maxHd, hd + 1), minHd)
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
root.right.right.left.left = Node(30)
root.right.right.left.left.left = Node(32)
root.right.right.left.right = Node(31)

'''
        8
      /   \
     3     10
   /   \     \
  1    16     14
      /  \   /  \
     4    7 19   2
           /  \
          30   31
         /
        32 
'''

printNodesAtDistanceKFromLeaf(root, [], 0, 0, 0)