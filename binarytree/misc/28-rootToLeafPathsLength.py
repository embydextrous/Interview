from tree import Node

def rootToLeafPathsUtil(root, pathLen, d):
    if root is None:
        return
    pathLen += 1
    if root.left is None and root.right is None:
        if pathLen in d:
            d[pathLen] += 1
        else:
            d[pathLen] = 1
    rootToLeafPathsUtil(root.left, pathLen, d)
    rootToLeafPathsUtil(root.right, pathLen, d)

def rootToLeafPaths(root):
    d = {}
    rootToLeafPathsUtil(root, 0, d)
    for pathLength in d:
        print("Tree has {} {} of length {}.".format(d[pathLength], "paths" if d[pathLength] > 1 else "path",pathLength))

'''
        8
      /   \
     3     10
   /   \     \
  1    16     14
      /  \   /  \
     4    7 19   2
    /         \
   11         18
             /
            22  
'''

root = Node(8)
root.left = Node(3)
root.left.left = Node(1)
root.left.right = Node(16)
root.left.right.left = Node(4)
root.left.right.left.left = Node(11)
root.left.right.right = Node(7)
root.right = Node(10)
root.right.right = Node(14)
root.right.right.left = Node(19)
root.right.right.left.right = Node(18)
root.right.right.left.right.left = Node(22)
root.right.right.right = Node(2)

rootToLeafPaths(root)