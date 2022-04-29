from tree import Node, inorder
from collections import deque

# 15, 20, 23, 25, 28, 29
# 31, 32, 33, 34, 36, 37, 38, 39
def findMirrorNodeUtil(a, b, target):
    print(a.data, b.data, target.data)
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
    if root is None:
        return None
    if target == root:
        return root
    return findMirrorNodeUtil(root.left, root.right, target)


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
print(findMirrorNode(root, root.right.right))
