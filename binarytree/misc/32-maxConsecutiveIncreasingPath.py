from tree import Node

# https://www.geeksforgeeks.org/maximum-consecutive-increasing-path-length-in-binary-tree/

def maxIncreasingPathUtil(root, lastNode, currentPathLen, maxPathLen):
    if root is None:
        return 0
    if lastNode is None:
        currentPathLen = 1
    elif root.data == lastNode.data + 1:
        currentPathLen += 1
    else:
        currentPathLen = 1
    if currentPathLen > maxPathLen[0]:
        maxPathLen[0] = currentPathLen
    maxIncreasingPathUtil(root.left, root, currentPathLen, maxPathLen)
    maxIncreasingPathUtil(root.right, root, currentPathLen, maxPathLen)

def maxIncreasingPath(root):
    if root is None:
        return 0
    maxPathLen = [0]
    maxIncreasingPathUtil(root, None, 0, maxPathLen)
    return maxPathLen[0]

root = Node(6)
root.right = Node(9)
root.right.left = Node(7)
root.right.right = Node(10)
root.right.right.right = Node(11)

print(maxIncreasingPath(root))