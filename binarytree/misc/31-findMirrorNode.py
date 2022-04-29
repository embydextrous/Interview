from tree import Node

def mirrorNodeUtil(left, right, target):
    if left is None or right is None:
        return None
    if left == target:
        return right
    if right == target:
        return left
    mirror = mirrorNodeUtil(left.left, right.right, target)
    if mirror:
        return mirror
    return mirrorNodeUtil(left.right, right.left, target)

def findMirrorNode(root, target):
    if root is None:
        return None
    if root == target:
        return root
    return mirrorNodeUtil(root.left, root.right, target)



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

print(findMirrorNode(root, root.right.left).data)