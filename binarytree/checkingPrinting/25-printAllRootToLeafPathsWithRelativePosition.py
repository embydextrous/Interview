from tree import Node

def printPath(path):
    maxHd, minHd = path[-1][2], path[-1][3]
    for pathObj in path:
        result = "-" * (pathObj[1] - minHd)
        result += str(pathObj[0].data)
        result += "-" * (maxHd - pathObj[1])
        print(result)
    print()

def printNodesAtDistanceKFromLeaf(root, path, hd, maxHd, minHd):
    if root is None:
        return
    path.append((root, hd, maxHd, minHd))
    if root.left is None and root.right is None:
        printPath(path)
    printNodesAtDistanceKFromLeaf(root.left, path, hd - 1, max(maxHd, hd - 1), min(minHd, hd - 1))
    printNodesAtDistanceKFromLeaf(root.right, path, hd + 1, max(maxHd, hd + 1), min(minHd, hd + 1))
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