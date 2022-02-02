from tree import Node
import sys

def maxSumRootToLeafUtil(root, path, pathSum, maxPathSum, maxPath):
    if root is None:
        return
    pathSum += root.data
    path.append(root.data)
    if root.left is None and root.right is None and pathSum > maxPathSum[0]:
        maxPathSum[0] = pathSum
        maxPath[0] = path[:]
    maxSumRootToLeafUtil(root.left, path, pathSum, maxPathSum, maxPath)
    maxSumRootToLeafUtil(root.right, path, pathSum, maxPathSum, maxPath)
    path.pop()

def maxSumRootToLeaf(root):
    if root is None:
        return 0
    maxPathSum = [-sys.maxsize-1]
    path = []
    maxPath = [None]
    maxSumRootToLeafUtil(root, path, 0, maxPathSum, maxPath)
    return (maxPathSum[0], maxPath[0])

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
print(maxSumRootToLeaf(root))