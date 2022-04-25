from tree import Node

def sumLongestPathUtil(root, pathSum, pathLen, maxPathLen, maxLenPathSum):
    if root is None:
        return 0
    pathSum += root.data
    if root.left is None and root.right is None and pathLen >= maxPathLen[0]:
        if pathLen == maxPathLen[0]:
            maxLenPathSum[0] = max(maxLenPathSum[0], pathSum)
        else:
            maxPathLen[0] = pathLen
            maxLenPathSum[0] = pathSum
    pathLen += 1
    sumLongestPathUtil(root.left, pathSum, pathLen, maxPathLen, maxLenPathSum)
    sumLongestPathUtil(root.right, pathSum, pathLen, maxPathLen, maxLenPathSum)

def sumLongestPath(root):
    if root is None:
        return 0
    maxPathLen = [0]
    maxLenPathSum = [0]
    sumLongestPathUtil(root, 0, 0, maxPathLen, maxLenPathSum)
    return maxLenPathSum[0]

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
root.right.right.left.left = Node(8)
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
          8   31 
         /
        4  
'''
print(sumLongestPath(root))