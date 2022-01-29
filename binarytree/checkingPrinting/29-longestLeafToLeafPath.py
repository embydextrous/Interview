from tree import Node

def longestLeafToLeafPathUtil(root, maxD, rootMap, maxRoot):
    if root is None:
        return 0
    lHeight = longestLeafToLeafPathUtil(root.left, maxD, rootMap, maxRoot)
    rHeight = longestLeafToLeafPathUtil(root.right, maxD, rootMap, maxRoot)
    if 1 + lHeight + rHeight > maxD[0]:
        maxD[0] = 1 + lHeight + rHeight
        maxRoot[0] = root
    rootMap[root] = [[], []]
    if root.left:
        left = rootMap[root.left][0]
        right = rootMap[root.left][1]
        rootMap[root][0] = left if len(left) > len(right) else right
        rootMap[root][0].append(root.left.data)
    if root.right:
        left = rootMap[root.right][0]
        right = rootMap[root.right][1]
        rootMap[root][1] = left if len(left) > len(right) else right
        rootMap[root][1].append(root.right.data)
    return 1 + max(lHeight, rHeight)

def longestLeafToLeafPath(root):
    maxD = [0]
    rootMap = {}
    maxRoot = [None]
    longestLeafToLeafPathUtil(root, maxD, rootMap, maxRoot)
    return rootMap[maxRoot[0]][0] + [maxRoot[0].data] + rootMap[maxRoot[0]][1]

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
print(longestLeafToLeafPath(root))