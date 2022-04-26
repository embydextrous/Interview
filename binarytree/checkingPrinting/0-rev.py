import heapq
from tree import Node
from collections import deque, defaultdict

# 26 29
def longestLeafToLeafPathUtil(root, maxLen, maxPath):
    if root is None:
        return (0, [])
    lHeight, lPath = longestLeafToLeafPathUtil(root.left, maxLen, maxPath)
    rHeight, rPath = longestLeafToLeafPathUtil(root.right, maxLen, maxPath)
    if len(lPath) <= len(rPath):
        mPath = rPath
    else:
        mPath = lPath
    if 1 + lHeight + rHeight > maxLen[0]:
        maxLen[0] = 1 + lHeight + rHeight
        maxPath[0] = lPath[:]
        maxPath[0].append(root.data)
        maxPath[0].extend(reversed(rPath))
    mPath.append(root.data)
    return (1 + max(lHeight, rHeight), mPath)
    
def longestLeafToLeafPath(root):
    maxLen = [0]
    maxPath = [[]]
    longestLeafToLeafPathUtil(root, maxLen, maxPath)
    return (maxLen[0], maxPath[0])
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

print(longestLeafToLeafPath(root))


'''
        a
      /   \
     b     c
   /   \     \
  d     e      f
       /  \   /  \
      g    h  i   j
'''
'''
---rootToLeaf
---rootToAnyNode
---AnyNodeToLeaf (NoBack)
---AnyNodeToAnyNode (NoBack)
AnyNodeToLeafNode (Back)
AnyNodeToAnyNode (Back)
Leaf to Leaf

printAllPaths
printPathWithMaxSum
printLongestPath
checkSequence
checkPathWithSum
'''


