from tree import Node, inorder
from collections import defaultdict, deque

# 20, 23, 25
# 31, 32, 33, 34, 36, 37, 38, 39
def findMirrorNodeUtil(a, b, target):
    if a is None or b is None:
        return None
    if a == target:
        return b
    if b == target:
        return a
    mirror = findMirrorNodeUtil(a.left, b.right, target)
    if mirror:
        return mirror
    return findMirrorNodeUtil(a.right, b.left, target)
    
def findMirrorNode(root, target):
    return findMirrorNodeUtil(root, root, target)

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
root.left.right.left.left = Node(11)
root.right.right.left.right = Node(18)
root.right.right.left.right.left = Node(22)


'''
        8
      /   \
     3     10
   /   \     \
  1    16     14
      /  \   /  \
     4    7 19   2
    /        \
   11        18 
             /
            22 
'''
print(findMirrorNode(root, root.right).data)
