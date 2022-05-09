from tree import Node

def distanceDown(root, a, k):
    if root is None:
        return -1
    if root == a:
        return k
    l = distanceDown(root.left, a, k + 1)
    if l != -1:
        return l
    return distanceDown(root.right, a, k + 1)

def findDistanceUtil(root, a, b, k):
    if root is None:
        return (None, -1)
    if root == a or root == b:
        if root == a and find(a, b):
            return (root, distanceDown(a, b, 0))
        if root == b and find(b, a):
            return (root, distanceDown(b, a, 0))
        return (root, k)
    left, distLeft = findDistanceUtil(root.left, a, b, k+1)
    right, distRight = findDistanceUtil(root.right, a, b, k+1)
    print(distLeft, distRight)
    if left and right:
        return (root, distLeft + distRight - 2 * k)
    return (left, distLeft) if left else (right, distRight)

def find(root, a):
    if root is None:
        return False
    return root == a or find(root.left, a) or find(root.right, a)


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

print(findDistanceUtil(root, root.left.right.left, root.left.right.right, 0))